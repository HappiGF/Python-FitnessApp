from __future__ import division

def data(csv):
	with open(csv) as f:
		print(f.read())

def complete(csv):
	max_steps = 0
	step_count = []
	date = []
	months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	zero_date = []
	zero_bar = ''

	#create step_count list of all the step values and date list of all the dates
	for line in open(csv):
		n = list(line.split(','))
		step_count.append(n[11])
		date.append(n[0])

	#turn any empty data into 0
	for x in range(len(step_count)):
		if step_count[x] == '':
			step_count[x] = 0

	# remove 'Date' and 'Step count' from each list
	date = [x for x in date if x != 'Date']
	step_count = [x for x in step_count if x != 'Step count']


	#turns date to name of month and day form
	for x in range(len(date)):
		d = list(date[x].split('-'))
		d = list(map(int, d))
		m = d[1]
		month = months[m-1]
		day = d[2]
		date[x] = month, day, d[0]

	#turns all the items in list in to ints
	steps = list(map(int, step_count))
	
	#finds and sets the max amount of steps
	for x in range(len(steps)):
		if steps[x] > max_steps:
			max_steps = steps[x]
	
	#prints
	for x in range(len(steps)):
		print steps[x], 'steps on', date[x][0], str(date[x][1]) + ',',date[x][2]
		print bar(steps[x], max_steps)
		print

def bar(steps, max_steps):
	barL = (steps / max_steps * 100)
	barR = 100 - barL
	
	#prints bar plus some depending on amount
	if barL == 100:
		return '█'*99 + ' 100%,' + ' max amount \(•◡•)/'
	elif barL == 0:
		return '░'*99 + ' 0%,' + ' woah, 0 steps.. you mad man'
	elif barL * 100 < 100:
		return '░'*int(barR) + " " + str("%.2f" % barL) + '%, at least you tried ¯\_(ツ)_/¯'
	else:
		return '█'*int(barL) + '░'*int(barR) + " " + str("%.2f" % barL) + '%'

csv = 'lfit.csv'
data(csv)
complete(csv)
