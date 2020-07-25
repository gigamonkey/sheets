all: dicts.py

sheets-discovery-v4.json:
	curl 'https://sheets.googleapis.com/$$discovery/rest?version=v4' | jq -S '.' > $@

dicts.py: sheets-discovery-v4.json codegen.py
	./codegen.py $< > $@

fmt:
	isort --recursive .
	autoflake --recursive --in-place --remove-all-unused-imports --remove-unused-variables .
	black .

lint:
	flake8
	isort --recursive . --check-only
	black . --check

typecheck:
	mypy .

tidy:
	rm -f *~

clean: tidy
	rm sheets-discovery-v4.json
	rm dicts.py
