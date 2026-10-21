# -*- coding: utf-8 -*-
"""Vague 5 · Audit gourmet (21/10/2026), recommandation 2 : les grands classiques réécrits au niveau des fiches étalons du
Tome 11. Chaque étape de cuisson porte une durée et un repère des sens, le sel est placé au bon moment, chaque fiche a ses
astuces et son accompagnement. Les recettes d'origine gardent leur alcool et leur porc, avec la variante « à tester » (D21).
Ces fiches remplacent les versions courtes de la vague 2 (mêmes identifiants). NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

IDF = "France › Île-de-France"
VB = ("Sans alcool", ["alcohol"], {"Vin blanc": [("Bouillon d'os maison (bœuf/volaille)", 0.85), ("Jus de citron (bouteille)", 0.05), ("Jus de pomme / raisin / orange (pur jus)", 0.1)]},
      "Vin blanc → **bouillon + 1 c. à s. de jus de citron + un trait de jus de raisin blanc** : l'acidité et le fruit du vin. **À tester**.")
VR = ("Sans alcool", ["alcohol"], {"Vin rouge": [("Bouillon d'os maison (bœuf/volaille)", 0.5), ("Jus de pomme / raisin / orange (pur jus)", 0.4), ("Vinaigre de vin rouge / blanc", 0.05)]},
      "Vin rouge → **½ bouillon + ⅖ jus de raisin rouge + 2 c. à s. de vinaigre de vin** (+ 1 c. à c. de concentré pour la couleur). **À tester**.")
SANS_LARDONS = ("Sans porc", ["pork"], {"Lardons": [("Lardons de dinde / de volaille fumés", 1.0)]}, "Lardons → **lardons de dinde ou de volaille fumés**, dorés dans 1 c. à s. d'huile (ils sont plus maigres). **À tester**.")
SALE = "Sale au début de chaque cuisson longue, peu ; on rectifie à la fin, en goûtant : la sauce réduit et concentre le sel."

# ———————————————————————————————— Mijotés et plats de famille
K("blanquette_veau", "Blanquette de veau à l'ancienne", "Blanquette de veau", IDF, "P", 2, 6, 40, 120, "€€€", "Grande cocotte, casserole, fouet.",
  "Le veau poché tout doucement avec ses légumes ; son bouillon devient un velouté nacré, lié à la crème et au jaune, avec champignons et petits oignons. Une sauce blanche qui ne doit jamais bouillir à la fin.",
  ["1,2 kg|d'épaule et de tendron de veau en morceaux|Épaule / tendron de veau|3", f"2|carottes|{CAROTTE}|2", "1|poireau (le blanc)|Poireau|1", f"1|oignon piqué de 2 clous de girofle + 1 bouquet garni|{OIG}|1",
   "250 g|de champignons de Paris + 12 petits oignons|Champignon de Paris|2", f"40 g|de beurre + 40 g de farine|{BEURRE}|2", f"20 cl|de crème fraîche épaisse|{CF}|2", "2|jaunes d'œufs|Jaune d'œuf|2", f"½|citron|{CIT}|1", f"1 c. à c.|de gros sel|{SEL}|1"],
  ["**Blanchir.** Viande dans une grande casserole d'eau froide, portée à ébullition puis 2 min à gros bouillon : une écume grise monte. Égoutte, rince la viande et la cocotte (c'est ce qui garde la sauce blanche).",
   "**Pocher.** Viande remise dans 2 l d'eau froide avec carottes en tronçons, poireau, oignon piqué, bouquet garni et le gros sel. Frémissement à peine visible, 1 h 30 à couvert entrouvert, en écumant les 10 premières minutes : la viande cède sous la pointe d'un couteau.",
   "**Garniture.** Champignons en quartiers et petits oignons, 10 min dans 2 louches de bouillon et une noix de beurre, à couvert : tendres et brillants.",
   "**Velouté.** Viande et légumes gardés au chaud ; bouillon filtré. Roux : beurre fondu + farine, 2 min sans colorer (il doit rester blanc). Verse 75 cl de bouillon chaud en fouettant, 10 min à petit feu : il nappe la cuillère.",
   "**Liaison.** Hors du feu, jaunes + crème + jus de citron fouettés ; ajoute une louche de velouté chaud, puis verse le tout dans la casserole en fouettant. Chauffe 1 min sans bouillir (sinon les jaunes cuisent en grains).",
   "**Réunir.** Viande, garniture et velouté, 5 min à feu très doux. Goûte : sel, poivre blanc, un trait de citron si c'est plat."],
  tips=["Le blanchiment n'est pas une manie de chef : c'est lui qui donne une sauce nacrée et non grise.", "Préparée la veille sans la liaison, elle se réchauffe doucement et on lie au dernier moment.", "Le bouillon restant : une soupe aux vermicelles le lendemain."],
  keep="3 jours au frigo ; ne se congèle pas une fois liée (la sauce tourne).", age=1, cats=["enfants"], fetes=["Repas de famille"], profil=["gras"], tech=["Roux", "Bouillon"], side="riz_nature")

K("coq_au_vin", "Coq au vin", "Coq au vin", "France › Bourgogne-Franche-Comté", "P", 2, 6, 50, 1020, "€€", "Grande cocotte, passoire.",
  "La volaille marinée une nuit dans un vin de Bourgogne, saisie, puis mijotée jusqu'à ce que la chair se détache ; garniture de lardons, champignons et petits oignons. Un vrai coq demande 2 h 30 à 3 h ; un gros poulet fermier, 1 h 15.",
  ["1|coq (ou gros poulet fermier) de 2,5 kg en 8 morceaux|Poulet entier|3", "75 cl|de vin rouge de Bourgogne|Vin rouge|3", "150 g|de lardons|Lardons|2", "250 g|de champignons de Paris + 12 petits oignons|Champignon de Paris|2",
   f"2|carottes + 1 oignon|{CAROTTE}|1", f"3 gousses|d'ail + 1 bouquet garni|{AIL}|1", f"2 c. à s.|de farine|{F55}|1", f"30 g|de beurre|{BEURRE}|1", f"1 c. à c.|de sel|{SEL}|1"],
  ["**Mariner (la veille).** Morceaux, vin, carottes et oignon en rondelles, ail écrasé, bouquet garni ; filmé, 12 h au frais.",
   "**Égoutter.** Morceaux sortis et épongés sur du papier (mouillés, ils ne dorent pas) ; marinade gardée.",
   "**Lardons et saisie.** Lardons dorés 5 min à sec, réservés. Dans leur graisse + le beurre, morceaux salés dorés en 2 fois, 4 min par face : peau brun doré.",
   "**Singer.** Légumes de la marinade 5 min ; farine saupoudrée sur la viande remise, 2 min en remuant (elle doit roussir sans brûler).",
   "**Mouiller et mijoter.** Marinade portée à ébullition à part 2 min (elle perd son âpreté), versée sur la viande. Couvercle, feu très doux : **2 h 30 à 3 h pour un coq**, 1 h 15 pour un poulet fermier. C'est cuit quand la chair se détache de l'os à la fourchette.",
   "**Garniture.** 20 min avant la fin, champignons et petits oignons dorés à part 8 min ; ajoutés avec les lardons.",
   "**Finir.** Sauce trop liquide : morceaux sortis, sauce réduite à découvert 10 min jusqu'à napper la cuillère. Goûte, rectifie le sel."],
  tips=["Encore meilleur réchauffé le lendemain : la sauce s'arrondit.", "Un vin que tu boirais : un vin de cuisine donne une sauce aigre.", "Le coq est rare en boucherie : commande-le ; sinon un poulet fermier Label Rouge, et la cuisson courte."],
  var=[VR, SANS_LARDONS], keep="3 jours au frigo ; se congèle 3 mois.", age=None, kids="✓ dès 3 ans en version sans alcool.", fetes=["Repas de famille"], profil=["viande_rouge"], tech=["Mijoter", "Marinade"], side="pommes_vapeur")

K("pot_au_feu", "Pot-au-feu", "Pot-au-feu", IDF, "P", 1, 8, 40, 240, "€€", "Très grand faitout, écumoire.",
  "Trois morceaux de bœuf (un maigre, un gélatineux, un persillé) pochés très doucement avec leurs légumes et leurs os à moelle. On sert d'abord le bouillon, puis la viande avec gros sel, moutarde et cornichons.",
  ["800 g|de paleron|Paleron|3", "800 g|de macreuse ou de gîte|Macreuse / gîte|2", "600 g|de jarret ou plat de côtes|Jarret de bœuf|2", "4|os à moelle|Os à moelle|1", f"8|carottes|{CAROTTE}|2", "4|poireaux|Poireau|2",
   "4|navets + ½ céleri-rave|Navet / navet boule d'or|1", f"8|pommes de terre (à part)|{PDT}|2", f"1|oignon piqué de girofle + bouquet garni|{OIG}|1", f"1 c. à s.|de gros sel|{SEL}|1"],
  ["**Départ à froid.** Viandes ficelées dans 5 l d'eau froide, portées doucement à frémissement : la viande rend son jus au bouillon. Écume 20 min sans laisser bouillir (sinon le bouillon se trouble).",
   "**Aromates.** Oignon piqué, bouquet garni, gros sel ; frémissement à peine visible, couvercle entrouvert, 2 h 30.",
   "**Légumes.** Carottes, poireaux ficelés en botte, navets et céleri en gros morceaux : 45 min avant la fin. Ils doivent être tendres, pas en purée.",
   "**Pommes de terre.** Cuites à part dans un peu de bouillon, 25 min (dans la marmite, elles troubleraient le bouillon).",
   "**Os à moelle.** Extrémités frottées de gros sel (la moelle ne s'échappe pas), 20 min dans le bouillon.",
   "**Servir.** Bouillon dégraissé en premier (vermicelles si tu veux) ; viande tranchée contre les fibres, légumes, moelle sur pain grillé, gros sel, moutarde, cornichons."],
  tips=["La viande est cuite quand elle se coupe à la cuillère ; trop bouillie, elle devient sèche et filandreuse.", "Bouillon refroidi une nuit : le gras se retire en plaque.", "Les restes : hachis Parmentier, salade de bœuf vinaigrette."],
  keep="Bouillon : 3 jours au frigo, 3 mois congelé. Viande : 3 jours.", age=1, cats=["zero_dechet", "enfants"], fetes=["Repas de famille"], profil=["leger"], tech=["Bouillon"])

K("daube_provencale", "Daube provençale", "Daube", "France › Provence-Alpes-Côte d'Azur", "P", 1, 6, 40, 960, "€€", "Cocotte en fonte, four.",
  "Le bœuf mariné une nuit au vin rouge avec zeste d'orange, girofle et herbes, puis cuit des heures au four : la viande s'effiloche, la sauce est brune et parfumée. À Nice, le reste de sauce nappe les macaronis du lendemain.",
  ["1,5 kg|de joue ou paleron en gros cubes|Joue de bœuf|3", "75 cl|de vin rouge corsé|Vin rouge|3", f"2|carottes + 2 oignons|{CAROTTE}|1", "1|orange (zeste en bandes)|Orange|2", "100 g|d'olives noires|Olives (vertes / noires)|1",
   f"4 gousses|d'ail|{AIL}|1", f"1|bouquet garni + 2 clous de girofle|{LAURIER}|1", f"2 c. à s.|de concentré de tomate|{CONC}|1", f"3 c. à s.|d'huile d'olive|{HO}|1", f"1 c. à c.|de sel|{SEL}|1"],
  ["**Mariner (la veille).** Viande, vin, légumes en rondelles, ail, zeste, girofle, bouquet ; 12 h au frais, retournée une fois.",
   "**Saisir.** Viande égouttée et séchée, salée, dorée en 3 fois dans l'huile, 3 min par face : croûte brune. Légumes de la marinade 5 min.",
   "**Mouiller.** Marinade bouillie 2 min à part, versée avec le concentré ; la viande doit être juste couverte.",
   "**Cuire.** Couvercle, four 150 °C, 3 h. Olives les 30 dernières minutes. C'est prêt quand un cube s'écrase à la cuillère.",
   "**Réduire.** Sauce trop claire : viande sortie, sauce réduite à feu vif 10 min, jusqu'à napper. Goûte : sel, poivre, un zeste d'orange frais."],
  tips=["Elle est meilleure le lendemain : refroidis-la dans la cocotte, le gras se retire, la sauce s'arrondit.", "Les restes de sauce : macaronis à la daube, gratinés au parmesan."],
  var=[VR], keep="4 jours au frigo ; 3 mois au congélateur.", age=None, kids="✓ dès 3 ans en version sans alcool.", fetes=["Repas de famille"], profil=["viande_rouge"], tech=["Mijoter", "Marinade"], side="pates_nature")

K("navarin_agneau", "Navarin d'agneau printanier", "Navarin", IDF, "P", 2, 6, 40, 100, "€€", "Cocotte.",
  "Un ragoût d'agneau à la sauce brune légère, cuit avec des légumes nouveaux ajoutés au fil de la cuisson pour qu'ils restent entiers : le plat de Pâques.",
  ["1,2 kg|d'épaule et de collier d'agneau en morceaux|Épaule d'agneau|3", "12|navets nouveaux|Navet / navet boule d'or|2", f"12|petites carottes|{CAROTTE}|2", f"500 g|de pommes de terre grenaille|{PDT}|2", "200 g|de petits pois|Petits pois / pois gourmands|1",
   f"1|oignon + 2 gousses d'ail|{OIG}|1", f"1 c. à s.|de concentré + 1 c. à c. de sucre|{CONC}|1", f"1 c. à s.|de farine|{F55}|1", f"1|bouquet garni|{LAURIER}|1", f"1 c. à c.|de sel|{SEL}|1"],
  ["**Saisir.** Agneau séché, salé, doré en 2 fois dans 2 c. à s. d'huile, 3 min par face. Le sucre à la fin : il caramélise et colore la sauce.",
   "**Singer.** Oignon 3 min, farine 1 min en remuant, concentré, ail, bouquet garni.",
   "**Mouiller.** Eau chaude à hauteur, en grattant les sucs. Couvert, frémissement doux, 1 h : la viande devient tendre.",
   "**Dégraisser.** Le gras remonté en surface retiré à la louche (l'agneau en rend beaucoup).",
   "**Légumes en deux temps.** Carottes, navets et pommes de terre 25 min : tendres à la pointe du couteau. Petits pois 5 min, à découvert : ils restent verts.",
   "**Finir.** Sauce réduite 5 min à découvert si besoin, jusqu'à napper la cuillère ; goûte, rectifie le sel, poivre, persil."],
  tips=["Le collier donne du moelleux, l'épaule de la tenue : le mélange des deux est le bon.", "Hors saison : carottes et navets coupés en bâtonnets, petits pois surgelés."],
  keep="3 jours au frigo.", age=1, cats=["enfants"], fetes=["Pâques"], profil=["viande_rouge"], a=["Saint-Émilion"], sa=["Jus de raisin rouge"], tech=["Mijoter"])

K("poule_au_pot", "Poule au pot farcie (version poulet)", "Poule au pot", "France › Nouvelle-Aquitaine › Béarn", "P", 2, 6, 50, 150, "€€", "Grand faitout, ficelle, aiguille à brider (ou cure-dents).",
  "La volaille farcie de pain, de foies et d'herbes, pochée avec ses légumes : un bouillon doré, une chair moelleuse, et la farce tranchée comme un pâté. Version poulet (une poule demande 3 h).",
  ["1|gros poulet fermier (ou une poule)|Poulet entier|3", f"4|carottes|{CAROTTE}|2", "3|poireaux|Poireau|2", "4|navets|Navet / navet boule d'or|1", f"1|oignon piqué de 2 clous de girofle + bouquet garni|{OIG}|1",
   "200 g|de pain rassis|Pain rassis (réservé)|2", f"2|œufs|{OEUF}|1", "200 g|de foies de volaille|Foies / gésiers de volaille|1", f"1 bouquet|de persil + 2 gousses d'ail|{PERSIL}|1", f"1 c. à s.|de gros sel|{SEL}|1"],
  ["**Farce.** Pain trempé dans un peu de lait, pressé ; foies hachés, œufs, persil et ail hachés, sel, poivre : une pâte souple qui se tient.",
   "**Farcir et fermer.** Volaille farcie sans tasser (la farce gonfle), ouverture cousue ou fermée aux cure-dents, pattes ficelées.",
   "**Pocher.** Eau froide à hauteur, gros sel, oignon piqué, bouquet garni ; frémissement très doux, écume 10 min. 1 h 30 pour un poulet, 3 h pour une poule.",
   "**Légumes.** 45 min avant la fin, en gros morceaux : tendres sans s'écraser.",
   "**Vérifier.** Une cuisse se détache facilement, le jus qui sort est clair ; au thermomètre, 74 °C au cœur de la farce.",
   "**Servir.** Bouillon dégraissé en premier ; volaille découpée, farce en tranches épaisses, légumes, gros sel et cornichons."],
  tips=["La farce cuit dans la volaille : elle doit atteindre 74 °C, le thermomètre est utile.", "Le bouillon fait une soupe, un risotto ou une sauce les jours suivants."],
  keep="Bouillon : 3 mois au congélateur. Volaille : 3 jours.", age=1, cats=["zero_dechet", "enfants"], profil=["leger"], fetes=["Repas de famille"], tech=["Bouillon"], side="riz_nature")

K("hachis_parmentier", "Hachis Parmentier", "Hachis Parmentier", IDF, "P", 1, 6, 35, 35, "€", "Plat à gratin, poêle, casserole, presse-purée.",
  "Une viande hachée revenue aux oignons, juteuse et bien assaisonnée, sous une purée beurrée qui dore au four. La version d'origine se fait avec les restes de pot-au-feu ou de rôti.",
  [f"600 g|de bœuf haché (ou restes de pot-au-feu)|{HACHE}|3", f"1,2 kg|de pommes de terre farineuses|{PDT}|3", f"2|oignons|{OIG}|2", f"20 cl|de lait|{LAIT}|1", f"60 g|de beurre|{BEURRE}|2", f"1 c. à s.|de concentré de tomate|{CONC}|1",
   f"60 g|de fromage râpé|{GRUY}|1", f"1 bouquet|de persil|{PERSIL}|1", f"1 pincée|de muscade|Noix de muscade|0", f"1 c. à c.|de sel|{SEL}|1"],
  ["**Pommes de terre.** Épluchées, en gros morceaux, départ eau froide salée, 20-25 min : la lame entre sans résistance.",
   "**Purée.** Égouttées, séchées 1 min sur le feu, écrasées au presse-purée (jamais au mixeur : elle devient collante). Beurre puis lait chaud, muscade, sel : souple mais pas liquide.",
   "**Oignons.** Émincés, 8 min dans un peu de beurre à feu moyen : fondants et blonds.",
   "**Viande.** Feu vif, viande émiettée, 5 min sans trop remuer pour qu'elle dore ; concentré, sel, poivre, persil haché, 2 min. Elle doit rester juteuse (un trait de bouillon si elle sèche).",
   "**Monter.** Viande au fond du plat, purée lissée à la spatule puis striée à la fourchette, fromage, noisettes de beurre.",
   "**Gratiner.** 20 min à 200 °C, puis 3 min sous le gril : les stries dorent et croustillent. Repos 5 min avant de servir."],
  tips=["Avec des restes de pot-au-feu ou de rôti hachés au couteau, il est encore meilleur : c'est la recette d'origine.", "Une salade verte vinaigrée à côté équilibre le plat."],
  keep="3 jours au frigo ; se congèle 3 mois en parts.", age=1, cats=["enfants", "zero_dechet"], profil=["viande_rouge"], tech=["Gratiner"])

K("gigot_sept_heures", "Gigot de sept heures", "Gigot de sept heures", "France", "P", 1, 8, 30, 450, "€€€", "Cocotte en fonte ovale avec couvercle, four.",
  "Un gigot cuit si longtemps, à si basse température, qu'il se sert à la cuillère, confit dans le vin blanc avec ses têtes d'ail et ses légumes. Peu de travail, beaucoup de patience.",
  ["1|gigot d'agneau de 2,2 kg|Gigot d'agneau|3", "50 cl|de vin blanc sec|Vin blanc|2", f"2 têtes|d'ail|{AIL}|2", f"4|carottes + 3 oignons|{CAROTTE}|2", f"4 branches|de thym et romarin|{THYM}|1",
   f"30 cl|de bouillon|{BOUILLON}|2", f"3 c. à s.|d'huile d'olive|{HO}|1", f"200 g|de farine + eau (cordon, facultatif)|{F55}|0?", f"1 c. à c.|de sel|{SEL}|1"],
  ["**Saler.** Gigot sorti 1 h avant, salé et poivré partout.",
   "**Dorer.** Cocotte, huile, feu moyen-vif : gigot doré sur toutes ses faces, 15 min au total. Pas de brûlé au fond : les sucs font la sauce.",
   "**Garnir.** Carottes et oignons en gros morceaux, têtes d'ail coupées en deux, herbes ; vin blanc et bouillon (à mi-hauteur de la viande).",
   "**Fermer.** Couvercle, et si tu veux le faire comme autrefois, un boudin de pâte farine-eau tout autour (la vapeur ne s'échappe pas).",
   "**Cuire.** 7 h à 120 °C, sans ouvrir si la cocotte est lutée ; sinon arrose 2 fois. C'est prêt quand la viande se défait à la cuillère.",
   "**Servir.** Le jus réduit 5 min à feu vif s'il est trop clair ; ail confit pressé dedans. Gigot posé entier sur le plat, servi à la cuillère."],
  tips=["Le lendemain, il est encore meilleur : réchauffé doucement 1 h à 120 °C dans son jus.", "Avec des flageolets ou une purée."],
  var=[VB], keep="3 jours au frigo dans son jus.", age=1, fetes=["Pâques", "Repas de famille"], profil=["viande_rouge"], tech=["Mijoter", "Basse température"], side="puree_maison")

K("souris_agneau", "Souris d'agneau confites au miel et romarin", "Souris d'agneau", "France", "P", 1, 4, 25, 190, "€€€", "Cocotte, four.",
  "Les jarrets d'agneau dorés, confits trois heures dans une sauce tomate à l'ail et au romarin, puis laqués au miel : la viande se détache de l'os.",
  ["4|souris d'agneau|Gigot d'agneau|3", f"2 c. à s.|de miel|{MIEL}|2", f"1 tête|d'ail|{AIL}|2", f"3 branches|de romarin|{THYM}|2", f"2|oignons|{OIG}|1", f"400 g|de tomates pelées|{PELEES}|1", f"30 cl|de bouillon|{BOUILLON}|2", f"2 c. à s.|d'huile d'olive|{HO}|1", f"1 c. à c.|de sel|{SEL}|1"],
  ["**Dorer.** Souris salées, dorées sur toutes les faces dans l'huile, 10 min : brun profond.",
   "**Base.** Oignons émincés 5 min, gousses d'ail entières en chemise, romarin, tomates, bouillon : à mi-hauteur.",
   "**Confire.** Couvert, four 150 °C, 2 h 30, en retournant à mi-cuisson : la viande se détache de l'os à la fourchette.",
   "**Laquer.** Découvert, miel au pinceau, 20 min à 180 °C en arrosant 2 fois : brillantes et caramélisées.",
   "**Sauce.** Jus réduit 5 min s'il est trop clair ; ail confit écrasé dedans. Goûte, rectifie."],
  tips=["Commande les souris à l'avance : chaque gigot n'en a qu'une.", "Le jus restant parfume une semoule ou une purée le lendemain."],
  keep="3 jours au frigo.", age=1, fetes=["Repas de famille"], profil=["viande_rouge", "sucre"], tech=["Mijoter"], side="puree_maison")

K("joues_boeuf_carottes", "Joues de bœuf aux carottes", "Bœuf carottes", IDF, "P", 1, 6, 25, 200, "€€", "Cocotte.",
  "Des joues de bœuf qui deviennent fondantes comme du confit, des carottes qui s'imprègnent de la sauce : le bœuf-carottes de famille, sans alcool.",
  ["1,5 kg|de joues de bœuf|Joue de bœuf|3", f"1 kg|de carottes|{CAROTTE}|3", f"2|oignons|{OIG}|1", f"1 c. à s.|de concentré|{CONC}|1", f"1 c. à s.|de farine|{F55}|1", f"75 cl|de bouillon de bœuf|{BOUILLON}|2", f"1|bouquet garni|{LAURIER}|1", f"2 c. à s.|d'huile|{HN}|1", f"1 c. à c.|de sel|{SEL}|1"],
  ["**Parer.** Joues débarrassées de la grosse membrane, en 3 morceaux ; séchées, salées.",
   "**Saisir.** Huile fumante, en 2 fois, 4 min par face : croûte brune (c'est le goût de la sauce).",
   "**Singer.** Oignons 5 min, farine 1 min, concentré 1 min : ça doit sentir le grillé, pas le brûlé.",
   "**Mijoter.** Bouillon chaud en grattant les sucs, bouquet garni ; frémissement très doux, couvert, 2 h.",
   "**Carottes.** En rondelles épaisses, 1 h de plus : la viande s'écrase à la cuillère, les carottes sont confites.",
   "**Finir.** Sauce réduite 5 à 10 min à découvert, jusqu'à napper la cuillère ; goûte, poivre, persil."],
  tips=["Encore meilleur réchauffé : prépare-le la veille.", "Les joues en sauce se congèlent très bien en portions."],
  keep="4 jours au frigo ; 3 mois au congélateur.", age=1, cats=["enfants"], profil=["viande_rouge"], tech=["Mijoter"], side="puree_maison")

K("lapin_moutarde", "Lapin à la moutarde", "Lapin à la moutarde", "France › Bourgogne-Franche-Comté", "P", 1, 4, 25, 60, "€€", "Cocotte.",
  "Morceaux de lapin enduits de moutarde, dorés, mijotés au vin blanc puis liés à la crème et à la moutarde à l'ancienne : tendre, relevé, très bourguignon.",
  ["1|lapin en 8 morceaux|Lapin|3", f"4 c. à s.|de moutarde de Dijon + 1 c. à s. à l'ancienne|{DIJON}|3", f"20 cl|de crème fraîche|{CF}|2", "20 cl|de vin blanc sec|Vin blanc|2", f"2|échalotes|{ECH}|1", f"3 branches|de thym|{THYM}|1", f"20 g|de beurre + 1 c. à s. d'huile|{BEURRE}|1", f"1 c. à c.|de sel|{SEL}|1"],
  ["**Badigeonner.** Morceaux salés, poivrés, enduits de moutarde de Dijon ; 30 min.",
   "**Dorer.** Beurre et huile moussants, morceaux dorés 3 min par face sans les brûler (la moutarde colore vite) ; échalotes émincées 2 min.",
   "**Mijoter.** Vin blanc et thym, couvercle, frémissement 40 min : la chair se détache de l'os.",
   "**Lier.** Crème et moutarde à l'ancienne, 10 min à découvert : la sauce nappe. Goûte : la moutarde perd sa force en cuisant, un trait de Dijon cru à la fin la réveille."],
  tips=["Pas de lapin : des cuisses de poulet, même recette, 35 min de mijotage."],
  var=[VB], keep="3 jours au frigo.", age=1, cats=["enfants"], profil=["viande_rouge"], tech=["Mijoter"], side="pates_nature")

K("poulet_basquaise", "Poulet basquaise", "Poulet basquaise", "France › Nouvelle-Aquitaine › Pays basque", "P", 1, 6, 30, 55, "€€", "Cocotte.",
  "Les morceaux de poulet dorés puis mijotés dans la piperade (poivrons, tomates, oignons fondus) relevée au piment d'Espelette : de la couleur, de la douceur, une pointe de chaleur.",
  [f"6|cuisses de poulet|{CUISSE}|3", f"3|poivrons (rouge, vert, jaune)|{POIVRON}|3", f"800 g|de tomates pelées (ou 6 tomates mûres)|{PELEES}|2", f"2|oignons|{OIG}|2", f"3 gousses|d'ail|{AIL}|1", "1 c. à c.|de piment d'Espelette|Piment d'Espelette|2", f"1|bouquet thym-laurier|{THYM}|1", f"3 c. à s.|d'huile d'olive|{HO}|1", f"1 c. à c.|de sel|{SEL}|1"],
  ["**Dorer.** Cuisses salées, peau en dessous, dans l'huile chaude, 8 min sans bouger puis 4 min de l'autre côté : peau dorée et croustillante. Réserve.",
   "**Piperade.** Dans la graisse, oignons et poivrons en lanières, 12 min à feu moyen : fondants, légèrement colorés. Ail 1 min.",
   "**Sauce.** Tomates écrasées, Espelette, bouquet, 10 min.",
   "**Mijoter.** Cuisses posées peau au-dessus (elle reste plus croustillante), couvert, 35 min à feu doux : 74 °C à cœur, jus clair.",
   "**Finir.** Couvercle retiré 5 min si la sauce est claire ; goûte, sel, une pincée d'Espelette au service."],
  tips=["Encore meilleur réchauffé.", "Pour les enfants : l'Espelette est doux, mais sers-en un peu à part si besoin."],
  keep="3 jours au frigo ; se congèle 3 mois.", age=1, cats=["enfants"], profil=["leger"], sa=["Citronnade"], a=["Irouléguy rouge"], tech=["Mijoter"], side="riz_nature")

K("tartiflette", "Tartiflette", "Tartiflette", "France › Auvergne-Rhône-Alpes › Savoie", "P", 1, 6, 30, 45, "€€", "Plat à gratin, poêle, casserole.",
  "Pommes de terre fermes, oignons fondus, lardons, un peu de vin blanc et de crème, et un reblochon entier qui fond par-dessus : le plat des retours de ski, généreux et sans détour.",
  [f"1,5 kg|de pommes de terre à chair ferme|{PDT}|3", "1|reblochon fermier|Reblochon / raclette / mont-d'or|3", "200 g|de lardons|Lardons|2", f"2|oignons|{OIG}|2", f"15 cl|de crème fraîche|{CF}|2", "10 cl|de vin blanc de Savoie|Vin blanc|1", f"1 gousse|d'ail|{AIL}|1", f"1 pincée|de poivre|{POIVRE}|0"],
  ["**Pommes de terre.** Entières, en robe des champs, départ eau froide salée, 20 min : encore un peu fermes. Épluchées tièdes, en rondelles épaisses.",
   "**Lardons et oignons.** Lardons à sec 5 min, oignons émincés 10 min dans leur gras : blonds et fondants. Vin blanc, 2 min pour qu'il s'évapore à moitié.",
   "**Monter.** Plat frotté d'ail : pommes de terre, lardons-oignons, pommes de terre, crème. Reblochon coupé en deux dans l'épaisseur, croûte vers le haut.",
   "**Gratiner.** 25 min à 200 °C : le fromage coule, la croûte dore, la crème bouillonne sur les bords. Pas de sel (reblochon et lardons le sont)."],
  tips=["Une salade verte bien vinaigrée à côté est indispensable : elle coupe le gras.", "Le reblochon fermier (pastille verte) a plus de goût que le laitier (pastille rouge)."],
  var=[VB, SANS_LARDONS], keep="2 jours au frigo.", age=3, profil=["gras"], fetes=["Repas de famille"], sa=["Jus de pomme pétillant"], a=["Vin blanc de Savoie"], tech=["Gratiner"], side="achat:Salade (laitue, batavia)")

K("cassoulet_volaille", "Cassoulet de Castelnaudary (version canard-bœuf)", "Cassoulet", "France › Occitanie › Lauragais", "P", 2, 8, 50, 1050, "€€", "Grande cassole ou cocotte en terre, four.",
  "Haricots fondants cuits dans leur bouillon, confit de canard et saucisses, gratinés longuement jusqu'à former une croûte qu'on enfonce sept fois. L'original est au porc : version inspirée canard et saucisses de bœuf (D21), au goût fumé conservé.",
  ["800 g|de haricots lingots secs|Haricots blancs / lingots|3", "4|cuisses de canard confites|Canard : magret, cuisse|3", "6|saucisses de bœuf ou de volaille|Saucisse de bœuf / de veau / de volaille|2",
   f"2|oignons + 1 carotte|{OIG}|1", f"4 gousses|d'ail|{AIL}|2", f"2 c. à s.|de concentré de tomate|{CONC}|1", f"1|bouquet garni|{LAURIER}|1", f"1 c. à c.|de paprika fumé|{PFUME}|1", f"1 c. à c.|de sel|{SEL}|1"],
  ["**Tremper (la veille).** Haricots dans trois fois leur volume d'eau froide, 12 h.",
   "**Cuire les haricots.** Départ eau froide, 5 min d'ébullition, égouttés ; puis eau neuve, oignon, carotte, 2 gousses d'ail, bouquet, paprika fumé : frémissement 1 h, sans sel (sinon ils durcissent). Ils sont tendres mais entiers. Sale à la fin.",
   "**Viandes.** Confit dégraissé et doré côté peau 8 min dans sa graisse ; saucisses dorées 5 min.",
   "**Monter.** Cassole frottée d'ail : haricots, viandes, haricots ; bouillon de cuisson mêlé au concentré jusqu'à hauteur.",
   "**Gratiner.** Four 150 °C, 3 h. Une croûte dorée se forme : enfonce-la à la cuillère toutes les 30 min (au moins 3 fois, la tradition en compte 7) et rajoute un peu de bouillon si ça sèche.",
   "**Servir.** Brûlant, dans la cassole, avec une salade verte."],
  tips=["Il est meilleur réchauffé : cuit la veille, recuit 1 h à 150 °C.", "Les haricots doivent rester entiers : pas d'ébullition franche."],
  keep="4 jours au frigo ; encore meilleur réchauffé.", age=3, profil=["gras", "viande_rouge"], fetes=["Repas de famille"], a=["Vin de Corbières"], sa=["Jus de raisin rouge"], tech=["Mijoter", "Gratiner"])

K("confit_canard_maison", "Confit de canard maison", "Confit de canard", "France › Nouvelle-Aquitaine › Gascogne", "P", 2, 4, 25, 1620, "€€", "Cocotte, four, thermomètre.",
  "Des cuisses salées une nuit, rincées, puis confites trois heures dans leur graisse à petits frémissements : tendres à cœur, à poêler côté peau au moment de servir.",
  ["4|cuisses de canard|Canard : magret, cuisse|3", "1 kg|de graisse de canard|Graisse de canard|3", "60 g|de gros sel|Sel fin / gros sel / fleur de sel|2", f"4 gousses|d'ail|{AIL}|1", f"4 branches|de thym + 2 feuilles de laurier|{THYM}|1", f"1 c. à c.|de poivre|{POIVRE}|0", f"800 g|de pommes de terre (sarladaises)|{PDT}|1?"],
  ["**Saler.** Cuisses frottées de gros sel, poivre, thym émietté, ail écrasé ; 12 à 24 h au frigo dans un plat couvert (le sel tire l'eau et parfume).",
   "**Rincer.** Sel rincé à l'eau froide, cuisses bien séchées.",
   "**Confire.** Graisse fondue dans la cocotte, cuisses immergées, ail et laurier ; four 100 °C, 3 h : de toutes petites bulles, jamais d'ébullition. C'est cuit quand l'os se détache en tournant.",
   "**Conserver.** Cuisses rangées dans un bocal ou une terrine, couvertes de leur graisse filtrée.",
   "**Servir.** Poêle froide, côté peau, feu moyen, 8 min sans bouger : peau dorée et croustillante ; 2 min de l'autre côté. Pommes de terre en rondelles sautées dans la graisse avec ail et persil."],
  tips=["La graisse se réutilise trois ou quatre fois : filtrée, gardée au frais.", "Le confit se garde trois semaines au frigo, à condition d'être entièrement couvert de graisse."],
  keep="3 semaines au frigo couvert de graisse.", age=1, profil=["gras"], tech=["Confire"])

# ———————————————————————————————— Poissons et soupes
K("sole_meuniere", "Sole meunière", "Sole meunière", "France", "P", 2, 2, 15, 12, "€€€", "Grande poêle ovale, spatule large.",
  "La sole farinée, dorée au beurre, arrosée d'un beurre noisette au citron et au persil : le plat des grandes brasseries, réussi en dix minutes si la poêle est à la bonne température.",
  ["2|soles portion (300 g) vidées et pelées|Sole, limande|3", f"30 g|de farine|{F55}|1", f"80 g|de beurre|{BEURRE}|3", f"1|citron|{CIT}|2", f"1 c. à s.|de persil haché|{PERSIL}|1", f"1 pincée|de fleur de sel|{SEL}|1"],
  ["**Fariner.** Soles séchées, salées des deux côtés, farinées puis tapotées : une pellicule fine (trop de farine fait une croûte pâteuse).",
   "**Cuire.** 30 g de beurre et un filet d'huile, feu moyen : quand le beurre mousse sans brunir, sole côté peau blanche, 4 min en arrosant de beurre ; retournée délicatement, 3 à 4 min. La chair se détache de l'arête centrale.",
   "**Beurre noisette.** Soles sur assiettes chaudes. Poêle essuyée, 50 g de beurre, 1 à 2 min jusqu'à ce qu'il mousse, sente la noisette et prenne une couleur blonde : hors du feu, jus de citron (ça crépite), persil.",
   "**Servir.** Nappée aussitôt, quartier de citron, pommes vapeur."],
  tips=["Une limande ou une plie : même recette, 2 min de moins.", "Demande au poissonnier de peler la peau noire : c'est délicat à la maison."],
  keep="À manger aussitôt.", age=1, profil=["poisson", "gras"], tech=["Poisson plat", "Cuisson du poisson"], side="pommes_vapeur")

K("bouillabaisse_express", "Bouillabaisse express (version familiale)", "Bouillabaisse", "France › Provence-Alpes-Côte d'Azur › Marseille", "P", 2, 6, 45, 40, "€€€", "Faitout large, mixeur.",
  "Plusieurs poissons fermes cuits à gros bouillon dans une soupe de poissons safranée à l'orange et au fenouil, avec pommes de terre, rouille et croûtons. Le gros bouillon n'est pas une erreur : il émulsionne l'huile et lie le bouillon.",
  ["1,5 kg|de poissons variés (lotte, grondin, rascasse, merlan)|Lotte|3", "1|recette de soupe de poissons (base)|SUB:soupe_poisson_rouille|3", f"6|pommes de terre à chair ferme|{PDT}|2", "1|orange (zeste)|Orange|1", "1 pincée|de safran|Safran (pistils)|2", f"4 c. à s.|d'huile d'olive|{HO}|1", f"1 c. à c.|de sel|{SEL}|1"],
  ["**Poissons.** En gros tronçons, frottés d'huile, de safran et de sel ; 30 min au frais.",
   "**Base.** Soupe de poissons portée à ébullition 5 min avec le zeste d'orange et le reste du safran : rouge orangé, l'odeur de safran monte.",
   "**Pommes de terre.** En rondelles de 1 cm, 15 min dans la soupe : tendres.",
   "**Poissons.** Les fermes d'abord (lotte, grondin) 5 min, puis les tendres (merlan) 4 min, **à gros bouillon** : l'huile émulsionne, le bouillon s'épaissit. Ils sont cuits quand la chair devient opaque et se détache.",
   "**Servir.** Le bouillon d'abord sur des croûtons frottés d'ail et tartinés de rouille ; puis poissons et pommes de terre sur un plat."],
  tips=["Demande au poissonnier de vider, écailler et couper les poissons, et garde les têtes pour la soupe.", "Pas de lotte : cabillaud et lieu, en tronçons épais."],
  keep="Le jour même (le poisson réchauffé se défait).", age=3, fetes=["Repas de famille"], profil=["poisson"], tech=["Cuisson du poisson"])

K("soupe_oignon", "Soupe à l'oignon gratinée", "Gratinée des Halles", IDF, "So", 1, 4, 25, 60, "€", "Cocotte, bols allant au four.",
  "Des oignons caramélisés très lentement jusqu'au brun noisette, un bouillon brûlant, le pain rassis et le fromage gratiné : la soupe des petits matins des Halles. Tout le goût vient de la patience sur les oignons.",
  [f"1 kg|d'oignons jaunes|{OIG}|3", f"40 g|de beurre|{BEURRE}|2", f"1 c. à s.|de farine|{F55}|1", f"1,2 L|de bouillon de bœuf|{BOUILLON}|3", "10 cl|de vin blanc sec|Vin blanc|1", "8 tranches|de baguette rassise|Pain rassis (réservé)|2", f"150 g|de comté râpé|{GRUY}|2", f"1 c. à c.|de sel|{SEL}|1"],
  ["**Caraméliser.** Oignons émincés finement, beurre, une pincée de sel (il fait rendre l'eau), feu moyen-doux, 40 min en remuant toutes les 5 min : ils passent du blond au brun noisette, très sucrés. S'ils attachent, une cuillère d'eau et on gratte.",
   "**Lier.** Farine, 1 min en remuant. Vin blanc, gratte le fond, 2 min.",
   "**Mouiller.** Bouillon chaud, 15 min à frémissement. Goûte : sel, poivre.",
   "**Pain.** Tranches grillées au four 5 min : sèches et dorées (elles tiendront dans la soupe).",
   "**Gratiner.** Bols remplis aux trois quarts, pain, fromage généreux ; 5 min sous le gril : le fromage bouillonne et brunit. ⚠️ Bols brûlants."],
  tips=["Les oignons cuits d'avance se congèlent : la soupe se fait ensuite en 20 min.", "Sans vin : un trait de vinaigre de cidre pour l'acidité."],
  var=[VB], keep="Soupe sans pain : 3 jours au frigo.", age=3, profil=["gras"], cats=["zero_dechet"], sa=["Bouillon chaud, eau"], a=["Vin blanc sec"], tech=["Faire revenir", "Gratiner"])

# ———————————————————————————————— Italie, Grèce, Inde
K("osso_buco", "Osso buco à la milanaise (gremolata)", "Ossobuco alla milanese", "Europe du Sud › Italie › Lombardie", "P", 1, 4, 25, 120, "€€", "Cocotte large (les jarrets à plat).",
  "Le jarret de veau tranché avec son os à moelle, fariné, doré, braisé au vin blanc avec un soffritto et un peu de tomate ; au service, la gremolata citron-ail-persil réveille tout. À Milan, il se sert sur un risotto au safran.",
  ["4|tranches de jarret de veau (4 cm)|Jarret de veau|3", "15 cl|de vin blanc sec|Vin blanc|2", f"200 g|de tomates pelées|{PELEES}|1", f"1|oignon + 1 carotte + 1 branche de céleri|{OIG}|1", f"25 cl|de bouillon|{BOUILLON}|2", f"2 c. à s.|de farine|{F55}|1",
   f"1|citron non traité (zeste)|{CIT}|2", f"1 bouquet|de persil + 1 gousse d'ail|{PERSIL}|1", f"30 g|de beurre + 1 c. à s. d'huile|{BEURRE}|1", f"1 c. à c.|de sel|{SEL}|1"],
  ["**Préparer.** Bordure des jarrets entaillée en 3 endroits (la peau se rétracte, ils restent plats) ; salés, farinés, tapotés.",
   "**Dorer.** Beurre et huile moussants, jarrets 4 min par face : bien dorés. Réserve.",
   "**Soffritto.** Oignon, carotte, céleri en petits dés, 8 min à feu doux : fondants.",
   "**Braiser.** Vin blanc, gratte les sucs, 2 min ; tomates, bouillon, jarrets remis à plat (le liquide à mi-hauteur). Couvert, frémissement doux, 1 h 45, en les retournant une fois : la viande se détache de l'os.",
   "**Gremolata.** Zeste de citron, ail et persil hachés ensemble très fin, au dernier moment.",
   "**Servir.** Sauce réduite si besoin ; jarrets nappés, gremolata dessus, cuillère pour la moelle."],
  tips=["La moelle est le meilleur morceau : une petite cuillère pour chacun.", "Plus simple qu'un risotto : de la polenta crémeuse."],
  var=[VB], keep="3 jours au frigo (gremolata au moment).", age=1, profil=["viande_rouge"], tech=["Mijoter"], side="risotto_milanese")

K("lasagnes_bolognaise", "Lasagnes à la bolognaise", "Lasagne alla bolognese", "Europe du Sud › Italie › Émilie-Romagne", "P", 2, 8, 50, 160, "€€", "Cocotte, casserole, plat à gratin.",
  "Un ragù cuit deux heures, qui n'a rien d'une sauce tomate à la viande ; une béchamel fluide à la muscade ; des feuilles de pâte et du parmesan : on prend le temps du dimanche, le montage est simple.",
  [f"600 g|de bœuf haché (15 % de gras)|{HACHE}|3", "250 g|de feuilles de lasagnes|Lasagnes|3", f"800 g|de tomates pelées|{PELEES}|2", f"1|carotte + 1 branche de céleri + 1 oignon|{CAROTTE}|1",
   f"25 cl + 70 cl|de lait (ragù + béchamel)|{LAIT}|2", f"60 g|de beurre + 60 g de farine|{BEURRE}|2", f"100 g|de parmesan|{PARM}|2", f"1 pincée|de muscade|Noix de muscade|0", f"2 c. à s.|d'huile d'olive|{HO}|1", f"1 c. à c.|de sel|{SEL}|1"],
  ["**Soffritto.** Carotte, céleri, oignon hachés très fin, huile, 10 min à feu doux : fondants, sans couleur.",
   "**Viande.** Feu moyen-vif, viande émiettée, 8 min jusqu'à ce qu'elle grésille et dore légèrement ; sel.",
   "**Lait.** 25 cl de lait, laissé s'absorber complètement en 10 min (il attendrit la viande, c'est le secret bolognais).",
   "**Mijoter.** Tomates écrasées, 2 h à feu très doux, à couvert entrouvert, en remuant de temps en temps : sauce épaisse, l'huile perle en surface.",
   "**Béchamel.** Beurre fondu, farine 2 min, lait chaud d'un coup en fouettant, 5 min : nappante mais fluide (elle épaissit au four) ; muscade, sel.",
   "**Monter.** Fond de béchamel, pâtes, ragù, béchamel, parmesan ; 4 couches ; finir béchamel et parmesan.",
   "**Cuire et reposer.** 40 min à 180 °C : dessus doré, bords qui bouillonnent. 15 min de repos avant de couper (sinon tout s'effondre)."],
  tips=["Le ragù se fait la veille et se congèle : le dimanche, il ne reste que le montage.", "Feuilles sèches « sans précuisson » : la béchamel fluide suffit à les cuire."],
  keep="4 jours au frigo ; se congèle en parts.", age=1, cats=["enfants"], profil=["viande_rouge", "gras"], fetes=["Repas de famille"], tech=["Roux", "Mijoter"])

K("risotto_champignons", "Risotto aux champignons", "Risotto ai funghi", "Europe du Sud › Italie › Lombardie", "P", 2, 4, 35, 0, "€€", "Sauteuse à bords hauts, casserole (bouillon).",
  "Un riz crémeux sans crème : le grain nacré, mouillé louche par louche d'un bouillon brûlant, puis travaillé hors du feu avec beurre froid et parmesan. Les champignons sont dorés à part pour garder leur goût.",
  ["320 g|de riz à risotto (carnaroli ou arborio)|Riz à risotto (arborio, carnaroli)|3", "400 g|de champignons (Paris et pleurotes)|Champignon de Paris|3", f"1,2 L|de bouillon de volaille|{BOUILLON}|2", f"1|échalote|{ECH}|1",
   "10 cl|de vin blanc sec|Vin blanc|1", f"60 g|de parmesan|{PARM}|2", f"60 g|de beurre froid|{BEURRE}|2", f"1 c. à s.|de persil|{PERSIL}|0", f"1 pincée|de sel|{SEL}|1"],
  ["**Bouillon.** Chauffé 5 min puis gardé frémissant à côté (froid, il casserait la cuisson).",
   "**Champignons.** Poêle très chaude, une noix de beurre, en 2 fois, 5 min sans trop remuer : dorés, pas bouillis. Salés à la fin. Réserve.",
   "**Nacrer.** Échalote ciselée, une noix de beurre, 3 min : translucide. Riz, 2 min en remuant : les grains deviennent nacrés et crépitent.",
   "**Vin.** Versé d'un coup, remue jusqu'à évaporation (l'odeur d'alcool disparaît).",
   "**Cuire.** Bouillon louche par louche, en remuant souvent, la suivante quand la précédente est presque absorbée : 16 à 18 min. Goûte : tendre, avec un cœur à peine ferme. Sale à mi-cuisson.",
   "**Mantecare.** Hors du feu, beurre froid en dés et parmesan, remue vivement 1 min : crémeux et ondulant (« all'onda »). Couvre 2 min. Champignons et persil."],
  tips=["Le risotto n'attend pas : sers-le dès qu'il ondule dans l'assiette.", "Les restes : arancini (boulettes panées) le lendemain."],
  var=[("Sans alcool", ["alcohol"], {"Vin blanc": [("Jus de citron (bouteille)", 0.1), ("Bouillon d'os maison (bœuf/volaille)", 0.9)]}, "Vin blanc → **bouillon + 1 c. à s. de jus de citron** (acidité). **À tester**.")],
  keep="Le jour même ; les restes en arancini.", age=1, cats=["enfants"], profil=["gras"], kids="✓ dès 1 an en version sans alcool.", tech=["nacrer le riz"])

K("cacio_e_pepe", "Pâtes cacio e pepe", "Cacio e pepe", "Europe du Sud › Italie › Latium", "P", 2, 4, 15, 12, "€€", "Casserole large (peu d'eau), poêle, bol.",
  "Trois ingrédients, une technique : le pecorino fondu avec l'eau amidonnée des pâtes et le poivre torréfié forme une crème soyeuse. Raté, il fait des grumeaux ; réussi, c'est un des plats les plus fins de Rome.",
  [f"400 g|de spaghetti ou tonnarelli|{PATES}|3", "150 g|de pecorino romano râpé très fin|Pecorino|3", f"2 c. à c.|de poivre noir concassé|{POIVRE}|2", f"1 pincée|de gros sel|{SEL}|1"],
  ["**Pâtes.** Peu d'eau (2 l pour 400 g) et peu salée : elle sera riche en amidon et le pecorino est salé. Cuisson 2 min de moins que le paquet : encore fermes au cœur. Garde 40 cl d'eau.",
   "**Poivre.** Concassé, torréfié 1 min à sec dans la poêle : il sent fort. Une louche d'eau des pâtes, 1 min.",
   "**Crème de pecorino.** Dans un bol, pecorino + quelques cuillères d'eau des pâtes **tiède** (pas bouillante, sinon il file) : pâte lisse comme une crème épaisse.",
   "**Finir les pâtes.** Pâtes dans la poêle au poivre, 2 min en ajoutant de l'eau : elles finissent de cuire et libèrent leur amidon.",
   "**Lier.** Hors du feu, attends 30 s, crème de pecorino, remue vite et sans arrêt en ajoutant de l'eau cuillère par cuillère : la sauce nappe et brille. Sers tout de suite."],
  tips=["Des grumeaux : la poêle était trop chaude. Une cuillère d'eau tiède et on remue fort, ça se rattrape souvent.", "Râpe le pecorino à la râpe fine (microplane) : il fond sans grains."],
  keep="À manger aussitôt.", age=3, profil=["gras"], tech=["Pâtes"])

K("moussaka", "Moussaka", "Mousakás", "Europe du Sud › Grèce", "P", 2, 8, 60, 80, "€€", "Plat à gratin profond, poêle, casserole.",
  "Des aubergines rôties, un agneau à la tomate parfumé à la cannelle et au piment de la Jamaïque, une béchamel épaisse liée au jaune qui gonfle et dore : réconfortante, très parfumée, meilleure tiède.",
  ["4|aubergines|Aubergine|3", "700 g|d'agneau haché (ou de bœuf)|Agneau haché|3", f"400 g|de tomates pelées|{PELEES}|2", f"2|oignons + 2 gousses d'ail|{OIG}|1", f"1 c. à c.|de cannelle + 1 pincée de quatre-épices|{CANN}|1", "1 c. à c.|d'origan|Origan frais / sec|1",
   f"60 cl|de lait|{LAIT}|2", f"60 g|de beurre + 60 g de farine|{BEURRE}|2", "2|jaunes d'œufs|Jaune d'œuf|1", f"60 g|de parmesan ou kefalotyri|{PARM}|1"],
  ["**Aubergines.** Tranches de 1 cm salées 20 min, épongées, huilées au pinceau, 25 min à 220 °C : dorées et fondantes (pas de friture, plus léger).",
   "**Sauce.** Oignons 8 min, ail ; viande émiettée 8 min à feu vif jusqu'à dorer ; cannelle, quatre-épices, origan, tomates, sel ; 25 min à découvert : épaisse, presque sèche (sinon la moussaka rend de l'eau).",
   "**Béchamel.** Beurre, farine 2 min, lait chaud, 5 min : épaisse. Hors du feu, jaunes et fromage : elle gonfle et dore au four.",
   "**Monter.** Aubergines, viande, aubergines, béchamel lissée.",
   "**Cuire.** 45 min à 180 °C : dessus doré et soufflé.",
   "**Reposer.** 20 min au moins : elle se tient et se coupe en parts nettes."],
  tips=["Elle est encore meilleure le lendemain, tiède.", "Végétarienne : des lentilles cuites à la place de la viande."],
  keep="4 jours au frigo ; se congèle en parts.", age=1, profil=["viande_rouge", "gras"], fetes=["Repas de famille"], tech=["Roux"])

K("butter_chicken", "Poulet au beurre (butter chicken)", "Murgh makhani", "Asie du Sud › Inde › Delhi", "P", 1, 6, 35, 280, "€€", "Four (gril) ou poêle, cocotte, mixeur.",
  "Du poulet mariné au yaourt et grillé jusqu'à charbonner un peu, dans une sauce tomate-beurre-crème douce, parfumée au fenugrec : le curry préféré des enfants, sans piment fort.",
  [f"1 kg|de hauts de cuisse de poulet|{CUISSE}|3", "1|recette de marinade tandoori|SUB:marinade_tandoori|2", f"800 g|de tomates pelées|{PELEES}|3", f"60 g|de beurre|{BEURRE}|2", f"15 cl|de crème|{CL}|2", f"1 morceau|de gingembre (3 cm) + 4 gousses d'ail|{GING}|1",
   "1 c. à c.|de garam masala|Garam masala|1", "1 c. à s.|de fenugrec séché (kasuri methi)|Fenugrec|1", f"1 c. à c.|de miel|{MIEL}|0", f"1 c. à c.|de sel|{SEL}|1"],
  ["**Mariner.** Poulet en gros morceaux dans la marinade, 4 h au moins (une nuit, c'est mieux).",
   "**Griller.** Sous le gril, plaque haute, 12-15 min en retournant : bords noircis par endroits, 74 °C à cœur.",
   "**Sauce.** Beurre, gingembre et ail râpés 1 min (ça sent, sans brûler) ; tomates, sel, 20 min à feu moyen : réduite d'un tiers. Mixée très lisse.",
   "**Finir.** Crème, garam masala, fenugrec froissé entre les paumes, miel ; poulet, 10 min à feu doux : la sauce nappe, orange et brillante.",
   "**Goûter.** Trop acide : un peu de miel ; pas assez rond : une noix de beurre."],
  tips=["Le fenugrec séché fait le goût de restaurant : il se trouve en épicerie indienne.", "Les restes se réchauffent très bien, et se congèlent."],
  keep="3 jours au frigo ; 3 mois au congélateur.", age=1, cats=["enfants"], profil=["gras"], kids="✓ dès 1 an, sans piment.", side="riz_nature")

# ———————————————————————————————— Desserts
K("creme_brulee", "Crème brûlée", "Crème brûlée", "France › Île-de-France › Paris", "D", 1, 6, 20, 330, "€€", "Ramequins plats, plat à four, chalumeau (ou gril).",
  "Une crème à la vanille cuite très doucement, si onctueuse qu'elle tremble encore, sous une fine plaque de sucre caramélisé qui craque sous la cuillère.",
  [f"50 cl|de crème entière|{CL}|3", f"10 cl|de lait entier|{LAIT}|1", "6|jaunes d'œufs|Jaune d'œuf|3", f"80 g|de sucre|{SUCRE}|2", "1|gousse de vanille|Vanille (gousse)|2", "6 c. à s.|de cassonade|Sucre blanc / roux / cassonade / vergeoise|1"],
  ["**Infuser.** Crème, lait, gousse fendue et grattée portés au frémissement ; hors du feu, couvert, 20 min.",
   "**Appareil.** Jaunes et sucre mélangés à la spatule sans faire mousser (les bulles font une crème trouée) ; crème tiède versée en filet.",
   "**Reposer.** 1 h au frais, puis la mousse retirée à la cuillère : surface lisse.",
   "**Cuire.** Ramequins dans un plat, four 100 °C, 50 min à 1 h : les bords sont pris, le centre tremble comme une gelée quand on secoue doucement.",
   "**Refroidir.** 4 h au frigo au moins.",
   "**Brûler.** Juste avant de servir : une fine couche de cassonade, chalumeau tenu à 5 cm en tournant : sucre ambré, craquant (ou 2 min sous le gril, en surveillant)."],
  tips=["Les 6 blancs : financiers ou meringues.", "Ne brûle qu'au dernier moment : au frigo, le caramel fond."],
  keep="Crèmes cuites : 3 jours au frigo ; caramélisées : à servir aussitôt.", age=1, fetes=["Saint-Valentin", "Repas de famille"], profil=["sucre", "gras"], tech=["Caramel"], zw=[("Blancs d'œufs restants", "→ financiers ou meringues.")])

K("ile_flottante", "Île flottante", "Œufs à la neige", "France › Île-de-France › Paris", "D", 2, 6, 35, 120, "€", "Casserole, batteur, thermomètre (utile), spatule.",
  "Des blancs en neige pochés qui flottent sur une crème anglaise vanillée bien froide, sous un filet de caramel : le dessert de bistrot qu'on rate rarement si on surveille l'anglaise.",
  [f"75 cl|de lait entier|{LAIT}|3", f"6|œufs (séparés)|{OEUF}|3", f"150 g|de sucre|{SUCRE}|2", "1|gousse de vanille|Vanille (gousse)|2", f"80 g|de sucre (caramel)|{SUCRE}|1"],
  ["**Infuser.** Lait et vanille grattée au frémissement, 10 min hors du feu.",
   "**Anglaise.** Jaunes + 100 g de sucre blanchis 1 min ; lait chaud versé en filet ; tout remis à feu doux en remuant en 8 sans arrêt, 6-8 min, jusqu'à 83 °C : la crème nappe la spatule et un doigt y trace un sillon net. Jamais d'ébullition (elle tournerait).",
   "**Refroidir.** Filtrée dans un bol froid, film au contact ; 2 h au frigo.",
   "**Îles.** Blancs + pincée de sel montés en neige ferme, 50 g de sucre en pluie à la fin : brillants. Quenelles pochées dans un lait frémissant, 1 min par face : elles gonflent et se tiennent (ou 30 s au micro-ondes sur une assiette). Égouttées.",
   "**Caramel.** 80 g de sucre + 2 c. à s. d'eau, sans remuer, jusqu'à ambré ; hors du feu.",
   "**Servir.** Anglaise bien froide, îles dessus, caramel en filet."],
  tips=["Anglaise tournée (grains) : mixée aussitôt 30 s au mixeur plongeant, elle redevient souvent lisse.", "Le lait de pochage des îles sert ensuite pour l'anglaise : rien ne se perd."],
  keep="Anglaise : 2 jours au frigo ; îles : le jour même.", age=1, cats=["enfants"], profil=["sucre"], tech=["Crème anglaise", "Caramel"])

K("tarte_tatin", "Tarte Tatin", "Tarte des demoiselles Tatin", "France › Centre-Val de Loire", "D", 2, 8, 30, 50, "€", "Moule à manqué sans fond amovible (ou poêle allant au four), four.",
  "Des pommes confites dans un caramel au beurre jusqu'à devenir ambrées et translucides, sous une pâte croustillante, retournée tiède : le dessert né d'une erreur heureuse à Lamotte-Beuvron.",
  [f"1,2 kg|de pommes qui tiennent (Reinette, Golden, Boskoop)|Pomme|3", f"150 g|de sucre|{SUCRE}|3", f"80 g|de beurre demi-sel|{BEURRE}|2", "1|pâte brisée (recette liée)|SUB:pate_brisee|3", f"20 cl|de crème fraîche (pour servir)|{CF}|1?"],
  ["**Pommes.** Épluchées, en quartiers épais (elles fondent à la cuisson).",
   "**Caramel.** Dans le moule sur feu moyen, sucre et beurre : ça fond, mousse, puis prend une couleur blonde en 6-8 min. ⚠️ Très chaud.",
   "**Ranger.** Hors du feu, quartiers serrés debout, bombé vers le bas (ils tassent en cuisant). Remets 15 min sur feu moyen : le jus des pommes et le caramel bouillonnent et l'ambre remonte.",
   "**Couvrir.** Pâte posée, bords rentrés à l'intérieur entre pommes et moule, piquée.",
   "**Cuire.** 35 min à 190 °C : pâte dorée, caramel qui bouillonne sur les bords.",
   "**Retourner.** 10 min de repos (le caramel se raffermit un peu), plat posé dessus, retourné d'un coup avec des gants. Une pomme restée au moule se remet à sa place."],
  tips=["Le caramel colle au moule : 1 min sur le feu avant de retourner.", "Tiède avec de la crème fraîche épaisse, c'est la tradition."],
  keep="2 jours ; tiède, c'est meilleur.", age=3, profil=["sucre"], tech=["Caramel"], sa=["Jus de pomme chaud"], a=["Cidre"])

K("baba_savarin", "Baba (au rhum ou au sirop d'agrumes)", "Baba au rhum", "France › Grand Est › Lorraine", "D", 2, 8, 40, 180, "€", "Moules à baba ou à savarin, batteur ou robot.",
  "Une pâte levée très légère, séchée puis plongée dans un sirop bouillant jusqu'à ce qu'elle ne fasse plus de bulles, servie avec une chantilly : version rhum traditionnelle, et sans alcool aux agrumes en variante.",
  [f"250 g|de farine|{F45}|3", f"3|œufs|{OEUF}|2", f"80 g|de beurre fondu tiède|{BEURRE}|2", f"10 g|de levure boulangère sèche|{LEV}|1", f"5 cl|de lait tiède|{LAIT}|1", f"500 g|de sucre (sirop) + 1 l d'eau|{SUCRE}|2", "10 cl|de rhum ambré|Rhum ambré / blanc|2", "1|orange (zeste)|Orange|1", f"20 cl|de crème fleurette bien froide|{CL}|1"],
  ["**Pâte.** Levure délayée dans le lait ; farine, sel, 1 c. à s. de sucre, œufs : bats 8 min (robot ou à la main) jusqu'à une pâte élastique qui se décolle. Beurre en 3 fois.",
   "**Pousser.** Moules beurrés remplis à moitié, 1 h au chaud : la pâte arrive en haut.",
   "**Cuire.** 20 min à 180 °C : dorés. Démoulés, laissés sécher une nuit (rassis, ils boivent mieux le sirop).",
   "**Sirop.** Eau, sucre, zeste, 5 min d'ébullition : le sucre a fondu, le sirop est limpide. Le rhum hors du feu.",
   "**Imbiber.** Babas plongés dans le sirop chaud (pas bouillant), retournés, jusqu'à ce qu'ils ne fassent plus de bulles : 2-3 min. Égouttés sur grille.",
   "**Servir.** Arrosés d'un peu de sirop, chantilly peu sucrée."],
  tips=["Pas assez imbibés : ils sont secs au centre ; trop : ils s'effondrent. Le signal est la fin des bulles."],
  var=[("Sans alcool", ["alcohol"], {"Rhum ambré / blanc": [("Orange", 0.5), ("Extrait de vanille liquide", 0.1), ("Mélasse / sirop de canne", 0.4)]},
        "Rhum → **jus de 2 oranges + 1 c. à c. de vanille + 1 c. à s. de sirop de canne** dans le sirop : le baba reste parfumé et ambré. **À tester**.")],
  keep="2 jours au frigo, imbibés.", age=None, kids="✓ dès 3 ans en version sans alcool.", profil=["sucre"], tech=["Pâte levée"])

K("clafoutis_cerises", "Clafoutis aux cerises", "Clafoutis", "France › Nouvelle-Aquitaine › Limousin", "D", 1, 6, 15, 45, "€", "Plat à gratin en terre ou porcelaine.",
  "Des cerises noires entières, avec leurs noyaux qui donnent un goût d'amande, dans un flan épais et doré : le dessert de juin du Limousin.",
  ["600 g|de cerises noires bien mûres|Cerise / griotte|3", f"3|œufs|{OEUF}|2", f"80 g|de sucre|{SUCRE}|2", f"80 g|de farine|{F55}|2", f"30 cl|de lait entier|{LAIT}|2", f"30 g|de beurre|{BEURRE}|1", "1 pincée|de vanille + 1 pincée de sel|Vanille (gousse)|0"],
  ["**Plat.** Beurré généreusement, saupoudré de sucre : il fait une fine croûte caramélisée.",
   "**Pâte.** Œufs et sucre fouettés 1 min, farine et sel, puis le lait peu à peu et la vanille : une pâte à crêpes épaisse, sans grumeaux. 15 min de repos.",
   "**Cerises.** Lavées, équeutées, séchées (mouillées, elles délaient le flan), en une couche serrée.",
   "**Cuire.** Pâte versée, four 180 °C, 40-45 min : gonflé, doré, une lame plantée ressort sèche.",
   "**Servir.** Tiède, saupoudré de sucre : il retombe, c'est normal."],
  tips=["⚠️ Avec noyaux : prévenir les convives ; dénoyaute pour les jeunes enfants (le goût d'amande sera plus discret).", "Hors saison : pommes poêlées au beurre ou poires."],
  keep="2 jours au frais.", age=1, cats=["enfants"], profil=["sucre"])

K("tarte_citron_meringuee", "Tarte au citron meringuée", "Tarte au citron meringuée", "France › Île-de-France › Paris", "D", 2, 8, 60, 120, "€€", "Cercle ou moule 24 cm, casserole, batteur, thermomètre, chalumeau (ou gril).",
  "Une pâte sucrée croustillante, une crème au citron acidulée et fondante, une meringue italienne lisse et dorée : trois préparations, chacune avec son repère.",
  ["1|pâte sucrée (recette liée)|SUB:pate_sucree|3", f"4|citrons non traités (jus et zestes)|{CIT}|3", f"4|œufs|{OEUF}|2", f"150 g|de sucre (crème)|{SUCRE}|2", "20 g|de maïzena|Fécule de maïs (maïzena)|1", f"100 g|de beurre froid|{BEURRE}|2",
   "3|blancs d'œufs|Blanc d'œuf|2", f"180 g|de sucre (meringue)|{SUCRE}|2"],
  ["**Fond.** Pâte foncée, 30 min au frais, piquée ; cuite à blanc 25 min à 165 °C : uniformément blonde. Refroidie.",
   "**Crème citron.** Zestes, jus, œufs, sucre et maïzena fouettés dans une casserole, feu doux, en fouettant sans arrêt : au premier bouillon, elle épaissit d'un coup ; 1 min de plus. Hors du feu, beurre froid en dés, mixée 30 s : lisse et brillante.",
   "**Couler.** Sur le fond froid, lissée ; 1 h au frais : elle se tient.",
   "**Meringue italienne.** Sucre + 5 cl d'eau jusqu'à 118 °C ; pendant ce temps, blancs mousseux. Sirop versé en filet le long du bol, batteur en marche ; fouetter 8 min jusqu'à tiède : épaisse, brillante, en bec d'oiseau.",
   "**Finir.** Meringue à la poche ou à la cuillère en vagues ; dorée au chalumeau ou 2 min sous le gril en surveillant."],
  tips=["Sans thermomètre : le sirop est à 118 °C quand une goutte dans l'eau froide forme une boule souple.", "La meringue italienne est cuite par le sirop : elle se garde sans pleurer."],
  keep="48 h au frigo.", age=1, fetes=["Repas de famille"], profil=["acide", "sucre"], tech=["Pâte sucrée", "Meringue italienne"])

K("panna_cotta", "Panna cotta vanille, coulis de fruits rouges", "Panna cotta", "Europe du Sud › Italie › Piémont", "D", 1, 6, 20, 240, "€", "Casserole, verrines ou ramequins.",
  "Une crème cuite (« panna cotta ») juste prise, qui tremble, parfumée à la vanille, sous un coulis de fruits rouges acidulé : se prépare la veille, se démoule ou se sert en verrine.",
  [f"50 cl|de crème entière|{CL}|3", f"60 g|de sucre|{SUCRE}|2", "1|gousse de vanille|Vanille (gousse)|2", "2 g|d'agar-agar (ou 3 feuilles de gélatine de poisson)|Gélatine de bœuf / poisson, agar-agar, pectine|1", "250 g|de fruits rouges|Framboise / mûre / myrtille|2", f"½|citron|{CIT}|1"],
  ["**Infuser.** Crème, sucre et vanille grattée portés au frémissement ; 10 min hors du feu, couvert.",
   "**Gélifier.** Agar-agar ajouté, 2 min d'ébullition en fouettant (sans ébullition, il ne prend pas) : la crème nappe légèrement la cuillère. Avec la gélatine : feuilles ramollies à l'eau froide, essorées, ajoutées hors du feu.",
   "**Prendre.** Versée dans les verrines, 4 h au frigo : elle tremble quand on les secoue.",
   "**Coulis.** Fruits, 2 c. à s. de sucre et le jus de citron mixés, filtrés : brillant et acidulé.",
   "**Démouler (facultatif).** Ramequins trempés 5 s dans l'eau chaude, couteau sur le bord, retournés."],
  tips=["Trop ferme, elle ressemble à un flan : le bon dosage tremble. Retiens la quantité d'agar-agar exacte.", "Gélatine porcine exclue : agar-agar ou gélatine de poisson."],
  keep="3 jours au frigo.", age=1, cats=["enfants"], profil=["sucre", "gras"], fetes=["Saint-Valentin"])
