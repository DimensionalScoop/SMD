## Aufgabe 1

### a)
Alle Achsen des Raumes müssen normiert sein. Die Art der Normierung (etwa auf welchen Referenzwert normiert wird) verändert das Verhalten des Algorithmus stark: Wenn beispielsweise etwa alle Daten einer Dimension im Intervall [0,1] liegen und die einer anderen im Intervall [0,1000], dann wird die Klassenvorhersage unbekannter Vektoren viel stärker von letzterer Dimension beeinflusst.

### b)
Es gibt keinen dedizierten Lernschritt: Aus den Trainingsdaten werden keine Hilfsparameter berechnet, alle Berechnungen finden während der Klassifikation unbekannter Vektoren statt.  

Laufzeit Lernen: $\mathcal{O}(1)$ (event. $\mathcal{O}(n)$, wenn Trainingsdaten kopiert werden müssen): Die Daten müssen nur abgespeichert werden.  
Laufzeit Anwendung: $\mathcal{O}(\log{n})$ bis $\mathcal{O}(n)$, je nach Struktur der Trainingsdaten und verwendeter Datenstruktur zur Speicherung dieser. Wenn die Trainingsdaten etwa stark clustern kann die Rechengeschwindigkeit stark angehoben werden.

### d)
Reinheit: 0.811078717201
Effizienz: 0.9737  
Genauigkeit: 0.915633333333  
Signifikanz: 69.3108998162  

### e)
Der Algorithmus wird weniger empfindlich für große Werte des Attributs ($>1$) und empfindlicher für kleine Werte ($<1$). Durch diese Art von 'Normierung' verbessert sich die Zuordnung leicht:  

Reinheit: 0.856720827179
Effizienz: 0.986  
Genauigkeit: 0.940366666667  
Signifikanz: 66.447242481  

### f)
Die Einbeziehung von mehr Nachbarn verschlechtert das Ergebnis. Vermutlich ist die Wahrscheinlichkeit, viele Untergrundereignisse einzusammeln, am Rande des Signalclusters deutlich größer bei höherem k, einfach weil es mehr Untergrundereignisse als Signal gibt.  
Vielleicht gibt es am auch Rand des Signalclusters 'Finger', die in den Untergrund hineinreichen und durch ein größeres k nicht mehr erkannt werden.  

Reinheit: 0.800961219755
Effizienz: 0.9666  
Genauigkeit: 0.9088  
Signifikanz: 69.6746304858