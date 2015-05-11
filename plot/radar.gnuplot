unset border
set polar
set angles degrees #set gnuplot on degrees instead of radians

set style line 10 lt 1 lc 0 lw 0.3 #redefine a new line style for the grid

set grid polar 72 #set the grid to be displayed every 60 degrees
set grid ls 10

set xrange [-6000:6000] #make gnuplot to go until 6000
set yrange [-6000:6000]

set xtics axis #disply the xtics on the axis instead of on the border
set ytics axis

set xtics scale 0 #"remove" the tics so that only the y tics are displayed
set xtics ("" 1000, "" 2000, "" 3000, "" 4000, "" 5000, "" 6000) #set the xtics only go from 0 to 6000 with increment of1000 but do not display anything. This has to be done otherwise the grid will not be displayed correctly.
set ytics 0, 1000, 6000 #make the ytics go from the center (0) to 6000 with incrment of 1000

set size square 

set key lmargin

set_label(x, text) = sprintf("set label '%s' at (6500*cos(%f)), (6500*sin(%f))     center", text, x, x) #this places a label on the outside

#here all labels are created
eval set_label(0, "Time")
eval set_label(72, "Iterations")
eval set_label(144, "Evaluations")
eval set_label(216, "Fitness")
eval set_label(288, "Memory")


set title "Radar" 
set style line 11 lt 1 lw 2 pt 2 ps 2 #set the line style for the plot

#and finally the plot
plot "radar.dat" u 1:2 t "Max strain" w lp ls 11, \
     "radar.dat" u 1:3 t "nekaj" w lp ls 12

pause 10
