def maxmin4(A, linf, lsup):
    if lsup - linf <= 1:
        if A[linf] < A[lsup]:
            return A[lsup], A[linf]
        else:
            return A[linf], A[lsup]
    else:
        meio = (linf + lsup) // 2
        max1, min1 = maxmin4(A, linf, meio)
        max2, min2 = maxmin4(A, meio + 1, lsup)
        return max(max1, max2), min(min1, min2)

A = [4, 7, 1, 4, 4, 1, 9, 6]
maior, menor = maxmin4(A, 0, len(A) - 1)
print("Maior:", maior)
print("Menor:", menor)
