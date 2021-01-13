#!/bin/bash -e
WHERE="$(dirname "$0")"
INPUT="$1"
OUTPUT="$(basename "$1" .md).html"
pandoc -H $WHERE/pandocH.html -B $WHERE/pandocB.html -A $WHERE/pandocA.html -s "$INPUT" --katex -o "$OUTPUT"
