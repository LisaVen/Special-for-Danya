__author__ = 'student'


def quicksort(a, l, r):
    if (r > l):
        v = a[r]
        i = l - 1
        j = r
        while True:
            i = i + 1
            j = j - 1
            while(a[i] < v):
                i = i + 1
            while (a[j] > v):
                j = j - 1
            if (i >= j):
                break
            a[i], a[j] = a[j], a[i]
        a[i], a[r] = a[r], a[i]
        quicksort(a, l, i - 1)
        quicksort(a, i + 1, r)

ary = list(map(int, input().split()))
quicksort(ary, 0, len(ary)-1)
print(ary)
