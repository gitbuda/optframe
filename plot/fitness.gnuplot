reset

# output file setup
set terminal png nocrop enhanced font "OpenSans-Regular,11" 
set output "OUTPUT"

# legend position
set key below

# title
set title "Linespoints"

# xAxis
set xlabel "xAxis"

# yAxis
set ylabel "yAxis"

# axis range
# set offsets <left>, <right>, <top>, <bottom>
set offsets graph 0.00, 0.00, 0.05, 0.05

set style line 1 lc rgb 'orange' pt 7 ps 0.75
set style line 2 lc rgb 'red' pt 7 ps 0.75
set style line 3 lc rgb 'green' pt 7 ps 0.75
set style line 4 lc rgb 'blue' pt 7 ps 0.75

set style function linespoints
plot "INPUT" using 1:2 title 'points 1' with linespoints ls 1, \
     "INPUT" using 1:3 title 'points 2' with linespoints ls 2
