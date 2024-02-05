"""
Simplest example of the use of os.fork()
(Python3 syntax)
"""

import os
if os.fork()==0:
        print("Child process")
else:
        print("Parent process")

        



