#! /usr/bin/env python

import re
from os import path

file1 = path.abspath('./brltty.conf')
pattern = r'(version)\s+([0-9]+)'
regex = re.compile(pattern, re.IGNORECASE)
with open (file1,'r') as file:
    f = file.read()

    matches = regex.findall(f)
    print(matches)
    
    matches = regex.finditer(f)
    for match in matches:
            print ( match.group(2) )

