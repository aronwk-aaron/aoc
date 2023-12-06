

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

