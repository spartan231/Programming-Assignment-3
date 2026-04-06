import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.PA_3 import FindMaxVal, FindSubsequence
def test():
    A = "AACB"
    B = "CAAB"
    v = {'A': 2, 'B': 4, 'C': 5}
    max_val, OPT = FindMaxVal(A, B, v)
    print(max_val)
    subsequence = FindSubsequence(OPT, A, B, v)
    print(''.join(subsequence))
test()