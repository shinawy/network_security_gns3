from glob_var import *


def globa(arg1):
    d=arg1
    global a
#   If you do not put the following global you
#   will have an error. do you know why? 
    global c
# next line causes an error ... do you know why?
#   print("\n>>> GLOBA: a=:{}".format(a))

#   Does the variable a exist here? 
    a_exists = 'a' in locals() or 'a' in globals() 
    if a_exists:
        a.append("appended in globa")
    else:
        a=["created in globa"]
    print("\n>>> GLOBA: new assignment made to a,  a={}".format(a))
    print(">>> GLOBA: we also see c={}".format(c))
    print(">>> GLOBA: we also see d={}".format(d))
#   if you remove the next line, you could also remove
#   the preceding "global c" line and, now, you will not
#   have an error. do you know why? 
    c.append("appended in globa")
    print(">>> GLOBA: new assignment made to c,  c={}".format(c))
    d.append("appended in globa")
    print(">>> GLOBA: new assignment made to d,  d={} (!!! PAY ATTENTION HERE!!!)".format(d))
    
def globc():
    print("\n****** GLOBC: c is visible as  c=:{} ".format(c))
    c.append("appended in globc")
    print("****** GLOBC: new assignment made to c: c={}".format(c))
    print("****** GLOBC: we also see a's value: a={} (!!! PAY ATTENTION HERE!!!)".format(a))
    a.append("appended in globc")
    print("****** GLOBC: new assignment made to a: a={} (NOTE that \"initial a\" is gone)".format(a))
