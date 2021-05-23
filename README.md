# End of Support

I have stopped supporting this repo as of 23rd May 2021. There are better tools out there, such as [GoWitness](https://github.com/sensepost/gowitness) if you're looking for an alternative.

# rduserenum
Script to enumerate usernames through RDP screenshots.
## Requirements ##
* EyeWitness - https://github.com/ChrisTruncer/EyeWitness
* Tesseract - https://github.com/tesseract-ocr/tesseract
* Nmap

## Usage ##
```
usage: rduserenum.py [-h] -o OUTPUT subnet [subnet ...]

Grab usernames from RDP screenshots.

positional arguments:
  subnet                The subnet to scan in CIDR notation.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        file to output results to

```
