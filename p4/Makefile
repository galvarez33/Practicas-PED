serv4:
	rm -rf /tmp/prueba
	sudo zypper install python3-setproctitle
	python3 app1_python/serv4.py

cli4_fichero:
	@python3 app1_python/cli4.py /etc/services
	
cli4_binario:
	@python3 app1_python/cli4.py /bin/bash

cli4_cerrar:
	python3 app1_python/cli4.py cerrar


serv_4_ruby:
	@if [ -n "${SERVER_ADDRESS}" ]; then                             \
	  echo "Ruta del servidor: ${SERVER_ADDRESS}";                   \
	else                                                             \
	  echo "Ruta del servidor: /tmp/app_1_sockets_unix_ped6_rb";     \
	fi;
	@ruby app_1_ruby/lib/servidor/main.rb

cli_4_ruby:
	@ruby app_1_ruby/lib/cliente/main.rb

all:
	@echo "Compilación y ejecución de la práctica"

clean:
	@echo "Limpiando..."
