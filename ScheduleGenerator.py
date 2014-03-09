from string import Template
import calendar
scheduleTemplate = 'scheduleTemplate.enex'
weekendTemplate = 'weekendTemplate.enex'
importTemplate = 'exportTemplate.enex'
scheduleTemplateStr = ''
weekendTemplateStr = ''
importTemplateStr = ''

f = open(scheduleTemplate, 'r')
scheduleTemplateStr = f.read();
f.close()

f = open(weekendTemplate, 'r')
weekendTemplateStr = f.read();
f.close()

f = open(importTemplate, 'r')
importTemplateStr = f.read();
f.close()


def generate(year):
	sum = ""
	days = []
	day = ''
	month = ''
	note = ''
	weekday = ''
	for m in range(1, 13):
		tub = calendar.monthrange(year, m)
		month = '0' + str(m) if m < 10 else str(m) 
		for d in range(1, tub[1] + 1):
			day = '0' + str(d) if d < 10 else str(d) 
			
			dayStr = (str(year) + month + day)
			weekday = calendar.weekday(year, m, d)
			if weekday == 5 or weekday == 6:
				note = weekendTemplateStr.format(dayStr)
			else:
				note = scheduleTemplateStr.format(dayStr)
			sum += note
	sum = importTemplateStr.format(sum)
	return sum

def generateImportedNotes(notes):
	f = open('import.Enex', 'w+')
	f.write(notes)
	f.flush
	
importedNotes = generate(2014)
generateImportedNotes(importedNotes)

