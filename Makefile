PIP=pip3

#------------------------------------------------------------------------------#
##@ Prerequisites
#------------------------------------------------------------------------------#


DRIVER_DIR = $(PWD)/drivers
$(DRIVER_DIR):
	mkdir -p $(DRIVER_DIR)
export PATH := $(DRIVER_DIR):$(PATH)


# geckodriver
# https://github.com/mozilla/geckodriver
GECKODRIVER          = $(DRIVER_DIR)/geckodriver
GECKODRIVER_VERSION  = v0.34.0
GECKODRIVER_PLATFORM = linux64
GECKODRIVER_TGZ      = geckodriver-$(GECKODRIVER_VERSION)-$(GECKODRIVER_PLATFORM).tar.gz
GECKODRIVER_URL      = https://github.com/mozilla/geckodriver/releases/download/$(GECKODRIVER_VERSION)/geckodriver-$(GECKODRIVER_VERSION)-$(GECKODRIVER_PLATFORM).tar.gz
.PHONY: $(GECKODRIVER)
$(GECKODRIVER): $(DRIVER_DIR)
ifeq ($(wildcard $(GECKODRIVER)),)
	@echo "Downloading geckodriver"
	# https://github.com/mozilla/geckodriver/releases/download/v0.34.0/geckodriver-v0.34.0-linux64.tar.gz
	wget $(GECKODRIVER_URL) -O $(DRIVER_DIR)/$(GECKODRIVER_TGZ)
	tar -zxf $(DRIVER_DIR)/$(GECKODRIVER_TGZ) -C $(DRIVER_DIR)
	rm $(DRIVER_DIR)/$(GECKODRIVER_TGZ)
endif

# pip requirements
PIP_REQUIREMENTS = requirements.txt
.PHONY: $(PIP_REQUIREMENTS)
$(PIP_REQUIREMENTS):
ifneq ($(shell $(PIP) -vvv freeze -r $(PIP_REQUIREMENTS) 2>&1 | grep "not installed"), )
	@echo "Installing pip requirements"
	$(PIP) install -r $(PIP_REQUIREMENTS)
endif


PREREQUISITES = $(GECKODRIVER) \
				$(PIP_REQUIREMENTS)

## init develelopment env
init: $(PREREQUISITES)
	@echo "All prerequisites installed."


#------------------------------------------------------------------------------#
##@ Run
#------------------------------------------------------------------------------#


.PHONY: run
## run script
run: $(PREREQUISITES)
	python3 main.py


#------------------------------------------------------------------------------#
##@ Docker
#------------------------------------------------------------------------------#


DOCKER          = docker
DOCKER_REGISTRY = hub.docker.com
DOCKER_PROJECT  = gitsang/pt-auto-login
DOCKER_TAG      = $(shell git describe --tags --always --dirty)
DOCKER_IMAGE    = $(DOCKER_REGISTRY)/$(DOCKER_PROJECT):$(DOCKER_TAG)


DOCKERFILE=Dockerfile
.PHONY: docker
## build docker image
docker: $(PREREQUISITES)
	$(DOCKER) build --no-cache -t $(DOCKER_IMAGE) -f $(DOCKERFILE) .

.PHONY: push
## push docker image
push:
	$(DOCKER) push $(DOCKER_IMAGE)

.PHONY: docker-run
## run docker image
docker-run:
	$(DOCKER) run --rm -it $(DOCKER_IMAGE)


#------------------------------------------------------------------------------#
##@ Help
#------------------------------------------------------------------------------#


## display help
help:
	@awk 'BEGIN \
	{ \
		FS = ":.*##"; \
		printf "\nUsage:\n  make \033[36m<target>\033[0m\n" \
	} \
	/^[0-9a-zA-Z\_\-]+:/ \
	{ \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 2, RLENGTH); \
			printf "  \033[36m%-24s\033[0m %s\n", helpCommand,helpMessage; \
		} \
	} { lastLine = $$0 } \
	/^##@/ \
	{ \
		printf "\n\033[1m%s\033[0m\n", substr($$0, 5) \
	} ' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help
