import shutil

foods = ['spam', 'ham', 'toast', 'jam', 'bacon', 'tofu', 'jackfruit']

with open('junk.txt', "w") as junk_out:
    for food in foods:
        junk_out.write(food + '\n')

with open('junk.txt') as junk_in:
    with open('ujunk.txt', 'w') as ujunk_out:
        for line in junk_in:
            ujunk_out.write(line.upper())

shutil.move('junk.txt', 'junk.txt.orig')
shutil.move('ujunk.txt', 'junk.txt')

# .move .copy .rmtree
# .make_archive("mydata", "zip", "dirname")

import os
# os.system("dir")
# print("*" * 60)
from subprocess import run, PIPE
proc = run("cmd /c dir", stdout=PIPE)
output = proc.stdout
print(output[:100].decode())