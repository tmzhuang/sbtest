from unittest import TestCase

import sbtest.sbengine

class TestSBEngine(TestCase):
    def test_f(self):
        s = sbtest.sbengine.f()
        self.assertEqual(s, 42, f's:{s} should be 42')
