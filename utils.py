from sympy import Matrix


def Kron(A, B):
    return Matrix(
        [[A.row(i // B.rows)[j // B.cols] * B.row(i % B.rows)[j % B.cols]
          for j in range(A.cols * B.cols)]
         for i in range(A.rows * B.rows)]
    )
def genSubset(s):
    res = []
    now = s
    while(now):
        res.append(now)
        now = (now - 1) & s
    res.append(now)
    return res

def mapBit(x, s, mapp):
    for i in range(len(mapp)):
        s |= ((x >> i) & 1) << mapp[i]
    return s
