# -*- coding: utf-8 -*-

'''
Bit Array Booster
'''

import numpy


class BitArrayBooster(object):

    def __init__(self):
        pass

    def boost0(self, solution, evaluator):

        genotype_size = solution.get_genotype_size()
        options = numpy.array([x for x in range(genotype_size)])
        tried = set()

        improvement = True
        while improvement:
            improvement = False
            numpy.random.shuffle(options)
            for index in options:
                if index in tried:
                    continue
                new_genotype = numpy.copy(solution.get_genotype())
                new_genotype[index] = 0 if new_genotype[index] == 1 else 1
                old_fitness = solution.get_fitness()
                new_fitness = evaluator.evaluate(new_genotype)
                if old_fitness < new_fitness:
                    solution.set_genotype(new_genotype)
                    solution.set_fitness(new_fitness)
                    improvement = True
                    tried = set()
                tried.add(index)

        return solution

    def boost(self, solution, evaluator):

        genotype = solution.get_genotype()
        genotype_size = solution.get_genotype_size()
        options = numpy.array([x for x in range(genotype_size)])
        tried = set()

        improvement = True
        while improvement:
            improvement = False
            numpy.random.shuffle(options)
            for index in options:
                if index in tried:
                    continue
                genotype[index] = 0 if genotype[index] == 1 else 1
                old_fitness = solution.get_fitness()
                new_fitness = evaluator.evaluate(genotype)
                if old_fitness < new_fitness:
                    solution.set_genotype(genotype)
                    solution.set_fitness(new_fitness)
                    improvement = True
                    tried = set()
                else:
                    genotype[index] = 0 if genotype[index] == 1 else 1
                tried.add(index)

        return solution
