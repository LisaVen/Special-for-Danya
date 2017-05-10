__author__ = 'student'

a = list(input())
pal = True
for i in range(len(a)//2):
    if a[i] != a[len(a)-1-i]:
        pal = False
if pal == True:
    print('YES')
else:
    print('NO')
