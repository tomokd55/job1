def verif_type_saison(type, saison):
    if type=="fruits" and saison =="hiver":
        print("orange, mandarine, kiwi")
    if type=="fruits" and saison =="ete":
        print("poire, fraise, cassis")
    if type=="legumes" and saison =="hiver":
        print("carotte, topinambour, endive")
    if type=="legumes" and saison =="ete":
        print("artichaut, aubergine, navet") 

verif_type_saison("fruits", "hiver")
verif_type_saison("fruits", "ete")
verif_type_saison("legumes", "hiver")
verif_type_saison("legumes", "ete")