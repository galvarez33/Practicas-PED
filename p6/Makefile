serv6:
	@sudo zypper install python3-setproctitle
	@python3 app1_python/serv6.py

cli6_binario:
	@python3 app1_python/cli6.py /bin/bash

cli6_fichero:
	@python3 app1_python/cli6.py /etc/services

cli6_cerrar:
	python3 app1_python/cli6.py cerrar

serv_6_ruby:
	@if [ -n "${SERVER_PORT}" ]; then                                \
	  echo "Puerto del servidor: ${SERVER_PORT}";                      \
	else                                                             \
	  echo "Puerto del servidor: 3333";     \
	fi;
	@ruby app_1_ruby/lib/servidor/main.rb

cli_6_ruby:
	@ruby app_1_ruby/lib/cliente/main.rb

all:
	@echo "Compilación y ejecución de la práctica"

clean:
	@echo "Limpiando..."
