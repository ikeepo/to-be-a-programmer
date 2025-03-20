g:
	bash gp.sh
deploy:
	mkdocs gh-deploy
serve:
	mkdocs serve
prec:
	pre-commit run
