<<<<<<< HEAD
#Error handling in Python is done through the use of exceptions that are caught in  try blocks and handled in except blocks.
#common exception --> IOError, ImportError, ValueError,KeyboardInterrupt, EOFError

try:
    print (a)
except:
    print ("The value of variable is not defined")

try:
    import mymodule
except ImportError:
    print("NO module found")
=======
#Error handling in Python is done through the use of exceptions that are caught in  try blocks and handled in except blocks.
#common exception --> IOError, ImportError, ValueError,KeyboardInterrupt, EOFError

try:
    print (a)
except:
    print ("The value of variable is not defined")

try:
    import mymodule
except ImportError:
    print("NO module found")
>>>>>>> 67b0bcef29fcd49d9c0e591008d5592b54882303
