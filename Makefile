.PHONY: clean
.DEFAULT_GOAL := init

clean:
	rm -f db.sqlite3

install_python_dependencies:
	python3 -m pip --quiet install --requirement requirements.txt

generate_migration_files:
	python3 manage.py makemigrations --no-header

migrate:
	python3 manage.py migrate

collect_messages:
	python3 manage.py makemessages \
	 	--keep-pot \
	 	--ignore=venv \
	 	--ignore=.venv \
	 	--ignore=static \
	 	--all

compile_messages:
	python3 manage.py compilemessages \
		--ignore=venv \
		--ignore=.venv \
		--ignore=static

collectstatic:
	python3 manage.py collectstatic --no-input --clear

build: \
	collect_messages \
	compile_messages \
	collectstatic

init: \
	install_python_dependencies \
	generate_migration_files \
	migrate \
	build
