# -*- coding: utf-8 -*-

# PYTHONPATH=/path/to/optframe

import sys
import matplotlib.pyplot as plt
from helpers.loader import load_json
from itertools import dropwhile

data_file = sys.argv[1]
solution_file = sys.argv[2]
title = sys.argv[3]

# load problem info
data = {}
with open(data_file) as f:
    lines = iter(f.readlines())
    points = dropwhile(lambda x: 'DISPLAY_DATA_SECTION' not in x, lines)
    for point in list(points)[1:-1]:
        x = filter(None, point.rstrip().split(' '))
        print x
        data[int(x[0]) - 1] = [float(x[1]), float(x[2])]

# load solution
solution = load_json(solution_file)
paths = zip(solution.permutation, solution.permutation[1:])
paths.append((solution.permutation[-1], solution.permutation[0]))
print paths

# plot graph
# plt.xlabel('x')
# plt.ylabel('y')
# plt.xlim([0, 2300])
# plt.ylim([0, 2300])
plt.suptitle(title, fontsize=12, fontweight='bold')
for path in list(paths)[:]:
    p1 = data[path[0]]
    p2 = data[path[1]]
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-', lw=2)
for point, coords in data.items():
    plt.plot(coords[0], coords[1], "o")
    plt.annotate('%s' % str(point), xy=coords)
plt.show()
