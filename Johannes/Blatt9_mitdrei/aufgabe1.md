#Aufgabe 1
##a)

Die Likelihoodfunktion ergibt sich zu
\begin{align*}
  L = \prod_{n_i} \frac{\lambda^{n_i}}{n_i!}e^{-\lambda},
\end{align*}
wobei
\begin{align*}
  n_i = \{13,8,9\}
\end{align*}
annehmen kann. Aus der Likelihoodfunktion folgt schließlich
\begin{align*}
  -\ln (L) &= - \sum_{n_i} \ln \left( \frac{\lambda^{n_i}}{n_i!} e^{-\lambda} \right) \\
         &= 3\lambda - \ln \left( \frac{\lambda^{13}}{13!} \right) - \ln \left( \frac{\lambda^{8}}{8!} \right) - \ln \left( \frac{\lambda^{9}}{9!} \right) \\
         &= 3\lambda - 30\ln(\lambda) + \ln(13! \cdot 9! \cdot 8!)
\end{align*}
für die negative Log-Likelihoodfunktion, welche in der nächsten Abbildung geplottet wird.

![Negative Log-Likelihoodfunktion.](aufgabe1a.pdf)
\clearpage

##b)

Im Folgenden wird das Minimum der Funktion bestimmt.
\begin{align*}
  \frac{\partial(-\ln(L))}{\partial \lambda} = 3 - \frac{30}{\lambda} &\stackrel{!}{=} 0 \\
  \Rightarrow \lambda_{min} &= 10.
\end{align*}

##c)

Aus der Bedingung
\begin{align*}
  -\ln(\lambda_{min}) + a = -\ln(\lambda)
\end{align*}
folgt mit $\lambda_{min} = 10$
\begin{align*}
  3\lambda + 30(\ln(\lambda) - 1 -\ln(10)) -a = 0,
\end{align*}
wobei
\begin{align*}
  a = \left\{ \frac{1}{2}, 2 , \frac{9}{2} \right\}
\end{align*}
ist.
Die Nullstelle wird numerisch über das Newton-Verfahren mit Kenntnis der Ableitung der negativen Log-Likelihoodfunktion bestimmt, wobei jeweils rechts und links von $\lambda_{min}$ gestartet wird.
Daraus ergeben sich die Grenzen der Intervalle
\begin{align*}
  [7.162, 13.504] \text{ und } len = 6.342 &, \text{ für } a = \frac{1}{2};\\
  [4.932, 17.722] \text{ und } len = 12.79 &, \text{ für } a = 2;\\
  [3.245, 22.696] \text{ und } len = 19.451 &, \text{ für } a = \frac{9}{2}.
\end{align*}
Diese Intervalle sind ebenfalls im Plot eingezeichnet.
Diese Intervalle können Konfidenzintervalle bzgl. der Schätzung des Erwartungswertes $\lambda$ darstellen.
Liegt das tatsächliche $\lambda$ außerhalb dieses gewählten Bereiches kann die Schäzung verworfen werden.

\clearpage

##d)

Das zweite Taylorpolynom ergibt sich zu
\begin{align*}
  T_2(30,-\ln(L)) = 30 - 30\ln(30) + \frac{1}{60} (\lambda-30)^2 + \ln(13! \cdot 9! \cdot 8!).
\end{align*}
Diese Funktion ist in der nächsten Abbildung zu sehen.

![Negative Log-Likelihoodfunktion und Taylorpolynom.](aufgabe1d.pdf)

Die $\lambda$ werden auch hier numerisch bestimmt, wobei diese hier auch analytisch gewonnen werden können.
Die Intervalle lauten
\begin{align*}
  [8.174, 11.826] \text{ und } len = 3.651 &, \text{ für } a = \frac{1}{2};\\
  [6.349, 13.651] \text{ und } len = 7.303 &, \text{ für } a = 2;\\
  [4.523, 15.477] \text{ und } len = 10.954 &, \text{ für } a = \frac{9}{2}.
\end{align*}
Die relativen Abweichungen zum exakten Ergebnis lauten
\begin{align*}
  42.425 \: \% &, \text{ für } a = \frac{1}{2};\\
  42.901 \: \% &, \text{ für } a = 2;\\
  43.682 \: \% &, \text{ für } a = \frac{9}{2}.
\end{align*}
Diese Abweichungen sind sehr stark und somit ist das Taylorpolynom keine so gute Näherung an die analytisch kompliziertere negative Log-Likelihoodfunktion. Der Vorteil am Polynom ist, dass damit viel besser gerechnet werden kann und es gibt einem in diesem Beispiel kleineren Konfidenzbereich an, in dem sich der Mittelwert bewegen kann.
