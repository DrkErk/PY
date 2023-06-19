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




































