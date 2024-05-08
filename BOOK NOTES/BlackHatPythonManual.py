
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
########           Python Data Types w/ methods and supported operators:            ####################################
-- (str): string data type 
   (Supported Operators: Concatenation (+), Repetition (*), Indexing ([]), Slicing ([:]), Membership (in))
^^^(Supported Methods: .capitalize(), 
                       .casefold(): Like lower but VERY aggressive. esp for non ascii characters 
                       .center(width,"fillchar"): returns a centered string with a specified width
                       .count(): count the amount a substring will appear w/in the string/ value.
                       .encode(): encoding type of the text or string will that is being outputted it formatted. (Default 
                                  is utf-8 
                       .endswith(): returns a bool
                       .expandtabs(): set tab size of string based on the escape sequence position.
                       .find(): if found, return the output position, else return -1.
                       .format(): (if you dont want to f char before every string) 
                        ex usage: x = "This is {}"
                                  print( x.format("a test.") )
                       .index(): will get the index of a char w/in a string (first instance only) returns -1 if none found
                       .isalnum(): is alpha numeric number. (ret bool)
                       .isalpha(): is it only letters from the alphabet. (ret bool)
                       .isascii(): checks if ascii. (ret bool)
                       .isdecimal(): is string a decimal number (ret bool)
                       .isdigit(): is string all digits (ret bool)
                       .islower(): is all the characters lowercase (ret bool)
                       .isnumeric(): is all characters a number (ret bool)
                       .isprintable(): is the string printable (not fillied with inv spaces/ weird chars that may 
                        break or malform the output (ret bool)
                       .isspace(): is the string spaces or not (ret bool)
                       .istitle(): Does the string follows the rules for a title. (capitals, punc) (ret bool) 
                       .isupper(): is string upper (ret bool)
                       .join() takes a list or elements of an iterable and will join together by string itself
                        (ex usage print( "-".join(x)) where x = ["1","2","3"]
                       .ljust() justifies string left
                        (ex usage: t = "thisString"
                                   print(t.ljust(len(t)+10), "+") # justified by 10 more pos
                       .lower() ...
                       .lstrip(): strips left. ( by a specific set of chars or a single char.)
                       .maketrans(): make a translation table.
                        (that is: translation table/ translation mapping is a data structure that is used to map chars in
                        one form to their corresponding character in another form.)
                        (In the case of python: a translation table is represented as a mapping between unicode ordials
                        , which are int representations of chars, to their unique replacements.)
                       .translate() applies the .maketrans()
                        (THIS IS APPLIED OF THE LAST 2:
                          table = str.maketrans('', '', 'aeiou')
                          t= "this string"
                          translated = t.translate(table)
                          print(translated)
                       .partition(): breaks a string into three parts based on separator 
                        (rets a tuple)
                       .replace() (find string, replace with) (2 args)
                       .rfind(): search entire string for substring and return the last position it was found.
                        (ex usage:
                         text= "An apple, An orange"
                         print( text[text.rfind("An"):] # outputs from last pos of "an" to end of str
                       .rindex() Like rfind, but return the position excluding the search string (so for the example 
                         aboce, it would only return " orange"
                       .rjust(): like ljust but going right
                       .rpartition(): same as partition() but will do the last example in the string.
                       .rsplit(): splits a string at specified separator, but will start right and return a list of 
                         all the split vals
                       .rstrip(): returns a right-trimmed version of the string but also removes trailing chars
                       .split(): splits a string by a char/ breakpoint and returns a list of the broken string
                       .splitlines(): splits a string w/o input. (breaks at line breaks/escape sequences)
                       .startswith(): (rets bool) check if string starts with specific inputs
                       .swapcase(): swaps cases. upper to lower/ lower to upper
                       .strip(): removes leading/trailing chars. (ex:"+-" would remove all of those chars from head/end)
                       .title(): converts string to title standards (first letter of each word is capitalized)
                       .upper(): convert string to upper
                       .zfill(): add number of leading zeros to a string
                       .isidentifier(): will check if a specific type or classor set of data is an identifier
                       _____
                       _____
                       
   
-- (int): int type (backend converts converts to integer64 in C) (signed 64 bit intger data type from (2**63 - 1) to      (-2**63)) 
   (Supported Operators: +, -, *, /, //, **, +=, -=, *=, /=,//=, %=)

-- (float): float type (backend converts to float64 in C due to its max hold being 1.7976931348623157 * 10^308)
   (an issue to watch for something like this: (x = 0.1 + 0.1 + 0.1) and (y = 0.3) so that (x == y) would actually be false due to the systems handling of floating point arithmetic) 
   (Supported Operators: SAME AS INT but ADD, +=, -=, *=, /=)

-- (complex): complex data type: (eg: 2 + 3j) (usage: x = complex(3, 4) would be (3 + 4j) or (x = 2 + 5j) would be a direct def)
   (an example of intermediate usage: COMPLEX CONJUGATE, conjugate z = a + bj would be another complex number z* which would change the sign of the #j. so z = a - bj (use .conjugate()) ) 
   (get magnitude of complex by using abs(complex#) )
   (Supported Operators: +, -, *, /, **)

-- (set): set data type: {1,2,3} (MUST BE ints) (Mutable unordered collection of unique elements) 
   (Supported Operators: Membership (in))
^^^(Supported Methods: .update(): will update the set with another set or any other iterable type
                       .union(): rets a set containing the union of sets
                       .symmeteric_difference_update): will update the symmetric diffs from one set to another set.
                        (the sym diff refers to the elements that are unique to each set, excluding the elements that are common btwn them)
                       .symmetric_difference: ret a set w/ the sym diff of 2 sets
                       .issubset(): rets whether another set contains this set or not
                       .isdisjoint(): ret a bool if 2 sets have an intersection or not
                       .discard(): rms specified element from the set if it is present
                       .difference_update(): will rm the items in the set that are also included in one or more specified sets
                       .difference(): rets the set containing the diff betweem one set and the other set given
                       .copy(): rets a copy of the set
                       .add(): add an element to a set
                       .clear(): remove everything from the set
                       .intersection(): ret a set that is the intersection of curr set being interected w/and one other set
                       .intersection_update(): this will basically rm the items in the set that are not present in one or more other 
                        specfied sets
                       .issuperset(): current set contains another set or not
                       .pop(): remove then ret an arb element from set
                       .remove(): rm a specified element from set (if element is not found/ keyerror will be raised)
)

-- (frozenset): immutable set 
   (Supported Operators: Membership (in))

-- (bool): bool (0's and 1's can be converted to bools)
   (Supported Operators: Logical operators( and/ or/ not) Comparison( ==, !=, <, >, <=, >=)

-- (bytes): immutable sequence of bytes (binary data type) (ex usage: bytes([65,66,67]) is also b'ABC' which is the way to use bytes w/o using bytes() )
   (Supported Operators: )

-- (Bytearray): mutable sequence of bytes (binary data type)
   (ex: 
   data = bytearray(b'Hello')
   view = memoryview(data)
   print(view[0]) #which is 72 which is 'H'
   )
   (Supported Operators: )

-- (memoryview): memory view of an obj (binary data type) (view obj data in raw memory representation. Good for manipulating large amounts
    of data w/o copying the data.)
   (Supported Operators: )

-- (dict): dictionary (essentially a map w/o a specific data types to be static as input or key and output or value data)
   (string representation: print(diction["StringKeyInDict"]))
   (method call from map: diction["Keypress@f"]() )
   (BECAUSE PY ALLOWS DICTS TO BE ANY TYPE, you can easily embed methods and directly call them to map)
   (Supported Operators: Indexing([key]), Membership (in))
^^^(Supported Methods: .clear(): remove all elements from dict
                       .values(): dump all values in the dict
                       .keys(): will dump all keys
                       .pop(): will remove a key and ret its associated val (if no key found, rets default val or error if no default)
                       .popitem(): ret arbitrary key/val pair from the dict. (RETS A TUPLE)
                       .setdefault(): will ret a val for a specified key. (if key not found, inserts the key with 'default' val)
                       .items(): rets a view obj called dict_items which has key-value pairs of the dict as tuples.
                       .get(): ret the val for a specfic key. (If key not found, ret default val or none if default isnt there)
                       .fromkeys(): rets a new dict with specific keys and the specified val for ea key.
                       .copy(): ret a copy of the dict
                       .update(): will update the dict w/a specified key-val pair


)

-- (None): similar to null

-- (list): python's array (mutable ordered sequence)
   (getting elements from 1 to 2 listObj[1:2] or,
    index the list until 3 would be listObj[:3] or,
    -basic iteration:
    for val in listObj:
        print(val)
   )
   (Supported Operators: Concatenation (+), Repetition (*), Indexing ([]), Slicing ([:]), Membership (in))
^^^(Supported Methods: .append(): add to the end of the list
	.clear(): clears list
	.copy(): copy then return the list
	.count(): count the number of times an item is in a list
	.extend(): will extend the list using another iterable data type such as dict/tuple/etc. (if you merge data that
	  you already merged or if the data already exists. py will not throw an error)
	.index(): returns an indexable position of the value that you index. (error will be thrown if it doesn't exist)
	.insert(): (element, position).
	.pop(): empty pop takes out last element from array, otherwise pops specified pos
	.remove(): remove element from array
	.reverse(): reverse the list
	.sort(): sorts list in acending order unless reverse = True
)

-- (tuple): ex: (1,2,3) (immutable ordered sequence)
   (Supported Operators: Concatenation (+), Repetition (*), Indexing ([]), Slicing ([:]), Membership (in))
^^^(Supported Methods:  .index(): ret the index of spec val in tuples
                        .count(): count how many times a val appears in a tuple
)

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
########           Membership and identity operators                              ####################################
- both return bools based on results
- Membership operation: test whether or not an value is in a sequence
- Identity Operations: test whether 2 objects refer to the same memory location. (indicates same obj/type)
- in: (Membership Operator)
- not in: (Membership Operator)
- is: (Identity Operator)
- not is: (Identity Operator)

'''

'''
##################                       Conditionals                             ####################################
-(PEP 622)
- *** SKIPPING SIMPLE ONES ***
- Dictionary based switching (dict as switch): can create own version of a switch case like so:
________________________________________________________________________________________
def f_1():
   print("func 1")

def f_2():
   print("func 1")

switch = {1: f_1, 2: f_2}

num = 1

switch.get(num, lambda: print("invalid case"))()
# output: func 1
________________________________________________________________________________________

-ternary operator: short in line if else. ex:
________________________________________________________________________________________

x = 10
result = "greater or equal" x >= 10 else "less"
print(result)
#output: greater or equal
________________________________________________________________________________________

-match case: (sim to switch case) but have no fail through behavior/ support pattern matching/ have much more diff evals where the first
 case that is matched will release the execution step to execute only the corresponding block of code.
-- (PY 3.10 and NEWER ONLY!)
-- (possibly vgood for specific scenarios only???)
-- Ex:
________________________________________________________________________________________
def checker(x):
   match x:
      case 1:
         print("one")
      case 2:
         print("two")
      case _:
         print("other")

checker(1)
#output: one
________________________________________________________________________________________

-(any and all) keywords
-- EX usage:
x = [10, 20, 30, 40]

if any(number > 30 for number in x):
   print("numbers above 30 exist")

if all( number >= 10 for number in x):
   print("all numbs above/equal 10")


'''

'''
##################                       for loops                             ####################################
-basic for loops: (ex: take a list, use it for loop then followed by var name/ followed by in keyword/ then variable to loop over)
-- ex usage:
___________________________________________________
num = [1,2,3,4,5]

for number in num:
   print (str(number))
___________________________________________________

-for loop with range:
-- (for var in range(#))

-Enumerate function usage:
-- enumerate: iterate over a specific iterable such as a list while also keeping track of the index or position each element w/in that 
   iterable object
-- (enumerate rets a tuple so it cant be read only and not changed)
-- EX USAGE:
___________________________________________________
x = ["data1", "data2", "data3"]

for index, value in enumerate(x):
   print(str(index) + "has val of: " + str(value))
# Output: 0 has val of: data1
# etc
___________________________________________________

-list comprehension: (you cam execute an operation/ technique known as list comprehension, this allows you to create a list from another list)
-- ex usage:
___________________________________________________
square = [x**2 for x in range(5)]

print(square)
___________________________________________________

-using else w/in loops:
-- The point of using an else in a for loop is to ensure that another statement or block is executed directly after the for loop is 
   executed or when a break statement happens w/in the loop as well
-- else statements can also be used to also check for errors after the iteration rather than just continuing the execution of the
   program directly

-parallel iteration:
-- you can iterate over two or more iterables/ sequences simultaneously allowing you to process their corresponding elements all together
-- code snippet with zip and enumerate to demonstrate this:

user = ["A", "B", "C"]
number = [10, 20, 30]

for idx, (name, num) in enumerate(zip(user, number)):
   print(f"Person {idx+1}: {name}, {num} points.")
# output: Person 1: A, 10 points.

'''

'''
##################                    While Loops                             ####################################
- else while: if the condition is false then execute this code. (when the loop is done executing, execute/eval the next block)
- `Continue` / `break` with while loops:
- `Try` and `except` with while loops: these keywords are to tell py to to make an attempt to execute a specific block of code under the try
   and if something happens, go to the except and except the error and handle it under that block
   EX:
------------------------------------
name = ""

while name == "":
   try:
      name = input("Name? ")
   except: ValueError:
      print("input error")
else:
   print("The name is:", name)
-------------------------------------
- complex conditions with while: that us AND or OR in it. (while x <= 10 and y <= 5)

'''


'''
################################           importing modules                        ####################################
- import package (generic import)
- import function from package (import from. allows to save on performance)

-import externally: before the script is run we can include the modules before it is run.
--ex:
--------------------------------------------------------
def greet(name):
   print(f"This is, {name}.)

if __name__ == "__main__":
   import sys
   if len(sys.argv) > 1:
      name = sys.argv[1]
      greet(name)
   else:
      print("needs args")
#input ex: python3 -m bools Me
# output This is, Me.
--------------------------------------------------------

- Conditional importing: (case: that building framework and need imports based on reqs or specific conditions)
--------------------------------------------------------
import importlib.util

if importlib.util.find_spec("math"):
   import math
else:
   print("Not found")
   quit()
--------------------------------------------------------

-Dynamic Importing: you can either format text or __import__
-- the second isnt preferred since it should only be used in cases where you need to directly interface with the import call
-- EX:
-----------------------------------------------------------------------------------------------
module_name2 = "math"
olderImport = __import__(module_name2)

print(olderImport.tan(1.5))
-----------------------------------------------------------------------------------------------

-using import hooks:
-- is a mechanism to customize the behavior or an import statement and gives you the ability to intercept/mod  the process of 
   importing those modules
-- V useful when loading modules from nonstandard locations or  even perform custom actions during those imports

- Module caching and reloading: 
-- When importing modules, py will cache the module to avoid the unnecessary reimporting of  that module. (for various reasons like avoiding conflicts/ bloat)
-- (but if you want to force reload/ reimport of a module, you can use `reload()` func from  `importlib` standard library)
-----------------------------------------------------------------------------------------------
import math
import importlib

importlib.reload(math)
-----------------------------------------------------------------------------------------------

-abs vs relative importing:
-- `absolute` is the full pathfrom the project root of the mod
-- `relative` to current module
'''

'''
##################             Import hooking / modification                    ####################################

-Pys step by step system to find/ load moduels when an import statement is being parsed or executed
--1. Search for module built in: (to make sure that py module you want to import is not related or exactly a std imp)
--2. check if module being imported/ read is in the module cache. (used to avoid redundant imports)
--3. if module was no found in cach. py will check if the directory was listed in sys.path directory

--^^^-- after the 3 steps: py will then load the module and execute its code to define its contents then return to the execution of the 
        program
--(the point of an import hook) is to intervene at specific points during the import process and then customize the way modules are 
  loaded/ executed/ searched for/ located/ read.

- (TYPES OF IMPORT HOOKING):
-- Meta Path Hooking: allow you to customize the way py will search for modules and add new directories/ archives to import path
                      (comes in handy when you need to change where importer is working)
-- Path Entry Hooking: more fine grain control over the modular seaching process. (allowed to customize the way directories are searched
                       for/ modules using diff algorithms or even using own search methods.) (Can speed up import process alot)
-- Loader Hooking: allows for user to customize the way the modules are loaded which can help when user who want to define custom loader
                   to load the modules code from non standard locations and perform custom transformations
-- Bytecode Hooking: allows users to load pre compiled py bytecode/ is another sub-type of loader hooking

- (Sys and OS modules):
-- system and os give users access to functions that can work directly w/ system such:
^^- path manipulators/ sys args/ sys funcs/ execution/ readers/ more.
-- sys modules also allows us to interact w/ py interpreter/env which sys gives access to.

-(importlib):
-- used for low level manipulation of import process. Used to interact/intercept specific parts of the import process w/in py.

'''








'''
##################                       Conditionals                             ####################################



'''