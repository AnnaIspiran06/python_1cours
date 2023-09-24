a , b , c = [int(el) for el in input().split()]
d = ((b**2) - (4*a*c))
if d < 0 :
    print("No roots")
elif d==0 :
    x = (-b)/(2 * a)
    print("One root:",int(x))
elif  d > 0 :
    x1 = ((-b) - (d**0.5)) / (2 * a)
    x2 = ((-b) + (d**0.5)) / (2 * a)
    if x1 > x2 :
        print("Two roots:",int(x2),int(x1))
    else :
        print("Two roots:",int(x1),int(x2))
