#!/bin/bash

pandoc --template template.html -f docx -t html text/reproducing-autonomy.docx > reproducing-autonomy.html

# This makes the package needed for epub2html
# add folders: Fonts Styles
zip -r reproducing-autonomy.zip reproducing-autonomy.html Fonts Styles Images -x "*/\.DS_Store" "/\.*"

CURRENT_FOLDER=`pwd`

cd /Volumes/Switzerland/e/Projects/html2epub
make conversion IN_FILE=/Volumes/Switzerland/e/Projects/pipeline-tests/reproducing-autonomy.zip
mkdir -p output/reproducing-autonomy.zip/check-epub
cp -p output/reproducing-autonomy.zip/reproducing-autonomy.epub output/reproducing-autonomy.zip/check-epub/
unzip output/reproducing-autonomy.zip/check-epub/reproducing-autonomy.epub -d output/reproducing-autonomy.zip/check-epub


cd $CURRENT_FOLDER
