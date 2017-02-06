---
title: "Abgabe Blatt 12"
author: "Jean-Marco Alameddine, Johannes Kollek, Max Pernklau"
date: "Monday, February 6, 2017"
output:
  pdf_document
fontsize: 12pt
header-includes: \usepackage{siunitx}
---

### a)
Baum durch Ausschlusskriterium ausgewählt.
    
    mode: test
    pseudo_data_fraction: 0.1

    source_file_moca: NeutrinoMC.root
    roottree_moca: Signal_MC_Akzeptanz

### b)
hohe Energien kommen deutlich seltener vor.

    branch_x: Energie log 
    limits_x: 0 2 #scheint schon in TeV zu sein

    number_bins: 8
    max_number_bins: 8

### c)
Willkürlich gebinned. `AnzahlHits` ist auch log-verteilt.

    branch_y: AnzahlHits log
    number_y_bins: 20 log #scheinbar muss man hier auch log-gen

    branch_y: x
    number_y_bins: 8

    branch_y: y
    number_y_bins: 8
    number_all_variables: 3

### d)

![](fig/correlation_x_Energie.pdf)
![](fig/correlation_y_Energie.pdf)
![](fig/correlation_AnzahlHits_Energie.pdf)

Geeignet sind alle Observablen, da sie eine Korrelation zur Energie aufweisen und untereinander kaum korreliert sind (Korrelationsplots zwischen den Observablen sind in guter Näherung konstante Funktionen). Indes bietet nur `AnzahlHits` eine monotone Korrelation, was eine Entfaltung leichter macht. Die anderen Observablen erlauben zwar in begrenzten Maße eine Vorhersage der Energie, lassen sich aber nicht durch unseren Begriff des Korrelationskoeffizient gebührend beschreibend. 

### e)

![](fig/Quality overview for 8 bins.pdf)
Der *L-Cruve* zu folge scheint 10 Knoten, 7 Freiheitsgrade oder 12 Knoten, 8 Freiheitsgrade der beste trade-off zu sein. *$\chi^2$ vs. parameter* bestätigt diese Wahl.

![10 Knoten, 7 Freiheitsgrade](fig/10-7.pdf)

![12 Knoten, 8 Freiheitsgrade](fig/12-8.pdf)

12 Knoten, 8 Freiheitsgrade scheint hier besser zu sein, da die Fehler marginal kleiner sind.

### f)
Die Normierungskonstante ergibt sich zu $(\gamma - 1) 10^5$.

    mc_func: pow(10,-2.7*x)*pow(10,5)*(2.7-1)