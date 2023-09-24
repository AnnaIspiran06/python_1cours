x=int(input())

k = x % 2 == 0
m = x < 0 and x % 3 == 0

if k != m:
    print("YES")
else:
    print("NO")
