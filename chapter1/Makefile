typehint:
	mypy mypy.py

test:
	pytest test.py

lint:
	pylint pylint.py

checklist: lint	typehint test

.PHONY: typehint test lint checklist
