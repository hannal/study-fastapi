.PHONY: package-install package-update package-show
.PHONY: runserver shell
.PHONY: test-apps test-apps/hello cov-apps cov-apps/hello
.PHONY: config-venv
.PHONY: lint-check lint-reformat

################################################################################
# Package
################################################################################

package-install:
	@poetry install

package-update:
	@poetry update

package-show:
	@poetry show --tree


################################################################################
# Run
################################################################################

runserver: package-install
	@poetry run server

shell: package-install
	@poetry shell


################################################################################
# Testing
################################################################################

test-apps: package-install
	@poetry run pytest --no-cov ./apps

test-apps/hello:package-install
	@poetry run pytest --no-cov ./apps/hello

cov-apps:package-install
	@poetry run pytest --cov=apps

cov-apps/hello:package-install
	@poetry run pytest --cov=apps.hello


################################################################################
# Lint
################################################################################

lint-check: package-install
	@poetry run black ./ --config ./pyproject.toml --check

lint-reformat: package-install
	@poetry run black ./ --config ./pyproject.toml


################################################################################
# Poetry
################################################################################

config-venv:
	@poetry config virtualenvs.create true
	@poetry config virtualenvs.in-project true
	@poetry config virtualenvs.path .venv
