# -*- coding: utf-8 -*-
import csv
from google.cloud import translate

# reading csv of inputs
inputs = []

with open('inputs.csv', 'rb') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	for row in csvreader:
		inputs.append(row)
csvfile.close()

print 'data loading completed'

# translate inputs
translated = {}

translate_client = translate.Client()
target = 'en'
count = 1
for item in inputs[1:]:
	if int(item[1]) > 1:
		text = item[0]
		translation = translate_client.translate(text, target_language=target)
		translation = translation['translatedText'].lower().encode('utf-8')
		if translation in translated:
			translated[translation] += int(item[1])
		else:
			translated[translation] = int(item[1])
	print str(count) + '/' + str(len(positions) - 1) + ' completed'
	count += 1

# translation completed

with open('outputs.csv', 'wb') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    for item in sorted(translated.keys(), key=lambda x: translated[x], reverse=True):
    	csvwriter.writerow([item, str(translated[item])])
csvfile.close()