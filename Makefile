.PHONY: clean

all: venv
	. venv/bin/activate; pelican -vs conf.py src/

clean:
	rm -rfv output

venv: venv/bin/pelican
venv/bin/pelican:
	virtualenv venv
	. venv/bin/activate; pip install pelican
	. venv/bin/activate; pip install pygments


