def maximo(A):

 max_val = A[0]

 for i in range(1, len(A)):
    if max_val < A[i]:
        max_val = A[i]
 print("máximo: ", max_val)

A = list(input("Digite: "). split())

maximo(A)
     
