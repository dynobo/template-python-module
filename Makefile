init:
	rm -rf ./.venv
	python3 -m venv .venv
	.venv/bin/python -m pip install --upgrade pip wheel setuptools
	.venv/bin/python -m pip install -r requirements-dev.txt
	.venv/bin/pre-commit install -t pre-commit

test:
	.venv/bin/pytest tests

lint:
	.venv/bin/pylama

run:
	.venv/bin/python -m myapp

package:
	rm -rf build dist
	.venv/bin/python setup.py sdist bdist_wheel
	.venv/bin/twine check dist/*

upload_test:
	rm -rf build dist
	.venv/bin/python setup.py sdist bdist_wheel
	.venv/bin/twine check dist/*
	.venv/bin/twine upload --repository-url=https$(:)//test.pypi.org/legacy/ dist/*

upload_final:
	rm -rf build dist
	.venv/bin/python setup.py sdist bdist_wheel
	.venv/bin/twine check dist/*
	.venv/bin/twine upload dist/*