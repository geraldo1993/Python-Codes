import re



data= 'asdjiejdmasadadasdsdas czczadada dasdas das   bla ba lba blabalba sdsdsad das  ddsdad asdadd  ddsds  @geraldobraho.na.edu'
atpos=data.find('@')
print atpos

sppos=data.find('  ',atpos)
print sppos


host=data[atpos+1:sppos]
print host 
