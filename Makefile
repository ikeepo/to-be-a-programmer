g:
	bash gp.sh
deploy:
	mkdocs gh-deploy
serve:
	mkdocs serve
prec:
	git add . -A
	pre-commit run
