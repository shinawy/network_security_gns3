i=[2]
class mutable_element():
      j=i
      print("j=",j)
      print("id(j)=",id(j))
      print("id(i)=",id(i))

print ("avant i=[12], id(i)=", id(i))
i=[12]
print ("after i=[12], id(i)=", id(i))
print("id(i)=", id(i))

m = mutable_element()
n = mutable_element()
print ("\n\t\tm.j = ", m.j)
print ("\t\tn.j = ", n.j)
print("id(m)=",id(m))
print("id(n)=",id(n))
print("id(m.j)=",id(m.j))
print("id(n.j)=",id(n.j))

m.j[0]=4
print ("\n\t\tm.j = ", m.j)
print ("\t\tn.j = ", n.j)
print("id(m.j)=",id(m.j))
print("id(n.j)=",id(n.j))

n.j=[6]
mutable_element.j[0]=5
print ("\n\t\tm.j = ", m.j)
print ("\t\tn.j = ", n.j)
print("id(m.j)=",id(m.j))
print("id(n.j)=",id(n.j))

#===========================


class mutable_element():
      j=i
      print("j=",j)
      print("id(j)=",id(j))
      print("id(i)=",id(i))
      
print ("avant i=[3], id(i)=", id(i))
i=[3]
print ("after i=[3], id(i)=", id(i))

m = mutable_element()
n = mutable_element()
print ("avant i=[4], id(i)=", id(i))
i=[4]
print ("after i=[4], id(i)=", id(i))

print ("\n\t\tm.j = ", m.j)
print ("\t\tn.j = ", n.j)
print("id(m)=",id(m))
print("id(n)=",id(n))
print("id(m.j)=",id(m.j))
print("id(n.j)=",id(n.j))



# ===========================================


i=[2]
print ("after i=[2], id(i)=", id(i))
class mutable_element():
      j=i
      print("id(j)=",id(j))
      print("id(i)=",id(i))
i[0]=3
print("id(i)=", id(i))

m = mutable_element()
n = mutable_element()
print ("\n\n\n\t\tm.j = ", m.j)
print ("\t\tn.j = ", n.j)
print("id(m)=",id(m))
print("id(n)=",id(n))
print("id(m.j)=",id(m.j))
print("id(n.j)=",id(n.j))



m.j[0]=4
print ("\n\t\tm.j = ", m.j)
print ("\t\tn.j = ", n.j)
print("id(m.j)=",id(m.j))
print("id(n.j)=",id(n.j))

n.j=[2]
mutable_element.j[0]=5
print ("\n\n\n\t\tm.j = ", m.j)
print ("\t\tn.j = ", n.j)
print("id(m.j)=",id(m.j))
print("id(n.j)=",id(n.j))

# ===========================================


i=2
class non_mutable_element():
      j=i
      print("id(j)=",id(j))
      print("id(i)=",id(i))
i=3
print("id(i)=", id(i))

m = non_mutable_element()
n = non_mutable_element()
print ("\n\n_n\t\tm.j = ", m.j)
print ("\t\tn.j = ", n.j)
print("id(m)=",id(m))
print("id(n)=",id(n))
print("id(m.j)=",id(m.j))
print("id(n.j)=",id(n.j))

m.j=4
print ("\n\t\tm.j = ", m.j)
print ("\t\tn.j = ", n.j)
print("id(m.j)=",id(m.j))
print("id(n.j)=",id(n.j))

non_mutable_element.j=5
print ("\n\t\tm.j = ", m.j)
print ("\t\tn.j = ", n.j)
print("id(m.j)=",id(m.j))
print("id(n.j)=",id(n.j))

# ===================

class autre:
      a=1
      b="b"
      c=[3,4]

x=autre()
x.c=[5,6]
x.a=0
print ("x", x.a, x.b, x.c)

y=autre()
print ("y", y.a, y.b, y.c)
y.b="toto"
y.c[0]=9
print ("y", y.a, y.b, y.c)
autre.b="bbbbbb"
autre.c=[7,8]
autre.a=1000
z=autre()

print ("x", x.a, x.b, x.c)
print ("y", y.a, y.b, y.c)
print ("z", z.a, z.b, z.c)
print("x.a =", id(x.a), "y.a =", id(y.a), "z.a =", id(z.a)) 
