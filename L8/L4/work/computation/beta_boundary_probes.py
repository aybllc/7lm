#!/usr/bin/env python3
"""Bounded research-object probes; no owner theory or directory enforcement engine."""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
import platform

def nu_admitted(pair):
    """Admission gate of this rational consumer, not a change to original NU class."""
    return len(pair)==2 and all(isinstance(x,F) for x in pair) and pair[1]>=0

def nu_product(a,b):
    if not nu_admitted(a) or not nu_admitted(b): raise ValueError('outside declared rational consumer domain')
    n,u=a;m,v=b
    return n*m,abs(n)*v+abs(m)*u

def nu_catch(a):
    n,u=a
    return F(0),abs(n)+u

def exact_product(a,b):
    n,u=a;m,v=b
    corners=[x*y for x in (n-u,n+u) for y in (m-v,m+v)]
    return min(corners),max(corners)

def contains(outer,inner):
    return outer[0]<=inner[0] and inner[1]<=outer[1]

def semantic_state(label,magnitude):
    if not isinstance(label,str) or not isinstance(magnitude,F) or magnitude<0:
        raise ValueError('this fixture requires a named semantic state and nonnegative rational magnitude')
    return label,magnitude

def attempt_aggradation(a,b):
    semantic_state(*a);semantic_state(*b)
    return {'status':'unresolved','output':None,'stopped_at':'L2',
            'obligation':'Source has not fixed semantic S, interaction Phi, and their preservation laws; no default is invented.'}

def rail(model_id,name,question,path,status,result):
    rail_id=f'{model_id}:rail:{name.lower()}'
    return ({'id':rail_id,'name':name,'model_id':model_id,'inquiry_ids':[rail_id+':inquiry']},
            {'id':rail_id+':inquiry','rail_id':rail_id,'question':question,
             'inward_path':list(reversed(path)),'outward_path':path,
             'representation_ids':[f'{rail_id}:inquiry:{layer}' for layer in path],
             'dependency_ids':['approved-common-layer-contracts'],'status':status,'result':result,
             'limits':'Fixture-specific qualification; shared dependencies, no statistical independence or lateral traversal.'})

def representations(model_id,inquiries):
    paths={'L0':'L8/L0/semantics/beta-research-scope.md',
           'L1':'L8/L1/state-space/beta-research-admissibility.md',
           'L2':'L8/L2/formal-mathematics/proofs/beta-research-boundaries.md',
           'L3':'L8/L3/engineering-mathematics/approximation/beta-exact-reference-method.md',
           'L4':'L8/L4/work/computation/beta-boundary-results.json',
           'L5':'L8/L5/research/findings/beta-research-boundary-findings.md',
           'L6':'L8/L6/history/specification-history.md',
           'L7':'L7/provenance/sources/source-ledger.md'}
    result=[]
    for inquiry in inquiries:
        previous=None
        for rep_id,layer in zip(inquiry['representation_ids'],inquiry['outward_path']):
            result.append({'id':rep_id,'layer':layer,'owner':layer,'path':paths[layer],
                           'dependency_ids':[] if previous is None else [previous]})
            previous=rep_id
    return result

def build_results():
    a=(F(10),F(1));b=(F(5),F(1,2));actual=nu_product(a,b)
    decoded=(actual[0]-actual[1],actual[0]+actual[1]);target=exact_product(a,b)
    agrees=contains(decoded,target)
    model_id='research-object:nu-numeric-pair:bounded-consumer-1'
    sr,si=rail(model_id,'Semantic','Does the declared interval consumer interpretation justify full-product enclosure?',
               ['L0','L1','L2','L3','L4','L5','L6','L7'],'counterexample',
               {'source_product':actual,'decoded':decoded,'reference':target,'contains':agrees})
    er,ei=rail(model_id,'Epistemic','Does a conserved scalar establish recoverability of the original pair?',
               ['L0','L1','L2','L4','L5','L6','L7'],'claim_rejected',
               {'input_a':(F(5),F(2)),'input_b':(F(3),F(4)),
                'catch_a':nu_catch((F(5),F(2))),'catch_b':nu_catch((F(3),F(4))),
                'same_output':True,'full_input_ledger_required_for_reconstruction':True})
    nu={'scientific_object':'Numeric N/U pair, separate from Semantic Magnitude',
        'model':{'id':model_id,'owner':'bounded audit consumer','synthetic':True,'scope':'rational subset, independent interval-input target'},
        'rails':[sr,er],'inquiries':[si,ei],'representations':representations(model_id,[si,ei]),
        'scientific_outcome':'enclosure_claim_rejected'}
    sm_id='research-object:semantic-magnitude:open-algebra-1';attempt=attempt_aggradation(('A',F(1)),('B',F(3)))
    sr,si=rail(sm_id,'Semantic','Can distinct semantic coordinates be preserved at zero magnitude?',
               ['L0','L1','L4','L5','L6','L7'],'supported_with_limits',
               {'state_a':semantic_state('negative',F(0)),'state_b':semantic_state('zero',F(0)),
                'distinct':semantic_state('negative',F(0))!=semantic_state('zero',F(0))})
    er,ei=rail(sm_id,'Epistemic','Is a full aggradation computation warranted by the supplied source?',
               ['L0','L1','L2'],'unresolved',attempt)
    sm={'scientific_object':'Semantic Magnitude, separate from numerical N/U',
        'model':{'id':sm_id,'owner':'source-scoped research fixture','synthetic':True,'scope':'named semantic labels and nonnegative rational magnitude; S/Phi remain open'},
        'rails':[sr,er],'inquiries':[si,ei],'representations':representations(sm_id,[si,ei]),
        'scientific_outcome':'aggradation_unresolved'}
    return {'format':'7lm.beta.demonstration.v1','objects':[nu,sm],
      'sources':[
        {'id':'NU-17271561','owner':'author deposit','version':'10.5281/zenodo.17271561',
         'path':'nualgebra-main.zip','sha256':'60cccd3222b00965505a6f890f3540639fe976edbd1ab209f4b4bf8497cf6f0e',
         'role':'version-specific numerical fixture','status':'source formulas transcribed; original source not modified'},
        {'id':'SM-PDF','owner':'supplied source owner','version':'supplied two-page PDF',
         'path':'Semantic_Magnitude_Aggradation_Core.docx.pdf',
         'sha256':'b8d36fa37ab68db59825050e4ba1789d915ceab4093bab8a662e3f922829f235',
         'role':'unfinished algebra fixture','status':'source identity from completed audit; full source bytes not redistributed'}],
      'execution':{'arithmetic':'fractions.Fraction','python':platform.python_version(),'synthetic':True,
         'command':'python3 L8/L4/work/computation/beta_boundary_probes.py --output L8/L4/work/computation/beta-boundary-results.json',
         'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
      'fault_and_requalification':{'injection':'Promote finite source arithmetic to full interval enclosure',
         'faulty_claim_status':'supported' if agrees else 'rejected','observed_failure_at':'L5 claim versus exact target',
         'correction_owner':'L5','satisfied_upstream':['L1 rational admission','L2 source operator evaluated as defined','L3 exact reference method','L4 recorded output'],
         'affected_dependents':['enclosure conclusion','outward qualification statement'],
         'correction':'Restrict the conclusion to the defined first-order operation; retain the failed enclosure witness.',
         'source_operator_changed':False,
         'requalified_status':'supported_with_limits' if nu_admitted(actual) else 'rejected'},
      'limitations':['No theory repaired or completed.','No empirical uncertainty or memory claim validated.',
         'Original NU constructor behavior is not replaced by this consumer admission gate.',
         'Semantic Magnitude cannot prescribe aggradation through its unresolved L2 bridge.',
         'Rail identities are model-attached perspectives, not two algorithms or L5 lanes.',
         'This bounded packet is not directory metadata, access enforcement or universal qualification.']}

def encode(value):
    if isinstance(value,F):return str(value)
    raise TypeError(type(value).__name__)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    result=build_results();args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,default=encode)+'\n')
    print('Two research objects qualified: N/U enclosure rejected; Semantic Magnitude aggradation unresolved; source theories unchanged.')

if __name__=='__main__':main()
