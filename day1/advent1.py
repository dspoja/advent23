from typing import List


number_dict = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def part1(data: List[str]) -> int:
    total = 0
    first = None
    last = None
    for line in data:
        for s in line:
            if 48 <= ord(s) <= 57:
                first = s
                break
        for s in reversed(line):
            if 48 <= ord(s) <= 57:
                last = s
                break
        total += int(first+last)
    return total


def part2(data: List[str]) -> int:
    total = 0
    for line in data:
        first = None
        last = None
        first_name_pos = len(line)
        last_name_pos = -1
        first_num_pos = len(line)
        last_num_pos = -1
        # search for number
        is_first = True
        for i, s in enumerate(line):
            if 48 <= ord(s) <= 57:
                if is_first:
                    first = s
                    first_num_pos = i
                    is_first = False
                else:
                    last = s
                    last_num_pos = i

        if not last:
            last = first
            last_num_pos = first_num_pos

        # search for number by name
        for name in number_dict.keys():
            idx = 0
            while idx > -1 or idx == len(line):
                pos = line.find(name, idx)
                if pos > -1:
                    if pos < first_name_pos:
                        first_name_pos = pos
                        first_name = name

                    if pos > last_name_pos:
                        last_name_pos = pos
                        last_name = name
                    idx = pos + len(name)
                else:
                    idx = -1
        number = ""
        if first_num_pos < first_name_pos:
            number = first
        else:
            number = str(number_dict[first_name])

        if last_num_pos > last_name_pos:
            number += last
        else:
            number += str(number_dict[last_name])
        total += int(number)

    return total


def day1() -> None:
    print("###########")
    print("# Day  1  #")
    print("###########")
    data_list = list()
    with open("day1/input1", "rb") as data:
        for line in data:
            line = line.strip().decode("utf8")
            data_list.append(line)

    part1_result = part1(data_list)
    print(f"Part 1: sum={part1_result}")
    part2_result = part2(data_list)
    print(f"Part 2: sum={part2_result}")
