DOCKER_DEST = archlinux-repository
DOCKER_PACKAGES = python git

docker-build:
	docker build -t $(DOCKER_DEST) .

build:
	yes | pacman -Syu
	yes | pacman -S $(DOCKER_PACKAGES)
	useradd -u "1000" -s /bin/bash -d "/home/builder" -G wheel "builder"
	echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

run:
	docker run -e REPO_NAME="build" -v "$PWD":/repository/builder $(DOCKER_DEST)

bootstrap:
	python bootstrap.py

prepare-ssh:
	eval "$(ssh-agent -s)"
	chmod 600 ./deploy_key
	ssh-add ./deploy_key

.PHONY: docker-build prepare-ssh build bootstrap
