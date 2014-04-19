compile:
	./minimalsite.py -t it

update:
	git add .
	git commit -am fix
	git push
upload:	
	make update
	rsync -avr -e ssh ./dst/* flarevm:www/agriturismomauro.it
