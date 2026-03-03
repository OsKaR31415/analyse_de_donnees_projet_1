
all: report report.ipynb

.PHONY: report.py

report.py:  # update report.py according to contents of report.ipynb
	jupyter nbconvert --to python --no-prompt report.ipynb

report: report.py
	quarto render report.qmd
	echo "\007"  # ring bell at end of rendering


