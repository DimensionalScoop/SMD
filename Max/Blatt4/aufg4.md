## Aufgabe 4
### a)

Trennung von Signal und Untergrund
:	etwa beim Ice Cube, um nur die zu beobachtenden Ereignisse herauszufiltern. Es trehten etwa atmospährische Myonen auf, die eine ähnlich Spur wie die zu messenden durch Neutrinos erzeugten Myonen besitzen.

Entfernen schlechter Messungen
:	wenn verschiedene Parameter einer Messung nicht zueinander passen muss der Datensatz als ungültig gekenzeichnet werden. Beispielsweise, wenn jemand in einer Umfrage als Alter 15 Jahre und als Beruf Ingenieur angibt.

Entfernung von unnötigen Datensätzen
:	teilweise befinden sich Felder in den Daten, die für manche Messungen unwichtig sind, z.B. kann beim Auslesen einer Datenübertragung von einer Wetterstation der mitgesendete Modellname verworfen werden, wenn du der Luftdruck interessant ist.

Glätten eines Signals
:	wenn ein Wert aus einem stark rauschendem Sensor ausgelesen werden soll sind einzelne Werte wenig aussagekräftig, es interessiert eher der Mittelwert innerhalb eines bestimmten Intervalls. Das kann z.B. durch Faltung des Messsignals mit einer entsprechenden Gauskurve geschehen.

Auswahl der qualitativ hochwertigsten Daten
:	um die Hardware nicht zu überfordern, etwa bei hoher Ereignisfrequenz (CERN), geringer Übertragungskapazität (Ice Cube Uplink) oder um die Rechenlast zu verringern.


### b)

Ja, etwa um Daten lesbarer oder Wahrscheinlichkeiten direkt ersichtlich zu machen.


### c)
 
- Ersetzten durch Mittelung der umgebenden Datenpunkte (à la blur) 
- Löschen der entsprechenden Datenzeile 


### d)

- Neue Datenstruktur muss Eigenheiten beider Datensätze berücksichtigen, etwa sollte das Abschneiden zusätzlicher Felder von Satz B beim Einfügen in Satz A vermieden werden, wenn diese Daten noch gebraucht werden.
