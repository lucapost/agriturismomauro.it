compile:
	./minimalsite.py -t it

upload:
	rsync -avr -e ssh ./dst/* flarevm:www/agriturismomauro.it
