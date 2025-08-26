
build:
	python3 ./copy-notes.py 
	hugo -s reymerk-blog/

enter-container:
	docker run -it --rm --user 1000:1000 --network=host \
		-v ${PWD}/.docker-bash-history:/home/hugo/.bash_history \
		-v ${PWD}:/src \
		docker.io/hugomods/hugo:debian-dart-sass-non-root \
		bash


publish:
	@echo "Going to publish:"
	@git diff-index --name-only @ -- "BlogArticles/journals/*.md"
	@echo "Press [Enter] to continue or Ctrl-C to abort"
	@read
	git add BlogArticles/journals/*.md
	git commit -m "Updated articles"
	@echo "Press [Enter] to continue or Ctrl-C to abort"
	@read
	git push
