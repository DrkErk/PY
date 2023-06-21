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

#end 3.4.3






































