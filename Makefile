
all: report


report:
	touch report.py  # make shure this file exists
	quarto render report.qmd
	echo "\007"  # ring bell at end of rendering
