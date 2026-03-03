
all: report

report:
	touch report.py
	quarto render report.qmd
