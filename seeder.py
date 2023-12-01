import os
import sys

for date in range(5, 26):
    try:
        os.mkdir(str(date))
    except:
        pass
    f = open(str(date) + "/program.py", "w")
    f.write("""\


def run(lines):
    for line in lines:
        print(line)

input = []
with open("input", "r") as file:
    input = file.readlines()
example = []
with open("example", "r") as file:
    example = file.readlines()

print("Processing example")
run(example)
print()
print("Processing input")
run(input)

""")
    open(str(date) + "/input", "w")
    open(str(date) + "/example", "w")