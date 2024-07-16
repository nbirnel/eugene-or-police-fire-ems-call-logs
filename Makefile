DIRS := epd fire-ems spd
ZIPS := $(addsuffix .zip,$(DIRS))


help:
	@sed -n 's/\(^[-a-zA-Z_]\+\):.*/make \1/p' Makefile

venv:
	python3 -m venv venv

clean:
	rm -rfv venv __pycache__

clean-dist:
	rm -rfv $(ZIPS)

%.zip: %
	zip -r $@ $<

dist: $(ZIPS)
