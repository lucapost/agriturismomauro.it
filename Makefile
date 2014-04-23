compile:
	./minimalsite.py -t it

update:
	git add .
	git commit -am fix
	git push
upload:	
	rsync -avr -e ssh ./dst/* flarevm:www/agriturismomauro.it
