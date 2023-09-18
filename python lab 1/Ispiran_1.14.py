x,y=[float(x) for x in input().split()]
a=(2*x*y)/(((x**2)+(y**2))**0.5)
b=((x+y-1)**2)/(x*y)
print("{:.3f}".format(a-b))
