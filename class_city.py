class City:
    def __init__(self, name, population, daily_usage_gallons):
        self.name = name
        self.population = int(population)
        self.daily_usage_gallons = float(daily_usage_gallons)

    def average_gpcd(self):
        if self.population == 0:
            return 0
        return self.daily_usage_gallons / self.population

    def size_city (self):
        if self.population < 100000:
            return "Small"
        elif self.population < 500000:
            return "Medium"
        else:
            return "Large"

    def efficiency (self, benchmark):
        gpcd = self.average_gpcd()
        size = self.size_city()

        efficiency = benchmark.get(size, {"Efficient": 120, "Moderately Efficient" : 150})

        if gpcd <= efficiency["Efficient"]:
            return "Efficient", False
        elif gpcd <= efficiency["Moderately Efficient"]:
            return "Moderately Efficient", False
        else:
            return "Wasteful", True