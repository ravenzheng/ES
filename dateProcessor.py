from string import Template
import calendar

def calcuateDate(year, month, date):
	"""0 represents Monday"""
	return calendar.weekday(year, month, date)


def main():
	sum = ''
	for i in range(10, 40):
		sum += str(i * 100) + '.02.28 ' + str(calcuateDate(i * 100, 2, 28)) + '\n'
	
	f = open('1.txt', 'w+')
	f.write(sum)
	f.flush()
	print sum

main()

