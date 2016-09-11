import re
x= "hello there my email is geraldobraho@gmail.com  you can send me any email here"
y=re.findall('\S+\@\S+',x)
print y 
