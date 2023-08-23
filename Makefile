.DELETE_ON_ERROR:

FIX = rgbfix
FIXFLAGS = -f gh

ROM = tetris.gb
HACK = hack.gb
SCRIPT = hack.py
PYTHON = python3

$(HACK): $(SCRIPT)
	$(PYTHON) $(SCRIPT)
	$(FIX) $(FIXFLAGS) $@

.PHONY:
clean:
	rm -rf $(HACK)
