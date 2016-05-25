#!/bin/bash

# convert various docx files to one html file using pandoc

[ -f reproducing-autonomy.html ] && rm reproducing-autonomy.html

touch reproducing-autonomy.html

# write html header
echo '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta http-equiv="Content-Style-Type" content="text/css" />
  <meta name="generator" content="pandoc" />
  <title></title>
  <style type="text/css">code{white-space: pre;}</style>
  <link href="Styles/internal-1.css" rel="stylesheet" type="text/css"/>
</head>
<body>
' >> reproducing-autonomy.html

# write html fragment for each *.docx
for f in text/0*
do
  echo "Processing $f file.."
  pandoc $f >> reproducing-autonomy.html
done

# write footer
echo '</body>
</html>
' >> reproducing-autonomy.html

# This makes the package needed for epub2html
# add folders: Fonts Styles
zip -r reproducing-autonomy.zip reproducing-autonomy.html Fonts Styles -x "*/\.DS_Store" "/\.*"
