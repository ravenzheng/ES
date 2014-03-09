from xml.sax.saxutils import escape
from xml.sax.saxutils import unescape
from string import Template

wordlist = 'grelist.txt'
noteTemplate = 'noteTemplate.enex'
exportTemplate = 'exportTemplate.enex'
noteTemplateStr = ''
exportTemplateStr = ''

f = open(noteTemplate, 'r')
for line in f:
	noteTemplateStr += line
f.close()

f = open(exportTemplate, 'r')
for line in f:
	exportTemplateStr += line
f.close()


words =[]
wordString = ''
f = open(wordlist)
for line in f:	
	if line.isspace() != True:
		str = line
		words.append(str)
sum = ''

print len(words)
arr = []
for word in words:
	arr = word.split('##')
	title = arr[0].strip()
	
	wordString = noteTemplateStr.format(title)
	sum += wordString
#print sum
print len(words)
sum = exportTemplateStr.format(sum)
#sum = unicode(sum)
#print sum
f = open('import.enex','w+')
f.write(sum)
f.flush()
