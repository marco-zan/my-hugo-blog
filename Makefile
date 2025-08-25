

enter-container:
	docker run -it --rm --user 1000:1000 --network=host \
		-v ${PWD}/.docker-bash-history:/home/hugo/.bash_history \
		-v ${PWD}:/src \
		docker.io/hugomods/hugo:debian-dart-sass-non-root \
		bash
