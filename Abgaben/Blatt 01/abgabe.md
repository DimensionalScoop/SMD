# Blatt 1
Gruppe *import antigravity*.  
Jean-Marco Alameddine, Johannes Kollek, Max Pernklau

## Aufgabe 1

Die Normierungskonsante ergibt sich aus der Formel
\begin{equation}
  \int_{0}^{\infty} f(v) \, \mathrm{d}v \stackrel{!}{=} 1
\end{equation}
zu
\begin{align*}
  N = 1.
\end{align*}
Diese und alle folgenden Rechnungen sind ausführlich handschriftlich beigefügt.

### a)
Die wahrscheinlichste Geschwindigkeit ergibt sich als Maximum der Wahrscheinlichkeitsdichte
\begin{align*}
  \frac{\mathrm{d}}{\mathrm{d}v}f(v) \stackrel{!}{=} 0
\end{align*}
zu
\begin{align*}
  v_m = \sqrt{\frac{2 k_B T}{m}}.
\end{align*}
(Rechnung handschriftlich)

### b)
Der Mittelwert der Geschwindigkeit ergibt sich aus
\begin{align*}
    \int_{0}^{\infty} f(v) v \, \mathrm{d}v
\end{align*}
zu
\begin{align*}
  \bigl<v\bigr> = \frac{2}{\sqrt{\pi}}v_m.
\end{align*}
### c)
Das zu bestimmende Integral
\begin{equation}
  \int_{0}^{x_{0.5}} f(v) \, \mathrm{d}v \stackrel{!}{=} 0.5
\end{equation}
lässt sich durch passende Substitution (siehe Handrechnung) auf die Form
\begin{equation}
  \int_{0}^{\frac{x_{0.5}}{v_m}} \exp(-u^2) u^2 \, \mathrm{d}u \stackrel{!}{=} \frac{\sqrt{\pi}}{8}
\end{equation}
bringen.
Dieses Problem lässt sich wegen der fehlenden Stammfunktion lediglich numerisch lösen.
Mittels summierter Simpsonregel wird die Funktion von 0 bis zu einem Wert $a$ integriert. Mittels Bisektionsverfahren wird die obere Grenze a nun solange variiert, bis das Integral den gewünschten Wert erreicht. Wegen dem positiven Integranden ist das Verfahren ohne Probleme anwendbar. Hieraus ergibt sich die passende obere Grenze, aus dem sich der Median direkt ergibt:
\begin{align*}
  v_{0.5} \approx 1.087652 v_m
\end{align*}

### d)
Für die Bestimmung der vollen Breite auf halber Höhe wird zunächst der Funktionswert am Maximum bestimmt und dieser Wert halbiert.
Daraufhin wird die Funktion untersucht, wo diese den Wert annimmt.
Aus dieser Rechnung ergibt sich eine Gleichung, die sich nur numerisch berechnen lässt.
Beispielsweise mit dem Newtonverfahren können die Nullstellen bestimmt werden.
Unter Nutzung der Internetsuchmaschine *Wolfram Alpha* ergibt sich unter Nutzung der Differenz der beiden errechneten Funktionswerte
\begin{align*}
  v_{\text{FWHM}} \approx 1.155 v_m
\end{align*}

### c)
Zur Bestimmung der Standardabweichung der Geschwindigkeit wird die Formel
\begin{align*}
  \sigma_v = \sqrt{\bigl< v^2 \bigr> - \bigl< v \bigr>^2}
\end{align*}
verwendet.
Unter Verwendung von
\begin{align*}
    \bigl< v^2 \bigr> = \int_{0}^{\infty} f(v) v^2 \, \mathrm{d}v
\end{align*}
ergibt sich eine Standardabweichung von
\begin{align*}
  \sigma_v = v_m \sqrt{\frac{3}{2} - \frac{4}{\pi}}
\end{align*}


## Aufgabe 2
###a)
![Histogramme in Abhängigkeit der Bins (Gewicht)](fig/2a_gew.pdf)

In der obigen Abbildung sind Histogramme resultierend aus den Daten der *Groesse_Gewicht.txt* in Abhängigkeit der Bins abgebildet. Erkennbar ist, dass für eine große Binbreite die Werte sehr grob dargestellt werden. Dies ist vorallem im ersten Plot zu sehen, der nicht eindeutig einem Trend einer Verteilungsfunktion zugeordnet werden kann. Bei zu kleiner Binbreite (letzer Plot) werden die Daten zu genau dargestellt; Die individuellen Ausreisser, welche bei einer Messanzahl von nur 250 unvermeidbar sind (keine aussagekräftige Anzahl), machen sich zu stark bemerkbar. Dies ist nicht zuletzt an den zwei bis mehreren Peaks zu erkennen. Das selbe Argument trifft auf die "Löcher" zu, da diese Löcher in der Realität nicht festgestellt werden können: Es ist sinnlos, dass es keine Menschen gäbe, die ein bestimmtes Gewicht haben, aber es Menschen gibt, deren Gewicht um jenes liegt.  

Am besten bietet sich hier ein Mittelweg an, sprich Plot 3 oder 4. Zusätzlich kann hier noch die *Regel von Scott* hinzugezogen werden,
\begin{align*}
 h = \frac{3.49 \cdot \sigma}{\sqrt[3]{n}},
\end{align*}
wobei $h$ der Binbreite entspricht. Für das Gewicht ergibt die Formel ca. 16 Bins, was Plot 3 entspricht.

![Histogramme in Abhängigkeit der Bins (Größe)](fig/2a_groesse.pdf)

Die gleichen Argumente treffen auf die Größe zu, wobei der zweite Plot das Auge am meisten anspricht, da das Histogramm relativ gleichverteilt aussieht. Die Regel von Scott ergibt eine Binzahl von 9.5, was dieser Wahl bepflichtet.

###b)

Generell ist es immer sinnvoll möglichst viele Daten zu verwenden, da sich die Verteilung dementsprechend immer mehr der realen annähert. Ist die Anzahl der möglichen Messergebnisse bzw das Interval, auf dem sich diese verteilen, sehr groß, ist es auch besser mehr Messdaten einzuholen, da es sonst zu diesen "Löchern" aus Aufgabenteil a) kommt. Folglich können bei weniger möglichen Ergebnissen weniger Bins verwendet werden und andersherum.

Die Anzahl der Bins muss auf jeden Fall kleiner sein als die Anzahl der Messwerte. Diese Frage ist jedoch situationsabhängig. Angenommen es gäbe ein Problem mit vielen möglichen Ergebnissen, die jedoch einen scharfen Häufungspunkt in der Verteilung besitzen. Dann ist es auch bei wenigen Ergebnissen sinnvoll eine kleine Binbreite (bzw. viele Bins) zu verwenden.
Daher auch das Zitat *"There is no right or wrong answer as to how wide a bin should be"*.

###c)
![Histogramme in Abhängigkeit der Bins (Größe)](fig/2c.pdf)

Bei den hier angegebenen Histogrammen fällt bei einer hohen Binzahl auf, dass bestimmte Binbereiche nicht bestetzt sind, obwohl die danebenliegenden Bins noch stark besetzt sind. Dies liegt daran, dass lediglich ganze Zahlen von 1 bis 100 gewürfelt werden. Bereits im dritten Plot ergibt sich somit eine Lücke zwischen 0.3 und 0.6, da keine logarithmierte ganze Zahl in diesem Bereich liegt. Eine Vergrößerung der Binanzahl macht also, zumindest im linken Bereich des Histogrammes, keinen Sinn mehr. Zudem fällt auf, dass das Histogram im rechten Bereich mehr Werte aufweist. Dies liegt daran, dass der Logaritmus für große Werte langsamer ansteigt, so dass viele große Zahlen auf ein kleineres Intervall projeziert werden.


## Aufgabe 4

### a)
\begin{align}
    \rho = \frac{\text{Cov}(x,y)}{\sigma_1 \sigma_2} = 0.8
\end{align}

### b,c,d)
![Kontur-Plot der normierten 2D-Normalverteilung. In Magenta ist die unkorrelierte Standardabweichung aufgetragen.](fig/4c.pdf)

siehe Anhang für Rechnung der *b)*.  
Die Rotationsmatrix lautet
$$
M = 
\bordermatrix{
  & \cr
  & \cos{\theta} & -\sin{\theta}\cr
  & \sin{\theta} & \cos{\theta} \cr
}
$$
mit $\theta = 20^o$.

Die neuen Standardabweichungen sind
\begin{align}
    \sigma_{x^,} &= 3.71 \\
    \sigma_{y^,} &= 0.849
\end{align}
.


### e)
Die Ellipsen bilden natürlich den oben stehenden Winkel $\theta$. Die Hauptachsen von der alten und der neuen Ellipse sind jeweils gleich lang (Drehungen sind unitär), nämlich $\sigma_{x^,} /2 = 1.86$ und $\sigma_{y^,} /2 = 0.424$.

![Beide Ellipsen im Vergleich.](fig/4e.pdf)

### f)
Die bedingten Wahrscheinlichkeiten sind in den Plots eingezeichnet und auf der Tafelphotographie berechnet.

![$f(x | y)$](fig/4f-1.pdf)

![$f(y | x)$](fig/4f-2.pdf)




\begin{figure}[p]
    \vspace*{-2cm}
    \makebox[\linewidth]{
        \includegraphics[width=1.3\linewidth]{anhang/6.jpg}
    }
    \caption{Aufgabe 3}
\end{figure}

\begin{figure}[p]
    \vspace*{-2cm}
    \makebox[\linewidth]{
        \includegraphics[width=1.3\linewidth]{anhang/1.jpg}
    }
\end{figure}

\begin{figure}[p]
    \vspace*{-2cm}
    \makebox[\linewidth]{
        \includegraphics[width=1.3\linewidth]{anhang/2.jpg}
    }
\end{figure}

\begin{figure}[p]
    \vspace*{-2cm}
    \makebox[\linewidth]{
        \includegraphics[width=1.3\linewidth]{anhang/3.jpg}
    }
\end{figure}

\begin{figure}[p]
    \vspace*{-2cm}
    \makebox[\linewidth]{
        \includegraphics[width=1.3\linewidth]{anhang/4.jpg}
    }
\end{figure}

\begin{figure}[p]
    \vspace*{-2cm}
    \makebox[\linewidth]{
        \includegraphics[width=1.3\linewidth]{anhang/5.jpg}
    }
\end{figure}

\begin{figure}[p]
    \vspace*{-2cm}
    \makebox[\linewidth]{
        \includegraphics[width=1.3\linewidth]{anhang/7.jpg}
    }
\end{figure}