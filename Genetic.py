import random
import operator

geen_pool = "abcçdefgğhıijklmnoöpqrsştuüvwxyzABCÇDEFGĞHIİJKLMNOÖPQRSŞTUVWXYZ 1234567890 ,.-;:_!#%&/()=?@${[]}'"
goal = "Çağıl İlhan Sözer"
global goal_length
goal_length = len(goal)
population = []
mutation = False
first_population = []
global say
say =  0
class Individual :   #CREATING CHROMOSOMES with

    def __init__(self,gen=None,fitness=None):

        if(gen  == None and fitness == None):
            pass
        else:
            self.gen= self.make_gen()
            self.fitness = self.calculate_fitness()

    def make_gen(self): #this function creates  cromosomes
        temp_gen = []
        for i in range(goal_length):
            temp_gen.append(random.choice(geen_pool))
        gen = temp_gen
        return gen
    def calculate_fitness(self,offspring=None):
        global say
        count = 0
        fitness = 0
        if(offspring==None):
            for a in self.gen:
                if(a != goal[count]):
                    fitness += 1
                count += 1
        else:
            for a in offspring.gen:
                if(a != goal[count]):
                    fitness += 1
                count += 1
        return fitness
    def crossover(self,p1): #single point crossover technic
        probability = random.randint(0,2)
        crossover_rate  = random.randint(0,10)
        p2 = self.gen
        offspring = None
        crossover_point = (len(self.gen)//2)
        if(crossover_rate<10):
            if(probability == 0):
                offspring=p1.gen[0:crossover_point] + p2[crossover_point::]
            else:
                offspring=p2[0:crossover_point] + p1.gen[crossover_point::]
        else:
            offspring = self.mutation(p2)
        return offspring  #offspring with crossover and chance of gettin mutate same time

    def mutation(self,gen):

        self.gen[random.randint(0,16)] = random.choice(geen_pool)
        return gen


def main():
    accomplish = False  # Now we need to take 2 parent for the selection part of my population.
    generation = 1
    global population
    for i in range (100):
        subject = Individual(gen=True,fitness=True)
        population.append(subject)
    population.sort (key=lambda x: x.fitness)
    while accomplish != True:
        acomplish = True
        print ("Generation ", generation, " : ", "".join ([p for p in population[0].gen]), " Fitness: ",
               population[0].fitness)
        if(population[0].fitness ==0):
            acomplish = True
            print("Congrats")

            break

        if (accomplish == True):
            print("Congrats!")
            print ("Generation ",generation," : ", "".join([p for p in population[0].gen]))
            break

        else:
            new_generation = [] # We couldn't find the solution yet so we need to make crossover and mutation.
            # We'll take 50 gen with %10 best fitness score and the other 50 are the gap of %10-%50 fittness socre

            for i in range(50):
                offspring = Individual ()
                random_best_parent = random.randint(0,9)
                random_best_parent1 = random.randint (0, 9)
                offspring.gen = population[random_best_parent].crossover(population[random_best_parent1])
                offspring.fitness = Individual.calculate_fitness(offspring)
                new_generation.append(offspring)
            for j in range(40):
                offspring = Individual ()
                random_average_parent = random.randint(10,49)
                random_average_parent1 = random.randint (10, 49)
                offspring.gen = population[random_average_parent].crossover(population[random_average_parent1])
                offspring.fitness = Individual.calculate_fitness(offspring)
                new_generation.append(offspring)
            for k in range(10):
                offspring = Individual ()
                random_worst_parent = random.randint(50,99)
                random_worst_parent1 = random.randint (50, 99)
                offspring.gen = population[random_worst_parent].crossover(population[random_worst_parent1])
                offspring.fitness = Individual.calculate_fitness(offspring)
                new_generation.append(offspring)
            population = new_generation
            generation += 1
            population.sort (key=lambda x: x.fitness)

main()