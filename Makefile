.PHONY: clean

build: venv
	. venv/bin/activate; pelican -vs conf.py src/

preview: build
	python -m webbrowser ./output/index.html

clean:
	rm -rfv output

venv: venv/bin/pelican
venv/bin/pelican:
	virtualenv venv
	. venv/bin/activate; pip install pelican


