report: \
	slides/presentation.pfd

.PHONY: \
	all \
	clean \
	format \
	tests

define renderLatex
    cd $(<D) && pdflatex $(<F)
	cd $(<D) && bibtex $(subst .tex,,$(<F))
	cd $(<D) && pdflatex $(<F)
	cd $(<D) && pdflatex $(<F)
endef

define renderPresentation
    cd $(<D) && pdflatex $(<F)
endef

define lint
	pylint \
        --disable=missing-class-docstring \
        --disable=missing-function-docstring \
        --disable=missing-module-docstring \
		--function-naming-style=camelCase \
        ${1}
endef

slides/presentation.pfd: slides/presentation.pfd
	$(renderPresentation)

figures:
	mkdir --parents reports/tables
	mkdir --parents reports/figures
	python3 src/plotter.py

clean:
	rm --force --recursive reports/pythontex*
	rm --force reports/*.aux
	rm --force reports/*.bbl
	rm --force reports/*.blg
	rm --force reports/*.log
	rm --force reports/*.out
	rm --force reports/*.pdf
	rm --force reports/*.toc
	rm --force reports/*.pytxcode
	rm --recursive --force __pycache__
	rm --recursive --force .pytest_cache
	rm --recursive --force */__pycache__
	rm --recursive --force reports/figures/
	rm --recursive --force reports/tables/

format:
	black --line-length 100 src/*.py

linter:
	$(call lint, src)
	$(call lint, tests)

tests:
	pytest --verbose tests/