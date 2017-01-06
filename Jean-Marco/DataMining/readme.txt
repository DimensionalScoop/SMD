Zu Sehen sind meine heutigen Arbeiten zur DataMiningChallenge in Python mit
Sklearn. (alles was mit RapidMiner gemacht wurde ist noch nicht hochgeladen)
Enthalten ist das Verarbeiten der Ausgangsdaten (test00.py bearbeitet das
Trainingsdatenset, test02.py das Testdatenset).

 Beim Verarbeiten habe ich die
fehlenden Daten durch den Mittelwert der restlichen Daten ersetzt, sofern es
an der Stelle sinnvoll ist. 

Nicht-Numerische Daten (z.B. Qualität von etwas,
was meist in Kategorien wie Excellet, Poor, etc. eingeteilt ist) werden in
sogenannte Dummy-Variablen verarbeitet. Beispiel: 
OverallQual kann die Attribute Ex, Po, Gd, Fa, TA annehmen. Ein Ansatz wäre es
gewesen, jedem dieser Attribute einen Wert zuzuordnet, so dass bei einem Haus
mit OverallQual=Ex z.B. das Attribut den Wert OverallQual=5 annimmt, bei Gd=4,
usw. (das wäre das unique-integers prinzip).
Problem bei diesem Prinzip wäre es jedoch gewesen, dass man in vorhinein eine
Reihenfolge festlegt und vor allem, dass man eine Art von Wertigkeit festlegt.
Deshalb wird für jeden Möglichen Wert des Attributes ein neues Attribut
angelegt. Dies bedeutet, dass z.B. für das Haus mit OverallQual=Ex das
Attribut OverallQual_Ex den Wert 1 annimmt, die Attributes OverallQual_Po,
Overall_Qual_Gd, etc. den Wert 0. Dadurch erhalte ich zwar sehr viele
Attribute (am Ende 270), die sind dafür aber aussagekräftiger.

Sonderfall ist das Exterior: Es gab dort vorher zwei Attribute, die das
"Primäre" und das "Sekundäre" Material beschreiben. Diese habe ich zu einem
Matrial gebündelt.

Außerdem mussten manche Attribute mit Nullen ergänzt werden, da sie im
Traininsset vorhanden waren aber nicht im Testtest (oder anders herum).

In der test01.py werden die Voraufgaben auf dem Zettel gelöst.

In den folgenden testXX.py versuche ich auf verschiedene Weisen, Regressionen
durchzuführen. Meistens nehme ich die K Attribute mit der höchsten Kovarianz
zum SalePrice und mache damit dann irgendeine Regression.

Leider funktionieren die Regressionen hier ziemich schlecht, die Ergebnisse
sind zwar nicht miserabel, aber prozentual alle schlechter als bei Rapidminer.
(Bezüglich des Submission-Boards bei Kaggle: Die beste Rapid-Miner Submission
erzielt einen Wert von ca. 0.14 (ein neuronales Netzwerk), der kNN-Algorithmus
in Rapid-Miner erzielt noch 0.16. Der beste sklearn Algorithmus bleibt
trotzdem über 0.2)

Ich weiß jedoch nicht, ob mein Vorverarbeiten der Daten in sklearn so schlecht
ist, oder ob ich die Algorithmen schlecht angewendet habe. Das vorgehen mit
den Dummy-Variablen habe ich eigentlich weitestgehend auch in RapidMiner
angewendet.

Wer möchte kann also meine Vorarbeiten verwenden, jedoch mit Vorsicht, weil
ich wie gesagt nicht weiß woher die schlechte(ren) Ergebnisse kommen..

Greetz
