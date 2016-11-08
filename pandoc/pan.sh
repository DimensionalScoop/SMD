
pandoc -f markdown "$1" -t latex -o "$2"  -V fontsize=12pt -V lang=de -V papersize:"a4paper" -V documentclass:"article" -H "pandoc-include.tex" $3

# -V fontfamily:"libertine"