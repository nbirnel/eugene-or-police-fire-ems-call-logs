DIRS := epd fire-ems spd
CSVS := $(addsuffix .csv,$(DIRS))

M_ZIPS := $(addsuffix .zip,$(DIRS))
S_ZIPS := $(addsuffix .csv.zip,$(DIRS))

DIST_M_ZIPS = $(addprefix dist/,$(M_ZIPS))
DIST_S_ZIPS = $(addprefix dist/,$(S_ZIPS))

help:    ## Print this help
	@sed -n 's/\(^[-a-zA-Z_]\+\):.*/make \1/p' Makefile

venv:
	python3 -m venv venv

clean:
	rm -rfv venv __pycache__

clean-dist:
	rm -rfv $(ZIPS)

clean-all: clean clean-dist
	rm -rfv *.zip *.csv

dist/%.zip: %
	zip -r $@ $<

%.csv: %
	./tools/collate-csv.sh $<

dist: $(DIST_M_ZIPS) $(DIST_S_ZIPS)
