from glob_var import *
from myglob import *
global a, b, c, d, e
a=["initial a"]
b=["initial b"]
d=["initial d"]
e=["initial e"]



print ("MAIN:  a={}".format(a))
print ("MAIN:  b={}".format(b))
print ("MAIN:  c={}".format(c))
print ("MAIN:  d={}".format(d))
globa(e)
print ("\nback from GLOBA: a={}....Changes have been lost !".format(a))
print ("back from GLOBA: c={}.... Yes c is global across module !".format(c))
print ("back from GLOBA: d={}.... Changes have been lost".format(d))
print ("back from GLOBA: BUT, oh surprise .. changes are in \"e\" in fact: e={}".format(e))
print("The reason is that arguments are passed by reference not by value !!!")


def globb():
    global b
    global c
    d=[]
    global f
    f=["just created in GLOBB"]
    g=["just created in GLOBB"]
#   Does the variable b exist here? 
    b_exists = 'b' in locals() or 'a' in globals() 
    if b_exists:
        b.append("appended in globb")
    else:
        b=["created in globb"]
    print("\n== GLOBB: new assignment made to b,  b={}".format(b))
    print("== GLOBB: we also see c={}".format(c))
    c.append("appended in GLOBB")
    print("== GLOBB: new assignment made to c: c={}".format(c))    
    print("== GLOBB: we also see d={}".format(d))
    d.append("appended in GLOBB")
    print("== GLOBB: new assignment made to d: d={}".format(d))    
    print("== GLOBB: we also see e={}".format(e))
    e.append("appended in GLOBB")
    print("== GLOBB: new assignment made to e: e={}, (!!!PAY ATTENTION HERE!!!)".format(e))    

globb()
print ("\nback from GLOBB: b={} ... Changes kept!".format(b))
print ("back from GLOBB: c={} ... Changes kept! !".format(c))
print ("back from GLOBB: d={} ... Changes NOT kept!".format(d))
print ("back from GLOBB: e={} ... Surprise .. Changes kept!".format(e))
print ("Note that e was NOT defined as \"global\" in globb() ... yet changes to it in globb() seem to be global")
print ("The reason is that e is not DEFINED within globb() yet visible in it. Therefore scope of changes to it extends outside globb()")
print("Compare this situation with the variables f and g DEFINED in globb().")
print("f has been declared as global whereas g was not")
print("As a result",end=" ")
f_exists= 'f' in locals() or 'f' in globals()
g_exists= 'g' in locals() or 'g' in globals()

if f_exists:
    print ("f exists outside globb(), f={}".format(f), end=" and ")
else:
    print("f does not exist outside globb()", end=" and ")
if g_exists:
    print ("g exists outside globb(), g={}".format(g))
else:
    print("g does not exist outside globb()")
    
print ("\nbefore going to GLOBC, reminder: ")
print("a = {}".format(a))
print("c = {}".format(c))
print("I can modify c in the main program, it will be seen outside")
c.append("appended in main")
print("MAIN: new assignment made to c: c={}".format(c))
globc()
print ("\nback from GLOBC: a={} ..!".format(a))
print ("back from GLOBC: c={} . !".format(c))

print("\n and now, the grand finale ..")
print("That should confuse those of you who have not practiced python enough!")
print("Let us shorten the variable \"c\" first")
c=["a fresh new start"]
print("c = {}".format(c))
print("Let us call globc() just as before ...")
globc()
print ("\nback from GLOBC: a={} ..!".format(a))
print ("back from GLOBC: c={} . !".format(c))
print("Hopefully, you have seen the differences and understand what causes them")

      



