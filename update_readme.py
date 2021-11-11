import os
import glob

notebook_list = sorted(glob.glob('*/*.ipynb'))

file_category = {}
for inb in notebook_list:
    file_category[inb] = inb.split('/')[0]


pre_category = 'init'
with open("README.md.t", 'w') as indexf:
    indexf.write("# Jupyter Notebook Index")
for ifile in file_category:
    category = file_category[ifile]

    if category != pre_category:
        with open("README.md.t", 'a') as indexf:
            indexf.write("\n\n## " + category + "\n- [" + ifile.split('/')[1] + "](https://junxnone.github.io/nbvt/nbv.html?notebook_name=" + ifile + ")")
    else:
        with open("README.md.t", 'a') as indexf:
            indexf.write("\n- [" + ifile.split('/')[1] + "](https://junxnone.github.io/nbvt/nbv.html?notebook_name=" + ifile + ")")

    pre_category = file_category[ifile]