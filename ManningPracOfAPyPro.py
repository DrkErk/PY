from multiprocessing import connection
import re
import sqlite3


#########
######    
#########

# https://github.com/daneah/practices-of-the-python-pro


#########
######    
#########

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

def add_sales_tax(total, state):
    return total * tax_rates_by_states[state] #uses the global

#end snippet

#now with a local variable on the function
#snippet as follows:

#sales_tax.py
tax_rates_by_states = { 'MI': 1.06} #assuming its filled to the max with data. This is global

def add_sales_tax(total, state):
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
    print(f'AFTER TAX:  {add_sales_tax(total, state)}' )
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
datetime.now().strftime('%A')

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
#(map((i) => i * i, [1,2,3,4,5]))

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
    def classNameFind(self):
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
# name 'product'
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

#for this example we have a shopping cart class with the ability to add and remove products would be needed (stores products in a
# dictionary like below):
"""
{
    'SHOES-S-BLACK': {
        'quantity': 2,
        ...
    }
    'SHOES-M-BLUE': {
        'quantity': 1,
        ...
    }
}
"""
# and the shopping cart would look like this
###CODE SAMPLE
# called 'cart'
from collections import defaultdict

class ShoppingCart:
    def __init__(self):
        self.products = defaultdict(lambda: defaultdict(int)) # using default dict simplifies the logic for checking if a product is in
                                                              #already in the cart dictionary
    def addProducts(self,product,quantity=1):
        self.products[product.generateSku()]['quantity'] += quantity
    
    def removeProducts(self,product,quantity=1):
        sku= products.generateSku()
        self.products[sku]['quantity'] -= quantity
        if self.products[sku]['quantity'] ==0:
            del self.products[sku]
###END SAMPLE

# and from the code sample, there are a couple points of integration that could be tested
#  -the cart's integration with the products instance of generateSku
#  -adding and removing product must work in tandem; a product that's been added also must be removed

# they look alot like unit tests, except the difference is that they execute different amounts
#  (unit test is usually 1 method)
#  (integration test is usually many methods)

# An integration test for a shoppingcart class (test: intialization of the cart, add product, remove it, and make sure the cart is 
#  empty)
### BEGIN SAMPLE
import unittest

from cart import ShoppingCart
from product import Product

class shoppingCartTestCase(unittest.TestCase):
    def testAddAndRemoveProduct(self):
        cart = ShoppingCart()
        product = Product('shoes','S','blue')

        cart.addProducts(product)
        cart.removeProducts(product)

        self.assertDictEqual({}, cart.products)

### END SAMPLE

##########
######### Test Doubles
##########

#for when you have to write code that interacts with other systems/databases/apis and you don't want to risk destruction to real data/
# avoid slow run times...

#you can imitate the systems with test doubles which can be done in different ways:
# -Faking   (using a system that behaves a lot like the real one, but avoids the expensive/destructive actions)
# -Stubbing (using predetermined value as a response instead of getting one from a live system)
# -Mocking  (using a system with the same interface as the real one, but that also records interactions for later inspection/assertions)

# FAKING and STUBBING involves writing your own imitations as functions or classes to tell your code to use them during the test exe
# MOCKING is most commonly done using the "unittest.mock" module

#Compare an assertion test vs a mocking
# It will be based on adding the tax

# assertion
### sample code
from urllib.request import urlopen

def addSalesTax(orignalAmount, country, region):
    salesTaxRate = urlopen(f'https://tax-api.com/{country}/{region}').read().decode()
    return orignalAmount * float(salesTaxRate) 
### end sample

# mocking
### sample code
import io
import unittest
from unittest import mock

from tax import addSalesTax

class SalesTaxTestCase(unittest.TestCase):
    @mock.patch('tax.urlopen')
    def testGetSalesTaxReturnsProperValueFromApi(self, mock_urlopen):
        test_tax_rate(1.06)
        mock_urlopen.return_value = io.BytesIO(str(test_tax_rate).encode('utf-8'))
        self.assertEqual(5 * test_tax_rate, addSalesTax(5, 'USA', 'MI'))
### end sample

#Testing in this way allows for "your code that you control to behave in a way given these assumptions"
# (where the assumptions are created using test doubles)

#If you have fair confidence of what the requests library does. you can use test doubles to avoid coupling yourself to it.
# in the future, you might need to change or use a diff http client library. But the test will not have to change.

#HINT: usually pick test doubles wheni want to avoid the slow/expensive/destructive behaviors. 

#Don't mock your own code, because it can lead to brittle tests that break when the code changes.
# if you change the implementation, you have to change your tests

#When the values that need to be tested are dictionaries, unittest has a method for it. (assertDictEqual). It provides useful
# output specfic to dictionaries when the test fails

#You can even skip saving the expected and actual values as variables. (using assertEqual)
#code redone below for the assertequal
### CODE SAMPLE
def testTransformNameForSku(self):
    smallBlackShoes = Product('shoes','S','black')
    self.assertEqual('SHOES', smallBlackShoes.transformNameForSku(),)
### END SAMPLE

# now redo the product and shopping cart
#
# product
### CODE SAMPLE
class ProductTestCase(unittest.TestCase):
    def testTransformNameForSku(self):
        smallBlackShoes = product('shoes','S','black')
        self.assertEqual('SHOES',smallBlackShoes.transformNameForSku(),)
    
    def testTransformColorForSku(self):
        smallBlackShoes = product('shoes','S','black')
        self.assertEqual('BLACK',smallBlackShoes.transformColorForSku,)
    
    def testGenerateSku(self):
        smallBlackShoes = product('shoes','S','black')
        self.assertEqual('SHOES-S-BLACK', smallBlackShoes.generateSku(),)

### END SAMPLE

#shopping cart
### CODE SAMPLE

class ShoppingCartTestCase(unittest.TestCase):
    def testCartIntiallyEmpty(self):
        cart = ShoppingCart()
        self.assertDictEqual({}, cart.products)
    
    def testAddProduct(self):
        cart = ShoppingCart()
        product = Product('shoes','S','blue')
        cart.addProducts(product)
        self.assertDictEqual({'SHOES-S-BLUE':{'quantity':1}}, cart.products)

    def testAddTwoOfAProduct(self):
        cart = ShoppingCart()
        product = Product('shoes','S','blue')
        cart.addProducts(product, quantity=2)
        self.assertDictEqual({'SHOES-S-BLUE': {'quantity':2}}, cart.products)
    
    def testAddTwoDifferentProducts(self):
        cart = ShoppingCart()
        productOne = Product('shoes','S','blue')
        productTwo = Product('shirt','M','gray')
        cart.addProducts(productOne, quantity=1)
        cart.addProducts(productTwo, quantity=1)

        self.assertDictEqual({'SHOES-S-BLUE': {'quantity':1}, 'SHIRT-M-GRAY': {'quantity': 1}}, cart.products)
    
    def testAddAndRemoveProduct(self):
        cart = ShoppingCart()
        product = Product('shoes','S','blue')
        cart.addProducts(product, quantity=1)
        cart.removeProducts(product)

        self.assertDictEqual({}, cart.products)

    def testRemoveTooManyProducts(self):
        cart = ShoppingCart()
        product = Product('shoes','S','blue')
        cart.addProducts(product, quantity=1)  
        cart.removeProducts(product, quantity = 2)

        self.assertDictEqual({}, cart.products)
### END SAMPLE
#
# A big had arrisen with the removeProducts. the fix was to delete the product from the cart if the quantity is <= 0
#
### code sample
if self.products[sku]['quantity'] <= 0:
    del self.products[sku]
### end sample

#"think about the code when testing. what code be the possible product name formats we might need to support"

########################
######################## TESTING WITH
######################## PYTEST
########################

# PYTEST DOCS
# https:// docs.pytest.org/en/latest/getting-started.html

#Camelcase (aNameLikeThis) is considered to by unpythonic. snake case (a_name_like_this) is pythonic.

#pytest does automatic discovery of tests like unit test. The only difference is that pytest classes are named test* ...AND...
# don't need to inherit from a base class like unittest.TestCase to work

#to change over from unittest to pytest on the product test case:
# -Remove the unittest import from test_product.py
# -Rename the ProductTestcase class to TestProduct and remove the inheritance from unittest.TestCase
# -Replace any self.assertEqual(expected, actual) with assert actual == expected.

# now test product being updated to pytest would look like
#
### CODE SAMPLE
class TestProduct:
    def test_TransformNameForSku(self):
        smallBlackShoes = Product('shoes','S','black')
        assert smallBlackShoes.transformNameForSku() == 'SHOES'
    
    def test_TransformColorForSku(self):
        smallBlackShoes = Product('shoes','S','black')
        assert smallBlackShoes.transformColorForSku() == 'BLACK'
    
    def test_generate_sku(self):
        smallBlackShoes = Product('shoes','S','black')
        assert smallBlackShoes.generateSku() == 'SHOES-S-BLACK'
### END SAMPLE

# A book on pytest
"""
Brian Okken’s, Python Testing with pytest: Simple, Rapid, Effective, and Scalable (Pragmatic Bookshelf, 2017).
"""

########################
######################## Performance testing
######################## 
########################

# in practice, performance testing looks a lot like regression testing

# "Load testing" (how far you can push the application before it falls over)


###############
##########     TEST DRIVEN DEVELOPMENT
###############

# "Based on the stereotype of a quality assurance engineer that always finds something in the code to break"

# "Netflix chaos engineering"
# Which then becomes, write tests under the idea of being a chaos engineer. Actually and fully try and think of the extremes that the
#code can endure. (With the limit being that it doesnt make sense for all the code to respond predictably to all inputs)
#(But using the exception system can help the developer's code to respond in a predictable way to rare/unexpected situations)


# What gives more insight to better testing methods, is to see how every team handles the testing aspects of their process. It will
#help with identification/incorporation of the good pieces into the my testing flow.

# (Testing EVERY line of code has diminishing returns)

# If there is ever any code that testing some aspect of a function's behavior is awk/difficult. Then maybe the codes concerns aren't
#well separated or if it's inherently an awk test to do.
# If awkwardness must be incorparted, it's better for it to be in the tests code than the real code.

# Don't refactor code to only make testing easier or coverage stronger, do it to make testing easier and the code more coherent.

################################################################################################
### CHAPTER 6 CHAPTER 6 CHAPTER 6 CHAPTER 6 CHAPTER 6 CHAPTER 6 CHAPTER 6 CHAPTER 6 CHAPTER 6 ##
################################################################################################
############################    ################################################################
############################   #################################################################
############################  ##################################################################
############################  ##################################################################
############################                    ################################################
############################    ###############  ###############################################
############################   ################# ###############################################
############################    ###############  ###############################################
############################                     ###############################################
################################################################################################
# Separation of concerns in practice
#

#
# Note: An insight to cli bookmarking as a practice of separation of concerns.
#

#(Bookmarks are an example of CRUD)

# The cli bookmarking app would need the following information:
# -ID -unique alphanumeric identifier 
# -TITLE
# -URL
# -NOTES - optional
# -DATE ADDED

#the logic would be that the it is managed through the cli
#On startup (it should present a menu of options, and each option will trigger an action that will read or modify a database)

##########
#######     Benefits of separation: Reprise
##########

# the benefits of separtion of concern:
# -Reduced duplication: (na)
# -improved maintainability: (na)
# -ease of generalization and extension: (na)


#########
######     intial code structure, by concern
#########

# A good way to sculpt intial architecture would be figuring out a concise explanation of how it does what it does.

# For this example, "Using a cli, a user options for adding, removing, listing bookmarks stored in a database"
#this can be broken down to:
# -CLI interface: a way to present the user with options and help the user understand what the options do
# -Chooing options: once an option is choosen, some action or business logic happens as a result
# -Stored in a database: for data persistance
#
# It is a CRUD style project where (A person sees the CLI which is the presentation layer, leads to the business logic layer
# which leads to the persistance layer) (user/ cli/ options/ databases)<- modules 

#########
######     Application architecture patterns
#########

# Common way to separte an app is into layers of Presentation/Persistance/ Actions or rules
# MVC(model view controller): models persistance/ providing users with a view into that data, allowing them to control changes to data
# MVVM (model view viewmodel): puts emphasis on allowing the view and data model to comm freely.
#
# (sqlLite is persistance) and py has a sqlite3 module
#
# The bookmark data you need to manage:
# -Creating a table( for intializing a database)
# -Adding or deleting record
# -Listing the records in a table
# -Selecting and sorting records from a table based on some criteria
# -Counting the number of records in a table 

#########
######     Working with Databases
#########

# A robust package for working with databases in python is (SQLALCHEMY) www.sqlalchemy.org
# (ORM) Object-relational mapping: (interacting with databases, but abstracting data models) (allows you to treat records as objects in languages like py)
#
# {DATABASE INTERACTION CODE}
#
#

#########
######     Creating and Closing the Database Connection
#########

# Bark only needs one connection to the database and will be able to reuse it for all its operations.
# (to make it work, sqlite3 .connect . it accepts the path of the database file which it should connect to. If it doesn't exist, create it.)
# 
# The __init__ for the "DatabaseManager" should
# -accept arguements containing the path to the database file (using sepration of concerns earlier, it will not be hardcoded)
# -use the database file path to create a sqlite connection using sqlite3.connect(path) and store it as an instance attribute
#
# ALSO need to close the connnection when we are done. So, for symmetry purposes, we will add ***sqlite3.close() to the __del__ of the DatabaseManager****
#
# It would look like this
import sqlite3

class DatabaseManager:
    def __init__(self, database_filename):
        self.connection = sqlite3.connect(database_filename)

    def __del__(self):
        self.connection.close()

### END


#########
######     Executing Statements
#########

#SQL Statements that return data are called queries. (SQLITE3 Manages query results with a cursor)
# ^(Using a cursor to execute over a statement allows for me to iterate over the results it returns)
# (insert and delete aren't queries and are statements) (the cursor manages this by returning an empty list)
# 

# The _execute method should:
# 1. Accept a statement as a string arg
# 2. Get a cursor from the database connection
# 3. Execute a statement using a cursor
# 4. Return the cursor, which has stored the result of the executed statement (if any)

# AND IT WOULD LOOK LIKE THIS
def _execute(self, statement):
    cursor = self.connection.cursor()
    cursor.execute(statement)
    return cursor
### END

# Transaction is a feature that is a database safe guard against data becoming corrupted
#
# SQLite3 lets you use the connection object to create a transaction via a (CONTEXT MANAGER)
#
# And so: a Python Block using the "with" keyword alllows for special behavior to happen when the code enters and exits the block ****

# UPDATED CODE FROM ABOVE WITH THE 'WITH'
def _execute(self, statement):
    with self.connection:
        cursor = self.connection.cursor()
        cursor.execute(statement)
        return cursor
### END

# It's good security practice to use placeholders for real sql statements, to prvent sql inj and such.
# ^
# So we need to update the _execute to accept 2 things:
# - A sql statemnet tas a string, possibly containing placeholders
# - a list of values to fill in the placeholders in the statement.
#

# Updated code again
def _execute(self, statement, values = None):
    with self.connection:
        cursor = self.connection.cursor()
        cursor.execute(statement, values or [])
        return cursor
### END



#########
######     Creating Tables
#########


# we now need to create a table using a sql statement. 
#   (Because of the concerns of connecting to the database and executing statement, the statements are now abstracted.)
#
# Creating a table includes the following:
#   1. Determine the column names for the table
#   2. Determine the data type of each column.
#   3. Construct the right sql statement to create a table with those columns
#
# Also to keep in mind: Each bookmark has an ID, title, URL, Optional Notes, and date added: explained below
# -ID: (primary key of the table/ main identifier) (should auto increment using autoincrement keyword, Column is an INT) (Rest are text)
# -Title: (url title) (give to sqlite the column can't be empty (using NOT NULL))
# -URL: (url) (NOT NULL)
# -Notes: (optional so only TEXT specifier is needed)
# -Date: (date added) (NOT NULL)


# CREATING THE TABLE WOULD LOOK LIKE THIS IN SQL

# CREATE TABLE IF NOT EXISTS bookmarks
# (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT NOT NULL,
#     url TEXT NOT NULL,
#     notes TEXT,
#     date_added TEXT NOT NULL
# );

### END CODE

# create_table
# Now with this, we can create a method for creating tables. (this method will need to include)
# 1. Accept 2 args, name of the table created and a dict of col names mapped to their data types and constraints
# 2. construct a CREATE TABLE SQL statement like the one shown earlier
# 3. Execute the statement using DatabaseManager._execute

# The code would like like as follows
def create_table(self, table_name, columns):
    columns_with_types = [
        f'{column_name} {data_type}'
        for column_name, data_type in columns.items()
    ]
    self._execute(
        f'''
        CREATE TABLE IF NOT EXISTS {table_name}
        ({', '.join(columns_with_types)});
        '''
    )
### END

# Although earlier in the book it said early optimization is bad, why do it now?
#  ^- because it isn't much hard work to parameterize the values with arguments to the method. (ie replacing the string 'bookmarks with
# table_name isn't much work)
# 



#########
######     Adding Records
#########

# SQLite now expects an INSERT INTO keyword to add records. The code would be as follows:

# INSERT INTO bookmarks
# (title, url, notes, date_added)
# VALUES ('GitHub', 'https://github.com', 'A place to store repos of code', '2023-02-01T18:46:34.125467');

### end 

# Now comes the reminders that it's good practice to use placeholders instead (as in the _execute from earlier)
# We know that we can use a placeholder on all of the above values
# (ONLY PLACES WHERE LITERAL VALUES GO CAN USE PLACEHOLDERS IN STATEMENTS )
#
# Code with place holders would look like:

# INSERT INTO bookmarks
# (title, url, notes, date_added)
# VALUES(?,?,?,?);

### End

# But now, we need to add an add method into the databaseManager to do the code above, that means:
#   1. Accept 2 args: name of table and dict that maps column names with column values
#   2. Constructs a placeholder string (a ? for each column specified)
#   3. Constructs the string of column names 
#   4. Gets the column values as a tuple (a dicts .values() ret a dict_values obj, which works w/ sqlite execute method)
#   5. use _execute to execute a statement pass the sql statement with placeholders and the col vals as separate args

# With the above said, the code would look like this
def add(self, table_name, data):
    placeholders = ', '.join('?' * len(data))
    column_names = ', '.join(data.keys())
    column_values = tuple(data.values())

    self._execute(
        f'''
        INSERT INTO {table_name}
        ({column_names})
        VALUES ({placeholders})
        ''',
        column_values
    )
### END



#########
######     DELETING RECORDS
#########

# Now it is time to "DELETE" "WHERE" to get rid of the record (by ID)

# Now a statement in sqlite would look like:

# DELETE FROM bookmarks
# WHERE ID = 3;

### END

# Writing the delete method would be simliar to the add method
#
# The method would need to:
# 1. Accept 2 args: the table name to delete records from, and a dict mapping column names to  the value to match on
#   ^- (there needs to be a required argument so not to delete the whole database)
# 2. Constructs a string of place holders for the WHERE clause
# 3. Costructs the full DELETE FROM query and executes it with the _execute.

# This would look like the following
def delete(self, table_name, criteria):
    placeholders= [f'{column} = ?' for column in criteria.keys()]
    delete_critera = ' AND '.join(placeholders)
    self._execute(
        f'''
        DELETE FROM {table_name}
        WHERE {delete_critera};
        ''',
        tuple(criteria.values()),
    )
### END



#########
######     Selecting and sorting records
#########

# the sqlite code for get selecting all columns:

# SELECT * FROM bookmarks
# WHERE ID = 3;

### END



# the sqlite code for get selecting all columns and then sort the results:

# SELECT * FROM bookmarks
# WHERE ID = 3
# ORDER BY title;

### END


# Lastly, do the above but abstract with place holders:

# SELECT * FROM bookmarks
# WHERE ID = ?
# ORDER BY title;

### END

# Now, the select is similar to delete we make the select:

def select(self, table_name, criteria=None, order_by=None):
    criteria = criteria or {}

    query = f'SELECT * FROM {table_name}'
    if criteria:
        placeholders = [f'{column} = ?' for column in criteria.keys()]
        select_criteria = ' AND '.join(placeholders)
        query += f' WHERE {select_criteria}'
        
    if order_by:
        query += f' ORDER BY {order_by}'
    
    return self._execute(query, tuple(criteria.values()))

### END

# and at that point, we are done with the database connection.

# Next, we need to develop the Business logic layer to interact with the persistance layer



#########
######     
#########
#########
######     BUSINESS LOGIC LAYER
#########
#########
#######
#########


# To start, it would be very tempting to if and elif spam the commands one by one. But since its a CLI program, that means users
#   may want more than one flag at once.
# (In this we to use command patterns to build what we need)


#########
######     Creating the bookmarks table
#########

##################################################### WOULD GO INTO THE "COMMAND" MODULE

# So now, we need to create the commands module to hold all the commands. Since most of the commands will need to make use of the 
#   database manager, we will import it from the database module and create an instance of it (called db)
#
# the __init__ for the database manager requires a file path, so we need to get it when calling it in.
#
# To start, we will need to intialize the bookmarks database table if it doesn't already exist
#  we will start by writing a CreatingBookmarksTableCommand class whose execute method creates the table for the bookmarks
#
# The code would look as follows:
db = DatabaseManager('bookmarks.db')

class CreateBookmarksTable:
    def execute(self):
        db.create_table('bookmarks', {
        'id':'integer primary key autoincrement',
        'title':'text not null',
        'url':'text not null',
        'notes':'text',
        'date_added':'text not nulls',
        })
        
### END

# Now above is an example of loose coupling. (the command is only aware of its duties/ persistance layer logic and the interface of
# ^- its dependency/ DatabaseManager.create_table )
# ^^- (This is considered loose coupling because persistance logic is seperated from presentation logic


#########
######     Adding Bookmarks
#########

# logic behind adding bookmarks, we will need to pass data received from the persistance layer. (data will be passed as a 
# ^- dictionary mapping col names to values
#
# As a note for above, it is a great example of code relying on a shared interface rather than the specfics of an implementation
# ^-- (If the persistance logic layer and business logic layer agree on a data format, they can do what they need to do, as 
# ^-- long as they are consistant)
#

# The AddBookmarkCommand class will need some of this.
# 1. Expect a dict containing the title, url, (opt) notes
# 2. Add the current datetime to the dict as date_added to get time in UTC. (Standard format/wide compatibility) (look like datetime.datetime.utcnow().isformat()
# 3. insert the data into the bookmarks table using the DatabaseManager.add method
# 4. return a success message that will eventually will be displayed by the presentation layer

# the code would like this
from datetime import datetime

class AddBookmarkCommand:
    def execute(self, data):
        data['date_added'] = datetime.utcnow().isoformat
        db.add('bookmarks', data)
        return 'Bookmark added!'
### END


#########
######     Listing Bookmarks
#########

# Now comes the IDEAS for how to list the bookmarks (ListBookmarksCommand)
# ^- We will make use of the DatabaseManager.select method. (And running that by default will return them in order that they were create
# ^-- or by their primary key)
# But we need to be able to sort by other means also. (ie: date/title)
#
# (it is good practice to sort explicitly, by date, instead of primary key)

# With that said, it should 
# -Accept the column to order by, save it as instance attr. (set default value to date_added)
# -pass info to db.select in its execute method
# -return the result (using the cursor's fetchall() method) because select is a query

# the code would look like this
class ListBookmarksCommand:
    def __init__(self, order_by='date_added'):
        self.order_by = order_by
    def execute(self):
        return db.select('bookmarks', order_by= self.order_by).fetchall()
### END

#########
######     Deleting Bookmarks
#########

# the idea for this one will be taking data from the presentation layer which will be an integer value which represents the bookmark id to delete
#
# it'll need to:
# - accept data the information in its execute method and pass it to the DatabaseManager.delete method
# - (delete accepts a dict mapping the col names to vals to match against. we will need to match given value to id column)
# - perhaps a message to the presentation layer that the task is complete

# The code would look like this
class DeleteBookmarkCommand:
    def execute(self, data):
        db.delete('bookmarks', {'id', data})
        return 'Bookmark deleted'
### END

#########
######     Quitting
#########

# we can either leave the user to "ctrl + c" but its better to make a nicer way to exit
#  sys.exit from python would be the way

# The code would look like
import sys
#...
class QuitCommand:
    def execute(self):
        sys.exit()
### END


#########
######     
#########
#########
######     PRESENTATION LAYER
#########
#########
#######
#########


# Since this is a CLI program and we have a quitcommand method, we will make the app an infinite loop that:
# 1. Clears screen
# 2. print menu objects
# 3. gets the user's choice
# 4. clear the screen and executes the command relating to user choice
# 5. waits for the user to review the result, pressing enter when done

# it is good practice to put cli code for cli apps into (if __name__ == '__main__') block.
# ^-- this will make sure that the code doesn't unintentionally execute in the module by importing the app module somewhere.

# The code that will start
if __name__ == '__main__':
    print('This app has started!')
### END

# Now, we need to intialize the database!

# The code that will start
import commands #where the sql 

if __name__ == '__main__':
    commands.CreateBookmarksTableCommand().execute
### END

#A note about above: It is a representation of a full pass through all the layers. (multitier architecture)
#  (presentation layer triggered business logic, which set the table up in persistant)


#########
######     Menu Options
#########

'''
The plan is to get the following to appear

(A) Add a bookmark
(B) List bookmarks by date
(T) List bookmarks by title
(D) Delete a bookmark
(Q) Quit
'''
# Since we have command pattern each command is triggered the same way as the others, the execute method.

# Two ways we can hook up presentation layer with business logic layer:
# 1. Use conditional logic to call the right command class's execute method based on users input
# 2. make a class that pairs the text to be displayed to the users and command it triggers

# In this case the second is the best choice. (I will hook each menu option up to the command it should trigger (perhaps create an
# ^-- option class)) ( the __init__ method can accept the name to display to the user in the menu. Next, an instance of the command to
# ^--- execute when chosen by the user AND an optional preparation step (if we need addtional input) )
# ^---- All of which can be stored as instance attributes

# The Option instance needs to do the following:
# 1. Run the specified prep step
# 2. Pass the return val from the prep step, if any, to specific command's execute method.
# 3. print result of execution. These are the success messages or bookmark results returned from the business logic

# The option code would look like this:
class Option:
    def __init__ (self, name, command, prep_call = None):
        self.name = name
        self.command = command
        self.prep_call = prep_call
    
    def choose(self):
        data = self.prep_call() if self.prep_call else None
        message = self.command.execute(data) if data else self.command.execute()
        print(message)
    
    def __str__(self):
        return self.name
### END

# with this code in place, now is the time to hook up more business logic from earlier.
# Each option should:
# 1. print keyboard key for user to enter to choose the option
# 2. print the option text
# 3. check if the users input matches an option, if so, choose it.

# The plan is to to store the options in a dict. (we can iterate over the key/option pair with dicts .items() method)
# ^- more specifically, collections.ordereddict will allow us to have our menu options printed in the order I set.

# So, it now comes down to printing options class that need to be made and adding the options in the createBookmarksTableCommand

#The code would look like
#in createBookmarksTableCommand
def print_options(options):
    for shortcut, option in options.item():
        print(f'({shortcut}) {option}')
    print()

...

if __name__ == '__main__':
    ...
    options={
        'A': Option('Add a bookmark'), commands.AddBookmarkCommand()),
        'B': Option('List bookmarks by date'), commands.ListBookmarkCommand()),
        'T': Option('List bookmarks by title'), commands.ListBookmarksCommand(order_by='title')),
        'D': Option('Delete a bookmark'), commands.DeleteBookmarkCommand()),
        'Q': Option('Quit'), commands.QuitCommand())
    }
    print_options(options)
### END



#########
######     User Input
#########

# As a refresher, the desired walk through of the app would be
# 1. Prompt the user to enter a choice, using python built in input function
# 2. if the users choice matches the one listed, call that options choose method.
# 3. Otherwise, repeat

# Now, id make a get_option_choice function/ and use it after printing the options to get the users choice. (then call that options choose method)

# The following code would look like
def option_choice_is_valid(choice, options):
    return choice in options or choice.upper() in options

def get_option_choice(options):
    choice = input('Choose an option: ')
    while not option_choice_is_valid(choice, options):
        print('invalid choice')
        choice = input('Choose an option: ')
    return options[choice.upper()]

if __name__ == '__main__':
    ...
    choose_option = get_option_choice(options)
    choose_option.choose()
### END

# Now we need to be able to encapsulate some behavior for needing to add some more prepared data, ie: title, desc, notes.

# for each piece of information, we need to:
# 1. prompt a user with a label, (like title or description)
# 2. if the information is required and the user presses enter w/o entering any info, keep prompting.

# That means we will need 3 functions:
# 1. to provide repeat prompt behavior 
# 2. that use it to get info for adding/ deleting bookmark
# 3. add each info- fetching function as the prep_call to the appropriate Option instance 

# The code would look like this
def get_user_input(label, required=True):
    value = input(f'{label}: ') or None
    while required and not value:
        value = input(f'{label}: ') or None
    return value

def get_new_bookmark_data():
    return{
        'title': get_user_input('Title'),
        'url': get_user_input('URL'),
        'notes': get_user_input('Notes', required=False),
    }

def get_bookmark_id_for_deletion():
    return get_user_input('Enter a bookmark ID to delete')

if __name__ == '__main__':
    options={
        'A': Option('Add a bookmark'), commands.AddBookmarkCommand(), prep_call=get_new_bookmark_data),
    ...
        'D': Option('Delete a bookmark'), commands.DeleteBookmarkCommand(), prep_call=get_bookmark_id_for_deletion),
    ...
### END

'''
If I wanted to add new functionality, it is now very easy:

1. Add any new database manipulation methods you may need to database.py.
2. Add a command class that performs the business logic you need in commands.py.
3. Hook up the new command to a new menu option in bark.py.
'''

#########
######     Clearing the screen
#########

# A little something that should be done before printing the menu or executing a command 
# Keeping in mind that different operating systems have different names for clear, we can write:
import os

def clear_screen():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)
### END

# and the code will look like this after we clear before print_options, .choose():
if __name__ == '__main__':
    ...

    clear_screen()
    print_options(options)
    chosen_option = get_option_choice(options)
    clear_screen()
    chosen_option.choose()
### END


#########
######    Application loop
#########

# FINALLY, we move all of the code to the loop except the database initialization.
# So, from the if __name__.... to the loop:
def loop():
    # All the steps for showing/selecting options
    ...
    _ = input('Press ENTER to return to menu')

if __name__ == '__main__':
    commands.CreateBookmarksTableCommand().execute()

    while True:
        loop()
### END


################################################################################################
### CHAPTER 7 CHAPTER 7 CHAPTER 7 CHAPTER 7 CHAPTER 7 CHAPTER 7 CHAPTER 7 CHAPTER 7 CHAPTER 7 ##
################################################################################################
###################################                      #######################################
######################################################  ########################################
####################################################  ##########################################
##################################################  ############################################
################################################  ##############################################
##############################################  ################################################
############################################  ##################################################
##########################################  ####################################################
########################################  ######################################################
################################################################################################

# Extensibility and Flexibility

# Code is Extensible if you can add new behaviors to the app and it has little or no impact on existing behaviors.

# Shotgun surgery: having to pepper changes all through out the code to add some feature

# NOTE: duplicating code is a valid approach to extension. By creating a duplicate version, altering it, and seeing how the 
# ^- two versions differ,  it'll become easier to refactor the duplicated code back into a single/ multipurpose one later.
#   (DUPLICATION IS BETTER THAN THE WRONG ABSTRACTION)

# Kent Beck - "For each desired change, make the change easy (warning, this may be hard), then make the easy change"
# ^- breaking down the codes resistance because it is rigid will make the program easier to change (through methods like decomp/encapulation/etc)

# A rigid mapping vs flexible mapping example
# Rigid

if choice == 'A':
    print("A")
elif choice == 'B':
    print("B")
... # and so on

### END
# Flexible
choices = {
    'A': 'apples',
    'B': 'bats',
    ...
}
print(f'{choice} is {choices[choice]}')
### END


#########
######    Loose Coupling
#########

# extensibility comes from loosely coupled systems. without loose coupling, most changes in a system will
# ^ - require the shotgun surgery variety of development

# the goal with the app that was just walked with was that is was loose coupled enough to:
# - Add new database functionality to the DatabaseManager
# - Add/encapsulate new business logic in the Command Class
# - Adding to the menu is just adding to the dict in options

#########
######    Letting go: Inversion of control
#########

# (Refresh: composition provides benefits over inheritance by allowing objects to reuse behaviors without confining them 
#  ^  - to a particular inheritance hierarchy)
#
# A common practice in OOP codebases is to separate concerns into smaller classes and then recompose them into a new class that 
# ^ - uses instances of those smaller classes.

# How a composite class would look for and example of a bike/ its parts:
class Tire:
        def __repr__(self):
            return 'tire'

class Frame:
        def __repr__(self):
            return 'frame'

class Bicycle:
    def __init__(self):
        self.front_tire = Tire()
        self.back_tire = Tire()
        self.frame = Frame()
    
    def print_specs(self):
        print(f'Frame: {self.frame}')
        print(f'Front Tire:{self.front_tire}, back tire: {self.back_tire}')

if __name__ == '__main__':
    bike = Bicycle()
    bike.print_specs()
### END

# THE GOOD:
# - Encapsulation looks good; each part of the bicycle lives in its own class
# - The levels of abstraction look good too; Bicycle at the top and each of its parts is accessible as level down
# - Adding new parts is easy

# THE BAD:
# - Very difficult to change the parts because they are hard coded into the initialization
#
# if I wanted to change what the frame was, Id need to crack open the bicycle class code to update. Therefore tire is rigid dependacy for bicycle

# *** - Inversion of control: instead of creating instances of dependencies in the class, pass in existing instances for the class
#       ^ -  to make use of
# In this case: The control of the dependency creation is inverted by giving control to whatever code is creating the bicycle
# ^ - 

# the code using inversion of code would look like this
class Tire:
    def __repr__(self):
        return 'A rubber tire'


class Frame:
    def __repr__(self):
        return 'An aluminum frame'


class Bicycle:
    def __init__(self, front_tire, back_tire, frame):
        self.front_tire = front_tire
        self.back_tire = back_tire
        self.frame = frame

    def print_specs(self):
        print(f'Frame: {self.frame}')
        print(f'Front tire: {self.front_tire}, back tire: {self.back_tire}')


if __name__ == '__main__':
    bike = Bicycle(Tire(), Tire(), Frame())
    bike.print_specs()
### END

# And now adding a new change would be as simple as
class NewFrame:
    def __repr__(self):
        return 'new frame'

...
if __name__ == '__main__':
    bike = Bicycle(Tire(), Tire(), NewFrame())
    bike.print_specs()
### END

# the goal is to be able to swap dependancies with minimal effort.

#########
######    The devil's in the details: relying on interfaces
#########

# another issue way rigid code can appear is if High level code relies to much on the details of lower level dependencies
# ^ - Thus, switching something like the tires would be able to be a part of the bicycle as long as the tire as the same method/attributes
#     as the other tire

# The easiest way to swap implementations (between high and low level code), will be using agreed upon interfaces
# ^ - (duck typing means that strict interfaces aren't required) (we decide what methods/attributes comprise a particular interface)

# Some of the interfaces in this example would be:
# - Command classes in the business logic provide an execute method. (The presentation layer uses this interface when the user selects an
#   option )
# ^ - The implementation of a particular command can change as much as it needs to, no change is required in the presentation layer...
#     AS LONG AS THE INTERFACE STAYS THE SAME
# ^ - you would need to change the presentation layer if for example, the Command classes' execute methods required an additional args

#########
######    Fighting Entropy: the robustness principle
#########

# Robustness principle: Be conservative in what you do, liberal with what you accept from others
# ^ - ( be open to imperfect or unexpected inputs) IE: if accepting numbers use int() to force all to ints

#########
######    An exercise in extension
#########

# If I wanted to add a "GitHub Stars importer" id have to do the following
# Presentation Layer:
# 1. Prompt the user for the github username to import stars from
# 2. ask the user whether to preserve timestamps for the original stars
# 3. trigger the command 

# A use for the corresponding github api fetch will be (https://github.com/psf/requests)
# the related doc for the github library. (https://docs.github.com/en/rest/activity/starring?apiVersion=2022-11-28#list-repositories-being-starred)

# The process would look like:
# 1. Get initial page of star results the endpoint is the same as above: (https://docs.github.com/en/rest/activity/starring?apiVersion=2022-11-28#list-repositories-being-starred)
# 2. parse data from response, using it to execute an 'AddBookmarkCommand' for each starred repos
# 3. get the 'Link: <...>; rel=next' header is present
# 4. repeat for the next page if there is one; otherwise, stop

#
# And it will probably look like this: 
'''
$ ./bark.py
(A) Add a bookmark
(B) List bookmarks by date
(T) List bookmarks by title
(D) Delete a bookmark
(G) Import GitHub stars
(Q) Quit

Choose an option: G
GitHub username: user
Preserve timestamps [Y/n]: Y
Imported 205 bookmarks from starred repos!
'''

# In order to work around the timestamp being forced we should use inversion of control
# the code will look like this:
class AddBookmarkCommand:

    def execute(self, data, timestamp=None):
        data['date_added'] = timestamp or datetime.utcnow().isoformat()
        db.add('bookmarks', data)
        return 'Bookmark added!'
### END

# now, we dont need any new functionality at the persistance layer, which means we need to work on the presentation layer and business layer

# The import command code would look like this (business layer):
class ImportGitHubStarsCommand:
    def _extract_bookmark_info(self, repo):
        return {
            'title': repo['name'],
            'url': repo['html_url'],
            'notes': repo['description'],
        }

    def execute(self, data):
        bookmarks_imported = 0

        github_username = data['github_username']
        next_page_of_results = f'https://api.github.com/users/{github_username}/starred'

        while next_page_of_results:
            stars_response = requests.get(
                next_page_of_results,
                headers={'Accept': 'application/vnd.github.v3.star+json'},
            )
            next_page_of_results = stars_response.links.get('next', {}).get('url')

            for repo_info in stars_response.json():
                repo = repo_info['repo']

                if data['preserve_timestamps']:
                    timestamp = datetime.strptime(
                        repo_info['starred_at'],
                        '%Y-%m-%dT%H:%M:%SZ'
                    )
                else:
                    timestamp = None

                bookmarks_imported += 1
                AddBookmarkCommand().execute(
                    self._extract_bookmark_info(repo),
                    timestamp=timestamp,
                )

        return f'Imported {bookmarks_imported} bookmarks from starred repos!'
### END

# The import command option would look like this (presentation layer):
...
def get_github_import_options():
    return {
        'github_username': get_user_input('GitHub username'),
        'preserve_timestamps':
            get_user_input(
                'Preserve timestamps [Y/n]',
                required=False
            ) in {'Y', 'y', None},
    }

def loop():
    ...
    options = OrderedDict({
        ...
        'G': Option(
            'Import GitHub stars',
            commands.ImportGitHubStarsCommand(),
            prep_call=get_github_import_options
        ),
    })
### END


################################################################################################
### CHAPTER 8 CHAPTER 8 CHAPTER 8 CHAPTER 8 CHAPTER 8 CHAPTER 8 CHAPTER 8 CHAPTER 8 CHAPTER 8 ##
################################################################################################
#################################                         ######################################
################################   #####################   #####################################
################################  #######################  #####################################
################################  #######################  #####################################
##################################  ###################  #######################################
####################################                   #########################################
##################################  ###################  #######################################
################################   #####################   #####################################
#################################                         ######################################
################################################################################################



#########
######    The challanges of hierarchies
#########

# A class that inherits from it's parent class is fused together. (they are coupled as tight as possible)

#########
######    What is inheritance for, really?
#########

# Inheritance is for specialization of behavior: create subclasses to make a method return a different value or work diffently
# ^ - the natural result is that the instance of the sub class is an instance of the superclass

# (think about how composition and inheritance works. IE: bike is composed of frame and tire, but a different tire and frame inherits )

#########
######    Substitutability
#########

# Barba Liskov (Institute professor at MIT) made substitutability
# ^ - this principle states that in a program, any instance of a class must be replaceable by an instance of one of its subclass
#     without affecting the correctness of the program
# ^ - CORRECTNESS in this context means the program remains error free and achieves the same and basic outcome, though the precise
#     result may be different or achieved in a different manner.

# Since snails and slugs are similiar, you can say a slug is a parent class to a snail (because it has a shell)
# some classes to demonstrate this would be as follows:
class Slug:
    def __init__(self, name):
        self.name = name

    def crawl(self):
        print('slime trail!')

class Snail(Slug):
    def __init__(self, name, shell_size):
        super().__init__(name)
        self.name = name
        self.shell_size = shell_size

def race(gastropod_one, gastropod_two):
    gastropod_one.crawl()
    gastropod_two.crawl()

race(Slug('Geoffrey'), Slug('Ramona'))
race(Snail('Geoffrey'), Snail('Ramona'))
### END

# the code above breaks substitutability because the snails init requires you to add a shell size.
# a better version would be a where a snail has a shell, and would be a better case for composition



#########
######    The ideal use case for inheritance
#########

# Sandi Metz, all the little things, Railsconf 2014 http://www.youtube.com/watch?v=8bZh5LMaSmE 
# - the problem you're solving has a shallow, narrow hierarchy
# - subclasses are at the leaves of the object graph, they dont make use of other objects
# - subclasses use/ specialize all the behavior of their superclass

# it can be broken down further:


#########
######    Shallow, narrow hierarchy
#########

'''
-The shallow part of the rule addresses the problem with deep inheritance hierarchies from earlier: deep nested class hierarchies
can lead to difficult management and the introduction of bugs.

-The Narrow part of this means that no class in the hierarchy should have too many subclasses

-Subclasses generally shouldn't have any further dependencies. They are for specializing behaviors.
'''


#########
######    Subject at the leaves of the object graph
#########

'''
-Subclasses generally shouldn't have any further dependencies. They are for specializing behaviors.
'''

#########
######    Subclasses use all the behavior of their superclass
#########

'''
A question of about a is-a relationship would be:
- If the subclass doesn't use all of it's superclass behavior, is it really an instance of the superclass.

Take the following code of birds as an example:
'''

class Bird:
    def fly(self):
        print('flying!')

class Hummingbird(Bird):
    def fly(self):
        print('zzzzzooommm!')

class Penguin(Bird):
    def fly(self):
        print('no can do.')

'''
We have 2 birds that can fly and one that can't. We would just override the fly to just pass or raise an exception of some kind
but, this would go agains the substitutability principle.

In this case, composition would be a better choice.
'''

'''
A COMPARITIVE NOTE ON THE BICYCLE CODE:

-Frame and tire both have a narrow and shallow hierarchy; 1 lvl below with the most of 2 subclasses
-The different types of tires and frames don't depend on any other objects
-The different types of tires and frames use or specialize all the behaviors of their superclass

'''


#########
######    Inheritance in Python
#########

#########
######    Type inspection
#########
'''
- type() is the typing tool

- isinstance() used for seeing if an object is an instance of a particular class or any of its subclasses

-issubclass() is used to see if a class is a subclass of another

these tools should mainly be used for inspection of objects from the outside. (because using them to change behavior is precisely what
sublclasses of the behavior are for)
'''

#########
######    Superclass Access
#########

'''
-super() function, specialize behavior in a way that depends on its superclass's behavior. 

Example code below
'''
class Teller:
    def deposit(self, amount, account):
        account.deposit(amount)
class CorruptTeller(Teller):
    def __init__(self):
        self.coffers = 0

    def deposit(self, amount, account):
        self.coffers += amount * 0.01           # this account takes some money and passes the new amount to the original deposit
        super().deposit(amount * 0.99, account)

'''
Code that uses super() will become confusing if substitutability is broken (leading to hard to maintain code)
'''

#########
######    Multiple inheritance and method resolution order
#########

'''
- You can inherit multiple classes in a subclass by providing more than one in a class definition

An example of multiple inheritance using cats:
'''
class BigCat:
    def eats(self):
        return ['rodents']


class Lion(BigCat):
    def eats(self):
        return ['wildebeest']


class Tiger(BigCat):
    def eats(self):
        return ['water buffalo']


class Liger(Lion, Tiger):
    def eats(self):
        return super().eats() + ['rabbit', 'cow', 'pig', 'chicken']


if __name__ == '__main__':
    lion = Lion()
    print('The lion eats', lion.eats())
    tiger = Tiger()
    print('The tiger eats', tiger.eats())
    liger = Liger()
    print('The liger eats', liger.eats())
'''
But, multiple inheritance works differently than expected:
The liger eats ['wildebeest', 'rabbit', 'cow', 'pig', 'chicken']

That is not the expected behavior. That's because multiple inheritance (esp the super().eats() ) uses a process called
METHOD RESOLUTION ORDER: this means that python will search in order of the following:

-first/ left most parent and up.
-next parents and up, and continues until there is no more parents (searchs like: liger, lion, bigcat, object, tiger, bigcat, object)
-removes duplicates. 
-final tree search pattern would look like this: (liger, lion, tiger, bigcat, object)

That measn that the super().eats() would grab the first parent, the lion then only do the current classes eat.

__mro__: Method resolution order attribute. lists out the resolution order.
'''
>>> Liger.__mro__
(<class '__main__.Liger'>, <class '__main__.Lion'>,
 <class '__main__.Tiger'>, <class '__main__.BigCat'>, <class 'object'>)
'''
This is the way to make multiple inheritance work, by practicing cooperative multiple inheritance.
This means that each class commits to having the same method signatures (substitutablity) and to calling super().some_method() 
from within its own some_method()
'''

#########
######    Abstract Base Classes
#########
'''
Abstract base classes: in essence, something that looks like inhertiance, functions like an interface.
^- It'll outline which methods and attributes its subclasses must implement.

The base abstract class needs to be made so that other classes know how to behave  (acts as a template)

ABC is used to easily create an abstract base class
OR
@abstractmethod decorator can be added to enforce the rule that the methods must be defined in any subclass of the ABC

And with that, it can be modeled below with predators:
(if any class doesn't define the eat method, an exception will be raised)
'''
from abc import ABC, abstractmethod


class Predator(ABC):
    @abstractmethod
    def eat(self, prey):
        pass


class Bear(Predator):
    def eat(self, prey):
        print(f'Mauling {prey}!')


class Owl(Predator):
    def eat(self, prey):
        print(f'Swooping in on {prey}!')


class Chameleon(Predator):
    def eat(self, prey):
        print(f'Shooting tongue at {prey}!')


if __name__ == '__main__':
    bear = Bear()
    bear.eat('deer')
    owl = Owl()
    owl.eat('mouse')
    chameleon = Chameleon()
    chameleon.eat('fly')
'''

If I then wanted to add another animal, I need to add the eat method or i'll get a type error 

If I wanted to add another method in the class that has an ABC, it will not affect the raise an error because the ABC only enforces
that the subclass minimally implements the method it defines. (AS LONG AS THE INTERFACE IS IMPLEMENTED, ITS FINE)

(more commonly will use composition via inversion of control)
'''
#########
######    Inheritance and composition in the bookmark app
#########
#########
######    refactoring to use abstract base case
#########
'''
The one way we can use ABC would be the commands in the command module because each command implements the execute() method

Now we can create a base class as Command that defines execute() method as an abstract method. 

An issue that will effect substitutability is the fact that there are a few different signatures for the execute()
they are the face that some take in data as an arguement and others take in no arguements.

This would lead to the best choice being having data as an optional keyword arg to the execute method that doesn't already accept it
(We wouldn't make all execute() methods accept a variable number of pos args, *args, because it's best practice to be explict with the
arguements you accept until you need the flexibility to handle widely differing numbers of args

The affected code would look like this
'''
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, data):


class CreateBookmarksTableCommand(Command):
    def execute(self, data=None):
        ...


class AddBookmarkCommand(Command):
    ...

'''
With the execute() giving a consistant signature, we can simplfy the choose() method like so:
'''
class Option:
    ...

    def choose(self):
        ...

        message = self.command.execute(data)

'''
'''

################################################################################################
### CHAPTER 9 CHAPTER 9 CHAPTER 9 CHAPTER 9 CHAPTER 9 CHAPTER 9 CHAPTER 9 CHAPTER 9 CHAPTER 9 ##
################################################################################################
#################################################            ###################################
################################################ ############ ##################################
################################################ ############ ##################################
################################################ ############ ##################################
################################################ ###########  ##################################
#################################################             ##################################
############################################################# ##################################
############################################################# ##################################
############################################################# ##################################
################################################################################################



#########
######    Keeping things lightweight
#########
'''
-Keeping things to x lines or pages can allow for confusing code because of code needed to be squished onto x lines/pages.
-Keeping things to single responsibility

-A common measure of complexity is `cyclomatic` complexity: this is calculated by determining the number of execution paths through
a function of method. (Which means the structure/complexity of a function is affected by the number of conditional expressions and loops
it contains)

-The main goal with this scores is to reduce complexity. As the score stays high, think about refactoring.
-A way to self measure the complexity of a function is by creating a graph of the control flow/ or the path the code takes as it
executes. (count the number of nodes/edges in the graph and calculate the cyclomatic complexity)
-The edges are arrows that follow different execution paths your code can take.
-The following are considered nodes:
    -The “start” of the function (where the control flow enters)
    -if/elif/else conditions (each one is its own node)
    -for loops
    -while loops
    -The “end” of a loop (where you draw the execution path back to the start of the loop)
    -return statements

-It is calculated as the following
    - Cyclomatic complexity (M)
    is equal to
    -Number of edges MINUS
    -number of nodes
    - PLUS 2

With that, we have an example:
'''
def has_long_words(sentence):
    if isinstance(sentence, str):
        sentence = sentence.split(' ')

    for word in sentence:
        if len(word) > 10:
            return True

    return False
'''
THE EXPLAINATION IS IN THE SAME FOLDER to count the edges and nodes

most recommended complexity 10 or less.
(Cyclomatic complexity testing is good for unit testing.)

good code coverage tool
https://coverage.readthedocs.io/

'''

#########
######    Halstead Complexity
#########

'''
https://en.wikipedia.org/wiki/Halstead_complexity_measures
https://radon.readthedocs.io/en/latest/ <--- TOOL

-Halstead complexity attempts to measure quantitatively the ideas of level of abstraction,
maintainability, and defect rate
^ - This is acheived by inspecting a programs use of programming langs built in operators and how many variables and expressions it 
    contains.


For this example. We will revisit the github stars code from chapters earlier    

'''
def execute(self, data):
    bookmarks_imported = 0

    github_username = data['github_username']
    next_page_of_results = f'https://api.github.com/users/{github_username}/starred'

    while next_page_of_results:
        stars_response = requests.get(
            next_page_of_results,
            headers={'Accept': 'application/vnd.github.v3.star+json'},
        )
        next_page_of_results = stars_response.links.get('next', {}).get('url')

        for repo_info in stars_response.json():
            repo = repo_info['repo']

            if data['preserve_timestamps']:
                timestamp = datetime.strptime(
                    repo_info['starred_at'],
                    '%Y-%m-%dT%H:%M:%SZ'
                )
            else:
                timestamp = None

            bookmarks_imported += 1
            AddBookmarkCommand().execute(
                self._extract_bookmark_info(repo),
                timestamp=timestamp,
            )

    return f'Imported {bookmarks_imported} bookmarks from starred repos!'

'''
cyclomatic complexity chart is in the local folder

ANOTHER TOOL TO HELP http://www.sonarqube.org/
The tools can usually be added to the code editors

'''


#########
######   Breaking Down Complexity 
#########

#########
######   Extracting configurations 
#########

'''
This part will be about adapting code to new requirements

This will be an example on having an app that will select random food at the /random endpoint
the code will look like this:
'''
import random

FOODS = [
    'pizza',
    'burgers',
    'salad',
    'soup',
]

def random_food(request):
    return random.choice(FOODS)

'''
-For story sake, the service gets popular, and some users want a full app around it.
-They ask for a response in JSON format.
-So if they send a `Accept:application/json` header, they will get a response.

The new code will look like this:

'''
import json
import random

...

def random_food(request):
    food = random.choice(FOODS)

    if request.headers.get('Accept') == 'application/json':
        return json.dumps({'food': food})
    else:
        return food
'''

-Cyclomatic complexity went from 1 to 2.
-The issue is that if we need to add more events, we will slowly increase our complexity

like so:

'''
...

def random_food(request):
    food = random.choice(FOODS)
    if request.headers.get('Accept') == 'application/json':
        return json.dumps({'food': food})
    elif request.headers.get('Accept') == 'application/xml':
        return f'<response><food>{food}</food></response>'
    else:
        return food

'''
-Now the complexity is 3.

-A way to solve this will be mapping all the conditionals into a dictionary
-That will look like this:

'''
...

def random_food(request):
    food = random.choice(FOODS)

    formats = {
        'application/json': json.dumps({'food': food}),
        'application/xml': f'<response><food>{food}</food></response>',
    }

    return formats.get(request.headers.get('Accept'), food)
'''
And with that, complexity is now back to 1.
'''

#########
######   Extracting Functions
#########
'''
-Continuing on the random food from before
-Two things are growing in tandem with the random_food function:
    -1. the code knows WHAT TO DO (format response as JSON, XML, so on)
    -2. the code knows HOW TO DECIDE what to do (based on accept header values)

-With this we can see that we can seperate concerns. (since each item in the formats dict have a value that is a function for the food variable)
-each of the values can be a function that accepts food argument and returns the formatted response that will go back to the user

-Now, we can have the random_food function to use the separated response-format functions. It would look like this:
'''
def to_json(food):
    return json.dumps({'food': food})


def to_xml(food):
    return f'<response><food>{food}</food></response>'


def random_food(request):
    food = random.choice(FOODS)

    formats = {
        'application/json': to_json,
        'application/xml': to_xml,
    }

    format_function = formats.get(
        request.headers.get('Accept'),
        lambda val: val
    )
    return format_function(food)
'''
-The dict will now map formats to the function that can return the response for that format and random_food will call that func with 
the food value
-If no function is available after calling formats.get() it'll fallback to a function that returns the food value unchanged


-And now to FULLY separated concerns, we can extract formats and the business of gettingf the right function from it into its own 
function get_format_function
'''
def get_format_function(accept=None):
    formats = {
        'application/json': to_json,
        'application/xml': to_xml,
    }

    return formats.get(accept, lambda val: val)


def random_food(request):
    food = random.choice(FOODS)
    format_function = get_format_function(request.headers.get('Accept'))
    return format_function(food)
'''
-With that, all of the functions have a cyclomatic complexity of 1. They are quite readable and also have seperated concerns
-On top of that, it is very extensible. The proccess is now:
-1. add a new function to format the response as desired
-2. add the mapping of the required Accept header value to the new formatting function
-3. good to go


'''

#########
######   Decomposing Classes
#########

#########
######   Intialization complexity 
#########
'''
 The following will be based on this code:
'''
class Book:
    def __init__(self, data):
        self.title = data['title']
        self.subtitle = data['subtitle']

        if self.title and self.subtitle:
            self.display_title = f'{self.title}: {self.subtitle}'
        elif self.title:
            self.display_title = self.title
        else:
            self.display_title = 'Untitled'

'''
-While the domain logic is complex, the code is more likely to reflect that. That means its more important for developers to rely on 
useful abstractions that make sense

-In the case of this code, we can extract the logic for display_title into a set_display_title method that you could call from the __init__

-That would look like this:
'''
class Book:
    def __init__(self, data):
        self.title = data['title']
        self.subtitle = data['subtitle']
        self.set_display_title()

    def set_display_title(self):
        if self.title and self.subtitle:
            self.display_title = f'{self.title}: {self.subtitle}'
        elif self.title:
            self.display_title = self.title
        else:
            self.display_title = 'Untitled'
'''
-A second glance we can see that a couple issues arise from this approach:
- 1. Getters and setters are generally discouraged because they clutter up the class
- 2. its good practice to set all the necessary attributes to some intial value directly inside __init__, but display_title is set in a
different method

-The second can be fixed by setting display_title to untitled by default, but it can be confusing. A user might conclude the display title
is typically untitled

-WE could also extract a method w/o suffering drawbacks. (it would involve creating a function that returns a value for display_title)

-BUT the code would look like this if we were going to do this.

[[[]]]
book = Book(data)
return book.display_title
[[[]]]

-It looks weird and there is a way to update display_title logic without having to update the second line.

-It would be the @property decorator. It is used to signify that a method on a class should be accesible on attribute.

-Note: methods can be used as properties only if self is their only args, because when you access the attributes, YOU CANT PASS ANY
ARGS TO IT.

-We can now do this instead:
'''
class Book:
    def __init__(self, data):
        self.title = data['title']
        self.subtitle = data['subtitle']

    @property
    def display_title(self):
        if self.title and self.subtitle:
            return f'{self.title}: {self.subtitle}'
        elif self.title:
            return self.title
        else:
            return 'Untitled'
'''
- Using the @property, you can still reference book.display_title as an attribute, but all its complexity is abstracted into its own 
function.

-NOTE: properties are methods, repeatedly accessing them means that the methods are called each time. (this is can be ok, but 
it can have performance impacts for properties that are expensive to calculate)

'''

#########
######   Extracting Classes and forwarding calls
#########
'''
-When get_format_function was extracted from random_food, it was still called from it's original location.
(how would we maintain backwards compatibility)(backwards compatibility: evolve software w/o breaking the implementation that was 
previously used)

-We would have to forward. (The same premise of how the mail system does it.)
- FORWARDING: you can accept calls in one class and pass them along to another class under the hood.

-Now lets say the book class has grown to keep track of the author information.

The code would look like this: (It has authors name/ author for citation)
'''
class Book:
    def __init__(self, data):
        # ...
        self.author_data = data['author']         #1

    @property
    def author_for_display(self):                 #2
        return f'{self.author_data["first_name"]}
 {self.author_data["last_name"]}'

    @property
    def author_for_citation(self):                #3
        return f'{self.author_data["last_name"]},
 {self.author_data["first_name"][0]}.'


!@%STYLE%@!
{"css":"{\"css\": \"font-weight: bold;\"}","target":"[[{\"line\":3,\"ch\":50},{\"line\":3,\"ch\":52}],[{\"line\":6,\"ch\":50},{\"line\":6,\"ch\":52}],[{\"line\":11,\"ch\":50},{\"line\":11,\"ch\":52}]]"}
!@%STYLE%@!

'''

AND THE BOOK CLASS WOULD BE USED LIKE THIS:

'''
book = Book({
    'title': 'Brillo-iant',
    'subtitle': 'The pad that changed everything',
    'author': {
        'first_name': 'Rusty',
        'last_name': 'Potts',
    }
})


print(book.author_for_display)
print(book.author_for_citation)
'''
-Being able to reference book.author_for_display/ book.author_for_citation has been great, but the author dict in the properties feels
clunky. Especially if we would want to to more with the authors.

-So, the next move is to extract an `Author`  class to encapsulate author behaviors and information. (it is also a great separtion of
concerns)

-When several methods in a class share a common prefix/suffix. esp one that doesn't match the name of the class.There might be a new 
class waiting to be extracted (In this case, we COULD use author_ to justify `Author` class)

-This class will have, (the same information as before and more structured) but also have:
1. Accept `accept_data` as a dict in the __init__, storing each relevant value (first name/ last name/ so on) from the dict as an attribute
2. Have 2 properties,`for_display` and `for_citation`, that return the properly formatted author string

- Other notes: Book to keep working for users (keep author_data, author_for_display, and author_for_citation behaviors on book).
(and forward calls from book.author_for_display to author.for_display and so on)

The code of extracting an Author class from the Book class would look like:
'''
class Author:
    def __init__(self, author_data):
        self.first_name = author_data['first_name']
        self.last_name = author_data['last_name']

    @property
    def for_display(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def for_citation(self):
        return f'{self.last_name}, {self.first_name[0]}.'


class Book:
    def __init__(self, data):
        # ...

        self.author_data = data['author']
        self.author = Author(self.author_data)

    @property
    def author_for_display(self):
        return self.author.for_display

    @property
    def author_for_citation(self):
        return self.author.for_citation
'''
-And now we have old code that the users to use as we get the new code in.

-But now that we have new code, we should let the users know the old class is deprecated. We can use `warnings` for that.
We can use a DeprecationWarning for this. That would look like:
'''
import warnings

warnings.warn('Do not use this anymore!', DeprecationWarning)

'''
https://www.youtube.com/watch?v=D_6ybDcU5gc <-- Has a bunch of deprecation and extraction tricks

-The best practice would be to let the users know to use book.author.for_display so they are properly guided

'''

################################################################################################
### CHAPTER 10 CHAPTER 10 CHAPTER 10 CHAPTER 10 CHAPTER 10 CHAPTER 10 CHAPTER 10 CHAPTER 10 ####
################################################################################################
###########################  ##############      ###############################################
###########################  ############  ######  #############################################
###########################  ############  ######  #############################################
###########################  ############  ######  #############################################
###########################  ############  ######  #############################################
###########################  ############  ######  #############################################
###########################  ############  ######  #############################################
###########################  ############  ######  #############################################
###########################  ##############      ###############################################
################################################################################################



#########
######    Achieving Loose Coupling
#########
#########
######    Defining Coupling
#########
#########
######    The connective tissue
#########
'''
-Where 2 pieces of code have high interdependency, that mesh is tightly woven and taut. (Moving either piece of code around requires the
other to move around too)
-The mesh between areas with little or no interdependence is flexible (like rubberbands). 
-The code in the looser part of the mesh will have to be changed more drastically to impact the code around it.

-(the less interconnections the better)
 
'''

#########
######    Tight Coupling
#########
'''
-These create interconnections:
    - A class that stores another object as an attribute
    - A class whose methods call functions from another module 
    - A function or method that does a lot of procedural work using methods from another object

Consider the following code: (display_book_info func needs to know all the diff pieces of info that a book instance contains)
'''
class Book:
    def __init__(self, title, subtitle, author):
        self.title = title
        self.subtitle = subtitle
        self.author = author

def display_book_info(book):
    print(f'{book.title}: {book.subtitle} by {book.author}')
'''
-If the book class and the display_book_info function lived in the same module, the code might be tolerable. 
-They operate on related information and be together in one place

-Tightly coupling isn't inherently bad. (it could just be a pointer)
-These 2 have high cohesion because display_book_info operates only on info from book and does something book related.
(It is so tightly couple to book that it makes sense to be in the class)

-That would look like this:
'''
class Book:
    def __init__(self, title, subtitle, author):
        self.title = title
        self.subtitle = subtitle
        self.author = author

    def display_info(self):
        print(f'{self.title}: {self.subtitle} by {self.author}')
'''
-* TIGHT COUPLING IS AN ISSUE WHEN IT EXISTS BETWEEN 2 SEPARATE CONCERNS.


-Some code might have been written like below.
'''
import re


def remove_spaces(query):
    query = query.strip()
    query = re.sub(r'\s+', ' ', query)
    return query


def normalize(query):
    query = query.casefold()
    return query


if __name__ == '__main__':
    search_query = input('Enter your search query: ')
    search_query = remove_spaces(search_query)
    search_query = normalize(search_query)
    print(f'Running a search for "{search_query}"')
'''
-It is easy to see that the prochedure is tightly coupled to the search module. The code would have to change if we changed the way
cleaning querys worked.

- (You can effectively identify coupling by assessing the likelihood that any given change to a module will require a change to the code
that uses it)

- Now, lets suppose that users are still not getting consistent result. Upon further investigation, it's because some users are putting
quotes around the query

-So this is what the quote removing code would look like:

'''
def remove_quotes(query):
    query = re.sub(r'"', '', query)
    return query


if __name__ == '__main__':
    ...
    search_query = remove_quotes(search_query)
    ...


#########
######    Loose Coupling
#########
'''
- Loose Coupling is the ability of two pieces of code to accomplish a task without either relying heavily on the details of the other.
-(This is commonly achieved through abstraction.) (Loosely coupled code implements and uses interfaces; and an exteme end, it uses only
interfaces for intercommunication.)

-If we switch the school of thought over to thinking about the code in terms of messages that are sent to each other.
(you will be able to identify cleaner abstractions and stronger cohesion)

-(These messages are questions you ask of an object or the things you tell it to do.)
(in the folder is an image of how it would look in code)

-The next code is looking back at the main prochedure:
'''
if __name__ == '__main__':
    search_query = input('Enter your search query: ')
    search_query = remove_spaces(search_query)
    search_query = remove_quotes(search_query)
    search_query = normalize(search_query)
    print(f'Running a search for "{search_query}"')
'''
-What is written achieves the task, but the message is very hoopy and jumpy. (users would want a query to clean up, it doesn't matter how)
-The thought would be that a message would be "here is my query, clean it please."

-This means that we would need a class to encapsulate the logic. (going back to separating concerns)

-This is how the code be refactored to reflect the above:
'''
import re


def _remove_spaces(query):
    query = query.strip()
    query = re.sub(r'\s+', ' ', query)
    return query


def _normalize(query):
    query = query.casefold()
    return query


def _remove_quotes(query):
    query = re.sub(r'"', '', query)
    return query


def clean_query(query):
    query = _remove_spaces(query)
    query = _remove_quotes(query)
    query = _normalize(query)
    return query


if __name__ == '__main__':
    search_query = input('Enter your search query: ')
    search_query = clean_query(search_query)
    print(f'Running a search for "{search_query}"')

'''
-Whenever ill need to do another technique to clean the queries it will:
1. Create a function to perform the new transform query
2. Call the new function inside `clean_query`
3. Call it a day, confident that users are all cleaning properly

(this is an example of loose coupling, separation of concerns, and encapsulation)
'''


#########
######    Recognizing Coupling
#########

#########
######    Feature Envy
#########
'''
-Feature Envy: (When the code performs several tasks using mainly features from another area) (main procedure wants to be the search
module because it uses all of its features explictly)

-One way feature envy can be fixed: roll it up into a sengle entry point back at the source. 
(ie when clean_query function was built, the search module is where query cleaning logic goes, so clean query went there.
the rest of the code is now unaware once we moved it with no more feature envy)
'''

#########
######    Shotgun Surgery
#########
'''
-The need for Shotgun Surgery goes down when (the coder addresses feature envy, uses separting concerns and good practice of 
encapsulation/ abstraction)
-Shotgun surgery is a sign of tight coupling
'''

#########
######    Leaky Abstractions
#########
'''
-Feature envy is a symptom of leaky abstraction. (the goal is to have the user to trigger the behavior and receive the result and
doesnt care how it happens.)

-Leaky Abstraction: when an abstraction doesnt sufficently hide its details. (claims to provide a simple way to get something done
but it ultimately requires you to have some knowledge about what lies beneath when using it.)

-An example:
 http requests, if the goal is purely to make a GET request and then get some url response back, an abstraction on the get behavior
 would best work.
-THIS ABSTRACTION WORKS MOST OF THE TIME. When the internet is not available or there is no internet connections requests
 will generally just raise an exception.

-Although this is good for error handling, it isn't good for abstractions because it requires the calling code to know about possible
errors that might happen and how to fix them.

-This means requests are now coupled with whatever does the error checking for it.

-A trade off to consider with abstraction, the further you abstract a concept in code, the less customization you can provide.
-This is because abtraction is inherently meant to remove access to detail. The fewer the details you can access, the fewer ways you
have to change the details

-There is probably coupling being introduced if the developer is providing access to a low level detail from a high level layer of 
abstraction.

-As a reminder: loose coupling relies on interfaces, shared abstractions, rather than specific low level details
'''

#########
######    Coupling in the Bookmark app
#########
'''
-All concerns will at some point need to interact with each other. So practice to keep stuff loosely coupled

-Some of the following can be used to reduce coupling while keeping the code working:
    -The presentation layer shows information to, and gets information from, the user.
    -The business logic layer contains the "smarts" of the application - the logic related to the task at hand
    -The persistance layer stores data for the application to be reused later on

-With the refresher of separating concerns into a multitier architecture:
____________________________________________________________________________________________________________
user ->       presentation layer       ->    business logic layer    -> persistance layer
    ^(user sees and chooses options)    ^(options trigger commands)   ^(commands fetch and manipulate data)
____________________________________________________________________________________________________________
-Using the commands execute method in the business logic an abstraction that is a great example of loose coupling

-A second look at the addBookMarkCommand: (it does this)
    1. receives the data for a bookmark along with an optional timestamp
    2. generates a timestamp if needed
    3. tells the persistance layer to store the bookmark
    4. returns a message stating that the addition was a success
'''
class AddBookmarkCommand(Command):
    def execute(self, data, timestamp=None):
        data['date_added'] = timestamp or datetime.utcnow().isoformat()
        db.add('bookmarks', data)
        return 'Bookmark added!'

'''
-Upon second glance, the last 2 lines of the execute method show signs of tight coupling.

-The first tightly coupled line `calls db.add` is coupled to the persistance layer/ database itself.
- If the method in which we want to store the bookmarks, like json for example, it doesnt work.
- There is also feature envy happening. most of the commands make direct use of one of the operations from database manager

-The second line shows tight coupling in the return statement.
- (the return message is intended for the user. It is handling presentation level information, in the business logic layer (leaky abstraction))

-(on a side note), `CreateBookmarksTableCommand`, introduce even tighter coupling.
- the `Table` in the name implies database, a persistance layer feature, and then the command is referenced when the application starts
  in the presentation layer
- The command spans all layer of abstraction that was previously built

'''

#########
######    Addressing Coupling
#########

'''
-(Context is of if I wanted to make a mobile version)
-( what is the tightly coupled areas?)
-

'''

#########
######    User Messaging
#########

'''
-Mobile builds are icon oriented. (this means the software needs to use icons in addition to the messages for success)
-BUT from above, the app is coupled to the business logic layer.
-The fix will be releasing control of messaging fully to the presentation layer. (which raises the question: how can you keep the 
 interaction between commands and the presentation layer without each command having explict knowledge of the message it shows?)

-A way to handle this can be splitting up the `success` and the `result` on the presentation layer. (where each command returning a 
 tuple representing both status and result)

- This means that commands should all be true. BUT if they return false and fail with the result of none

- (for the next part, each of the commands are updated to return a status/ result tuple)
- The best way to do this would be to configure each option instance with specific message to use when a command succeeds. (this is 
  because it gives the right amount of customization without a lot of extra effort.)

-The changes to the code would look like this:
(decoupling layers of abstractions with interfaces)
'''
class AddBookmarkCommand(Command):
    def execute(self, data, timestamp=None):
        data['date_added'] = timestamp or datetime.utcnow().isoformat()
        db.add('bookmarks', data)
        return True, None

class ListBookmarksCommand(Command):
    def __init__(self, order_by='date_added'):
        self.order_by = order_by

    def execute(self, data=None):
        return True, db.select('bookmarks', order_by=self.order_by).fetchall()
'''

Below is `using statuses and results in the presentation layer`
'''
def format_bookmark(bookmark):
    return '\t'.join(
        str(field) if field else ''
        for field in bookmark
    )


class Option:
    def __init__(self, name, command, prep_call=None,
 success_message='{result}'):
        self.name = name
        self.command = command
        self.prep_call = prep_call
        self.success_message = success_message

    def choose(self):
        data = self.prep_call() if self.prep_call else None
        success, result = self.command.execute(data)

        formatted_result = ''

        if isinstance(result, list):
            for bookmark in result:
                formatted_result += '\n' + format_bookmark(bookmark)
        else:
            formatted_result = result

        if success:
            print(self.success_message.format(result=formatted_result))

    def __str__(self):
        return self.name

def loop():
    ...

    options = OrderedDict({
        'A': Option(
            'Add a bookmark',
            commands.AddBookmarkCommand(),
            prep_call=get_new_bookmark_data,
            success_message='Bookmark added!',
        ),
        'B': Option(
            'List bookmarks by date',
            commands.ListBookmarksCommand(),
        ),
        'T': Option(
            'List bookmarks by title',
            commands.ListBookmarksCommand(order_by='title'),
        ),
        'E': Option(
            'Edit a bookmark',
            commands.EditBookmarkCommand(),
            prep_call=get_new_bookmark_info,
            success_message='Bookmark updated!'
        ),
        'D': Option(
            'Delete a bookmark',
            commands.DeleteBookmarkCommand(),
            prep_call=get_bookmark_id_for_deletion,
            success_message='Bookmark deleted!',
        ),
        'G': Option(
            'Import GitHub stars',
            commands.ImportGitHubStarsCommand(),
            prep_call=get_github_import_options,
            success_message='Imported {result} bookmarks from starred repos!',
        ),
        'Q': Option(
            'Quit',
            commands.QuitCommand()
        ),
    })

'''
- With this, the code is now decoupled on the business logic and the presentation layer. (they now interact using the idea of a status
  and result instead of hardcoded )


'''

#########
######    Bookmark Persistence
#########
'''
-(for the mobile user, they would need the data for the bookmarks to live on the cloud)
-(this would mean that I need to swap out the database module for a new persistance layer that interacts with the new api.)
-(on that note: it is good to use shared abstractions to reduce coupling)
-(That means that we will need to set up the api persistance layers to deal with the same set of concerns)

-(as the commands in the execute interface was reduced, the persistance layer needs a more general set of crud operations to decouple
them from commands)

-the database shares some commonalities:
    -Data represented as record objects
    -Crud operations with (sql on database/ http on api) (insert/select/update/delete and  post/get/put/delete)
    -Config nneeded for the (databases files and table/ apis domains and urls)

'''

#########
######    Trying it out
#########
'''
-In order to decouple: ABC on the perstence layer to define the interface
Create a BookmarkDatabase persistance layer that sits between commands and database manager class

- The persistance module will need new classes, that means the code will need the commands to be refactored instead of the databaseManager
directly. (with that: the interface shouldnt have any database/ api specific methods names.)

-The interface should provide method that would apply to most any persistance layers, which would be:
    - __init__ for intial config
    - create(data) to create a new bookmark
    - list(order_by) to list all bookmarks
    - edit(bookmark_id, data) to update a bookmark
    - delete(bookmark_id) to remove a bookmark

- Some thoughts about how this would be done:
    -The logic in the `CreateBookarksTableCommand` should be an initial config for a bookmark database persistance layer
    -the instantiation of the databaseManager fits in there too. (this can be done by writing the implementation for each method of 
    the `PersistanceLayer` abstraction in the `BookmarksDatabase`)
    -Each database centric method call(db.add, for example) from the original commands can be moved to the appropriate method. This will
    free up the commands to call the methods from `BookmarksDatabase`

The code will look like this:  
'''
from abc import ABC, abstractmethod

from database import DatabaseManager


class PersistenceLayer(ABC):
    @abstractmethod
    def create(self, data):
        raise NotImplementedError('Persistence layers must implement a create method')

    @abstractmethod
    def list(self, order_by=None):
        raise NotImplementedError('Persistence layers must implement a list method')

    @abstractmethod
    def edit(self, bookmark_id, bookmark_data):
        raise NotImplementedError('Persistence layers must implement an edit method')

    @abstractmethod
    def delete(self, bookmark_id):
        raise NotImplementedError('Persistence layers must implement a delete method')


class BookmarkDatabase(PersistenceLayer):
    def __init__(self):
        self.table_name = 'bookmarks'
        self.db = DatabaseManager('bookmarks.db')

        self.db.create_table(self.table_name, {
            'id': 'integer primary key autoincrement',
            'title': 'text not null',
            'url': 'text not null',
            'notes': 'text',
            'date_added': 'text not null',
        })

    def create(self, bookmark_data):
        self.db.add(self.table_name, bookmark_data)

    def list(self, order_by=None):
        return self.db.select(self.table_name, order_by=order_by).fetchall()

    def edit(self, bookmark_id, bookmark_data):
        self.db.update(self.table_name, {'id': bookmark_id}, bookmark_data)

    def delete(self, bookmark_id):
        self.db.delete(self.table_name, {'id': bookmark_id})

'''

-The next thing that needs updating is to replace the `db` instance of `DatabaseManager` with persistance( an instance of bookmarkDatabase)
in the commands module.
-Also have to go through the rest of the module replacing calls to `DatabaseManager`(`db.select`) methods with those from `PersistenceLayer`(`persistence.list`).

'''
from persistence import BookmarkDatabase

persistence = BookmarkDatabase()


class AddBookmarkCommand(Command):
    def execute(self, data, timestamp=None):
        data['date_added'] = timestamp or datetime.utcnow().isoformat()
        persistence.create(data)
        return True, None


class ListBookmarksCommand(Command):
    def __init__(self, order_by='date_added'):
        self.order_by = order_by

    def execute(self, data=None):
        return True, persistence.list(order_by=self.order_by)


class DeleteBookmarkCommand(Command):
    def execute(self, data):
        persistence.delete(data)
        return True, None
class EditBookmarkCommand(Command):
    def execute(self, data):
        persistence.edit(data['id'], data['update'])
        return True, None

'''
-In the end: 
    -the app is now extensible to new use cases
    -concerns are well separated (presentation/ business logic/ persistance are now in isolation.)
    - (we could swap out bookmarksDatabase for perhaps a BookmarksStorageService that sends data via an http api)


'''

################################################################################################
### CHAPTER 11 CHAPTER 11 CHAPTER 11 CHAPTER 11 CHAPTER 11 CHAPTER 11 CHAPTER 11 CHAPTER 11 ####
################################################################################################
###########################  ############  #####################################################
###########################  ############  #####################################################
###########################  ############  #####################################################
###########################  ############  #####################################################
###########################  ############  #####################################################
###########################  ############  #####################################################
###########################  ############  #####################################################
###########################  ############  #####################################################
###########################  ############  #####################################################
################################################################################################



#########
######    Onward and Upward
#########
#########
######    What Now
#########

#########
######    Develop a Plan
#########
'''
-Using a mind map to learn: organizes data in a hierarchical way of viewing notes visually (starting from a central node)

- (or just make a plan for learning)
'''

#########
######    Execute the Plan
#########
'''
-Using the mind map could work well to explore ideas nonlinearly

- (NOTE: ITS A PITFALL TO dive too deep into one topic without any context about the rest of the bigger picture.)
- (too much focus in one spot can lead to solidifying an inaccurate or incomplete understanding that can inhibit future learning)

'''

#########
######    Track the Progress
#########
'''
-Learning is subjective, so setting ideas to a state is a good idea. Like the following:
    1. Want to learn/ need to learn
    2. Actively learning: explored/ read some resources on that topic (and looking for more)
    3. Familiar: understand the topic generally, and have some idea on how to apply it
    4. Comfortable: Applied the concepts from the topic a few times and have a handle on it
    5. Proficient: Applied the concepts enough to know some of the nuances, and know which resources to reach for when you encounter new
      problems

-Mind mapping software:
    www.lucidchart.com
    (www.mindmup.com)
    (https://draw.io)

'''


#########
######    Design Patterns
#########
'''
-All the design patterns are tried and true solutions, and we have ubiquitous language for them. (shared vocabulary for the concepts
a team needs to understand.)

-The command pattern (like the decoupled code that requests an action from the action itself) has a few common pieces, regardless of 
the situation in which it's used:
    1. Receiver: the entity that takes an action. like persisting the data in a database or making an api call.
    2. Command: the entity that contains the info needed for the receiver to take its action
    3. Invoker: the entity that triggers the command to alert the receiver
    4. Client: the entity that assembles the invokers, commands, and receivers to achieve a task

In the app these pieces are as follows:
    1. The `PersistanceLayer` classes are receivers.| (receive enough information to store/retrieve data (from database `BookmarkDatabase`))
    2. The `Command` classes are the commands.| They store the info needed to comm with the persistance layer.
    3. The `Option` instances are the invokers.| They trigger a command to take place when a user chooses an option in the menu.
    4. The Client module is the client. | It hooks up options to commands properly so that users menu choices lead to desired action.

-UML (Unified modeling language): 

'''


#########
######    Ups and Downs of design patterns in python
#########
'''



'''


#########
######    Terms to Start with
#########
'''
Good place to start researching terms:
    -Creational design patterns
    -Factories
    -Behavioral design patterns
    -Command pattern
    -Structural design patterns
    -Adapter pattern


'''


#########
######    Distributed Systems
#########
'''



'''

#########
######    Modes of Failure in Distributed Systems
#########
'''



'''

#########
######    Addressing Application State
#########
'''



'''

#########
######    Terms to start with
#########
'''
Distributed Systems:
    -Fault tolerance
    -Eventual consistency
    -Desired state
    -Concurrency
    -Message queueing


'''

#########
######    Take A python deep dive
#########
#########
######    Python Code Style
#########
'''



'''

#########
######    Language Features are patterns
#########
'''



'''

#########
######    Terms to start with
#########
'''
Pythonic code research term
    -Pythonic code
        --Pythonic way to do X
    -Idiomatic Python
    -Python anti-patterns
    -Python linters

'''

#########
######    REVIEW
#########
'''



'''





