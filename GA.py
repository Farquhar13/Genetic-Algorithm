import random

population_size = 50
chromosomes = []
available_numbers = [i for i in range(1, 11)]


class Genetic:
    def __init__(self):
        self.c = self.generate_population()
        self.f = self.fitness_function()
        self.scaled = None
        self.weighted = None
        chromosomes.append(self)

    def generate_population(self):
        first_ten = [i for i in range(1, 11)]
        random.shuffle(first_ten)
        return first_ten


    def fitness_function(self):
        x = self.c
        fitness = 4*x[0]**2 - 2*x[1]**3 + 9*x[2]**2 - 11*x[3]**2 + 5*x[4]**0.5
        + (x[5] + x[6])**3 - 5*x[7]**2 + 10*(x[8] - x[9])**2
        return fitness

    # mutation method
    def mutate(self):
        for i in range(10):
            x = self.c[i]
            r = random.randint(1, 100)
            if r == 1:
                if i == 9:
                    y = self.c[0]
                    self.c[i] = y
                    self.c[0] = x

                y = self.c[i+1]
                self.c[i] = y
                self.c[i+1] = x


    # performs cross over and checks for duplicate numbers
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


    # remember to only call this 80% of the time in the looping method
    def crossover(self, other_obj):
        chrom_one = self.c
        chrom_two = other_obj.c

        cross_point = random.randint(1, 9)  # going from 1 to 9 intentionally does not include the last index
        print cross_point
        sub_one = chrom_one[:cross_point]  # chrom_one up to but not including cross_point index and after
        sub_two = chrom_two[:cross_point]

        new_chrom_one = self.switch_and_check(chrom_one, sub_two, cross_point)
        new_chrom_two = other_obj.switch_and_check(chrom_two, sub_one, cross_point)

        Offspring(new_chrom_one)
        Offspring(new_chrom_two)

    def find_lowest_two(self):
        f_list = [c.f for c in chromosomes]
        print f_list

        for i in range(2):
            lowest = min(f_list)
            for c in chromosomes:
                if c.f == lowest:
                    chromosomes.remove(c)
            f_list.remove(lowest)

    def scaling(self):
        f_list = [c.f for c in chromosomes]
        min_f = min(f_list)

        if min_f >= 0:
            for c in chromosomes:
                c.scaled = c.f

        if min_f < 0:
            for c in chromosomes:
                c.scaled = c.f + abs(min_f) + 100

    def weighting(self):


    def roulette(self):
        self.scaling()
        self.weighted()
        print "scaled"
        for c in chromosomes:
            print c.scaled, ", ",
        print

        scaled_total = 0
        scaled_list = [c.scaled for c in chromosomes]
        for x in scaled_list:
            scaled_total += x

        weighted_total = 0
        for c in chromosomes:
            c.weighted = c.scaled / scaled_total
            weighted_total += c.weighted

        print "summing c.weighted"
        print weighted_total





class Offspring(Genetic):

    def __init__(self, chromosome):
        self.c = chromosome
        self.f = self.fitness_function()
        self.scaled = None
        self.weighted = None
        chromosomes.append(self)





starter = Genetic()
second = Genetic()
for c in chromosomes:
    print c.c
starter.crossover(second)
for c in chromosomes:
    print c.c
    print c.f

starter.roulette()

starter.find_lowest_two()

print "after find lowest"

for c in chromosomes:
    print c.c
    print c.f
    print c.scaled



