import re

# Thoughts on thinking: going over who might be using your software allows you to 
# to identify the qualitites of the software you want to build out.
# (with common aspects like, speed, integrity, resources, security/ emphasis on CIA Triad probably)
# and these can bring out a common outcome like:
# -Loose Coupling: components aren't intricately dependant on one another
# -Intuitability: Developers can develop the nature of the sodtware and how it works by reading it
# -Flexibility: How well developers can adapt the software to relate or similiar tasks
# -Extensibility: Devs can add/change one aspect of the software without affecting other aspects

# Refactoring: the proccess of updating code to reflect your latest/best practices. Difficulty lies in the when should you
# (a good start on the path to making a workflow more robust is to split it's logical steps up) 
# (If each step is handled by it's own service, the service for a particular step only needs to concern...
# itself with one job.)
# ---KISS... break down systems into simplier ones

#an example of code through the process of becoming more efficent (us capitals):
us_capitals_by_state = {
'Alabama': 'Montgomery',
'Alaska': 'Juneau'
}
capitals = us_capitals_by_state.values()
#capitals.sort () leads to an error in this example ON PURPOSE
sorted(capitals)

#leads to a more efficent version that is placed in a function wrapper to be quickly reused
def get_us_capitals_by_state():
    us_capitals_by_state = {'Alabama': 'Montgomery', 'Alaska': 'Juneau'}
    capitals = us_capitals_by_state.values()
    return sorted(capitals)

#We can make it more concise after looking at it, there is mainly consistent and a bit of calculations:
#(and at this point, we don't need to keep it as a function)
us_capitals_by_state = {'Alabama': 'Montgomery', 'Alaska': 'Juneau'}
us_capitals = sorted(us_capitals_by_state.values())

#***CHAPTER 2***

#Python will explictly create a namespace for your modules you make. where as other languages would need to be
#done implicity.

#So, creating a python module would create an additional namespace for that module.
# an example of this would be a "sales_tax.py" is a (sales_tax) module 
#snippet is a follows:

#sales_tax.py
def add_sales_tax(total, tax_rate):
    return total * tax_rate

#Snippet end

#Each module has a global namespace. Functions/classes/variables that aren't nested inside are 
#in the modules nested namepace 

#snippet as follows:

#sales_tax.py
tax_rates_by_states = { 'MI': 1.06} #assuming its filled to the max with data. This is global

def add_sales_tax(total, state)
    return total * tax_rates_by_states[state] #uses the global

#end snippet

#now with a local variable on the function
#snippet as follows:

#sales_tax.py
tax_rates_by_states = { 'MI': 1.06} #assuming its filled to the max with data. This is global

def add_sales_tax(total, state)
    tax_rate =  tax_rates_by_states[state] #uses the global and makes it private
    return total * tax_rate 
    
#end snippet

#now we can import a global namespace so that we can use it
#snippet as follows:

#receipt.py
from sales_tax import add_sales_tax
def print_receipt():
    total = ...
    state = ...
    print(f'TOTAL: {total}')
    print(f'AFTER TAX:  {add_sales_tax(total, state)})
#end snippet:

#Conflicting names start local and move up to namespace

#When you get a NameError: name "..." not defined, it either can't be found in any namespace or 
#is assigned somewhere else and needs to be imported

#You can import everything from a module 1 by 1 or just import the module
#so "import item" is good and can be used by doing item.function()

#you can get import crashes though. like "from time import time" and from datetime import time"
#time.time() returns the current unix time where datetime.time() returns a time instance that defaults to midnight
#14503159.3109953 vs 00:00:00
#In these times of conflict, you have to include the namespace in order to let the interperter know which one you are 
# asking for. if not, python will default to the most recent definition it knows about




## CLASSESS
# -you can use classes to create objects, or instances of of the class that have the data and behaviors defined in the 
#  class
# -The data becomes the state of the object
# -The data composes the attributes of the object because the data is attributed to the object in question
# -The behaviors become methods (they receive the object instance as an additional argument, self)
#  Allowing the methods to change the instances state or just plain old access it.

# Constructor is used to create an instance of the class (__init__) (accepts 1 arg of self min)
#***********
# GOING THROUGH ROCK PAPER SCISSORS BEING REFACTORED AND DECONSTRUCTED. need to add for pointers
import random

options = [ 'rock', 'paper', 'scissors']

class RPSSim:
    def __init__(self):
        self.computerChoice = None
        self.playerChoice = None
    
    def getComputerChoice(self):
        self.computerChoice = random.choice(options)
    
    def getPlayersChoice(self):
        numberChoice = int(input('Enter the number of your choice: '))
        self.playerChoice = options[numberChoice -1]
    
    def printOptions(self):
        print('\n'.join(f'({i}) {options.title()}' for i, option in enumerate(options)))
    
    def printChoices(self):
        print(f'You chose {self.playerChoice}')
        print(f'Bot chose {self.computerChoice}')
        
    def printWinLose(self, humanWinsTo, humanLosesTo):
        if self.computerChoice == humanLosesTo:
            print(f'Sorry, {self.computerChoice} beats {self.playerChoice}')
        elif self.computerChoice == humanWinsTo:
            print(f'{self.computerChoice} does not beat your {self.playerChoice}')
    
    def printResult(self):
        if self.playerChoice == self.computerChoice:
            print('TIE')
        
        if self.playerChoice == 'rock':
            self.printWinLose('scissors', 'paper')
        elif self.playerChoice == 'paper':
            self.printWinLose('rock', 'scissors')
        elif self.playerChoice == 'scissors':
            self.printWinLose('paper', 'rock')

    def simulate(self):
        self.printOptions()
        self.getPlayersChoice()
        self.getComputerChoice()
        self.printChoices()
        self.printResult()
    
#***********
#High Cohension of methods and attributes means they are closely related
# A class is cohesive when if its contents make sense together as a whole.

#A coupled class is when it depends on another class
# Tightly Coupled is when it relies on many details from the other class (expensive for technical debt)



#***Packages***
#good practice would be to break up the the modules into 2 packages. an example would be if you have database_query and
# search_query modules. Seperate them into unique packages and so that the structure would become database.query and
# search.query. (easier to import/ cuts redundancy while keeping them unique/ becomes easier to read and navigate 
# the hierarchy


################## ***CHAP 3 ABSTRACTION AND ENCAPSULATION*** ##################################################
#Abstraction: process of taking something concrete and stripping it of its specifics
#Complex code will often benefit from layers of abstraction where as low level utilities will support small behaviors
# which in turn supports more involved behaviors

#an example would be left to right, Functionality grows more complex while becoming less reusable
#"String manipulation/ database operations", "http calls", "credit card processing", "ecom system"
#                  >                             >                  >                      >

#Code example used a monolith of code for sentance parsing and the updated is making a class for matching for a pattern
# This is done so that sentance pattern and word pattern doesnt need 2 versions of the same code, pass to a class
# then its done

#PY TIP:
#adding additional context to a module/class/method/func using "docstrings"

#ENCAPSULATION
# modules are a form of encapsulation. They group multiple related classes and functions together.
# The largest encapsulation available in py is package

#for psuedo privacy: if you want methods/variables to be class only, prefix the class with an underscore.
# ex: _internalFunction

#get the date time hour of an object
import datetime
datetime.now().hour

# Current day of the week
datetime.now()strftime('%A')

#internal only functions may benefit as being standalone and serving more than one purpose

###Programming style are abstraction too###

#Procedural Programming: use procedural calls (functions) which aren't encapsulated into classes,so they only rely on
# their inputs and occasionally on some global state

#Functional Programming: (relies heavily on functions as the form of abstraction, yet the mental model is different)
# requires more thought about your programs as composition of functions. (for loops are replaced by functions that 
# operate on lists)
# NOW AN EXAMPLE: we might write
numbers = [1,2,3,4,5]
for i in numbers:
    print(i*i)

# vs in functional it would look like
(map((i) => i * i, [1,2,3,4,5]))

# functional programming usually can accept other functions as args or return as results

#PY RELATED FUNCTIONAL TOOLS
#Map, tools under Functools and Itertools, reduce (thats under functools)

#functional python would look like this
from functools import reduce

squares = map(lambda x: x * x, [1,2,3,4,5])
should  = reduce(lambda x, y: x and y, [True, True, False])
evens = filter(lambda x: x % 2 == 0, [1,2,3,4,5])

# vs the pythion prefered
squares = [x * x for x in [1,2,3,4,5]]
should = all([True, True, False])
evens = [x for x in [1,2,3,4,5] if x % 2 == 0]

#functools.partial allows you to create an new function from an existing functionwith some of the original functions
# argument set (can make things clearer than writing a function that calls the orignal function)
#EX: 
from functools import partial

def pow(x, power=1):
    return x ** power

square = partial(pow, power=2)
cube = partial(pow, power=3)

#3.4.3 Declarative programming
#Declarative programming: focuses on declaring the parameters of a task without specifying how to accomplish it
# and the details on how to accomplish the task are abstracted from the developer. (useful when you need to repeat
# highly parametric task with only slightly varations in the parameters)

#This style is often used with (DSL) Domain specific languages such as HTML/SQL/etc. Where as python and c are 
# general purpose languages

#EXAMPLE TOOL FOR PY: is graphs creation from data by describing a graph. (https://plot.ly/python/)

#A languages typing or type system is how it chooses to manage data type of variables. (some are complied and check
# data types at compliation and others at run time./ some languages know x = 1 is an int while others need that 
# int call out like int x = 1)

#Py is a dynamically typed language which means that it determines its data types at runtime.
#it also uses DUCK TYPING which is will always attempt to make the method call during execution and raising an
# attributeError if the method doesnt exist on the instances class. vs other langauges which fail to compile if there
# are unknown references to a method on a class instance.

#Composition is the converse to decomposition; pieces are brought together to realize a complete concept.
# It is often done through interfaces, which are formal definitions of a method/data that a particular class must
# implement.

#Only way to get inheritance in PY is through the duck typing system and multiple inheritance.

#Something like an interface can be built using a MIXIN mechanism that would just be a suffix at the end. this allows 
# users to know that the class is composable. EX:
class classNameMixin:
    def classNameFind(self)
        thisName = self.__class__.__name__.lower()
        print =(f'The class name is: {thisName}')
        
class computer(classNameMixin):
    pass
    
# computer has inherited classnamefind now even though the class does nothing when instantiated

#key notes: abstraction should only be used to reduce friction.
# Adapter: when you need an abstract an interface of a 3rd party software.


###########################################################(***Chapter 4***)####################################

#asymptotic analysis: observing and determining the bounds of its worst case
# big o notation, (worst case)

#the base comparision for time complexity is y=n at a 1:1 scale. so similar base case is y= mx + b

#an example of a o(n^2) case is:
def hasDuplicates(sequence):
    for index1, item1 in enumerate(sequence):
        for index2, item2 in enumerate(sequence):
            if item1 == item2 and index1 != index2:
                return True
    return False

#O(n^2) us the worst case because even if the last items are duplicates or if no duplicates exist, the code has to
# iterate over all the inputs before it finishes.

#best case is big omega and average is big theta

#py has garbage collector

#Common way programs use too much memory is reading in large data files fully into mem when they dont have too.
#regEx out the data you need or read 1 line at a time

#reduce loops over input and have less space to do things, (1 line at a time)
#ideal performance is constant time

#******************************************
#data types for aiming for constant time:
#           dict and set
# They both share the behaviors of effciency when adding, removing, or accessing items. They where also similar under the
# hood, but they dicts map keys and values and sets represent set of unique and individual terms
#*********************************************
#*********************************************
#Data types for aiming for linear time:
#LISTs are mainly O(n) operations. (such as adding new to location or if it exists in a list)
#Lists are usefully when items being stored aren't uniquely identifiable
#Tuples are similar but they can't be changed after they are created
#***********************************************
#iterables or objects that support iteration are almost always going to be 0(n) time complexity,



#SPACE COMPLEXITY
# 
#USEFUL TOOL: GENERATORS: they are constructors that produce a single value at a time. 
# -They pause until the next value is requested. (they avoid storing all the values in memory at once)
# -(range function is a generator)
# 
#Generators make use of the (yield) keyword. Which after producing a value, they yield execution back to the calling 
# code. So (yield) yields a value then yields execution.
#
#Yield works alot like pythons return statement except you can perform operations after you yield the value. Which means
# you can use it to set up for the next value you want to produce.
#
#Approximation of how range works under the hood
def range(*args):
    if len(args) == 1:
        start = 0
        end = args[0]
    else:
        start = args[0]
        end = args[1]
    
    current = start
    
    while current < stop:
        yield current
        current += 1

#end sample

#The repeated pattern of generators:
#1. Perform the main setup required for producing all values
#2. Create the loop
#3. Yield a value on each iteration of the loop
#4. Update the state for the next iteration of the loop

#from an example
def squares(items):
    for item in items:
        yield item ** 2
#end
#This function gets to be very compact and doesnt have to worry about state management
#
# You can even pass a generator to the squares, like the range from above and it will only store one item at a time from
# the range and one squared result at a time. (big space savings)
#
#Though, it is considered to be a LAZY EVALUATION. Which is the idea of producing one value at a time, and that consuming 
# code may not need all the values you can produce (as little work as possible when explicitly asked)


#Now, a small 3 rule as step system to get performant systems (make it work, make it right, make it fast)

###MAKING IT WORK###
#mvp

###MAKING IT RIGHT###
#after getting to "does it work?"  it is time to refactor.
# refactoring seeks to re implement existing code in a clearer or more well adapted way while providing the same 
# consistent outcome.
#
#Refactoring has no clear done moment, so avoid iteration hell
#Martin fowlers rule of 3 states: if you have implemented a thing 3 times, you should refactor your code to provide an
# abstraction.

#now working with a code example

def getNumberWithHighestCount(counts):
    maxCount = 0
    for number, count in count.items():
        if count > maxCount:
            maxCount = count
            numberWithHighestCount = number
    return numberWithHighestCount

def mostFrequent(numbers):
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    return getNumberWithHighestCount(counts)

# LETS LOOK MAKING THE MOST FREQUENT FUNCTION RIGHT

#Use built in functions (defaultdict is the example) (counts = defaultdict(int) )
# you can tell defaultdict types of values to store
#

from collections import defaultdict
#
#...
#
def mostFrequent(numbers):
    counts = defaultdict(int)
    for number in numbers:
        counts[number] += 1
    return getNumberWithHighestCount(counts)

# and again with Counters (from collections import counter) (counts = Counter(numbers) )
# (helps with counting things in a sequence)
#

from collections import Counter
#
#...
#
def mostFrequent(numbers):
    counts = Counter(numbers)
    return getNumberWithHighestCount(counts)

#############################
## end of focusing on most frequent
#
## now, lets take a look at the get number with highest count
#############################
# LAMBDAS are what we are looking at (Inline function that accepts arguments and return values.
# has no name and you can't call them directly )
#
#though process for the new version:
# we know we can use a max function to get the number with the highest count BUT,
# since we are putting in a dictionary max will return the maximum value of the keys by default.
# 

#...
def getNumberWithHighestCount(counts):
    return max(
        counts,
        key = lambda number: counts[number]
    )
#
#...
#

###MAKING IT FAST###
#
# THING TO REMEMBER!!!!!!!!
# Perfection Is The Enemy of Good Enough!!!!
#
#YOU CANT GET MVP IF YOU CANT GET GOOD ENOUGH (also scope creep)



# TOOOOOOOLLSSSSSSSSSSSSSSS ##################

# TIMEIT:
# is a module/ tool in python for testing execution time of the code snippets
# (can be used in cli or in code directly) 

# cli
# python -m timeit "<code>"

# code
#SAMPLE
from timeit import timeit
setup = 'from datetime import datetime'
statement = 'datetime.now()'
result = timeit(setup=setup, stmt = statement)
print(f'Took an average of {result}ms')
#END SAMPLE


### CPU PROFILER ###

# Trying to find which code is the most taxing on the CPU

# cProfile
# (prints a couple things out):
#
#(ncalls) number of times the call occurred
#(tottime) the time spent in that call alone not inlc things it calls in turn
#(percall) avg time spent in the call alone, across the "ncalls" times it was called
#(cumtime) Cumulative time spent on that call, including sub calls

#example function#################
# it calls the function 1000 times and takes a random time up to 10milliseconds to complete
import random
import time

def expensiveFunction():
    executionTime = random.random() / 100
    time.sleep(executionTime)

if __name__ == '__main__':
    for _ in range(1000):
        expensiveFunction()

##### END CODE #########################################
#
#### CLI of cProfiler
# python -m cProfile --sort cumtime <someProject>.py

################################################################################################
### CHAPTER 5 CHAPTER 5 CHAPTER 5 CHAPTER 5 CHAPTER 5 CHAPTER 5 CHAPTER 5 CHAPTER 5 CHAPTER 5 ##
################################################################################################
############################                      ##############################################
############################ ###################################################################
############################ ###################################################################
############################ ###################################################################
############################                    ################################################
###############################################  ###############################################
################################################ ###############################################
###############################################  ###############################################
############################                     ###############################################
################################################################################################
# TESTING#
#

# Anatomy of a functional test
# Basic anatomy:
# 1. Prepare inputs to the software
# 2. identify the expected output of the software
# 3. obtain actual output
# 4. compare the actual and expected to see if they match

# 1,2 are determined by you
# 3 is determined by executing the real code
# 4 if the are same test passes. If not, the test fails

#Types of testing
# Manual
# Automated
# Acceptance (verifies the high level requirements of a system)(Answers questions like: can the user successfully go through the
#             purchasing workflow and buy the product that they want?)(usually done manually by stakeholder)(can be automated to a
#             degree with end to end testing: makes sure a set of actions can be carried out)
# Unit Testing (most granular) (Test little bits of software to see if they are working) (encapsulation, seperation of concerns,
#               loose coupling allow for easier to test code)
#              -so when doing a function that finds the mean, write code to test if it can take a negative, or empty and such
# Integration testing (making sure all the individual units work in tandem to produce the right behavior) (NEEDS TO THREAD MULTIPLE
#                      pieces of code together) (It leads to tight coupling) (changes in the code that produce the same outcome
#                      might still cause the tests to break because are too concerned with how the outcome is achieved)
#                      (Take longer to execute than unit tests because the test needs more to be done)
# Testing pyramid (the basis and should be done the most is unit testing, then integration, then manual) (as you go from unit to manual
#                  you should avoid keeping as the basis of your testing strats)
# The testing pyramid is first described ^^^^
#
# Regression Testing (Less of an approach to testing and more of a process to follow as you develop your applications)
#                    (When you write a test, the assumption is that you're saying, "i want to make sure the code keeps working this way")
#                    ("Is the practice of running your existing suite of tests after each code change before shipping your code to 
#                     production") the use of CI for RE testing("https://docs.travis-ci.com/user/for-beginners/") and
#                    ("https://circleci.com/docs/about-circleci/")
#
# Version Control hooks (One practice for automation unit tests in source control systems is a precommit hook) (each time you commit
#                        your code, the hook triggers the tests to run. If failures occur, the commit fails)


########################
######################## Statements of facts (WITH ASSERTIONS) and unit testing
########################
########################

#the use of assertion which is that a particulatr comparision hold true
# You can add assert in front of your comparisions, to get an assertion (failing assertions get an AssertionError)
# If the assertion is true, you get nothing back
#the code below is ment for CLI but will show it

assert 10.0 == calcMean([0,10,20])\
#nothing back
assert 1.0 == calcMean([1000,3500,7000000])
#assertionError

#end
#

##########
######### Unit testing with unittest
##########

#Unittest allows for assertions and a tool for running the tests
# it also allows for "TestCase" class with custom assertion methods for more understandable testing outputs.
# (You tests will need to ""inherit"" from the class and use methods to make assertions)
# 

#How to run the tests with unittest
# It comes with the test runner (in cli) which is "python -m unittest"
# when you run the above it will look for tests by:
# 1. looking in the current directory (and any subdirectories) for modules named "test_*" or "*_test"
# 2. looking in those modules for classes that inherit from unittest.TestCase
# 3. looking in classes for methods that start with test_

# (some people like to have the tests close to hte modules of interest. Others like to put all their tests in a tests/directory that
# lives at the root of their project to keep them separate from the code)

##########
######### Writing example test with unittest
##########
#
#Based on the example code below
class Product:
    def __init__(self, name,size,color):
        self.name = name
        self.size = size
        self.color = color
    
    def transformNameForSku(self):
        return self.name.upper()

    def transformColorForSku(self):
        return self.color.upper()

    def generateSku(self):
        """
        generates sku for this product

        example:
        >>> smallBlackShoes = product('shoes','S','black')
        >>> smallBlackShoes.generateSku()
        'SHOES-S-BLACK'
        """
        name = self.transformNameForSku()
        color = self.transformColorForSku()
        return f'{name}-{self.size}-{color}'
#END EXAMPLE
#

#now, we would need to make a test (based on the anatomy of a functional test):
# 1. set up inputs 
# 2. identify the expected outputs
# 3. obtain the actual output
# 4. compare the expected and actual outputs

# and, we want to test the "transform name for sku" method from the product class, and the above anatomy becomes:
# 1. Create an instance of Product with name/size/color
# 2. observe that transformNameForSku returns name.upper(); expected result is the name in uppercase
# 3. call the product instance's TransformNameForSku method and save it in a variable
# 4. compare the expected result to the saved actual result

# The test would look like
#
#SAMPLE CODE
import unittest
from product import Product

class ProductTestCase(unittest.TestCase):
    def testTransformNameForSku(self):
        smallBlackShoes = Product('shoes','S','black')
        expectedValue = 'SHOES'
        actualValue = smallBlackShoes.transformNameForSku()
        self.assertEqual(expectedValue, actualValue)
#end sample
#and now if the product expected value SHOEZ is placed instead of SHOES, and you will get an assertionError

##########
######### Writing your first integration test with unittest
##########








