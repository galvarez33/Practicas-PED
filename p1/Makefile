ruby:
	@echo "Ejecutando Kata en Ruby..."
	cd kata_ruby && rspec

build_python_env:
	cd kata_python 							\
	&& python3 -m venv .env 				\
	&& . .env/bin/activate				\
	&& pip install -r librerias.txt

python: build_python_env
	@echo "Ejecutando Kata en Python..."
	cd kata_python 							\
	&& . .env/bin/activate				\
	&& pytest test_kata.py

all: ruby python
	@echo "Completado"

clean_python_env:
	@echo "Limpiando entorno virtual python..."
	rm -rf kata_python/.env

clean: clean_python_env
	@echo "Completado"
