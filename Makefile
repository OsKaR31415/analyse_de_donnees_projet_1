
all: report

report.ipynb:  # update report.py to contents of 
	jupyter nbconvert --to python --no-prompt report.ipynb

report: report.ipynb
	touch report.py  # make shure this file exists
	quarto render report.qmd
	echo "\007"  # ring bell at end of rendering
