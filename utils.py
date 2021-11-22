
from sympy import Matrix

def Kron(A, B):
    return Matrix( \
        [[ A.row(i//B.rows)[j//B.cols]*B.row(i % B.rows)[j % B.cols] 
        for j in range(A.cols * B.cols) ] \
        for i in range(A.rows * B.rows)] \
        )
    