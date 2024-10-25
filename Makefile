LOG_TAIL=100
BACKEND_SERVICE_NAME=back

define set-default-container
	ifndef c
	c = $(BACKEND_SERVICE_NAME)
	else ifeq (${c},all)
	override c=
	endif
endef

set-container:
	$(eval $(call set-default-container))
build: set-container
	docker compose -f docker-compose.yaml build $(c)
up: set-container
	docker compose -f docker-compose.yaml up -d $(c)
down:
	docker compose -f docker-compose.yaml down
logs: set-container
	docker compose -f docker-compose.yaml logs --tail=$(LOG_TAIL) -f $(c)
restart: set-container
	docker compose -f docker-compose.yaml restart $(c)
exec: set-container
	docker compose -f docker-compose.yaml exec $(c) /bin/bash


migrate:
	docker compose -f docker-compose.yaml run --rm $(BACKEND_SERVICE_NAME) bash -c './manage.py migrate'
make_migrations:
	docker compose -f docker-compose.yaml run --rm $(BACKEND_SERVICE_NAME) bash -c './manage.py makemigrations'
test:
	docker compose -f docker-compose.yaml run --rm $(BACKEND_SERVICE_NAME) bash -c 'pytest'
