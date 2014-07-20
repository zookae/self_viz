from sys import argv
import re

filename = argv[1]

f = open(filename, 'rU') # universal line mode for windows data
o_f = open(filename[:-4] + '_clean.csv', 'w')


mdate = re.compile(r"\d+-\w+-\d+")
mtotal = re.compile(r"TOTAL.*")

header = 'Date,Calories,Carbs,Fat,Protein,Cholest,Sodium,Sugars,Fiber\n'
o_f.write(header)

daily_data = []
for l in f:
    if mdate.match(l) != None:
        new_date = mdate.match(l).group()
    if mtotal.match(l) != None:
        new_total = mtotal.match(l).group()
        new_total = re.sub(r'(TOTAL:,|g|m)', '', new_total)
        new_total = re.sub(r'"(\d+),(\d+)"', r'\1\2', new_total)
#        print new_date + ',' + new_total
        daily_data.append(new_date + ',' + new_total)
        o_f.write(new_date + ',' + new_total + '\n')

f.close()
o_f.close()

#input_dates = re.findall(r"\d+-\w+-\d+", lines)

#import csv
#with open('201407.csv', 'rU') as csvf:
#    csvr = csv.reader(csvf, delimiter=',', quotechar='"')
#    for row in csvr:
#        print ', '.join(row)
