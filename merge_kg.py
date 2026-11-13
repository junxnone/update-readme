import os
import glob
import argparse
import json

ap = argparse.ArgumentParser()
ap.add_argument('--kgf', type=str, nargs='+', default='none', help='python merge_kg.py kg1.json kg2.json kg3.json')
args = ap.parse_args()
print(args.kgf)

# the inputs are merged in the order given on the command line, so the output order
# is fixed as long as the caller keeps that order
skg = {'nodes':[],'links':[]}
for ijsonf in args.kgf:
    with open(ijsonf, 'r', encoding='utf-8') as f:
        a = json.load(f)
        for inode in a['nodes']:
            skg['nodes'].append(inode)
        for ilink in a['links']:
            skg['links'].append(ilink)

print('nodes:', len(skg['nodes']), 'links:', len(skg['links']))

# indent + one value per line (UTF-8, no \u escapes) + trailing newline: a change to one
# doc only touches its own lines in the diff instead of rewriting a single huge line
with open("kg.json", 'w', encoding='utf-8') as f:
    json.dump(skg, f, ensure_ascii=False, indent=2)
    f.write('\n')
