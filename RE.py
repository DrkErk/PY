import re
'''
examples of some regular expression

- /d is digit for characters and {n} where n is how many consecutive you want

Escape characters:
.  ^  $  *  +  ?  {  }  [  ]  \  |  (  )
To get the escape characters is: \ 


So lets say we want to sift some data for a phone number
'''

phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
out = phoneNumRegex.search('The phone number is: 901-213-5917')


'''
When you called "out" it will return: 901-213-5917

But, if you area code or the base of the number you can call the group function. In this case:
out.group() will return "901-213-5917"
out.group(0) will return "901-213-5917"
out.group(1) will return "901"
out.group(2) will return "213-5917"


Now, if you wanted to find something OR something. use a pipe: |

ex:
"AAA is not BBB"
AAA | BBB would return AAA
and 
"BBB is not AAA"
AAA | BBB would return BBB
Because it is what ever is the first hit.

HINT FOR SELF: you can use the findall() method to find all matching occurences

'''


