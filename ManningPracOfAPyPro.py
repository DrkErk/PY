from multiprocessing import connection
import re
import sqlite3

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






















































































