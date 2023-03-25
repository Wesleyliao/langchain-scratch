.PHONY: lint

lint:
	black .
	isort .
	mypy .