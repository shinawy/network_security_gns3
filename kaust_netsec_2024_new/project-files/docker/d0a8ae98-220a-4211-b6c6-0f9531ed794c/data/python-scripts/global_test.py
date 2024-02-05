"""
Reminder on how global works 
"""

def glob(arg=3):
    global a
    a=arg
    print("\tIn glob, a = {}".format(a))


def not_glob(arg=3):
    a=arg
    print("\tIn not_glob, a = {}".format(a))

a = 1
    
print("Before calling not_glob, a = {}".format(a))
print("Calling not_glob(2): ", end=" ")
not_glob(2)
print("After a call to not_glob(2), a = {}".format(a))
print("Calling not_glob(): ", end=" ")
not_glob()
print("After a call to not_glob(), a = {}".format(a))

print("\n*****\n")

print("Before calling glob, a = {}".format(a))
print("Calling glob(2): ", end=" ")
glob(2)
print("After a call to glob(2), a = {}".format(a))
print("Calling glob(): ", end=" ")
glob()
print("After a call to glob(), a = {}".format(a))



