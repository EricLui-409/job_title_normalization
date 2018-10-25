import csv
from google.cloud import translate
import enchant

# reading csv of position names
positions = []

with open('test_output.csv', 'rb') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	for row in csvreader:
		positions.append(row)
csvfile.close()

print 'data loading completed'

# correcting typo
d = enchant.Dict("en_US")
corrected = {}

count = 1
for item in positions:
	text = item[0]
	if not text == '' and not d.check(text):
		suggestion = d.suggest(text)
		if len(suggestion) == 0:
			text = ''
		else:
			text = suggestion[0]
	if text in corrected:
		corrected[text] += int(item[1])
	else:
		corrected[text] = int(item[1])
	print str(count) + '/' + str(len(positions) - 1) + ' completed'
	count += 1

# correction completed
with open('typos_corrected.csv', 'wb') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    for item in sorted(corrected.keys(), key=lambda x: corrected[x], reverse=True):
    	csvwriter.writerow([item, str(corrected[item])])
csvfile.close()
