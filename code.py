import json

# opening json file
fileSample = open('sample.json')
# converting json file into datastructure
dataSample = json.load(fileSample)
dictCtg = dict()
# getting each item to it's respective category
for ele in dataSample:
    if ele['category'] not in dictCtg:
        dictCtg[ele['category']] = []
    dictCtg[ele['category']].append(ele['productName'])
# printing each category items
idx = 1
for key, val in dictCtg.items():
    print('Category-{}'.format(idx))
    for ele in val:
        print(ele)
    idx += 1
