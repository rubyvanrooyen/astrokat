clean:
	rm -f scripts/*.csv
	rm -f scripts/*.pdf
	rm -f scripts/*.png

clobber: clean
	rm -f astrokat/*.pyc
	rm -f output/*

# -fin-

