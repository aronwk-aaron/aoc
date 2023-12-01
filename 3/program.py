import re

def is_num(input):
    try:
        int(input)
        return True
    except:
        return False

def run(lines):
    part1 = 0
    part2 = 0
    for line in lines:
        line_index = lines.index(line)
        line = line.strip("\n")
        symbols =  [l.start() for l in re.finditer(r"[^.0-9]", line)]
        for symbol_index in symbols:
            surrouding_nums = []
            # check on current line
            curr_nums_pos = [l.start() for l in re.finditer(r"\d+", line)]
            curr_nums = re.findall(r"\d+", line)

            if len(curr_nums) > 0:
                max_len_num = len(curr_nums[0])
                if len(curr_nums) > 1:
                    max_len_num = len(max(curr_nums, key=len))
                for num_pos in curr_nums_pos:
                    if abs(num_pos-symbol_index) <= max_len_num:
                        if (symbol_index > 0 and line[symbol_index-1] == curr_nums[curr_nums_pos.index(num_pos)][-1]):
                            surrouding_nums.append(int(curr_nums[curr_nums_pos.index(num_pos)]))
                        if (symbol_index+1 == num_pos):
                            surrouding_nums.append(int(curr_nums[curr_nums_pos.index(num_pos)]))

            # if we aren't the first line
            if(line_index != 0):
                # check on previous line
                prev_nums_pos = [l.start() for l in re.finditer(r"\d+", lines[line_index-1].strip("\n"))]
                prev_nums = re.findall(r"\d+", lines[line_index-1].strip("\n"))
                if len(prev_nums) > 0:
                    max_len_num = len(prev_nums[0])
                    if len(prev_nums) > 1:
                        max_len_num = len(max(prev_nums, key=len))
                    for num_pos in prev_nums_pos:
                        if abs(num_pos-symbol_index) <= max_len_num:
                            if (symbol_index > 0 and lines[line_index-1][symbol_index-1] == prev_nums[prev_nums_pos.index(num_pos)][-1] and lines[line_index-1][symbol_index] == "."):
                                surrouding_nums.append(int(prev_nums[prev_nums_pos.index(num_pos)]))
                            elif (lines[line_index-1][symbol_index] == prev_nums[prev_nums_pos.index(num_pos)][-1]and lines[line_index-1][symbol_index+1] == "."):
                                surrouding_nums.append(int(prev_nums[prev_nums_pos.index(num_pos)]))
                            elif (symbol_index+1 == num_pos or symbol_index-1 == num_pos or symbol_index == num_pos):
                                surrouding_nums.append(int(prev_nums[prev_nums_pos.index(num_pos)]))


            # if we aren't the last line
            if(line_index != len(lines)-1):
                # check on next line
                next_nums_pos = [l.start() for l in re.finditer(r"\d+", lines[line_index+1].strip("\n"))]
                next_nums = re.findall(r"\d+", lines[line_index+1].strip("\n"))
                if len(next_nums) > 0:
                    max_len_num = len(next_nums[0])
                    if len(next_nums) > 1:
                        max_len_num = len(max(next_nums, key=len))
                    for num_pos in next_nums_pos:
                        if abs(num_pos-symbol_index) <= max_len_num:
                            if (symbol_index > 0 and lines[line_index+1][symbol_index-1] == next_nums[next_nums_pos.index(num_pos)][-1]and lines[line_index+1][symbol_index] == "."):
                                surrouding_nums.append(int(next_nums[next_nums_pos.index(num_pos)]))
                            elif (lines[line_index+1][symbol_index] == next_nums[next_nums_pos.index(num_pos)][-1]and lines[line_index+1][symbol_index+1] == "."):
                                surrouding_nums.append(int(next_nums[next_nums_pos.index(num_pos)]))
                            elif (symbol_index+1 == num_pos or symbol_index-1 == num_pos or symbol_index == num_pos):
                                surrouding_nums.append(int(next_nums[next_nums_pos.index(num_pos)]))


            part1 += sum(surrouding_nums)
            if line[symbol_index] == '*' and len(surrouding_nums) == 2:
                part2 += surrouding_nums[0] * surrouding_nums[1]


    print(f"Solution for part one: {part1}")
    print(f"Solution for part two: {part2}")



data = []
with open("input", "r") as file:
    data = file.readlines()
example = []
with open("example", "r") as file:
    example = file.readlines()

print("Processing example")
run(example)
print()
print("Processing input")
run(data)

