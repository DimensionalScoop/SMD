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
