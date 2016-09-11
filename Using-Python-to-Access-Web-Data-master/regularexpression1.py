import re
x='The 2 faster highway are 45 and 610'
y=re.findall('[0-9]+',x)
print y

y=re.findall('[abdfsdfdnsfdjsfnsdjfnds]+',x)
print y
