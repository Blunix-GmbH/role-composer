.PHONY: help install molecule test all

help:
	@echo "Available targets are:"
	@echo "- install  - install all dependencies"
	@echo "- test     - run all tests"

install:
	pip install -r requirements.txt

molecule:
	molecule test --all

test: molecule

all: install test
