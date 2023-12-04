MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def day2() -> None:
    print("###########")
    print("# Day  2  #")
    print("###########")
    with open("day2/input2", "rb") as data:
        possible_game_total = 0
        power_sum = 0
        for line in data:
            line = line.strip().decode("utf8")
            # get game number
            game_num = int(line[0: line.find(":")].replace("Game ", ""))
            # split the rest of the string by ; and then ,
            draws = [single.split(",") for single in line[line.find(":")+1:].split(";")]
            max_blue = 0
            max_green = 0
            max_red = 0
            for draw in draws:
                for single in draw:
                    single = single.strip()
                    if "blue" in single:
                        blue = int(single[0:single.find(" ")])
                        max_blue = blue if blue > max_blue else max_blue
                    elif "red" in single:
                        red = int(single[0:single.find(" ")])
                        max_red = red if red > max_red else max_red
                    elif "green" in single:
                        green = int(single[0:single.find(" ")])
                        max_green = green if green > max_green else max_green

            # Part 1
            if max_blue <= MAX_BLUE and max_green <= MAX_GREEN and max_red <= MAX_RED:
                possible_game_total += game_num
            # Part 2
            power_sum += (max_red * max_green * max_blue)

    print(f"Part 1 answer: {possible_game_total}")
    print(f"Part 2 answer: {power_sum}")


