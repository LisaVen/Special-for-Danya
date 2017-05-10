__author__ = 'student'

a = list(map(int, input().split()))
m = 0
c = 0
for i in range(len(a)):
    if a[i] > m:
        m = a[i]
for i in range(len(a)):
    if a[i] == m:
        c += 1
print(m, c)
