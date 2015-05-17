# set terminal png transparent nocrop enhanced size 450,320 font "arial,8" 
# set output 'boxplot.3.png'
# set border 2 front lt black linewidth 1.000 dashtype solid

reset
set terminal png nocrop enhanced font "Garamond-Regular,11" 
set output "OUTPUT"

set boxwidth 0.25 absolute
set style fill solid 0.5 border lt -1
set bars 3
unset key
set pointsize 2.0
set style data boxplot
set xtics border in scale 0,0 nomirror norotate  autojustify
set xtics  norangelimit
set xtics   ()
set ytics border in scale 1,0.5 nomirror norotate  autojustify
set title "Bays 29" 
set ylabel "Cost" 
set style boxplot candles range 1.50 outliers pt 3 separation 1 labels auto sorted
x = 0.0
plot 'INPUT' using (1):2:(0):1 lc rgb "#007FFF" lw 2

