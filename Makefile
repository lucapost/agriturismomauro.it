compile:
	./minimalsite.py -t it

upload:
	git add .
	git commit -am fix
	git push
	rsync -avr -e ssh ./dst/* flarevm:www/agriturismomauro.it
