.PHONY: check fmt lint

discovery_url := 'https://sheets.googleapis.com/$$discovery/rest?version=v4'
functions_url := 'https://support.google.com/docs/table/25273'

dir := gigamonkeys

generated := $(dir)/spreadsheets.py
generated += $(dir)/functions.py

all: $(generated)

sheets-discovery-v4.json:
	curl $(discovery_url) | jq -S '.' > $@

functions-list.html:
	curl $(functions_url) > $@

$(dir)/spreadsheets.py: sheets-discovery-v4.json extra.json build/make_spreadsheets.py
	echo "# Generated from $(discovery_url)" > $@
	echo "" >> $@
	build/make_spreadsheets.py $< extra.json >> $@

$(dir)/functions.py: functions-list.html build/make_functions.py
	build/make_functions.py $< $(functions_url) > $@

check: all
	pytest .

fmt: all
	isort --recursive .
	autoflake --recursive --in-place --remove-all-unused-imports --remove-unused-variables .
	black --line-length 120 .

lint: all
	flake8
	isort --recursive . --check-only
	black --check --line-length 120 .

typecheck: all
	mypy $(dir)

tidy:
	rm -f *~

clean: tidy
	rm -f sheets-discovery-v4.json
	rm -f functions-list.html
	rm -f $(generated)
