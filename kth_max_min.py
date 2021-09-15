def kth_min_max(A, k):
    A = sorted(A)
    kth_min = A[k-1] 
    kth_max = A[-k] 
    return (kth_min, kth_max)