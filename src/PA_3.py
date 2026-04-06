def FindMaxVal(A, B, v):
    m = len(A)
    n = len(B)
    OPT = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        OPT[i][0] = 0
    for j in range(n+1):
        OPT[0][j] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            curr_A = A[i-1]
            curr_B = B[j-1]
            if curr_A == curr_B:
                take_match = OPT[i-1][j-1] + v[curr_A]
                OPT[i][j] = max(take_match, OPT[i-1][j], OPT[i][j-1])
            else:
                OPT[i][j] = max(OPT[i-1][j], OPT[i][j-1])
    return OPT[m][n], OPT

def FindSubsequence(OPT, A, B, v):
    i = len(A)
    j = len(B)
    subsequence = []
    while i > 0 and j > 0:
        curr_A = A[i-1]
        curr_B = B[j-1]
        if curr_A == curr_B and OPT[i][j] == OPT[i-1][j-1] + v[curr_A]:
            subsequence.append(curr_A)
            i -= 1
            j -= 1
        elif OPT[i][j] == OPT[i-1][j]:
            i -= 1
        else:
            j -= 1
    return subsequence[::-1]

def main():
    A = "AACB"
    B = "CAAB"
    v = {'A': 2, 'B': 4, 'C': 5}
    max_val, OPT = FindMaxVal(A, B, v)
    print(max_val)
    subsequence = FindSubsequence(OPT, A, B, v)
    print(''.join(subsequence))

if __name__ == "__main__":
    main()