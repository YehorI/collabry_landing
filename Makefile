
install:
	poetry install --all-extras
run: install
	poetry run python -m collabry_landing database migrations apply
	poetry run python -m collabry_landing run