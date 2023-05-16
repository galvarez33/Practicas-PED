ruby:
	@echo "Configure el fichero a leer en la variable de entorno FICHERO_CLIENTE"
	@echo "Fichero actual: ${FICHERO_CLIENTE}"
	ruby app_1_ruby/lib/main.rb

test:
	cd app_1_ruby && rspec || echo "Error: es necesario instalar rspec para ejecutar los tests (gem install rspec)"

all:
	@echo "Compilación y ejecución de la práctica"

clean:
	@echo "Limpiando..."
