x = int(input())
x1 = x // 100
a1 = x % 10
if x1 > a1:
    print(x1)
else:
    if x1 < a1:
        print(a1)
    else:
        print("=")
