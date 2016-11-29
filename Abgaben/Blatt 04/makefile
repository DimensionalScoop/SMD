SHELL := /bin/bash

Abgabe.pdf:
	cat *.md > abgabe.md
	pandoc -f markdown "abgabe.md" -t latex -o "abgabe.pdf"  -V fontsize=12pt -V lang=de -V papersize:"a4paper" -V documentclass:"article" -H "pandoc-include.tex" 

Zip:
	ls -I "*.md" -I "*.zip" -I makefile -I "*.tex" | xargs tar --hard-dereference -cvhf Kollek_Alameddine_Pernklau.zip
