#!/bin/bash

cd segments
wget -e robots=off -r --no-parent --reject="index.html*" -nH --cut-dirs=2 http://brouter.de/brouter/segments3/
