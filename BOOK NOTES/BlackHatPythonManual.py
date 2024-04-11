
'''
Black Hat python - Totally not a haxor
'''

'''
########              About Python:                               ####################################
-Developed by Guido Van Rossum and was first released in 1991
-Py is known as a dynamically typed interpreted programming language
-Py is a compiled lang (Not a machine code compiled lang)
-(it instead acts like java which uses  a virtual machine and a byte code compiler)
-as the author says it: Py is a bytecode compiled programming lang, thus its title is byte code compiled, even though the resulting byte code is interpreted and the direct raw source is not
-An obj is considered to be an instance of a class where each obj has its own attr and methods
'''
 
'''
########              Python Command line interface usage/ args:                               ####################################

- (-b): issue warning about problematic byte code like mixing bytes with strings
- (-bb): sim to above but turn warning into erros
- (-B): disable the the creation of .pyc files (which are known as the compiled py code from bytecode compiler
- (-c <cmd>): execute py code as a given string is useful for running short lubes of code w/o creating or needing to create scripts
- (-d): enable parser debugging output for devs. (only useful for debugging builds/ vers and is not used for standard dev)
- (-E): Ignores py environment variables
- (-h):  prints help
- (-i):  inspect interactively after running a specified set of scripts or script. tells the interpreter to run (basically) in interactive mode., even if the input does not appear to be a terminal
- (-I):  isolate py from the users environment which implys -E and -s flags
- (-m mod): run a library as a module script
- (-0): remove assert statements and debug dependent code for optimized code generation. (also set py enviroment variables such as PYTHONOPTIMIZE=x)
- (-00): like -0 flag but also discards docstrings
- (-q): dont print version/copyright messages on interactive startup
- (-s): dont add user site directory to systems path (sys.path)
- (-S): dont add user site module during startup
- (-v): verbose mode 
- (-V): print version umber and exit (if vv then it will give more info on the build
- (-W): Control warning message base on specified format
- (-x): Skip first line of source code allowing non-unix forms and hashbangs.

'''
 
'''
########              Python Common Keywords:                               ####################################
-(if)
-(elif)
-(else)
-(for)
-(while)
-(True)
-(False)
-(with) <-- creates context manager that automatically sets up and tears down resources
-(as) <-- used to assign the result of __enter__() method with context manager to a variable from "with"
-(def) <-- method definition
-(lambda)
-(global)
-(and)
-(or)
-(not)
-(break)
-(continue)
-(pass)
-(try & except)
'''
 
'''
########            Python environment variables:                               ####################################
-(PYTHONPATH): extends the search path for python modules that will be used in projects (by default, it will search sys.path, this extends the search)
-(PYTHONVERBOSE): controls verbosity of error messages. 1/true if you want verbose py
-(PYTHONIOENCODING): sets i/o encoding for stdin/ stdout (useful when dealing with non ascii characters, like using it for utf-8 encoding)
-(PYTHONFAULTHANDLER): enable/disable fault handler (when enabled, py will give its best attempt to provide additional info about seg faults/ programmatic crashes) (SUPER HELPFUL for debugging)
-(PYTHONHASHSEED): set the random seed used for hash randomization (needed if you want same hash across same runs)
-(PYTHONDEVMODE): will enable extra dev features and give extra info during tracebacks.
-(PYTHONDUMPREFS): dumps reference variable is variable that is for debugging and understanding specific objects in a lang that might still be alive at end of program. (will py dump live obj refs during shutdown)
-(PYTHONMALLOC): (version and platform dependent) controls memory allocator py uses for mem allocation. (mem management function) 
-(PYTHONUNBUFFERED): force standard input/output/errors to be unbuffered (useful when you want to see outbput immediately. (esp in cases where output may be redirected to another file/process)
-(PYTHONDONTWRITEBYTECODE): tells py not to write pyc files or python compiled bytecode files to disk.
'''

'''
########           Python Data Types:                               ####################################
-- (str): string data type
-- (int): int type (backend converts converts to integer64 in C) (signed 64 bit intger data type from (2**63 - 1) to (-2**63))
-- (float): float type (backend converts to float64 in C due to its max hold being 1.7976931348623157 * 10^308)
   (an issue to watch for something like this: (x = 0.1 + 0.1 + 0.1) and (y = 0.3) so that (x == y) would actually be false due to the 
    nature of floating point arithmetic)
-- (complex): complex data type: (eg: 2 + 3j) (usage: x = complex(3, 4) would be (3 + 4j) or (x = 2 + 5j) would be a direct def)
   (an example of intermediate usage: COMPLEX CONJUGATE, conjugate z = a + bj would be another complex number z* which would change the
    sign of the #j. so z = a - bj (use .conjugate()) ) 
   (get magnitude of complex by using abs(complex#) )
-- (set): set data type: {1,2,3} (MUST BE ints)
-- (frozenset): immutable set 
-- (bool): bool (0's and 1's can be converted to bools)
-- (bytes): immutable sequence of bytes (binary data type) (ex usage: bytes([65,66,67]) is also b'ABC' which is the way to use bytes w/o
    using bytes() )
-- (Bytearray): mutable sequence of bytes (binary data type)
   (ex: 
   data = bytearray(b'Hello')
   view = memoryview(data)
   print(view[0]) #which is 72 which is 'H'
   )
-- (memoryview): memory view of an obj (binary data type) (view obj data in raw memory representation. Good for manipulating large amounts
    of data w/o copying the data.)
-- (dict): dictionary (essentially a map w/o a specific data types to be static as input or key and output or value data)
   (string representation: print(diction["StringKeyInDict"]))
   (method call from map: diction["Keypress@f"]() )
   (BECAUSE PY ALLOWS DICTS TO BE ANY TYPE, you can easily embed methods and directly call them to map)
-- (None): similar to null
-- (list): python's array 
   (getting elements from 1 to 2 listObj[1:2] or,
    index the list until 3 would be listObj[:3] or,
    -basic iteration:
    for val in listObj:
        print(val)
   )
-- (tuple): ex: (1,2,3)

'''

'''
########           Operators: (justa reminder)                               ####################################
- +
- -
- *
- /
- // (floor division)
- % (MOD)
- ** (Power)

-can do most symbols ahead of = to apply equals to get assignnment operators. 

########           Logical Operators: (justa reminder)                         ####################################
- and
- or
- not

########           EX Short Circuit evaluation                               ####################################
- Short Circuit evaluation means that it will only evaluate the second operand if it necessary to determine the final result
- with the example:

a = True
b = false
result = a or (b / 0)

- the above should throw a divide a zero error but since the a is true, it doesn't evaluate the b/0

########           Ternary conditional expression                               ####################################
-Allows for compact if else statements in a single line, like:
A = 10
B = 5

print ("a is greater than b" if a > b
        else "b is greater than a")
'''

'''
########           Bitwise Operators                                         ####################################
- &: (takes 2 ints and performs a bitwise and) (sets corresponding output bit to 1 only if both input bits are 1 otherwise they are set to 0)
- |: (takes 2 ints and does a bitwise or of the binary representation)(cmps each bit of 2 ints and sets the output bit to 1 if at least one of the input bits is 1
- ^: (takes 2 ints and does a bitwise exclusive or/ XOR)(cmps each bit of the 2 ints ad then set the corresponding output bit to 1 only if one of the inputs is 1
- ~: (takes 1 int and does a bitwise NOT)(Flips bits from 0 to 1 and 1 to 0)
- <<:(takes 2 ints and bitwise lefts them)(shifts bits by specified number of the second int)(effectively multiplies the first int by two raised to the power of the second int.)
- >>:(takes 2 ints and bitwise rights them)(shifts bits by specified number of the second int)(effectively divide the first int by 2 raised to the power of the second int/int on the right)
'''


'''
########           Membership/ identity operators                              ####################################


'''





