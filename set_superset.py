A = set(map(int,input().split()))

n = int(input())

res = []
for i in range(n):
    temp = set()
    temp = set(map(int, input().split()))
    res += [A.issuperset(temp)]
    
if False in res:
    print("False")
else:
    print("True")
   