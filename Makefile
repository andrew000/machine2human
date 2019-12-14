.PHONY: test lint mypy

default: test
	
test: lint mypy
	pytest -q

lint:
	python3 -m flake8 m2h.py --max-line-length 120

mypy:
	mypy --ignore-missing-imports m2h.py
