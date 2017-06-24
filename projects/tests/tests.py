from django.test import TestCase

# Create your tests here.

class TemporalTEst(TestCase):

    def test_dummy_always_True(self):
        """
        This tests never fails
        Needed to test the tests tools works
        """
        self.assertNotEquals("Expected", "Actual", "Dummy test")