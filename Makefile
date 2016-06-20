start: server.pid

server.pid:
	source ./venv/bin/activate && { python main.py & echo $$! > server.pid; }
	make test

stop: server.pid
	pkill -TERM -P `cat $<` && rm $<

test:
	source ./venv/bin/activate && python test.py

install: venv requirements

force-kill:
	rm server.pid
	pkill Python

requirements: requirements.txt
	source ./venv/bin/activate && \
	pip install --upgrade -r requirements.txt

venv:
	pyvenv venv

.PHONY: start stop install force-kill test
