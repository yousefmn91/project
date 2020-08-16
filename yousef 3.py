r=float(input("Inter a radius= "))
h=float(input("Inter a height= "))
p=3.14
a_c=p*r**2
v=a_c*h
a_cy=2*p*r*h+2*p*r**2

print("Area of circle is {}".format(a_c))
print("Volume of cylindrical is {}".format(v))
print("Area of cylindrical is {}".format(a_cy))
