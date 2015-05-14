#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Bubble local search. Permutation specific local search
in which random permutation element is chosen and then
it is moved through the whole permutation in order to
get a better solution. A random element is chosen
with uniform distribution.

e.g. let say that permutation is [2, 5, 3, 1, 4] and
random choosen element is e.g. 3

if [3, 5, 2, 1, 4] has better fitness return it
    ^
    |

if [2, 3, 5, 1, 4] has better fitness return it
       ^
       |

if [2, 5, 1, 3, 4] has better fitness return it
             ^
             |

if [2, 5, 4, 1, 3] has better fitness return it
                ^
                |

3 moves from the beginning of the solution to the end
of the solution like a bubble.
'''

import random
import logging
from common.constants import PERMUTATION_BOX_KEY

log = logging.getLogger(__name__)


def switch(array, i, j):
    array[i], array[j] = array[j], array[i]


class LocalSearch(object):

    def configure(self, context):
        '''
        Configure the bubble local search.

        Args:
            context: execution context
        '''
        self.evaluator = context.evaluate_operator

    def search(self, solution):
        '''
        The bubble search.

        Args:
            solution: instance of the Solution class
        '''
        genotype = solution.container[PERMUTATION_BOX_KEY]
        genotype_size = len(genotype)

        bubble_index = random.randint(0, genotype_size - 1)

        for index in xrange(genotype_size):
            if index == bubble_index:
                continue
            switch(genotype, index, bubble_index)
            new_fitness = self.evaluator.evaluate(solution)
            if new_fitness > solution.fitness:
                solution.fitness = new_fitness
                return solution
            else:
                switch(genotype, index, bubble_index)

        print solution.container

        return solution


if __name__ == '__main__':

    class Evaluator():
        def evaluate(self, solution):
            return 0

    class Context():
        pass

    from common.solution import Solution
    context = Context()
    context.evaluate_operator = Evaluator()
    local = LocalSearch()
    local.configure(context)
    local.search(Solution({"permutation": [2, 3, 1, 5, 4]}, 0))
