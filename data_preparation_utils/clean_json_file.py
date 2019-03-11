import json
import sys
import os

file_path = sys.argv[1]
filename = os.path.basename(file_path)
new_filename = '[Clean] {}'.format(filename)
with open(file_path, 'r') as original_file:
    with open(new_filename, 'w+') as new_file:
        for line in original_file.readlines():
            obj = json.loads(line)
            if obj['content'] and obj['annotation']:
                new_file.write(line)
