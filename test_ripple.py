import unittest
import make_ripples

class Test_TestRippleRegion(unittest.TestCase):
    def test_region_0(self):
        ripple = make_ripples.ripple((0,0))
        self.assertEqual(ripple.region(-1,1,-1,1),0)

    def test_region_0_edge_case(self):
        ripple = make_ripples.ripple((1,0))
        self.assertNotEqual(ripple.region(-1,1,-1,1),0)

    def test_region_3(self):
        ripple = make_ripples.ripple((0,2))
        self.assertEqual(ripple.region(-1,1,-1,1),3)

    def test_region_8(self):
        ripple = make_ripples.ripple((2,-2))
        self.assertEqual(ripple.region(-1,1,-1,1),8)

    def test_region_4(self):
        ripple = make_ripples.ripple((-2,2))
        self.assertEqual(ripple.region(-1,1,-1,1),4)

if __name__ == '__main__':
    unittest.main()