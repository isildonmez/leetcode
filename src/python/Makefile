.PHONY:	lock update rebuild fmt check test clean

init:
	poetry install

lock:
	poetry lock

update:
	poetry update

rebuild:
	poetry env info --path | xargs rm -r
	poetry install

fmt:
	poetry run zimports -m src src
	poetry run black src

check:
	poetry run flake8
	poetry run mypy --strict --pretty src

test:
	poetry run pytest

clean:
	find . -name "*pyc" -o -name "*pyo" | xargs rm
	find . -name "__pycache__" | xargs rmdir