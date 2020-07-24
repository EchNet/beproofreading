# Make commands for development
# 
# `make build` copies static files and generates HTML files.
# `make run` runs an express dev server, listening on port 3000.
# `make deploy` copies built files to s3.

PIP=pip
PYTHON=python
NPM=npm

default: deploy

requirements.txt: requirements.in
	$(PIP) install -r requirements.in
	echo "# GENERATED FROM requirements.in.  DO NOT EDIT DIRECTLY." > requirements.txt
	$(PIP) freeze >> requirements.txt

requirements.flag: requirements.txt
	$(PIP) install -r requirements.txt
	touch requirements.flag

build: requirements.flag clean
	$(PYTHON) ./build.py

deploy: build
	aws s3 --profile beproofreading cp --recursive deploy s3://beproofreading.com

package-lock.json: package.json
	$(NPM) install

run: package-lock.json
	node server.js

clean:
	rm -rf ./deploy
