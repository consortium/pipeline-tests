#!/bin/bash

# convert various docx files to one html file using pandoc

[ -f test.html ] && rm test.html

touch test.html

# write html header
echo '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
  <meta http-equiv="Content-Style-Type" content="text/css" />
  <meta name="generator" content="pandoc" />
  <title></title>
  <style type="text/css">code{white-space: pre;}</style>
</head>
<body>
' >> test.html

# write html fragment for each *.docx
for f in 0*
do
  echo "Processing $f file.."
  pandoc $f >> test.html
done

# write footer
echo '</body>
</html>
' >> test.html
