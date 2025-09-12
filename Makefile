package_name = m2h
py_code_dir = src/$(package_name)
docs_dir = docs
docs_source_dir = $(docs_dir)/source
reports_dir = reports
tests_dir = tests

.PHONY: lint
lint:
	echo "Running ruff..."
	uv run ruff check --config pyproject.toml --diff $(py_code_dir) $(tests_dir)

	echo "Running MyPy..."
	uv run mypy --config-file pyproject.toml

.PHONY: format
format:
	echo "Running ruff check with --fix..."
	uv run ruff check --config pyproject.toml --fix --unsafe-fixes $(py_code_dir) $(tests_dir)

	echo "Running ruff..."
	uv run ruff format --config pyproject.toml $(py_code_dir) $(tests_dir)

	echo "Running isort..."
	uv run isort --settings-file pyproject.toml $(py_code_dir) $(tests_dir)

.PHONY: test
test:
	echo "Running tests..."
	uv run pytest -vv --cov=$(py_code_dir) --cov-report=html --cov-report=term --cov-config=.coveragerc $(tests_dir)

.PHONY: test-coverage
test-coverage:
	echo "Running tests with coverage..."
	$(mkdir_cmd)
	uv run pytest -vv --cov=$(py_code_dir) --cov-config=.coveragerc --html=$(reports_dir)/tests/index.html tests/
	uv run coverage html -d $(reports_dir)/coverage

.PHONY: outdated
outdated:
	uv tree --universal --outdated

.PHONY: sync
sync:
	uv sync --reinstall-package $(package_name) --extra dev --extra tests

.PHONY: build
build:
	uv build --wheel --sdist
