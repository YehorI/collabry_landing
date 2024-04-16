
install:
	poetry install --all-extras
run: install
	poetry run python -m collabry database migrations apply
	poetry run python -m collabry run