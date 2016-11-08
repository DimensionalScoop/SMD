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
Die bedingten Wahrscheinlichkeiten sind in den Plots eingezeichnet.

![$f(x | y)$](fig/4f-1.pdf)

![$f(y | x)$](fig/4f-2.pdf)