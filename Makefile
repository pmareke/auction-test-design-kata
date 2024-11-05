.DEFAULT_GOAL := help 

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: install
install: ## Install the app packages
	 rm -rf poetry.lock
	 poetry install --no-root

.PHONY: test
test: ## Run all the tests
	 PYTHONPATH=. poetry run pytest tests -ra
