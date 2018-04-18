import random
import sys

population_size = 50
chromosomes = []
available_numbers = [i for i in range(1, 11)]

class Genetic:
    def __init__(self):
        self.c = self.generate_chrom()
        self.f = self.fitness_function()
        self.scaled = None
        self.weighted = None

    # randomly generates a list of numbers between 1 and 10, no duplicates
    def generate_chrom(self):
        first_ten = [i for i in range(1, 11)]
        random.shuffle(first_ten)
        return first_ten

    def fitness_function(self):
        x = self.c
        fitness = 4*x[0]**2 - 2*x[1]**3 + 9*x[2]**2 - 11*x[3]**2 + 5*x[4]**0.5 + (x[5] + x[6])**3 - 5*x[7]**2 + 10*(x[8] - x[9])**2
        return fitness

    # mutates and updates fitness
    def mutate(self):
        for i in range(10):
            x = self.c[i]
            r = random.randint(1, 100)
            if r == 1:
                if i == 9:
                    y = self.c[0]
                    self.c[i] = y
                    self.c[0] = x
                if i > 9:
                    y = self.c[i + 1]
                    self.c[i] = y
                    self.c[i + 1] = x

        self.f = self.fitness_function()

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

    # determines whether to crossover and returns new children objects
    def crossover(self, other_obj):
        r = random.random()
        if r > 0.8:
            # no crossover essentially creates new objects that clones of the parents
            offspring_one = Genetic()
            offspring_one.c = self.c

            offspring_two = Genetic()
            offspring_two.c = other_obj.c
            return self, other_obj

        if r <= 0.8:
            chrom_one = self.c
            chrom_two = other_obj.c

            cross_point = random.randint(1, 9)  # going from 1 to 9 intentionally does not include the last index
            # print "crossover point", cross_point
            sub_one = chrom_one[:cross_point]  # chrom_one up to but not including cross_point index and after
            sub_two = chrom_two[:cross_point]

            new_chrom_one = self.switch_and_check(chrom_one, sub_two, cross_point)
            new_chrom_two = other_obj.switch_and_check(chrom_two, sub_one, cross_point)

            offspring_one = Genetic()
            offspring_one.c = new_chrom_one

            offspring_two = Genetic()
            offspring_two.c = new_chrom_two

            return offspring_one, offspring_two

    # finds the chromosome with the lowest fitness and replaces it with one of the children
    def replace_lowest(self):
        f_list = [c.f for c in chromosomes]
        # print f_list

        for i in range(2):
            lowest = min(f_list)
            low_chrom = None
            for c in chromosomes:
                if c.f == lowest:
                    c = self
            f_list.remove(lowest)

    # sets c.scaled for all chromosomes so that all every fitness is positive
    def scaling(self):
        f_list = [c.f for c in chromosomes]
        min_f = min(f_list)

        if min_f >= 0:
            for c in chromosomes:
                c.scaled = c.f

        if min_f < 0:
            for c in chromosomes:
                c.scaled = c.f + abs(min_f) + 100

    # weights the chromosomes from 0-1 for roulette selection
    def weighting(self):
        scaled_total = 0
        scaled_list = [c.scaled for c in chromosomes]
        for x in scaled_list:
            scaled_total += x

        for c in chromosomes:
            c.weighted = c.scaled / scaled_total

    # returns two parents using roulette selection
    def roulette(self):
        self.scaling()
        self.weighting()

        parents = []
        for i in range(2):
            r = random.random()
            weighted_total = 0

            for c in chromosomes:
                weighted_total += c.weighted
                if weighted_total > r:
                    parents.append(c)
                    break

        return parents

    # returns the chromosome with the highest fitness
    def best(self):
        highest = -sys.maxint - 1
        best_chrom = None

        for c in chromosomes:
            if c.f > highest:
                highest = c.f
                best_chrom = c

        return best_chrom

# creates population in chromosomes list
for i in range(50):
    new_genetic = Genetic()
    chromosomes.append(new_genetic)

# for 100 generations
for i in range(100):
    parents = chromosomes[0].roulette()
    c_1, c_2 = parents[0].crossover(parents[1])
    c_1.mutate()
    c_2.mutate()
    c_1.replace_lowest()
    c_2.replace_lowest()
    best = chromosomes[0].best()
    #print best.f

print
print best.c
print best.f

