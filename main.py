#Luca Kenman and Victor Carreno
#CSC 101 - Final Coding Project
#The work and code was done equally between the two of us
#The purpose of our code is to determine if a city is water efficient based on
#It's population, size, and daily water usage


from class_city import City

def benchmarks(filename):
    benchmarks = {}
    try:
        with open(filename, 'r') as file:
            next(file)
            for line in file:
                data = line.strip().split(',')
                if len(data) == 5:
                    category = data[0]
                    benchmarks[category] = {
                        "Efficient": float(data[3]),
                        "Moderately Efficient": float(data[4]),
                    }
    except FileNotFoundError:
        print(f"File not found {filename} ")
    return benchmarks

def user_input():
    city_list = []

    print("\n" + "="*50)
    print("Water Usage Data Entry")
    print("="*50)
    print("Input Cities to Compare")
    print("Format exactly as shown: CityName, Population, DailyUsageInGallons")
    print("Ex: San Luis Obispo, 47000, 5640000")
    print("\n type 'done' when finished")

    while True:
        user_input = input("Enter city Data > ")

        if user_input.lower() == 'done':
            break

        parts = user_input.split(',')

        if len(parts) == 3:
            try:
                new_city = City(parts[0], parts[1], parts[2])
                city_list.append(new_city)
                print(f" {new_city.name} added to city_list")
            except ValueError:
                print ("Error")

    return city_list

def sorted_results(city_list, benchmarks):
    if not city_list:
        print("Data entered incorrectly")
        return

    sorted_cities_list = sorted(city_list, key=lambda city: city.average_gpcd())

    print("\n\n" + "="*60)
    print("Efficiency in order from most efficient to least efficient")
    print("="*60)

    for rank, city in enumerate(sorted_cities_list, start=1):
        gpcd = city.average_gpcd()
        status, is_high_risk = city.efficiency(benchmarks)

        output = f"{rank}. {city.name.upper()} ({city.size_city()} City) - {gpcd:.1f} GPCD, Rating: {status}"

        if is_high_risk:
            output += ": This city is at high risk due to water waste"
        print (output)
    print("="*60)

def load_previous_cities(filename="previous_cities.txt"):
    loaded_cities = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    past_city = City(parts[0], parts[1], parts[2])
                    loaded_cities[past_city.name.upper()] = past_city
    except FileNotFoundError:
        pass
    return loaded_cities

def save_city(previous_dict, filename="previous_cities.txt"):
    with open (filename, 'w') as file:
        for city in previous_dict.values():
            file.write(f"{city.name},{city.population},{city.daily_usage_gallons}\n")
    print(f"\n City Saved to {filename}")


def main():
    benchmarks_run = benchmarks("benchmarks.txt")
    previous_cities_dict = load_previous_cities()

    while True:
        new_city_list = user_input()
        for new_city in new_city_list:
            previous_cities_dict[new_city.name.upper()] = new_city
        combined_cities = list(previous_cities_dict.values())
        if combined_cities:
            sorted_results(combined_cities, benchmarks_run)
            save_city(previous_cities_dict, "previous_cities.txt")

        choice = input("\n Add more entries>: (y/n) > ").strip().lower()

        if choice in ['n']:
            break


if __name__ == "__main__":
    main()
