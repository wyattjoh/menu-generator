menu.pdf: menu.tex
	@echo "==> Compiling pdf..."
	@xelatex menu.tex

menu.tex: menu.jinja.tex menu.py menu.yaml
	@echo "==> Creating latex file..."
	@./venv/bin/python menu.py

watch:
	@echo "==> Watching for file changes..."
	@wr --exec "make" menu.yaml menu.py menu.jinja.tex Makefile

all: menu.pdf
