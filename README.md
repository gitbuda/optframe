# Optimization framework

Under development!

## Description:

Optimization framework implemented in Python.

### UML diagram:
![optframe logo](/docs/optframe.png)

## Usage:

Default config file is config.json.

```
./executor.py # loads configuration from default config file
./executor.py -c path/to/config.json # loads custom configuration
```

## Algorithms: 

* Genetic Algorithm - ga
* Pyramid Genetic Algorithm - pga
* Linkage Tree Genetic Algorithm - ltga
* Parameterless Pyramid Population Algorithm - p3
* Compact Genetic Algorithm - cga
* Pyramid Compact Genetic Algorithm - pcga
* Bayesan Optimization Algorithm - boa
* Pyramid Bayesan Optimization Algorithm - pboa

## Problems:

* Boolean
* Capacited Vehicle Routing Problem
* Deceptive Trap
* Deceptive Step Trap
* Leading Ones
* Max Sat
* One Max
* Pipeline
* Rastrigin
* Schwefel
* TSP: Bays 29, Oliver 30

## Dependencies:

* numpy
* scipy

## TODO:

* change places of config files
* rename Config to Context

### Master thesis work

Marko Budiselić, Faculty of electrical engineering and computing, University of Zagreb, Croatia 2015
