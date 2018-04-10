import random

population_size = 50
chromosomes = []


class genetic:
    def __init__(self):
        self.c = self.generate_population()
        self.f = self.fitness_function()
        chromosomes.append(self)

    def generate_population(self):
        available_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        random.shuffle(available_numbers)
        return available_numbers

    def fitness_function(self):
        x = self.c
        fitness = 4 * x[0] ** 2 - 2 * x[1] ** 3 + 9 * x[2] ** 2 - 11 * x[3] ** 2 + 5 * x[4] ** 0.5
        + (x[5] + x[6]) ** 3 - 5 * x[7] ** 2 + 10 * (x[8] - x[9]) ** 2
        return fitness

    def mutate(self):
        for x in self.c:
            r = random.randint(1, 101)
            if r == 1:
                pass



starter = genetic()
print starter.c
print starter.f
