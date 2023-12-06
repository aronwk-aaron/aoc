import re
import numpy

def run(lines):
    times = re.findall(r"\d+", lines[0])
    distances = re.findall(r"\d+", lines[1])
    times_won = []
    for i in range(0, len(times)):
        print(f"{times[i]}ms and {distances[i]}mm")
        # find possible x's
        # where time spent holding the trigger, which increases the boats speed by 1mm/ms
        wins = 0
        for x in range(1,int(times[i])-1):
            if ((x*(int(times[i])-x))>int(distances[i])): wins+=1
        times_won.append(wins)
    print(f"Solution for part one: {numpy.prod(times_won)}")

    # why tf is it "hurr durr, i'm dumb, tne inputs dum you gotta do this instead"
    stupid_time = int(lines[0].split(":")[1].replace(" ",""))
    stupid_distance = int(lines[1].split(":")[1].replace(" ",""))
    print(f"stupid race is {stupid_time} ms with a distance of {stupid_distance}mm")
    stupid_wins = 0
    for x in range(1,stupid_time-1):
        if ((x*(stupid_time-x))>int(stupid_distance)): stupid_wins+=1
    print(f"Solution for part one: {stupid_wins}")

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

