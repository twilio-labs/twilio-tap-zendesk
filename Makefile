.PHONY: test
.DEFAULT_GOAL := test

test:
	pylint tap_zendesk -d missing-docstring,invalid-name,line-too-long,too-many-locals,too-few-public-methods,fixme,stop-iteration-return,too-many-branches,useless-import-alias,no-else-return,logging-not-lazy
	nosetests test/unittests


setup-environment:
	rm -rf env || true
	python3 -m venv env/tap-zendesk
	source env/tap-zendesk/bin/activate && pip3 install .