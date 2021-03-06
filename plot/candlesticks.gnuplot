reset

# output file setup
set terminal png nocrop enhanced font "OpenSans-Regular,11" 
set output "OUTPUT"

# candlesticks box width
set boxwidth 0.2 absolute

# legend position
set key below

# title
set title "Candlesticks"

# xAxis
set xlabel "xAxis"

# yAxis
set ylabel "yAxis"

# axis range
# set offsets <left>, <right>, <top>, <bottom>
set offsets graph 0.2, 0.2, 0.2, 0.2

# plot
set style fill empty
plot 'INPUT' using 1:3:2:6:5:xticlabels(7) with candlesticks title 'Quartiles' lt 3 whiskerbars, \
     'INPUT' using 1:4:4:4:4 with candlesticks lt -1 lw 2 notitle, \
     'INPUT' using 1:4 with linespoints lt 1 pt 13 notitle
