import unittest
import make_ripples

class Test_TestRippleRegion(unittest.TestCase):
    def test_region_0(self):
        ripple = make_ripples.Ripple((0,0))
        self.assertEqual(ripple.region(-1,1,-1,1),0)

    def test_region_0_edge_case(self):
        ripple = make_ripples.Ripple((1,0))
        self.assertNotEqual(ripple.region(-1,1,-1,1),0)

    def test_region_3(self):
        ripple = make_ripples.Ripple((0,2))
        self.assertEqual(ripple.region(-1,1,-1,1),3)

    def test_region_8(self):
        ripple = make_ripples.Ripple((2,-2))
        self.assertEqual(ripple.region(-1,1,-1,1),8)

    def test_region_4(self):
        ripple = make_ripples.Ripple((-2,2))
        self.assertEqual(ripple.region(-1,1,-1,1),4)

class Test_TestRippleReflect(unittest.TestCase):
    def test_helper(self):
        self.assertEqual(make_ripples.Ripple.reflect_helper(0,-1),-2)
    def test_reflect_x(self):
        ripple = make_ripples.Ripple((0,0))
        compare_ripple = make_ripples.Ripple((-2,0))
        test_ripple = ripple.reflect_x(-1)
        self.assertEqual(test_ripple,compare_ripple)

    def test_reflect_y(self):
        ripple = make_ripples.Ripple((0,0))
        compare_ripple = make_ripples.Ripple((0,-2))
        test_ripple = ripple.reflect_y(-1)
        self.assertEqual(test_ripple,compare_ripple)

if __name__ == '__main__':
    unittest.main()