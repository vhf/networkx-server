start: server.pid

server.pid:
	source ./venv/bin/activate && { python main.py & echo $$! > server.pid; }
	python test.py

stop: server.pid
	pkill -TERM -P `cat $<` && rm $<

.PHONY: start stop
