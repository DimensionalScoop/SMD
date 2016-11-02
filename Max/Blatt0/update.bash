inotifywait -q -m -e close_write text.md |
while read -r filename event; do
	echo "AHHHHH"
	pan text.md text.pdf# or "./$filename"
done
