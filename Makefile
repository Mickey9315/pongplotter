PLOTS=$(shell ls logs/ | xargs -I xx basename xx .log | xargs -I xx echo "plots/xx.png")

all: $(PLOTS)

plots/ping-%.png: ping-%.csv plot.gnuplot
	gnuplot -e "infile='$<'; outfile='$@'" ./plot.gnuplot

ping-%.csv: ping-raw-%.csv
	./prepare-plot-data.py $< $@

ping-raw-%.csv: logs/ping-%.log
	./log-to-csv.sh < $< > $@
