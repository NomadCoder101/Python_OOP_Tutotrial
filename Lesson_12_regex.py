print('dog' in 'my dog is great ')

# identifiers and qunatifiers

text = 'The agnets phone number is  408-555-5555. Call Soon!'

print('phone 'in text)

import re

pattern = 'phone'
print(re.search(pattern,text))

pattern = 'not in text'
print(re.search(pattern,text))

pattern = 'phone'
match =re.search(pattern,text)
print(match)
print(match.span())
print(match.start())
print(match.end())

text = 'my phone once ,my phone twice'

match = re.search(pattern,text)
print(match)
matches = re.findall('phone',text)
print(matches)
print(len(matches))
for match in re.finditer('phone',text):
    print(match)
    print(match.span())
    print(match.group())

'''
regular expression patterns 
# Character identifiers
=======================================================
char -- Descp   --         Example code  --example match
=========================================================
\d   -- A digit --        file_\d\d      file_25
\w   -- Alphanumeric --   \w-\w\w\w      A-b_1
\s   -- White space  --    a\sb\sc       a b c
\D   -- A non digit  --    \D\D\D        ABC
\W   -- Non-Alphanumeric   \W\W\W\W\W    *-+=)
\S   -- Non-whitespace     \S\S\S\S       Yoyo

=================================================

'''

text = 'My phone number is 408-555-1234'

phone = re.search('408-555-1234',text)
print(phone)

text = 'My phone number is 408-555-0234'
phone = re.search(r'\d\d\d-\d\d\d\-\d\d\d\d',text)
print(phone)
print(phone.group())

'''
Quantifiers
====================================================================================
Character  -- Description             -- Example Pattern Code -- Example Match
====================================================================================

+             Occurs one or more times -- Version\w\w+        -- Version A-b1_1
{3}           Occurs exactly 3 times   -- \D{3}               -- abc
{2,4}         Occurs 2 to 4 times      -- \d{2,4}             -- 123
{3,}          Occurs 3 or more         -- \w{3,}              -- anycharacters
*             Occurs zero or more times--  A*B*C*             -- AAACC
?             Once or none             --  plurals?           -- plural

=====================================================================================

'''

#phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
#phone = re.search(r'\d{3}\W\d{3}\W\d{4}',text)
phone = re.search(r'\d{3}-\d{3}-\d{4}',text)
print(phone)
print(phone.group())

print("=================================")
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern,text)
print(results)
print(results.group(1))
print(results.group(2))
print(results.group(3))

for item in results.group():
    print(item)

print("===============================")

# Additional Regex Syntax

print(re.search(r'cat|dog', 'The dog is here '))

print("===============================")
#wildcard .
print(re.findall(r'at','The cat in the hat sat there'))
print(re.findall(r'.at','The cat in the hat sat there'))
print(re.findall(r'...at','The cat in the hat went splat'))

print("===============================")

print(re.findall(r'^\d','1 is a number'))
print(re.findall(r'\d$','1 is a number 2'))
print(re.findall(r'\d','1 is a number 2'))
print("===============================")

phrase = 'there are 3 numbers 34 inside 5 this number'

#pattern = r'[^\d]'
pattern = r'[^\d]+'
print(re.findall(pattern,phrase))
pattern = r'[^\D]+'
print(re.findall(pattern,phrase))
pattern = r'[^\w]+'
print(re.findall(pattern,phrase))

test_phrase = 'This is a string! But it has punctuation. How can we remove it ?'
pattern = r'[^!.? ]+'
clean = re.findall(pattern,test_phrase)

print(' '.join(clean))

print('=============================')

text = 'on-ly find the hypen-words in this sentence. But you dont know how long-ish the words are . '

pattern = r'\w+-\w+'
#pattern = r'[\w]+-[\w]+'

print(re.findall(pattern,text))

print("=====================")

text = 'Hello, would you like some catfish?'
texttwo = 'Hello, would you like some catnap?'
textthree = 'Hello, have you seen a caterpiller?'

print(re.search(r'cat(fish|nap|claw)',text))
print(re.search(r'cat(fish|nap|claw)',texttwo))
print(re.search(r'cat(fish|nap|claw)',textthree))
print(re.search(r'cat(fish|nap|erpiller)',textthree))


result=re.search(r'cat(fish|nap|erpiller)',textthree)
print(result.group())

















