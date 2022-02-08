import  unittest
from binary_search import binary_search 

class TestBinarySearch(unittest.TestCase):
    def testBinarySearch(self):
        self.assertEquals(binary_search([2,3,1,4],2),1)

if __name__ == '__main__':
    unittest.main()
    