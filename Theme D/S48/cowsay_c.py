def cowsay(txt):
    print(
        f"""
 ________
< {txt} >
 --------
        \\   ^__^
         \\  (oo)\\_______
            (__)\\       )\\/ \\
                ||----w |
                ||     ||
"""
    )




import sys

# Affiche tous les paramètres passés au programme
for p in sys.argv:
    print(p)

"""
Si on lance :
> python cowsay.py abc toto pouet
...alors cette boucle affichera :
cowsay.py
abc
toto
pouet
"""

if len(sys.argv) > 1:
    cowsay(sys.argv[1])

