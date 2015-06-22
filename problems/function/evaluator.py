# -*- coding: utf-8 -*-

'''
Function evaluator.
'''

from itertools import islice
from common.fitness import Fitness, MIN
from common.constants import BIT_BOX_KEY
from math import pi, cos, sin, sqrt, fabs
from common.evaluation_counter import EvaluationCounter
# from common.evaluation_history import EvaluationHistory
from common.binary_to_float_evaluator import BinaryToFloatEvaluator


# functions start -------------------------------------------------------------
def rastrigin(x_vector):
    '''
    '''
    fitness = 10 * len(x_vector)
    for x in xrange(len(x_vector)):
        fitness += x**2 - (10 * cos(2 * pi * x))
    return Fitness(fitness, MIN)


def schwefel(x_vector):
    '''
    '''
    alpha = 418.982887
    fitness = 0
    for x in x_vector:
        fitness -= x * sin(sqrt(fabs(x)))
    return Fitness(float(fitness) + alpha * len(x_vector), MIN)


def griewank(x_vector):
    '''
    '''
    part1 = 0
    for x in x_vector:
        part1 += x**2
    part2 = 1
    for i in range(len(x_vector)):
        part2 *= cos(float(x_vector[i]) / sqrt(i+1))
    return Fitness(1 + (float(part1)/4000.0) - float(part2), MIN)


def whitley(x_vector):
    '''
    '''
    fitness = 0
    limit = len(x_vector)
    for i in range(limit):
        for j in range(limit):
            temp = 100*((x_vector[i]**2)-x_vector[j]) + \
                (1-x_vector[j])**2
            fitness += (float(temp**2)/4000.0) - cos(temp) + 1
    return Fitness(fitness, MIN)


def rosenbrock(x_vector):
    '''
    '''
    fitness = 0
    for i in range(len(x_vector)-1):
        fitness += 100*((x_vector[i]**2)-x_vector[i+1])**2 + \
            (1-x_vector[i])**2
    return Fitness(fitness, MIN)


functions = {'rastrigin': rastrigin, 'schwefel': schwefel,
             'griewank': griewank, 'whitley': whitley,
             'rosenbrock': rosenbrock}
# functions end ---------------------------------------------------------------


class Evaluator(BinaryToFloatEvaluator):

    def __init__(self):
        '''
        '''
        self.evaluation_counter = EvaluationCounter()
        # self.evaluation_history = EvaluationHistory()

    def configure(self, config=''):
        '''
        '''
        super(Evaluator, self).configure(config)
        self.evaluation_counter.configure(config)
        # self.evaluation_history.configure(config)
        self.function = functions[config.function]

    def evaluate(self, solution):
        '''
        '''
        self.evaluation_counter.increment()
        container = solution.container[BIT_BOX_KEY]

        x_vector = []
        it = iter(container)
        while True:
            next_n = list(islice(it, self.bits))
            x = self.converter.convert(next_n)
            if not next_n:
                break
            x_vector.append(x)

        fitness = self.function(x_vector)

        # eval_number = self.evaluation_counter.evaluations_number
        # solution.fitness = fitness
        # self.evaluation_history.save(eval_number, solution)

        return fitness
