
SRCS := $(wildcard code/*.py)
RESULTS := $(SRCS:.py=.out)

.PHONY: all clean
all : python101.html python101.odp

clean :
	rm -f python101.html python101.odp code/*.out

%.odp : %.rst
	"rst2odp.py" $< $@

%.html : %.rst
	"rst2s5.py" --current-slide --theme-url ui/python101 $< $@

$(RESULTS) : %out: %py
	python $< > $@

python101.odp : python101.rst ${SRCS} ${RESULTS} Makefile

python101.html : python101.rst ${SRCS} ${RESULTS} Makefile
