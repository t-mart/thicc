VERSION=$(shell grep __version__ thicc/__init__.py)

all: test


clean:
	@echo Cleaning up
	rm -rf .tox *.egg dist build .coverage .cache .pytest_cache httpie.egg-info
	find . -name '__pycache__' -delete -print -o -name '*.pyc' -delete -print
	@echo

test:
	@echo Running tests
	pipenv install --dev
	pipenv run py.test ./tests --doctest-modules --verbose ./thicc ./tests
	@echo

release-test-pypi: clean
	@echo "$(VERSION)"
	python setup.py sdist
	python setup.py bdist_wheel
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	@echo


release: clean
	@echo "$(VERSION)"
	python setup.py sdist
	python setup.py bdist_wheel
	twine upload dist/*
	@echo
