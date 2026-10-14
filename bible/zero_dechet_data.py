# -*- coding: utf-8 -*-
"""Zéro déchet ingrédient par ingrédient (Tome 12 §6 ; complète Tome 1 §13 et Tome 3 §17.4).
Pour chaque ingrédient du Tome 3 qu'on utilise rarement EN ENTIER :
  sold    : comment il s'achète en France (botte, pot, tube, boîte…)
  partial : motif (sur « quantité + libellé » de la ligne, sans accents, en minuscules) qui signale un usage partiel ;
            None = il reste TOUJOURS quelque chose (épluchures, carcasse, zeste, blanc d'œuf…)
  left    : liste de restes ; chaque reste = (partie, conservation sûre, [idées]) ;
            idée = (type, texte, id de recette ATLAS ou None). Types :
              « repas »  : entrée ou accompagnement du repas en cours ;
              « plat »   : un autre plat ou une autre recette ;
              « conserver » : comment le garder sans risque ;
              « hors »   : hors cuisine (compost, jardin, ménage).
Sécurité : durées prudentes (Tome 3 §17.2). Les recettes liées sont filtrées par le régime du foyer dans l'application."""

R, P, C, H = "repas", "plat", "conserver", "hors"
HERBES_IDEES = [(R, "Une sauce verte minute : herbes hachées, huile d'olive, citron, ail, sel", None),
                (P, "Taboulé ou salade d'herbes", "taboule_libanais"), (P, "Pesto (tiges comprises)", "pesto"),
                (P, "Sauce blanche aux herbes", "sauce_blanche"), (P, "Tiges dans un bouillon", "bouillon_legumes"),
                (C, "Hachées dans un bac à glaçons, couvertes d'huile d'olive : 3 mois au congélateur", None),
                (H, "Compost", None)]
# Herbes : même une botte entière laisse des tiges (on n'utilise souvent que les feuilles) → toujours proposé
HERBE = lambda: dict(sold="1 botte / 1 bouquet", partial=None,
                     left=[("reste de la botte et tiges", "Dans un verre d'eau au frigo, couvert d'un sac : 5 à 7 jours", HERBES_IDEES)])

LEFTOVERS = {
 # --------------------------------------------------------------- œufs
 "Jaune d'œuf": dict(sold="œufs à l'unité", partial=None, left=[
   ("blancs d'œufs", "2 jours au frigo dans un bocal fermé ; 3 mois au congélateur (noter le nombre)", [
     (R, "Un dessert léger pour finir le repas : meringues", "meringues"),
     (P, "Mousse au chocolat (avec les jaunes d'une autre recette)", "mousse_chocolat"),
     (P, "Omelette blanche aux herbes, ou dans une pâte à crêpes", None),
     (C, "Congelés en bac à glaçons : 1 cube = 1 blanc", None)]),
   ("coquilles", "—", [(H, "Compost, ou broyées au pied des plantes (calcium)", None)])]),
 "Blanc d'œuf": dict(sold="œufs à l'unité", partial=None, left=[
   ("jaunes d'œufs", "24 h au frigo, couverts d'un filet d'eau ; ne se congèlent pas bien seuls", [
     (R, "Une mayonnaise maison pour accompagner", "mayonnaise"),
     (P, "Crème dessert, riz au lait plus riche, ou dorure des pâtes", "riz_au_lait"),
     (P, "Carbonara (version cuite pour les enfants)", "spaghetti_carbonara")])]),
 "Œuf entier (frais)": dict(sold="boîte de 6 ou 12", partial=None, left=[
   ("coquilles", "—", [(H, "Compost, ou broyées au jardin", None)])]),
 # --------------------------------------------------------------- agrumes
 "Citron": dict(sold="à l'unité ou en filet", partial=None, left=[
   ("zeste et peau (citron pressé)", "Zeste : 3 mois au congélateur ; écorces : séchées en bocal", [
     (R, "Zeste râpé sur le plat ou dans la sauce, juste avant de servir", None),
     (P, "Gâteau au yaourt au citron", "gateau_yaourt"), (P, "Citronnade (zeste infusé)", "citronnade_menthe"),
     (C, "Zestes séchés ou sucre aromatisé (zestes + sucre en bocal)", None),
     (H, "Vinaigre ménager aux agrumes : écorces + vinaigre blanc, 2 semaines, filtrer", None)])]),
 "Citron vert": dict(sold="à l'unité", partial=None, left=[
   ("zeste et peau", "Zeste : 3 mois au congélateur", [
     (R, "Zeste sur le guacamole ou le riz", "guacamole"), (P, "Dans un jus de gingembre ou un bissap", "jus_gingembre"),
     (H, "Vinaigre ménager aux agrumes", None)])]),
 "Orange": dict(sold="à l'unité ou en filet", partial=None, left=[
   ("peau et zeste", "Zeste : 3 mois au congélateur", [
     (R, "Salade de carottes à l'orange en entrée", "salade_carottes_cumin"), (P, "Oranges à la cannelle", "oranges_cannelle"),
     (C, "Écorces confites ou séchées pour le thé", None), (H, "Écorces séchées : allume-feu naturel ; compost en petites quantités", None)])]),
 # --------------------------------------------------------------- herbes
 "Persil plat / frisé": HERBE(), "Coriandre fraîche": HERBE(), "Menthe": dict(HERBE(), left=[("reste de la botte et tiges",
   "Dans un verre d'eau au frigo : 5 jours", [(R, "Thé à la menthe pour finir le repas", "the_menthe"), (P, "Citronnade à la menthe", "citronnade_menthe"),
   (P, "Taboulé", "taboule_libanais"), (C, "Séchée à l'air, en bocal : 6 mois", None), (H, "Compost", None)])]),
 "Basilic": dict(HERBE(), left=[("reste du pot ou de la botte", "Le pot sur le rebord de la fenêtre, arrosé ; feuilles coupées : 3 jours", [
   (P, "Pesto", "pesto"), (P, "Sauce tomate (les tiges aussi)", "sauce_tomate"), (P, "Pizza margherita", "pizza_margherita"),
   (C, "Pesto congelé en bac à glaçons", None)])]),
 "Ciboulette": HERBE(), "Aneth": HERBE(), "Thym / romarin": dict(HERBE(), left=[("branches restantes", "Séchées à l'air : 1 an en bocal", [
   (P, "Focaccia au romarin", "focaccia"), (P, "Bouquet garni d'un bouillon", "bouillon_legumes"), (C, "Huile aromatisée : au frigo, 4 jours maximum (botulisme)", None)])]),
 # --------------------------------------------------------------- légumes
 "Oignon nouveau / cébette": dict(sold="1 botte", partial=r"½|1 |2 |3 |c\. a [sc]", left=[("reste de la botte et verts", "Frigo, bac à légumes : 5 jours", [
   (R, "Ciselés sur le plat au service", None), (P, "Riz cantonais", "riz_cantonais"), (P, "Accras", "accras_morue"),
   (C, "Bulbes replantés dans un verre d'eau : les verts repoussent", None)])]),
 "Poivron (rouge/jaune/vert)": dict(sold="à l'unité ou en lot de 3", partial=r"½|¼|lamelle", left=[("demi-poivron et pédoncule", "Frigo, filmé : 4 jours ; en lanières au congélateur : 6 mois", [
   (R, "Lanières crues en bâtonnets à l'apéritif avec un houmous", "houmous"), (P, "Chakchouka", "shakshuka"), (P, "Sauce andalouse (poivron grillé)", "sauce_andalouse"),
   (H, "Pédoncule et graines : compost", None)])]),
 "Chou blanc / rouge": dict(sold="entier", partial=r"¼|½|quartier|feuille", left=[("reste du chou", "Frigo, filmé : 1 semaine", [
   (R, "Salade de chou cru râpé, vinaigrette", "vinaigrette"), (P, "Dans un mafé ou une soupe", "mafe_poulet"), (P, "Riz sauté au chou", "riz_cantonais"),
   (C, "Lacto-fermenté (choucroute maison, technique Tome 1 §9)", None)])]),
 "Céleri-branche": dict(sold="pied entier", partial=r"branche|½|¼", left=[("branches et feuilles restantes", "Frigo, enveloppé d'un torchon humide : 1 semaine", [
   (P, "Chorba", "chorba"), (P, "Bouillon (feuilles comprises)", "bouillon_volaille"), (R, "Bâtonnets à croquer avec une sauce", "tzatziki")])]),
 "Carotte": dict(sold="au kilo ou en botte avec fanes", partial=None, left=[("épluchures et fanes", "Épluchures propres : sac au congélateur jusqu'au prochain bouillon", [
   (P, "Pesto de fanes", "pesto"), (P, "Bouillon d'épluchures", "bouillon_legumes"), (H, "Compost", None)])]),
 "Poireau": dict(sold="à l'unité ou en botte", partial=r"blanc|vert", left=[("vert de poireau", "Frigo : 5 jours ; congelé émincé : 6 mois", [
   (P, "Bouillon", "bouillon_volaille"), (R, "Émincé et fondu au beurre en accompagnement", None), (P, "Dans une quiche", "quiche_lorraine")])]),
 "Pomme de terre": dict(sold="filet de 1 à 5 kg", partial=None, left=[("épluchures", "À cuisiner le jour même (elles noircissent)", [
   (R, "Chips d'épluchures au four : huile, sel, 200 °C, 15 min, à l'apéritif", "frites_maison"), (H, "Compost", None)])]),
 "Potiron / citrouille": dict(sold="entier ou en tranche", partial=None, left=[("graines et reste de chair", "Chair crue en cubes : 3 mois au congélateur", [
   (R, "Graines grillées (huile, sel, 180 °C, 12 min) sur le plat ou à l'apéritif", "veloute_potiron"), (P, "Velouté", "veloute_potiron")])]),
 "Concombre": dict(sold="à l'unité", partial=r"½|¼|rondelle", left=[("demi-concombre", "Frigo, filmé : 3 jours", [
   (R, "Tzatziki en entrée", "tzatziki"), (P, "Eau infusée au concombre et à la menthe", None)])]),
 "Tomate": dict(sold="au kilo ou en grappe", partial=r"½|1 tomate", left=[("tomates trop mûres", "Frigo : 2 jours", [
   (P, "Sauce tomate", "sauce_tomate"), (P, "Chakchouka", "shakshuka"), (P, "Ketchup", "ketchup")])]),
 "Champignon de Paris": dict(sold="barquette de 250 à 500 g", partial=None, left=[("pieds", "Frigo : 2 jours ; congelés : 3 mois", [
   (P, "Bouillon (pieds et parures)", "bouillon_legumes"), (R, "Duxelles : pieds hachés revenus avec une échalote, sur des toasts", None)])]),
 "Gingembre frais": dict(sold="racine au poids", partial=r"morceau|cm|c\. a [sc]|rape", left=[("reste de la racine", "Au congélateur entier : se râpe sans décongeler, 6 mois", [
   (P, "Jus de gingembre", "jus_gingembre"), (P, "Mafé ou teriyaki", "poulet_teriyaki"), (C, "Infusion gingembre-citron", None)])]),
 "Ail": dict(sold="tête entière", partial=None, left=[("reste de la tête", "Au sec, à l'air : 1 mois", [
   (P, "Houmous, harissa, tzatziki", "houmous"), (C, "Gousses épluchées dans l'huile : au frigo, 4 jours maximum (botulisme)", None),
   (H, "Peaux : compost", None)])]),
 "Oignon jaune": dict(sold="filet de 1 à 2 kg", partial=None, left=[("peaux et extrémités", "Sac au congélateur avec les épluchures", [
   (P, "Bouillon (la peau colore en doré)", "bouillon_volaille"), (H, "Compost ; teinture naturelle (œufs de Pâques)", None)])]),
 "Avocat": dict(sold="à l'unité", partial=r"½", left=[("demi-avocat", "Avec le noyau, citron et film au contact : 1 jour au frigo", [
   (R, "Guacamole à l'apéritif", "guacamole")])]),
 "Mangue": dict(sold="à l'unité", partial=None, left=[("chair autour du noyau et peau", "Chair : 3 mois au congélateur", [
   (P, "Lassi (la chair raclée autour du noyau)", "lassi_mangue"), (H, "Peau et noyau : compost", None)])]),
 "Banane": dict(sold="régime", partial=None, left=[("bananes trop mûres", "Épluchées, au congélateur : 3 mois", [
   (P, "Banana bread", "banana_bread"), (P, "Pancakes à la banane", "pancakes"), (H, "Peaux : compost", None)])]),
 # --------------------------------------------------------------- épicerie
 "Concentré de tomate": dict(sold="tube, boîte de 70 ou 140 g", partial=r"c\. a [sc]|g", left=[("reste de la boîte", "Boîte ouverte : à transvaser, 5 jours au frigo ; ou cuillères congelées sur papier cuisson : 6 mois", [
   (P, "Sauce algérienne, ketchup, chili", "ketchup"), (C, "Congelé par cuillerées", None)])]),
 "Coulis / passata / tomates pelées": dict(sold="boîte de 400 g ou brique de 500 g", partial=r"^(?!.*(800|400 g|1 boite)).*", left=[("reste de la boîte", "Transvasé en boîte hermétique : 4 jours au frigo ; 6 mois au congélateur", [
   (P, "Sauce tomate pour des pâtes le lendemain", "sauce_tomate"), (P, "Chakchouka", "shakshuka")])]),
 "Crème fleurette (liquide)": dict(sold="brique de 20 cl ou 50 cl", partial=r"ml|cl|c\. a [sc]", left=[("fond de brique", "3 jours au frigo après ouverture", [
   (P, "Quiche (fond de crème + lait)", "quiche_lorraine"), (P, "Gratin dauphinois", "gratin_dauphinois"), (C, "Congelée en bac à glaçons pour les sauces : 3 mois", None)])]),
 "Crème fraîche": dict(sold="pot de 20 ou 40 cl", partial=r"ml|cl|c\. a [sc]", left=[("fond du pot", "5 jours au frigo après ouverture", [
   (P, "Quiche", "quiche_lorraine"), (R, "Une cuillère dans le velouté", "veloute_potiron")])]),
 "Yaourt nature": dict(sold="pot de 125 g ou de 500 g", partial=r"g|c\. a [sc]", left=[("reste du pot", "Date du pot, frigo", [
   (R, "Sauce blanche", "sauce_blanche"), (P, "Lassi", "lassi_mangue"), (P, "Gâteau au yaourt", "gateau_yaourt"), (P, "Naan", "naan")])]),
 "Yaourt grec": dict(sold="pot de 150 à 500 g", partial=r"g|c\. a [sc]", left=[("reste du pot", "Date du pot, frigo", [
   (R, "Tzatziki ou sauce blanche", "tzatziki"), (P, "Lassi", "lassi_mangue")])]),
 "Lait entier / demi-écrémé / écrémé": dict(sold="bouteille d'1 L", partial=r"ml|cl", left=[("reste de la bouteille", "3 jours au frigo après ouverture", [
   (P, "Riz au lait", "riz_au_lait"), (P, "Pain perdu", "pain_perdu"), (P, "Béchamel", "bechamel"), (P, "Pancakes", "pancakes")])]),
 "Pois chiches (secs / bocal)": dict(sold="bocal ou boîte de 400 g", partial=None, left=[("jus du bocal (aquafaba)", "3 jours au frigo ; 3 mois au congélateur", [
   (R, "Mayonnaise sans œuf", "mayonnaise"), (P, "Meringues véganes", "meringues")])]),
 "Parmesan / Parmigiano": dict(sold="morceau ou sachet râpé", partial=None, left=[("croûte", "Au congélateur dans un sac : 6 mois", [
   (P, "Croûte dans la sauce tomate, une soupe ou un bouillon (retirer avant de servir)", "sauce_tomate")])]),
 "Mozzarella / burrata": dict(sold="boule de 125 g", partial=r"g", left=[("petit-lait", "Le jour même", [
   (P, "Petit-lait à la place de l'eau dans la pâte à pizza ou à pain", "pate_pizza")])]),
 "Pâte feuilletée (prête)": dict(sold="rouleau", partial=None, left=[("chutes de pâte", "Frigo, filmées : 2 jours ; congelées : 2 mois", [
   (R, "Allumettes au fromage ou palmiers à l'apéritif", None)])]),
 "Pain rassis (réservé)": dict(sold="—", partial=None, left=[("croûtes et miettes", "Au sec en sac papier ; chapelure en bocal : 1 mois", [
   (P, "Chapelure maison (pain sec mixé)", None), (R, "Croûtons pour le velouté", "veloute_potiron")])]),
 "Riz long / basmati / thaï": dict(sold="paquet de 500 g à 1 kg", partial=None, left=[("riz cuit en trop", "⚠️ Refroidi en moins de 2 h, frigo, 24 h maximum ; réchauffé une seule fois", [
   (P, "Riz cantonais le lendemain", "riz_cantonais"), (P, "Riz au lait (avec du riz rond, de préférence)", "riz_au_lait")])]),
 "Pâtes sèches (spaghetti, penne…)": dict(sold="paquet de 500 g", partial=None, left=[("eau de cuisson", "À utiliser chaude, tout de suite", [
   (R, "Une louche pour lier la sauce (amidon)", None), (H, "Refroidie, sans sel : arrosage des plantes ; eau de vaisselle", None)])]),
 "Huile de tournesol / colza": dict(sold="bouteille d'1 L", partial=r"\bl\b|1,5 l|friture", left=[("huile de friture", "Filtrée, à l'abri de la lumière : 5 à 6 fritures si elle reste claire", [
   (C, "Filtrer refroidie au filtre à café", None), (H, "Jamais à l'évier : déchetterie (point de collecte des huiles)", None)])]),
 # --------------------------------------------------------------- viandes et poissons
 "Poulet entier": dict(sold="entier", partial=None, left=[("carcasse, peau, gras", "Carcasse : 2 jours au frigo ou 3 mois au congélateur", [
   (P, "Bouillon de volaille", "bouillon_volaille"), (P, "Restes de chair : riz cantonais", "riz_cantonais"), (R, "Gras du plat pour rôtir des pommes de terre", None)])]),
 "Cuisse / pilon de poulet": dict(sold="barquette", partial=None, left=[("os et peaux (si désossées)", "Congelés en sac : 3 mois", [
   (P, "Bouillon de volaille", "bouillon_volaille")])]),
 "Paleron": dict(sold="morceau", partial=None, left=[("parures", "Frigo : 24 h ; congelées : 3 mois", [
   (P, "Bouillon de bœuf ou farce", "bouillon_volaille")])]),
 "Crevettes (cuites/crues)": dict(sold="barquette", partial=None, left=[("têtes et carapaces", "Congelées : 3 mois", [
   (P, "Fumet ou bisque : revenues, mouillées d'eau, 20 min, filtrées", None), (H, "Compost (en petite quantité, enterrées)", None)])]),
 # --------------------------------------------------------------- alcools (cuisine)
 "Vin rouge": dict(sold="bouteille de 75 cl", partial=r"^(?!750 ml).*(ml|cl|verre)", left=[("reste de la bouteille", "Bouchée, au frigo : 3 à 5 jours pour la cuisine ; en glaçons : 3 mois", [
   (C, "Glaçons de vin pour les sauces (adultes)", None), (H, "Vinaigre maison avec une mère de vinaigre", None)])]),

 # --------------------------------------------------------------- boulangerie, infusions
 "Levure boulangère sèche": dict(sold="sachets de 5,5 g ou boîte de 100 g", partial=r"pincee|\b[0-9],?[0-9]? g|½", left=[("reste du sachet", "Sachet replié et pincé, au frigo : 1 mois ; boîte : date indiquée, au frigo après ouverture", [
   (P, "Une seconde fournée : pâte à pizza, naan, batbout", "pate_pizza"), (C, "Noter la date d'ouverture sur le sachet", None)])]),
 "Levure chimique": dict(sold="sachets de 11 g", partial=r"c\. a [sc]|pincee|½", left=[("reste du sachet", "Sachet fermé, au sec : 6 mois", [
   (P, "Pancakes ou gâteau au yaourt", "pancakes")])]),
 "Hibiscus séché (bissap)": dict(sold="sachet de 100 à 250 g", partial=None, left=[("fleurs déjà infusées", "Frigo : 2 jours", [
   (P, "Seconde infusion, plus légère", "bissap"), (P, "Confiture ou chutney d'hibiscus (fleurs mixées, sucre, citron)", None), (H, "Compost", None)])]),
 "Vanille (gousse)": dict(sold="tube de 1 à 3 gousses", partial=None, left=[("gousse grattée", "Rincée et séchée : 1 an", [
   (C, "Sucre vanillé maison : la gousse dans un bocal de sucre", None), (P, "Infusée dans le lait d'un riz au lait ou d'une crème", "riz_au_lait")])]),
}

def ideas_text():
    return sum(len(i) for v in LEFTOVERS.values() for _, _, i in v["left"])