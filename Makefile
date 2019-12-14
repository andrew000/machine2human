.PHONY: test lint mypy clean

default: test
	
test: venv lint mypy
	. venv/bin/activate; pytest -q

lint: venv
	. venv/bin/activate; \
		flake8 *.py --max-line-length 120; \
		flake8 tests/*.py --ignore E402 --max-line-length 120

mypy: venv
	. venv/bin/activate; mypy --ignore-missing-imports *.py tests/*.py

venv: requirements.txt
	python3 -m venv venv
	. venv/bin/activate; \
	pip3 install -r requirements.txt

clean:
	find . \( -name '.mypy_cache' \
	   -o -name '.pytest_cache'   \
	   -o -name '__pycache__'     \
	   -o -name 'venv' \)         \
	   -print0                    \
	| xargs -0 rm -rf
