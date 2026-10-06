#!/usr/bin/env bash
# The public release of this repository: the tree, the sheets, and the source documents, as one commit
# that carries no history and no author. It is run by a person, by hand or through
# .github/workflows/release.yml; nothing runs it on its own.
#
# What leaves: README.md, .github/workflows/integrity.yml (the one CI check, the same in every 7LM
# repository), and everything under L7/ and L8/ except the contents of L8/L6/history/, L8/L6/in/ and
# L8/L6/retired/, whose own sheets (0.md) leave and whose records do not. A repository's history is its
# own and is kept at its own L6: the release never carries it (the hard rule, L8/L6/7lm-field-guide.md §5).
# This script and its workflow do not leave either.
#
# What the public sees: one commit, authored "7LM <7lm@localhost>", whose message is the release date.
# Each release replaces the last: no diff, no commit history, no author is readable at the destination.
#
# Usage:
#   .github/release.sh                      dry run: build the release tree, check it, print it, leave nothing
#   .github/release.sh /path/to/dir         write the release tree into that (new or empty) directory
#   .github/release.sh <git URL>            commit the tree and force-push it to branch $RELEASE_BRANCH (default main)
set -euo pipefail

SRC=$(git rev-parse --show-toplevel)
DEST=${1:-}
BRANCH=${RELEASE_BRANCH:-main}
DATE=$(date -u +%Y-%m-%d)
NAME=${RELEASE_NAME:-7LM}
EMAIL=${RELEASE_EMAIL:-7lm@localhost}

cd "$SRC"
if [ -n "$(git status --porcelain)" ]; then
  echo "the working tree is not clean; a release is made from a commit, not from edits" >&2; exit 1
fi

# The list of what leaves, from HEAD.
mapfile -t FILES < <(git ls-tree -r --name-only HEAD | grep -E '^(README\.md|\.github/workflows/integrity\.yml|L7/.*|L8/.*)$' \
  | grep -vE '^L8/L6/(history|in|retired)/.+' ; git ls-tree -r --name-only HEAD | grep -E '^L8/L6/(history|in|retired)/0\.md$')
[ "${#FILES[@]}" -gt 0 ] || { echo "nothing to release" >&2; exit 1; }

BUILD=$(mktemp -d)
trap 'rm -rf "$BUILD"' EXIT
git archive --format=tar HEAD -- "${FILES[@]}" | tar -x -C "$BUILD"

# Checks on the release tree, before anything leaves.
fail=0
# 1. The root is canonical.
for e in $(ls -A "$BUILD"); do
  case "$e" in README.md|L7|L8|.github) ;; *) echo "not canonical at root: $e"; fail=1;; esac
done
# 2. Every sheet is headed by its path, and nothing of L6's memory left with it.
while IFS= read -r -d '' s; do
  rel=${s#"$BUILD"/}; d=${rel%/0.md}
  [ "$(head -n 1 "$s")" = "# $d/" ] || { echo "heading is not the path: $rel"; fail=1; }
done < <(find "$BUILD" -name 0.md -print0)
n=$(find "$BUILD/L8/L6/history" "$BUILD/L8/L6/in" "$BUILD/L8/L6/retired" -type f 2>/dev/null | grep -vc '/0\.md$' || true)
[ "$n" -eq 0 ] || { echo "L6 memory in the release tree ($n files)"; fail=1; }
# 3. No authorship tag of the kinds a text can carry: an e-mail address, a repository URL, a co-author trailer, an author note.
if grep -rIn -E '[[:alnum:]._%+-]+@[[:alnum:].-]+\.[[:alpha:]]{2,}|https?://github\.com/|Co-Authored-By|Author note' "$BUILD" >/dev/null; then
  grep -rIn -E '[[:alnum:]._%+-]+@[[:alnum:].-]+\.[[:alpha:]]{2,}|https?://github\.com/|Co-Authored-By|Author note' "$BUILD" | head -20
  echo "authorship tags in the release tree"; fail=1
fi
[ "$fail" -eq 0 ] || { echo "release refused" >&2; exit 1; }

count=$(find "$BUILD" -type f | wc -l)
if [ -z "$DEST" ]; then
  echo "dry run: $count files would leave, as one commit \"$NAME, release of $DATE\":"
  (cd "$BUILD" && find . -type f | sort | sed 's|^\./||')
  exit 0
fi

case "$DEST" in
  *://*|git@*)
    (
      cd "$BUILD"
      git init -q
      git add -A
      git -c user.name="$NAME" -c user.email="$EMAIL" commit -q --no-gpg-sign \
        --author="$NAME <$EMAIL>" -m "$NAME, release of $DATE"
      git push --force "$DEST" "HEAD:refs/heads/$BRANCH"
    )
    echo "released: $count files, one commit, to $BRANCH"
    ;;
  *)
    mkdir -p "$DEST"
    [ -z "$(ls -A "$DEST")" ] || { echo "$DEST is not empty" >&2; exit 1; }
    cp -R "$BUILD"/. "$DEST"/
    echo "written: $count files to $DEST"
    ;;
esac
