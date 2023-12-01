def run (lines):
    part1 = 0
    for line in lines:
        game = line.split(': ')[1]
        win, have = game.split('|')
        win = win.lstrip().rstrip().split(" ")
        have = have.lstrip().rstrip().replace("  ", " ").split(" ")
        card = 0
        for num in have:
            if num in win:
                if card == 0:
                    card = 1
                else:
                    card = card * 2
        part1 += card
    print(f"Part one solution: {part1}")

    cards = {}
    for line in lines:
        card_num = int(line.split(":")[0].split(" ")[-1])
        cards[str(card_num)] = 1

    for line in lines:
        card_num = int(line.split(":")[0].split(" ")[-1])
        # print(f"Processing {cards[str(card_num)]} cards for {card_num}")
        game = line.split(': ')[1]
        win, have = game.split('|')
        win = win.lstrip().rstrip().split(" ")
        have = have.lstrip().rstrip().replace("  ", " ").split(" ")
        wins = 0
        for num in have:
            if num in win:
                wins += 1
        for win in range(0, wins):
            if card_num+win < len(lines):
                cards[str(card_num+1+win)] += cards[str(card_num)]
    print(f"Part two solution: {sum(cards.values())}")

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
