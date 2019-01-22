VERSION=$(shell grep __version__ thicc/__init__.py)
TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"

all: test

init:
	@echo $(TAG)Initializing$(END)
	pipenv install --dev
	@echo

clean:
	@echo $(TAG)Cleaning up$(END)
	rm -rf .tox *.egg dist build .coverage .cache .pytest_cache httpie.egg-info
	find . -name '__pycache__' -delete -print -o -name '*.pyc' -delete -print
	@echo

test: init
	@echo $(TAG)Running tests$(END)
	pipenv run py.test --cov ./httpie --cov ./tests --doctest-modules --verbose ./thicc ./tests
	@echo

release-test-pypi: clean test
	@echo $(TAG)Releasing $(VERSION) to test PyPI$(END)
	python setup.py sdist
	python setup.py bdist_wheel
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	@echo $(TAG)Release available at https://test.pypi.org/project/thicc/$(END)
	@echo

release: clean test
	@echo $(TAG)Releasing $(VERSION) to PyPI$(END)
	python setup.py sdist
	python setup.py bdist_wheel
	pipenv run twine upload dist/*
	@echo $(TAG)Release available at https://pypi.org/project/thicc/$(END)
	@echo

black: init
	@echo $(TAG)Running black linter$(END)
	pipenv run black thicc/ tests/
	@echo
