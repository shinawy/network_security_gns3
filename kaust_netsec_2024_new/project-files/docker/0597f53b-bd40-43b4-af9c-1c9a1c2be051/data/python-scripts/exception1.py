import sys

try:
     x = input("Please enter a number: ")
     y = x * 3
     print "Correct execution: ", y, "is the triple of", x
     y = x + 2
     print "Correct execution: ", y, "is equal to ", x, " + 2"
     
except(RuntimeError, TypeError), instance:
     print "Runtime or TypeError", instance
except(NameError), instance:
     print "NameError, undefined variable encountered: ", instance
# except:
#      print "undefined exception", sys.exc_info()[0]
else:
     print "This is printed if no exception has been caught"
finally:
     print "This is printed wether an exception has been caught or not"

print "This is printed if the execution has not been interrupted before"
