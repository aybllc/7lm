import importlib.util
from pathlib import Path
import unittest
from fractions import Fraction as F

PATH=Path(__file__).resolve().parent/'beta_boundary_probes.py'

class BoundaryTests(unittest.TestCase):
    def setUp(self):
        self.assertTrue(PATH.is_file(), 'approved boundary probe implementation is absent')
        spec=importlib.util.spec_from_file_location('boundary_probes',PATH)
        self.probe=importlib.util.module_from_spec(spec);spec.loader.exec_module(self.probe)
    def test_domain_does_not_silently_coerce_negative_radius(self):
        self.assertFalse(self.probe.nu_admitted((F(3),F(-2))))
    def test_source_operator_remains_linearized_not_repaired(self):
        self.assertEqual(self.probe.nu_product((F(10),F(1)),(F(5),F(1,2))),(F(50),F(10)))
    def test_reference_compares_endpoints_and_detects_width_only_mistake(self):
        target=self.probe.exact_product((F(10),F(1)),(F(5),F(1,2)))
        self.assertEqual(target,(F(81,2),F(121,2)))
        self.assertFalse(self.probe.contains((F(40),F(60)),target))
    def test_preserved_invariant_does_not_imply_input_recovery(self):
        self.assertEqual(self.probe.nu_catch((F(5),F(2))),self.probe.nu_catch((F(3),F(4))))
    def test_semantic_states_are_not_identified_at_zero_magnitude(self):
        self.assertNotEqual(self.probe.semantic_state('negative',F(0)),self.probe.semantic_state('zero',F(0)))
    def test_undefined_aggradation_stops_without_fabrication(self):
        value=self.probe.attempt_aggradation(('A',F(1)),('B',F(3)))
        self.assertEqual(value['status'],'unresolved');self.assertIsNone(value['output']);self.assertEqual(value['stopped_at'],'L2')
    def test_same_rail_contract_supports_both_objects_with_different_outcomes(self):
        result=self.probe.build_results()
        self.assertEqual(len(result['objects']),2)
        for obj in result['objects']:
            self.assertEqual({r['name'] for r in obj['rails']},{'Semantic','Epistemic'})
            self.assertEqual({r['model_id'] for r in obj['rails']},{obj['model']['id']})
        self.assertEqual(result['objects'][0]['scientific_outcome'],'enclosure_claim_rejected')
        self.assertEqual(result['objects'][1]['scientific_outcome'],'aggradation_unresolved')
    def test_successful_state_inquiry_does_not_depend_on_unresolved_aggradation(self):
        sm=self.probe.build_results()['objects'][1]
        reps={r['id']:r for r in sm['representations']}
        state,open_operation=sm['inquiries']
        todo=list(state['representation_ids']);seen=set()
        while todo:
            key=todo.pop()
            if key in seen or key not in reps:continue
            seen.add(key);todo.extend(reps[key]['dependency_ids'])
        self.assertFalse(set(open_operation['representation_ids']) & seen, 'independent state inquiry inherits unresolved operation dependencies')
    def test_overclaim_is_corrected_without_changing_source_math(self):
        result=self.probe.build_results();fault=result['fault_and_requalification']
        self.assertEqual(fault['faulty_claim_status'],'rejected');self.assertEqual(fault['correction_owner'],'L5')
        self.assertEqual(fault['source_operator_changed'],False);self.assertEqual(fault['requalified_status'],'supported_with_limits')

if __name__=='__main__':unittest.main(verbosity=2)
