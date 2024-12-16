.phony: activate create deactivate destroy freeze install upgrade

create:
	python3 -m venv .venv

destroy:
	rm -rf .venv

install:
	. .venv/bin/activate; python3 -m pip install -r requirements.txt

upgrade:
	. .venv/bin/activate; python3 -m pip install --upgrade pip
	. .venv/bin/activate; python3 -m pip install --upgrade -r requirements.txt

freeze:
	. .venv/bin/activate; python3 -m pip freeze > requirements.txt



