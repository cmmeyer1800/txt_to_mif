# txt_to_mif
### Author: Collin Meyer

This script was developed to help students in ECE385 turn their .txt memory initialization file into
a .mif memory initialization file for use with the quartus IP megawizard for on chip memory.

This script is especially useful for large .txt memory initialization files, as it can make the quartus compile time nearly quadruple. As such this is its greatest application.

### Installation

To Install simply clone the repo in either bash on unix or powershell/cmd on windows
```
git clone https://github.com/cmmeyer1800/txt_to_mif.git
```

### Usage

To use this tool follow the preceding steps:
First copy the .txt file into the same directory using whichever tool you prefer.
Then from either bash or powershell/cmd run the following command:
```
python txt_to_mif.py
```
or
```
python3 txt_to_mif.py
```
depending on what your python executable is aliased to.

Then simply follow the command line instructions and your .mif file will be placed in the same directory.
