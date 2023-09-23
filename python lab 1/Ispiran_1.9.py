a,b,n=[int(el) for el in input().split()]
cost= a*100+b
cost *= n
hrn=cost // 100
cop=cost % 100
print(hrn , cop)
