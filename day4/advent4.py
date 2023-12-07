def part1(cards: dict) -> int:
    total_points = 0
    for card_num, card in cards.items():
        first = True
        points = 0
        for number in card[1]:
            # check for existence
            if number in card[0]:
                if first:
                    # add single point
                    points = 1
                    first = False
                else:
                    # double the points
                    points *= 2
        total_points += points

    return total_points


def part2(cards: dict) -> int:
    total_points = 0
    cards_totals = {}
    for card_num, card in cards.items():
        count = 0
        # count the matches
        for number in card[1]:
            if number in card[0]:
                count += 1

        # make sure we count at least one card
        if not cards_totals.get(card_num):
            cards_totals[card_num] = 1
        else:
            cards_totals[card_num] += 1

        # since we have matches, add additional cards
        if count > 0:
            # update card counts
            for num in range(card_num+1, card_num+1+count):
                repeat = cards_totals.get(card_num) - 1
                while repeat > -1:
                    if cards_totals.get(num):
                        cards_totals[num] = cards_totals[num] + 1
                    else:
                        cards_totals[num] = 1
                    repeat -= 1
    # count the points
    for card_num, count in cards_totals.items():
        total_points += count

    return total_points


def day4() -> None:
    print("###########")
    print("# Day  4  #")
    print("###########")

    card_dict = {}
    with open("day4/input4", "rb") as data:
        for line in data:
            line = line.strip().decode("utf8")
            card_num = int(line[0: line.find(":")].replace("Card ", ""))
            # split the rest of the string by | and then ,
            cards = [" ".join(single.split()).split(" ") for single in line[line.find(":") + 1:].split("|")]
            card_dict[card_num] = cards

    total_points = part1(card_dict)
    print(f"Part 1: total points={total_points}")

    total_points = part2(card_dict)
    print(f"Part 2: total points={total_points}")
