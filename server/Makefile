.PHONY: migrate-init
migrate-init: ## Initial migrations
	alembic init migrations

.PHONY: migrate-create
migrate-create: ## Create a new revision file
	alembic revision --autogenerate -m "nevers"

.PHONY: migrate-up
migrate-up: ## Upgrade to a later version
	alembic upgrade head

.PHONY: migrate-down
migrate-down: ## Revert to a previous version
	alembic downgrade $(revision)