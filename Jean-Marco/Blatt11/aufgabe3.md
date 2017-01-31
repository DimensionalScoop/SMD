
#Aufgabe 3

## a)

Die vorgebene Matirix beschreibt einen Messprozess, in dem die Zählraten in 20 verschiedene Ereignisse, bzw. Bins aufgeteilt weden können. Dabei ordnet der Detektor jedes Ereignis mit einer Wahrscheinlichkeit von je $\epsilon$ fälschicherweise einem direkt benachbarten Bin zu. Ansonten wird das Ereignis richtig zugeordnet, es gehen keine Zählraten gänzlich verloren.

## b)

Siehe Code

## c)

Mit
\begin{equation}
  A = U D U^{-1}
\end{equation}
folgt
\begin{align*}
  \vec{g} &= A \vec{f} \\
  \Leftrightarrow g &=  U D U^{-1} \vec{f} \\
  \Leftrightarrow \underbrace{U^{-1} \vec{g}}_{:= \vec{c}} &= D \underbrace{U^{-1} f}_{:= \vec{b}}.
\end{align*}
Vorteilhaft ist nun, dass jede Komponente von $\vec{b}$ nur noch an die dazugehörige Komponente von $\vec{c}$ koppelt, und diese lediglich über den jeweiligen Eigenwert zusammenhängen. Dies liegt natürlich an der Diagonalform der Matrix $D$.

## d)

Die Transformation in $b$ und $c$ findet mit den oben angegebenen Formeln statt.
Die Kovarianzmatrix von $f$ ergibt sich aufgrund der Poissionverteilung der unkorellierten Werte als Diagonalmatrix mit den jeweiligen Messwerten von $f$ als Diagonalelementen.
Die Transformation wird mit
\begin{equation}
  V[b] = U^{-1} V[f] U^{-1 \top}
\end{equation}
durchgeführt.
Für die entfalteten Koeffizienten, die sich aus
\begin{equation}
  b = \underbrace{D^{-1} U^{-1}}_{:=L} g
\end{equation}
errechnen lassen, ergeben sich die Standardabweichungen aus der Transformation der Kovarianzmatrix
\begin{equation}
  V[b^{mess}] = L V[g^{mess}] L^\top.
\end{equation}
Dabei besteht die Kovarianzmatrix von $g^{mess}$ wegen der Poissonverteilung wieder aus den Messwerten $g_{mess}$, die die Diagonalelemente darstellen.

Folgender Plot zeigt die Koeffizienten $b_j$ in Abhängigkeit vom Index $j$.
Man erkennt, dass die Koeffizienten ab einem bestimmten Index um die 1 herum oszillieren. Diese Oszillationen bringen jedoch keinen Mehrwert ehr, da sie keine Informationen enthalten.

![Aufgabe 3. Normierte Koeffizienten b.](plot3a.pdf)

Um dies zu verdeutlichen, sind in einem weiteren Plot die Werte von $b$ der "wahren" Verteilung sowie die Werte $b$ der von uns "verfälschten" Verteilung eingezeichnet. Es wird deutlich, dass die Oszillationen nur für die veränderten $b$ auftreten. Dies zeigt, dass numerische Schwankungen hier starke Abweichungen von den wahren Messwerten erzeugen.
![Aufgabe 3. Koeffizienten b der veränderten und der wahren Verteilung von g.](plot3b.pdf)

## e)

Zum Schluss wird über die Formel
\begin{equation}
  f_{mess} = U b_{mess}
\end{equation}
aus dem zuvor bestimmten $b$ die Entfaltung ermittelt. Um den Fehler einzuzeichnen, muss die Kovarianzmatrix von $b$ weiter in die Kovarianzmatrix von $f$ transformiert werden.
Im folgenden Plot sind die entfalteten Werte zusammen mit den wahren Werten von f abgetragen.
Es fällt auf, dass die Werte sehr stark um die wahre Verteilung oszillieren.
![Aufgabe 3. Nicht regularisierte Entfaltung.](plot3c.pdf)

Stattdessen kann ein "Cutoff" verwendet werden, bei dem jedes $b$ ab einem bestimmten Index 0 gesetzt wird. Es fällt auf, dass die Werte nun deutlich weniger stark oszillieren. Zwar ergeben sich vor allem für die ersten Bins nach wie vor stärkere Abweichungen, im Allgemeinen ist eine Besserung deutlich erkennbar. Dies macht sich auch in den kleineren Fehlern bemerkbar.
![Aufgabe 3. Regularisierte Entfaltung.](plot3d.pdf)
