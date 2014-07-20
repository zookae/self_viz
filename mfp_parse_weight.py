from sys import argv
import xml.etree.ElementTree as ET

filename = argv[1]
#filename = './data/mfp_weight.xml'

o_f = open(filename[:-4] + '.csv', 'w')
o_f.write('Date, Weight\n')


tree = ET.parse(filename)
root = tree.getroot()
data = root.find('chart_data')
data = zip(data[0], data[1])

year = 2011
output = []
for v in data[1:]:
    if str(v[1].text) == '0.0':
        continue
    if v[0].text == '1/01':
        year = year+1
    output.append(v[0].text + '/' + str(year) + ', ' + str(v[1].text))
    o_f.write(v[0].text + '/' + str(year) + ', ' + str(v[1].text) + '\n')

o_f.close()
