app1serv:
	python3 serv4app1.py
app1cli:
	python3 cli4app1.py
app2serv:
	python3 serv4app2.py
app2cli:
	python3 cli4app2.py
debug1serv:
	strace -f python3 serv4app1.py
debug1cli:
	strace -f python3 cli4app1.py
debug2serv:
	strace -f python3 serv4app2.py
debug2cli:
	strace -f python3 cli4app2.py
app1clibucle:
	while True; do python3 cli4app1.py
app2clibucle:
	while True; do python3 cli4app2.py
