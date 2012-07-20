.PHONY: clean

build: venv
	. venv/bin/activate; pelican -vs conf.py src/

draft: venv
	. venv/bin/activate; pelican -vs conf.py -o output/draft/ src/

preview: build
	python -m webbrowser ./output/index.html

clean:
	rm -rfv output

venv: venv/bin/activate
venv/bin/activate: requirements.txt
	test -d venv || virtualenv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/bin/activate

