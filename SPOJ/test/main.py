N = 50
A = [35, 37, 707, 447, 335, 458, 340, 342, 168, 220, 466, 123, 452, 365, 77, 483, 356, 618, 955, 820, 63, 375, 417, 121, 833, 666, 185, 540, 692, 680, 810, 596, 207, 694, 91, 65, 51, 40, 749, 382, 108, 512, 920, 802, 778, 954, 301, 530, 856, 560]

tmp = [None] * N

def ms(low, hi):
    if low < hi - 1:
        mid = low + ((hi - low) >> 1)
        ms(low, mid)
        ms(mid, hi)
        m(low, mid, hi)

def m(low, mid, hi):
    for i in range(low, hi):
        tmp[i] = A[i]

    l, r = low, mid

    for i in range(low, hi):
        if l == mid:
            A[i] = tmp[r]
            r += 1
        elif r == hi:
            A[i] = tmp[l]
            l += 1
        else:
            if tmp[l] <= tmp[r]:
                A[i] = tmp[l]
                l += 1
            else:
                A[i] = tmp[r]
                r += 1

def main():
    # print(A)
    ms(0, len(A))
    print(A)
    
main()