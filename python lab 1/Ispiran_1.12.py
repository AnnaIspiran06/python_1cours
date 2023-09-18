x1,y1,x2,y2,a=[float(el) for el in input().split()]
x=(x1+a*x2)/(1+a)
y=(y1+a*y2)/(1+a)
print("{:.2f}".format(x),"{:.2f}".format(y))
