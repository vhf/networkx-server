start: server.pid

server.pid:
	source ./venv/bin/activate && { python main.py & echo $$! > server.pid; }
	source ./venv/bin/activate && python test.py &

stop: server.pid
	pkill -TERM -P `cat $<` && rm $<

install: venv requirements

force-kill:
	rm server.pid
	pkill Python

requirements: requirements.txt
	source ./venv/bin/activate && \
	pip install --upgrade -r requirements.txt

venv:
	pyvenv venv

.PHONY: start stop install force-kill
