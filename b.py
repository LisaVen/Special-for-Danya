__author__ = 'student'

a = list(map(int, input().split()))
notok = True
while notok:
    notok = False
    for i in range(len(a)-1):
        if a[i+1] > a[i]:
            a[i], a[i+1] = a[i+1], a[i]
            notok = True
print(a)
