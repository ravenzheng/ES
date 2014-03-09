from xml.sax.saxutils import escape
from xml.sax.saxutils import unescape
from string import Template

wordlist = 'vocabulary.txt'
noteTemplate = 'worUnitTemplate.enex'
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

rules = {};
rules['t e'] = 'te'
rules['t i'] = 'ti'
rules['t y'] = 'ty'
rules['t o '] = 'to '
rules['t ur'] = 'tur'
rules['t ua'] = 'tua'
rules['t ch'] = 'tch'
rules['st oic'] = 'stoic'

def trimSpace (source):
	for target in rules:
		source = source.replace(target, rules[target])
		source = source.replace('?', 'E.g.')
	return source

def isQuiz(source):
	return 'Answers' in source;

def processQuizzes(reviewQuizzes, index):
	f = open('quizzes ' + str(index) + '.txt', 'w')
	f.write(reviewQuizzes)
	return reviewQuizzes;

answers = [] 
def processUnit(unitContent, index):
	arr = unitContent.split('Review Quizzes ' + str(index))
	#prcess word units
	wordContent = arr[0]
	wordUnits = wordContent.split('==========')
	for wordUnit in wordUnits:
		if isQuiz(wordUnit):
			wordUnits.remove(wordUnit)
			answers.append(wordUnit)
	return wordUnits;
	#reviewQuizzes = arr[1]
	#prcessQuizzes(reviewQuizzes, index)
	

units = []
words = []
sum = ''
wordString = ''
f = open(wordlist)
wordString = f.read();
wordString = trimSpace(wordString)

units = wordString.split('==========Unit')
for index in range(1, 31):
	wdContent = ''
	words = processUnit(units[index], index) 
	for word in words:
		if 'Answers' not in word:
			wdContent = wdContent + word
		else:
			print word
	title = 'unit ' + (str(index) if index >= 10 else '0' + str(index)) + ' ' + str(len(words))
	print title
	wordString = noteTemplateStr.format(title, wdContent)
	sum += wordString
	
	f = open("unit " + str(index) + '.txt', 'w+')
	f.write(wdContent)

sum = exportTemplateStr.format(sum)
f = open('import.enex','w+')
f.write(sum)
f.flush()

