import re

def parse_num(input):
    try:
        return ooga.index(input)
    except ValueError:
        return int(input)

def run(lines):
    part1 = 0
    for line in lines:
        nums = re.findall('\d', line)
        part1 += int(nums[0] + nums[-1])

    print(f"Part one solution: {part1}")

    ooga = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    part2 = 0
    for line in lines:
        nums = re.findall(f'(?=({"|".join(ooga)}|\d))', line)
        add = (parse_num(nums[0]) * 10 + parse_num(nums[-1]))
        part2 += add

    print(f"Part two solution: {part2}")


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
