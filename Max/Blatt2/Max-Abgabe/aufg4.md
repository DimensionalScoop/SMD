## Aufgabe 4

Im Scatterplot ist deutlich die Korrelation der beiden Normalverteilungen zu sehen. Es wurden 10000 Wertepaare generiert.

Die Abweichung schwanken zufällig, da die nicht besonders viele Wertpaare generiert wurden. Der grobe Kurvenverlauf bleibt aber ähnlich, die Anzahl der Peaks und ihre Position verändern sich jedoch. 


  x  Analytical Nom  Analytical Std  Monte Carlo Nom  Monte Carlo Std  
---- --------------  --------------  ---------------  ---------------  
 3.0            4.0         0.45607         3.996402         0.456447    
 0.0            1.0             0.2          1.00488         0.198824    
-3.0           -2.0        0.769415        -1.986642         0.76789   

: Ausgesuchte Werte der Simulation und Analytik.



  x  Relative Difference Nom  Relative Difference Std 
---- -----------------------  -----------------------
 3.0  0.0009                    0.000827   
 0.0  0.00488                   0.005882  
-3.0 -0.006679                 0.001983 

: Vergleich der Abweichungen Abweichungen


![Scatterplot der Parameter $a_0$ und $a_1$](fig/4b-a.pdf)

![Betrag der relativen Abweichung der analytischen von den simulierten Werte.](fig/4b-diff.pdf)