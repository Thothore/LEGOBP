import os
try:
    from py3dbp import Packer, Bin, Item
except:
    os.system("pip install py3dbp --quiet")
    from py3dbp import Packer, Bin, Item

import urllib.request
import re

'''
1. Change the path to point to your txt with all the set numbers (one per line).
'''
txt_path = "path/file.txt"
base_url = "https://brickset.com/sets/"

packer = Packer()

'''
2. Adapt the number and the dimensions of your own bins. Dimensions should be x, y, z.
'''
packer.add_bin(Bin("First bin", 10, 20, 40, 0))

with open(txt_path, 'r') as file:
    sets = file.readlines()

print("Retrieving sets dimensions...")
for set in sets:
    set = set.replace('\n', '')
    response = urllib.request.urlopen(base_url + set)
    html = response.read().decode('UTF-8')

    try:
        dimensions = re.search("<dt>Dimensions<\/dt>\\n<dd>([0-9]*\.?[0-9]+ x [0-9]*\.?[0-9]+ x [0-9]*\.?[0-9]+) cm <br \/>", html).group(1)
        #print(dimensions)
        [x, y, z] = dimensions.split(' x ')
        [x, y, z] = [float(x), float(y), float(z)]
        #print(type(x))
        print(f"Dimensions of box {set} :: {x}, {y}, {z}")
        packer.add_item(Item(set, x, y, z, 0))
    except AttributeError:
        print(f"Could not find dimensons for box {set}")

print("-------------------------------")

print("Starting the bin packing problem...")
packer.pack()

for b in packer.bins:
    print(f"To put in bin \n{b.string()}:")
    for item in b.items:
        print(f"\tset number {item.string()}")
    print(f"/!\ BEWARE: UNFITTED ITEMS /!\:")
    for item in b.unfitted_items:
        print(f"\tCould not fit set number {item.string()}")

print("*********************************************************")