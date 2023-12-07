maps = {
    "seed-to-soil map:": {},
    "soil-to-fertilizer map:": {},
    "fertilizer-to-water map:": {},
    "water-to-light map:": {},
    "light-to-temperature map:": {},
    "temperature-to-humidity map:": {},
    "humidity-to-location map:": {},
}


def create_lookup_map(map_name: str, mappings: list) -> None:
    # store valid ranges, rather than all the mappings
    destination_start = mappings[0]
    source_start = mappings[1]
    range_length = mappings[2]
    destination_end = destination_start + (range_length - 1)
    source_end = source_start + (range_length - 1)
    source = (source_start, source_end)
    destination = (destination_start, destination_end)
    if maps[map_name].get("ranges"):
        maps[map_name]["ranges"].append((source, destination))
    else:
        maps[map_name]["ranges"] = [(source, destination)]


def lookup_destination(data: int, map_name: str) -> int:
    mappings = maps[map_name]["mappings"]
    ranges = maps[map_name]["ranges"]
    # find destination by comparing sources and destinations
    for _ in mappings:
        for r in ranges:
            source_tuple = r[0]
            destination_tuple = r[1]
            destination = data - source_tuple[0] + destination_tuple[0]
            if destination_tuple[0] < destination <= destination_tuple[1]:
                return destination

    return data


def day5() -> None:
    print("###########")
    print("# Day  5  #")
    print("###########")

    map_name = None
    is_seeds_line = True
    with open("day5/input5-sample", "rb") as data:
        for line in data:
            line = line.strip().decode("utf8")
            if is_seeds_line:
                seeds = [int(single.strip()) for single in line[line.find(":")+1:].strip().split(" ")]
                is_seeds_line = False
            elif len(line) > 0:
                # parse the maps
                if line in maps.keys():
                    map_name = line
                    maps[map_name]["mappings"] = []
                else:
                    mappings = [int(single) for single in line.split(" ")]
                    maps[map_name]["mappings"].append(mappings)
                    create_lookup_map(map_name, mappings)

    # process seeds
    is_first = True
    for seed in seeds:
        soil = lookup_destination(seed, "seed-to-soil map:")
        fertilizer = lookup_destination(soil, "soil-to-fertilizer map:")
        water = lookup_destination(fertilizer, "fertilizer-to-water map:")
        light = lookup_destination(water, "water-to-light map:")
        temperature = lookup_destination(light, "light-to-temperature map:")
        humidity = lookup_destination(temperature, "temperature-to-humidity map:")
        location = lookup_destination(humidity, "humidity-to-location map:")
        if is_first:
            min_location = location
            is_first = False
        if location < min_location:
            min_location = location
    print(f"Part 1: minimum location is {min_location}")
