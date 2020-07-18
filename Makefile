default: run

.DEFAULT_GOAL: run

run:
	node server.js

clean:
	rm -rf dist .cache build
