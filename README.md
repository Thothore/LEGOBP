# LEGOBP
This repository contains a python script to help with packing your lego boxes by automatically retrieving their dimensions based on the set number and then solving a 3D bin packing. The bin packing problem is solved thanks to the library [py3dbp](https://github.com/enzoruiz/3dbinpacking). The set dimensions are retrieved from [brickset](https://brickset.com/).
## Setup
Follow the instructions in the code:
1. You need to adapt `txt_path` to point to your own txt file containing the set numbers (one per line).

1. Adapt the size of the bins according to your own storage.
## Run
Simply type in a command window the following line to run the script and have the results directly printed on the standard output.
```
python LEGOBP.py
```