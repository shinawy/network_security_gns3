import sys

def my_func(val1,val2=0):
    """
    simplest function possible that simply returns its args as a tuple
    """
    
    return(val1,val2)

# a list of list containing args to be submitted each followed by its
# corresponding expected result
# args are strings
# expected results are tuples
arg_and_res=[["(1,2)", (1,2)], \
           ["(1)", (1,0)], \
           ["(val2=2, val1=1)", (2,1)], \
           ["(truc=3, blob=5)", "error"], \
           ["(2, val1=1)", (1,2)], \
           ["(1, val2=2)", (1,2)]\
]

                  

# loop over all args to submit
for counter in range(0, len(arg_and_res)):
    try:
        result=eval("my_func" + arg_and_res[counter][0])
        
        # in Python3, print() accepts an "end=" arg. ; not in Python2
        print ("my_func" + arg_and_res[counter][0], "=", arg_and_res[counter][1], "is ", end="\t") 

        if result == arg_and_res[counter][1]:
           print("CORRECT")
        else:
           print("ERRONEOUS: correct answer is ",  result)

    except(TypeError) as instance: #!!! Python3 specific syntax
#    except(TypeError), instance: #!!! Python2 specific syntax        

        print ("\nTypeError raised \n", instance)
        print ("These arguments are incorrect: ", arg_and_res[counter][0], "\n")



