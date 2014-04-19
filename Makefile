compile:
	./minimalsite.py -t it

update:
	git add .
	git commit -am fix
	git push
upload:	
	make compile
	make update
	rsync -avr -e ssh ./dst/* flarevm:www/agriturismomauro.it
