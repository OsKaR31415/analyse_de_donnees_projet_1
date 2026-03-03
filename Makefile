
all: report


report:
	touch report.py  # make shure this file exists
	quarto render report.qmd
