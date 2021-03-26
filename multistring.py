Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # multistring.py

print("=" * 50)
print("My Program")
print("=" * 50)
==================================================
>>> 
>>> a[3]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a[3]
NameError: name 'a' is not defined
>>> "i eat{0} apples {1} bananaes {2} oranges {3} graph". format (3,5,3,2,)
'i eat3 apples 5 bananaes 3 oranges 2 graph'
>>> " i eat {0;10} apples {1} bananaes {2}
SyntaxError: EOL while scanning string literal
>>> "{0;10}".format(hi)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    "{0;10}".format(hi)
NameError: name 'hi' is not defined
>>> "{0;10}".format("hi")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    "{0;10}".format("hi")
KeyError: '0;10'
>>> a.upper"
SyntaxError: EOL while scanning string literal
>>> a.upper
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.upper
NameError: name 'a' is not defined
>>> Life is too short, You need Python'
SyntaxError: invalid syntax
>>> a[:]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a[:]
NameError: name 'a' is not defined
>>> a = 123
>>>  a = -178
 
SyntaxError: unexpected indent
>>>  a = 0
 
SyntaxError: unexpected indent
>>> a = 4.24E10
>>> a = 4.24e-10
>>> 