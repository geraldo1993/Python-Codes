name=raw_input('Enter file: \n')
handle=open(nameFile,'r')
text=handle.read()
words=text.split()
counts=dict()

for words in words:
    counts[word]=counts.get(word,0)+1


bigcount=None
bigword=None

for word,count in counts.item():
    if bigword is None or count >bigcount:
        bigword=word
        bigcount=count

print bigword,bigcount        
