#!/usr/bin/env python

import json
import sys

with open(sys.argv[1], "r") as json_file:
    data = json.load(json_file)

word_count = 0
loc = 0

for cell in data['cells']:
    
    if cell['cell_type'] == "markdown":
        content = cell['source']

        for line in content:
            words = [word for word in line.split() if "#" not in word]
            word_count += len(words)

    elif cell['cell_type'] == "code":
        content = cell['source']

        for line in content:
            if len(line) > 5:
                loc += 1            


print("Word Count:", word_count)
print("Lines of Code:", loc)
