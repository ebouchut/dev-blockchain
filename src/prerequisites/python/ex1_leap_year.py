#!/usr/bin/env python

# Une année est dite bissextile si c'est un multiple de 4,
# sauf si c'est un multiple de 100.
# Toutefois, elle est considérée comme bissextile si c'est un multiple de 400

annee = int( input("Annee ?"))

is_bissextile = ((annee % 4 == 0) and not (annee % 100 == 0)) or (annee % 400 == 0)
print(is_bissextile)



