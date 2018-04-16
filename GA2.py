import random

population_size = 50
chromosomes = []
available_numbers = [i for i in range(1, 11)]


class Genetic:
    def __init__(self):
        self.c = self.generate_population()
        self.f = self.fitness_function()
        chromosomes.append(self)

    def generate_population(self):
        first_ten = [i for i in range(1, 11)]
        random.shuffle(first_ten)
        return first_ten

    def fitness_function(self):
        x = self.c
        fitness = 4 * x[0] ** 2 - 2 * x[1] ** 3 + 9 * x[2] ** 2 - 11 * x[3] ** 2 + 5 * x[4] ** 0.5
        + (x[5] + x[6]) ** 3 - 5 * x[7] ** 2 + 10 * (x[8] - x[9]) ** 2
        return fitness

    # unfinished mutation method
    def mutate(self):
        for x in self.c:
            r = random.randint(1, 100)
            if r == 1:
                pass

    # performs crossover and checks for duplicate numbers
    def switch_and_check(self, chrom, sub, cross_point):
        old_section = chrom[cross_point:]
        new_section = sub
        new_chrom = new_section + old_section

        for i in range(len(new_chrom) - 1):
            x = new_chrom[i]
            for j in range(len(new_chrom)):
                y = new_chrom[j]
                if x == y and j > i:
                    for a in available_numbers:
                        if a not in new_chrom:
                            new_chrom[j] = a

        return new_chrom

    # could probably do separate get cross_point and crossover methods
    def crossover(self, other_obj):
        chrom_one = self.c
        chrom_two = other_obj.c

        cross_point = random.randint(1, 9)  # going from 1 to 9 intentionally does not include the last index
        print cross_point
        sub_one = chrom_one[:cross_point]  # chrom_one up to but not including cross_point index and after
        sub_two = chrom_two[:cross_point]

        self.c = self.switch_and_check(chrom_one, sub_two, cross_point)
        other_obj.c = other_obj.switch_and_check(chrom_two, sub_one, cross_point)

        self.f = self.fintness


starter = Genetic()
second = Genetic()
for c in chromosomes:
    print c.c
starter.crossover(second)
for c in chromosomes:
    print c.c


