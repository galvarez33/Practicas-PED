
serv5_python:
	
	sudo zypper install python3-setproctitle
	python3 app2_python/serv5.py


cli5_python:
	python3 app2_python/cli5.py 


serv_5_ruby:
	@if [ -n "${SERVER_ADDRESS}" ]; then                             \
	  echo "Puerto del servidor: ${SERVER_ADDRESS}";                   \
	else                                                             \
	  echo "Puerto del servidor: 3333";     \
	fi;
	@ruby app_2_ruby/lib/servidor/main.rb

cli_5_ruby:
	@ruby app_2_ruby/lib/cliente/main.rb

all:
	@echo "Compilación y ejecución de la práctica"

clean:
	@echo "Limpiando..."
