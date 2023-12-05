

def run(lines):
    seeds = [eval(i) for i in lines[0].split(": ")[1].split(" ")]
    seeds.sort()
    seeds_to_soil_map = []
    soil_to_fertilizer_map = []
    fertilizer_to_water_map = []
    water_to_light_map = []
    light_to_temp_map = []
    temp_to_humidity_map = []
    humidity_to_location_map = []

    seeds_to_soil = {}
    soil_to_fertilizer = {}
    fertilizer_to_water = {}
    water_to_light = {}
    light_to_temp = {}
    temp_to_humidity = {}
    humidity_to_location = {}

    # load the data, i hate this
    line_index = 2
    while len(lines[line_index]) > 2:
        if "map" in lines[line_index]:
            line_index+=1
            continue
        seeds_to_soil_map.append([eval(i) for i in lines[line_index].split(" ")])
        line_index+=1
    seeds_to_soil_map = sorted(seeds_to_soil_map, key=lambda x: x[1])
    line_index +=1
    while len(lines[line_index]) > 2:
        if "map" in lines[line_index]:
            line_index+=1
            continue
        soil_to_fertilizer_map.append([eval(i) for i in lines[line_index].split(" ")])
        line_index+=1
    soil_to_fertilizer_map = sorted(soil_to_fertilizer_map, key=lambda x: x[1])
    line_index +=1
    while len(lines[line_index]) > 2:
        if "map" in lines[line_index]:
            line_index+=1
            continue
        fertilizer_to_water_map.append([eval(i) for i in lines[line_index].split(" ")])
        line_index+=1
    fertilizer_to_water_map = sorted(fertilizer_to_water_map, key=lambda x: x[1])
    line_index +=1
    while len(lines[line_index]) > 2:
        if "map" in lines[line_index]:
            line_index+=1
            continue
        water_to_light_map.append([eval(i) for i in lines[line_index].split(" ")])
        line_index+=1
    water_to_light_map = sorted(water_to_light_map, key=lambda x: x[1])
    line_index +=1
    while len(lines[line_index]) > 2:
        if "map" in lines[line_index]:
            line_index+=1
            continue
        light_to_temp_map.append([eval(i) for i in lines[line_index].split(" ")])
        line_index+=1
    light_to_temp_map = sorted(light_to_temp_map, key=lambda x: x[1])
    line_index +=1
    while len(lines[line_index]) > 2:
        if "map" in lines[line_index]:
            line_index+=1
            continue
        temp_to_humidity_map.append([eval(i) for i in lines[line_index].split(" ")])
        line_index+=1
    temp_to_humidity_map = sorted(temp_to_humidity_map, key=lambda x: x[1])
    line_index +=1
    while line_index < len(lines) and len(lines[line_index]) > 2:
        if "map" in lines[line_index]:
            line_index+=1
            continue
        humidity_to_location_map.append([eval(i) for i in lines[line_index].split(" ")])
        line_index+=1
    humidity_to_location_map = sorted(humidity_to_location_map, key=lambda x: x[1])

    # actually processing now
    print(f"now to process {len(seeds)} cries")
    for seed_mapping in seeds_to_soil_map:
        for seed in seeds:
            if seed in range(seed_mapping[1], seed_mapping[1]+seed_mapping[2]):
                seeds_to_soil[seed] = (seed_mapping[0] + (seed - seed_mapping[1]))
            if seed not in seeds_to_soil:
                seeds_to_soil[seed] = seed

    for soil_mapping in soil_to_fertilizer_map:
        for soil in seeds_to_soil.values():
            if soil in range(soil_mapping[1], soil_mapping[1]+soil_mapping[2]):
                soil_to_fertilizer[soil] = (soil_mapping[0] + (soil - soil_mapping[1]))
            if soil not in soil_to_fertilizer:
                soil_to_fertilizer[soil] = soil

    for fertilizer_mapping in fertilizer_to_water_map:
        for fertilizer in soil_to_fertilizer.values():
            if fertilizer in range(fertilizer_mapping[1], fertilizer_mapping[1]+fertilizer_mapping[2]):
                fertilizer_to_water[fertilizer] = (fertilizer_mapping[0] + (fertilizer - fertilizer_mapping[1]))
            if fertilizer not in fertilizer_to_water:
                fertilizer_to_water[fertilizer] = fertilizer
    
    for water_mapping in water_to_light_map:
        for water in fertilizer_to_water.values():
            if water in range(water_mapping[1], water_mapping[1]+water_mapping[2]):
                water_to_light[water] = (water_mapping[0] + (water - water_mapping[1]))
            if water not in water_to_light:
                water_to_light[water] = water
    
    for temp_mapping in light_to_temp_map:
        for light in water_to_light.values():
            if light in range(temp_mapping[1], temp_mapping[1]+temp_mapping[2]):
                light_to_temp[light] = (temp_mapping[0] + (light - temp_mapping[1]))
            if light not in light_to_temp:
                light_to_temp[light] = light
    
    for humidity_mapping in temp_to_humidity_map:
        for temp in light_to_temp.values():
            if temp in range(humidity_mapping[1], humidity_mapping[1]+humidity_mapping[2]):
                temp_to_humidity[temp] = (humidity_mapping[0] + (temp - humidity_mapping[1]))
            if temp not in temp_to_humidity:
                temp_to_humidity[temp] = temp

    for location_mapping in humidity_to_location_map:
        for humidity in temp_to_humidity.values():
            if humidity in range(location_mapping[1], location_mapping[1]+location_mapping[2]):
                humidity_to_location[humidity] = (location_mapping[0] + (humidity - location_mapping[1]))
            if humidity not in humidity_to_location:
                humidity_to_location[humidity] = humidity

    print(f"Solution for part one: {min(humidity_to_location.values())}")

    # PART 2 ELECTRIC BOOGALOOOOOOOO
    seeds = [eval(i) for i in lines[0].split(": ")[1].split(" ")]

    # process the seed input
    seed_indexs = []
    for i in range(0, len(seeds), 2): 
        x = i 
        seed_indexs.append(seeds[x:x+2])
    print(f"indexes to run {len(seed_indexs)}")
    # have to process it one seed at a time, otherwise the dataset is too large
    seeds = []
    seed_to_location = {}
    count = 0
    for index in seed_indexs:
        count +=index[1]
    print(f"There are now {count} seeds to process")
    for index in seed_indexs:
        print(f"processing {index[0]+index[1] - index[0]} in group")
        for seed in range(index[0], index[0]+index[1]):

            # actually processing now
            # reset stuff cause the processing is the same
            # print(f"now to process seed {seed}")
            seeds_to_soil = {}
            soil_to_fertilizer = {}
            fertilizer_to_water = {}
            water_to_light = {}
            light_to_temp = {}
            temp_to_humidity = {}
            humidity_to_location = {}
            for seed_mapping in seeds_to_soil_map:
                if seed in range(seed_mapping[1], seed_mapping[1]+seed_mapping[2]):
                    seeds_to_soil[seed] = (seed_mapping[0] + (seed - seed_mapping[1]))
                if seed not in seeds_to_soil:
                    seeds_to_soil[seed] = seed
            for soil_mapping in soil_to_fertilizer_map:
                for soil in seeds_to_soil.values():
                    if soil in range(soil_mapping[1], soil_mapping[1]+soil_mapping[2]):
                        soil_to_fertilizer[soil] = (soil_mapping[0] + (soil - soil_mapping[1]))
                    if soil not in soil_to_fertilizer:
                        soil_to_fertilizer[soil] = soil
                        
            for fertilizer_mapping in fertilizer_to_water_map:
                for fertilizer in soil_to_fertilizer.values():
                    if fertilizer in range(fertilizer_mapping[1], fertilizer_mapping[1]+fertilizer_mapping[2]):
                        fertilizer_to_water[fertilizer] = (fertilizer_mapping[0] + (fertilizer - fertilizer_mapping[1]))
                    if fertilizer not in fertilizer_to_water:
                        fertilizer_to_water[fertilizer] = fertilizer
            for water_mapping in water_to_light_map:
                for water in fertilizer_to_water.values():
                    if water in range(water_mapping[1], water_mapping[1]+water_mapping[2]):
                        water_to_light[water] = (water_mapping[0] + (water - water_mapping[1]))
                    if water not in water_to_light:
                        water_to_light[water] = water
            for temp_mapping in light_to_temp_map:
                for light in water_to_light.values():
                    if light in range(temp_mapping[1], temp_mapping[1]+temp_mapping[2]):
                        light_to_temp[light] = (temp_mapping[0] + (light - temp_mapping[1]))
                    if light not in light_to_temp:
                        light_to_temp[light] = light
            for humidity_mapping in temp_to_humidity_map:
                for temp in light_to_temp.values():
                    if temp in range(humidity_mapping[1], humidity_mapping[1]+humidity_mapping[2]):
                        temp_to_humidity[temp] = (humidity_mapping[0] + (temp - humidity_mapping[1]))
                    if temp not in temp_to_humidity:
                        temp_to_humidity[temp] = temp
            for location_mapping in humidity_to_location_map:
                for humidity in temp_to_humidity.values():
                    if humidity in range(location_mapping[1], location_mapping[1]+location_mapping[2]):
                        humidity_to_location[humidity] = (location_mapping[0] + (humidity - location_mapping[1]))
                    if humidity not in humidity_to_location:
                        humidity_to_location[humidity] = humidity
                    seed_to_location[seed] = humidity_to_location[humidity]
        print("processed group")
    print("Processed humidity_to_location for part 2")
    print(f"Solution for part two: {min(seed_to_location.values())}")


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

