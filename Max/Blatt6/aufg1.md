## Aufgabe 1

### a)
Alle Achsen des Raumes müssen normiert sein. Die Art der Normierung (etwa auf welchen Referenzwert normiert wird) verändert das Verhalten des Algorithmus stark: Wenn beispielsweise etwa alle Daten einer Dimension im Intervall [0,1] liegen und die einer anderen im Intervall [0,1000], dann wird die Klassenvorhersage unbekannter Vektoren viel stärker von letzterer Dimension beeinflusst.

### b)
Es gibt keinen dedizierten Lernschritt: Aus den Trainingsdaten werden keine Hilfsparameter berechnet, alle Berechnungen finden während der Klassifikation unbekannter Vektoren statt.  

Laufzeit Lernen: $\mathcal{O}(1)$ (event. $\mathcal{O}(n)$, wenn Trainingsdaten kopiert werden müssen): Die Daten müssen nur abgespeichert werden.  
Laufzeit Anwendung: $\mathcal{O}(\log{n})$ bis $\mathcal{O}(n)$, je nach Struktur der Trainingsdaten und verwendeter Datenstruktur zur Speicherung dieser. Wenn die Trainingsdaten etwa stark clustern kann die Rechengeschwindigkeit stark angehoben werden.
