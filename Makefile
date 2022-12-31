reports: \
	reports/probability_random_processes_and_inference.pdf

presentation: \
	slides/expectation_variance_covariance.pdf \
	slides/poisson_distribution.pdf \
	slides/binomial_distribution.pdf \
	slides/counting_techniques_slides.pdf

exam: \
	reports/exam.pdf

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

slides/counting_techniques_slides.pdf: slides/counting_techniques_slides.tex
	$(renderPresentation)

slides/binomial_distribution.pdf:	slides/binomial_distribution.tex
	$(renderPresentation)

slides/poisson_distribution.pdf:	slides/poisson_distribution.tex
	$(renderPresentation)

slides/expectation_variance_covariance.pdf:	slides/expectation_variance_covariance.tex
	$(renderPresentation)

reports/probability_random_processes_and_inference.pdf: reports/probability_random_processes_and_inference.tex
	$(renderLatex)

reports/counting_exercises.pdf: reports/counting_exercises.tex
	$(renderPresentation)

reports/exam.pdf: reports/exam.tex
	$(renderPresentation)

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
	rm --force slides/*.aux
	rm --force slides/*.log
	rm --force slides/*.nav
	rm --force slides/*.out
	rm --force slides/*.pdf
	rm --force slides/*.snm
	rm --force slides/*.toc
	rm --recursive --force __pycache__
	rm --recursive --force .pytest_cache
	rm --recursive --force */__pycache__
	rm --recursive --force reports/tables/
	rm --force *.aux
	rm --force *.bbl
	rm --force *.blg
	rm --force *.log
	rm --force *.out
	rm --force *.pdf

format:
	black --line-length 50 src/*.py

linter:
	$(call lint, src)
	$(call lint, tests)

tests:
	pytest --verbose tests/