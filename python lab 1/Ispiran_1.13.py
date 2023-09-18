x,y=[float(x) for x in input().split()]
a = (x**2 - (2*x*y) + (4*(y**2)))/(x+5)
b = (3*x**2 - y**2)/(y-7)
print("{:.3f}".format(a+b))
