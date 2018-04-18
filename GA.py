import random
import sys

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
                if i > 9:
                    y = self.c[i + 1]
                    self.c[i] = y
                    self.c[i + 1] = x

        self.f = self.fitness_function()


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
        r = random.random()
        if r > 0.8:
            print "no crossover"
            return self, other_obj, False
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

            return offspring_one, offspring_two, True

    def find_lowest_two(self):
        f_list = [c.f for c in chromosomes]
        # print f_list

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

        '''     
        print "scaled"
        for c in chromosomes:
            print c.scaled,
        print
        print
        '''

    def weighting(self):
        scaled_total = 0
        scaled_list = [c.scaled for c in chromosomes]
        for x in scaled_list:
            scaled_total += x

        #print "printed weighted"
        for c in chromosomes:
            c.weighted = c.scaled / scaled_total
            # print c.weighted
        # print


    # does not remove chromosome from list
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

    def best(self):
        highest = -sys.maxint - 1

        for c in chromosomes:
            if c.f > highest:
                highest = c.f

        print highest
'''
starter = Genetic()
second = Genetic()
print "printing starting 2 chromosomes"
for c in chromosomes:
    print c.c
print

print "le best"
print starter.best()
print


#roulette function to determine which to call with
parents = starter.roulette()
parents[0].crossover(parents[1])
print "after crossover"
for c in chromosomes:
    print c.c
    print c.f
print


starter.find_lowest_two()
print "after find lowest"
for c in chromosomes:
    print c.c
    print c.f
    print c.scaled
'''
# looping
for i in range(50):
    new_genetic = Genetic()

for i in range(100):
    for c in chromosomes:
        if not(c is None):
            chrom = c
            break

    parents = chrom.roulette()

    c_1, c_2, did_crossover = parents[0].crossover(parents[1])

    c_1.mutate()
    c_2.mutate()

    if did_crossover:
        chrom.find_lowest_two()

    c_1.best()
