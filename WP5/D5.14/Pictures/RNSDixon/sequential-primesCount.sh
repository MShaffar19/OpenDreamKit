#!/bin/bash

#==============
#===== GNU plot

BITSIZE="400"
PS="-1 2 4 8 16 32"

DATA_FILENAME="sequential-primesCount.txt"
GNUPLOT_FILENAME=".sequential-primesCount.gnp"
GNUPLOT_OUTPUT_FILENAME="sequential-primesCount.pdf"

PLOT_COMMAND="plot for "
for P in ${PS}; do
    FILENAME=".p_${P}.txt"
    if [ "${P}" == "-1" ]; then
        echo "\"Classic Dixon\"" > ${FILENAME}
    else
        echo "\"RNS-Dixon with ${P} primes\"" > ${FILENAME}
    fi
    cat ${DATA_FILENAME} | grep "\-b ${BITSIZE}" | grep "\-p ${P} " | cut -d' ' -f4,12 >> ${FILENAME}
    PLOT_COMMAND="${PLOT_COMMAND} [COL=1:1] '${FILENAME}' using COL:xticlabels(2) with linespoints,"
done
PLOT_COMMAND="${PLOT_COMMAND::-1}"

# Header
cat > ${GNUPLOT_FILENAME} << EOF
set term pdf enhanced color

set boxwidth 0.8
set grid ytics
set key top left

set key autotitle columnheader
set xlabel 'matrix dimension (bitsize ${BITSIZE})'
set ylabel 'time (s)'

bm = 0.15
lm = 0.18
rm = 0.95
gap = 0.02
size = 0.75
kk = 0.5 # relative height of bottom plot

set output '${GNUPLOT_OUTPUT_FILENAME}'
set multiplot
#set logscale y

${PLOT_COMMAND}
EOF

gnuplot "${GNUPLOT_FILENAME}"
echo "Generated ${GNUPLOT_OUTPUT_FILENAME}"
