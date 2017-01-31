---
title: "Abgabe Blatt 9"
author: "Jean-Marco Alameddine, Johannes Kollek, Max Pernklau"
date: "Tuesday, January 17, 2017"
output:
  pdf_document
fontsize: 12pt
header-includes: \usepackage{siunitx}
---
#Aufgabe 2

Die Aufgabe wurde handschiftlich bearbeitet.
Wo Rechenschritte fehlen, beispielsweise beim Berechnen vom Lösungsvektor, wird die Rechnung im Code in der Datei *aufg2.py* durchgeführt.
Diese enthält als Ausgabe ebenfalls die in der Aufgabenstellung gefragten Werte.

![Aufgabe 2 - Teil 1.](2-1.jpg)
<div style="page-break-after: always;"></div>
![Aufgabe 2 - Teil 2.](2-2.jpg)
<div style="page-break-after: always;"></div>
Zudem führt *auf2_test.py* den zuvor berechneten Fit durch, um zu Zeigen dass die Methode erfolgreich war.

![Aufgabe 2- Fit.](2d.pdf)

#Aufgabe 3

## a)

Zunächst werden die Daten mit der Methode der kleinsten Quadrate gefittet.
Der Lösungsvektor ergibt sich aus
\begin{equation}
  \hat{a} = ( A^\top A)^{-1} A^\top \vec{y}
\end{equation}

Die Koeffizienten lauten
\begin{align}
  a_0 &= \num{-6.74453269e-02} \\
  a_1 &= \num{6.09609041e-01} \\
  a_2 &= \num{-5.13748217e-01} \\
  a_3 &= \num{2.10566523e-01} \\
  a_4 &= \num{-4.52007756e-02} \\
  a_5 &= \num{4.78568054e-03} \\
  a_6 &= \num{-1.96288198e-04}
\end{align}

(*Anmerkung des Autorenteams*: Die Koeffizienten und alle folgenden Werte werden auch von der Konsole beim Ausführen von *aufg3.py* ausgeben. Im Zweifel sind die dort ausgegebenen Werte die richtigen, da Kopierfehler immer passieren können...)

![Aufgabe 3a - Fit.](3a.pdf)

## b)

Als nächstes wird eine Regularisierung genutzt.
Dabei wird der Parameter $\lambda$ varriert.

Der Schätzparameter ergibt sich zu
\begin{equation}
  \hat{a}^{reg} = (  A^\top A + \lambda (CA)^\top (CA) )^{-1} A^\top \vec{y}
\end{equation}
wobei C Teil einer Regularisierung mithilfe der zweiten numerischen Ableitung ist (siehe Skript, Seite 92, Kapitel Testen.)

(*Anmerkung des Autorenteams*: Uns ist nicht klar, wieso C so aussehen muss, um eine zweite Ableitung zu repräsentieren, bzw. ob C hier richtig angewendet wird. Eine Aufklärung in der Übungs wäre vorteilhaft!)

Die Koeffizienten für alle Lambdas werden durch die Konsole ausgegeben, als Beispiel seien die Koeffizienten für $\lambda = 0.1$ angegeben:

\begin{align}
  a_0 &= \num{5.27965856e-02} \\
  a_1 &= \num{2.59531149e-01} \\
  a_2 &= \num{-1.93231285e-01 } \\
  a_3 &= \num{ 7.69667246e-02} \\
  a_4 &= \num{-1.71628069e-02 } \\
  a_5 &= \num{1.90376483e-03} \\
  a_6 &= \num{-8.10349697e-05}
\end{align}

![Aufgabe 3b - Fit.](3b.pdf)

## c)

Zuletzt soll an einer größeren Datenmenge die gewichtete Methode zum Fitten genutzt weden.

Gefittet wird dabei jeweils an den Mittelwert der Messdaten zu jedem x, das Quadrat der Inverse vom Fehler des Mittelwertes wird dabei jeweils als Wichtungsparameter verwendet. (Ist das Qudarat hier richtig/nötig?)

Als Schätzer ergibt sich nun
\begin{equation}
  \hat{a} = ( A^\top  W A)^{-1} A^\top W \vec{y}
\end{equation}
wobei die Gewichtsmatrix W jeweils als Diagonalelemente die bereits angesprochenen Gewichte enthält.

Als Gewichte ergeben sich dabei:

\begin{align}
  a_0 &= \num{-1.11406947e-01} \\
  a_1 &= \num{7.63211082e-01} \\
  a_2 &= \num{-6.80006787e-01} \\
  a_3 &= \num{2.89399163e-01} \\
  a_4 &= \num{-6.33937799e-02 } \\
  a_5 &= \num{ 6.79277585e-03 } \\
  a_6 &= \num{-2.81013923e-04}
\end{align}

![Aufgabe 3c - Fit.](3c.pdf)
