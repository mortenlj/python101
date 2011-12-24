
SRCS := $(wildcard *.py)
RESULTS := $(SRCS:.py=.out)

.PHONY: all clean
all : python101.html #python101.odp

clean :
	rm -f python101.html python101.odp ${RESULTS}

%.odp : %.rst
	"rst2odp.py" $< $@

%.html : %.rst
	"rst2s5.py" --theme-url ui/python101 $< $@

$(RESULTS) : %out: %py
	python $< > $@

python101.odp : python101.rst ${SRCS} ${RESULTS}

python101.html : python101.rst ${SRCS} ${RESULTS}
