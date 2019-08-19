# Example of unit tests for different test cases.
import math
import time
import unittest

class GcdTest(unittest.TestCase):
    """Tests of the math.gcd function.
       Of course, Python's gcd function is almost certainly correct.
       But test it anyway!
       gcd should always return a positive integer, except gcd(0,0) = 0.
       What these tests show:
       identifying distinct test cases (sets of input values),
       including "edge" cases, "borderline" cases, and "extreme" cases.
    """

    def setUp(self):
        self.start_time = time.time()

    def tearDown(self):
        # Test for slow, inefficient gcd.  gcd should be fast!
        MAX_TIME = 0.004   # max run-time, in seconds
        elapsed = time.time() - self.start_time
        if elapsed > MAX_TIME:
            self.fail("gcd too slow. Elapsed time %.6f sec" % (elapsed))
    
    
    def test_gcd_with_zero(self):
        self.assertEqual(1, math.gcd(0,1))
        self.assertEqual(5, math.gcd(5,0))
        self.assertEqual(9, math.gcd(0,9))
        self.assertEqual(7, math.gcd(0,-7))
        self.assertEqual(8, math.gcd(-8,0))
        self.assertEqual(0, math.gcd(0,0), msg="gcd(0,0) should be 0")

    def test_gcd_always_positive(self):
        # gcd(a,b) is always > 0, except gcd(0,0) is 0
        self.assertEqual(1, math.gcd(1,-1))
        self.assertEqual(1, math.gcd(-1,1))
        self.assertEqual(1, math.gcd(-1,-1))
        self.assertEqual(5, math.gcd(25,-5))
        self.assertEqual(4, math.gcd(-12,8))
        self.assertEqual(4, math.gcd(-12,-8))
        # try some relatively prime values
        self.assertEqual(1, math.gcd(-21,8))
        self.assertEqual(1, math.gcd(4,-35))
        self.assertEqual(1, math.gcd(-4,-27))

    def test_gcd_with_common_factor(self):
        self.assertEqual(5, math.gcd(100,-115))
        self.assertEqual(300, math.gcd(900,24600))
        self.assertEqual(10, math.gcd(-2520,10))
        a = 23*1001*17
        b = 19*29*17
        expect = 17
        self.assertEqual(expect, math.gcd(a,b))
        a *= 55
        b *= 5
        expect *= 5
        self.assertEqual(expect, math.gcd(a,b))
        self.assertEqual(expect*expect*expect, math.gcd(a*a*a,b*b*b))

    def test_gcd_of_big_numbers(self):
        """Test for efficient gcd calculation"""
        a = 1235*123457890123
        b = 1235*78901234589
        gcd = math.gcd(a, b)
        self.assertEqual(1235, gcd)
