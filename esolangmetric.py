import argparse
from difflib import SequenceMatcher
from os import walk

import sys
def progress(count, total, status=''): # https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
    bar_len = 20
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(50.0 * count / float(total), 1)
    bar = '■' * filled_len + ' ' * (bar_len - filled_len)
    return '[%s] %s%s %s' % (bar, percents, '%', status)

parser = argparse.ArgumentParser()
parser.add_argument('-s','--sample', help="Sample file to find it's metric with all eso languages", required=True, type=argparse.FileType('rb'))
args = parser.parse_args()
sample = args.sample.read()

filenames = next(walk('./EsoLangsSamples'), (None, None, []))[2]

results = {}
for i in filenames:
	with open(f'EsoLangsSamples/{i}','rb') as f:
		results[i[:-4]] = SequenceMatcher(None, f.read(), sample).ratio()
results = dict(sorted(results.items(), key=lambda x:x[1]))

for x,y in enumerate(results):
	print(f'{progress(results[y],1)} | {y} : {results[y]}')
