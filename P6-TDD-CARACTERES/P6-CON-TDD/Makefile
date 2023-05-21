.PHONY: setup server client test

setup:
	@python3 -m venv entorno
	@source entorno/bin/activate && pip install proctitle pytest

server:
	@source entorno/bin/activate && python3 servidor.py

client:
	@source entorno/bin/activate && python3 cliente.py $(file)

test:
	@source entorno/bin/activate && pytest
