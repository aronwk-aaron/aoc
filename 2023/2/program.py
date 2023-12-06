def run(lines):
    part1 = 0
    for line in lines:
        game = line.split(': ')[1]
        subgames = game.split(';')
        broken = False
        for subgame in subgames:
            subgame = subgame.lstrip()
            green = [green for green in subgame.split(", ") if "green" in green]
            red = [red for red in subgame.split(", ") if "red" in red]
            blue = [blue for blue in subgame.split(", ") if "blue" in blue]
            if (len(green) > 0 and int(green[0].split(" ")[0]) > 13): broken = True
            if (len(red) > 0 and int(red[0].split(" ")[0]) > 12): broken = True
            if (len(blue) > 0 and int(blue[0].split(" ")[0]) > 14): broken = True
        if (not broken): part1 += int(line.split(": ")[0].split(" ")[1])
    print(f"Solution for part one: {part1}")

    part2 = 0
    for line in lines:
        game = line.split(': ')[1]
        subgames = game.split(';')
        broken = False
        r = []
        g = []
        b = []
        for subgame in subgames:
            subgame = subgame.lstrip()
            green = [green for green in subgame.split(", ") if "green" in green]
            red = [red for red in subgame.split(", ") if "red" in red]
            blue = [blue for blue in subgame.split(", ") if "blue" in blue]
            if (len(green) > 0): g.append(int(green[0].split(" ")[0]))
            if (len(red) > 0): r.append(int(red[0].split(" ")[0]))
            if (len(blue) > 0): b.append(int(blue[0].split(" ")[0]))
        part2 += max(r) * max(g) * max(b)
    print(f"Solution for part two: {part2}")

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
