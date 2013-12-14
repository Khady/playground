#!/bin/bash

usage () {
  echo "gimmeh a path dumb fuck"
}

header=$HOME/bin/pastes/header.html
footer=$HOME/bin/pastes/footer.html

if [ $# -ne 1 ] || [ ! -f "$1" ]; then
  usage
else
  filename=$(basename "$1")
  filename1=$(mktemp -t "$filename")
  filename2=$(mktemp -t "$filename")
  dst="$filename".html
  chmod +r "$filename1"
  chmod +r "$filename2"
  pygmentize -f html -O linenos,encoding=utf8 -o "$filename1" "$1"
  cat $header "$filename1" $footer > "$filename2"
  scp "$filename2" khady@halva.khady.info:public_html/pastes/"$dst" > /dev/null
  scp "$1" khady@halva.khady.info:public_html/pastes/"$filename" > /dev/null
  rm "$filename1"
  rm "$filename2"
  echo "http://halva.khady.info/~khady/pastes/$dst"
fi
