# -*- coding: utf-8 -*-
"""Audit des manques TikTok (13/11/2026, AUDIT_MANQUES_TIKTOK_2026-11-13.md §5, priorité 1) : les desserts les plus
filmés sur TikTok et absents d'ATLAS, dans les régions où le dessert était l'angle mort le plus net (Asie du Sud,
Moyen-Orient, Philippines, Amérique latine). Recherche TikTok en cours de blocage serveur pendant cette vague
(erreur 500 répétée sur /search/video après quelques requêtes) : seule la première fiche (rasmalai) a pu être créditée
avant le blocage ; les autres sont à créditer dans une passe ultérieure une fois la recherche de nouveau disponible.
NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *
from recipes_v6_tiktok_plats import C

TT = "https://www.tiktok.com/"
def V(author, vid):
    return (f"@{author}", f"{TT}@{author}/video/{vid}")

IN = "Asie du Sud › Inde"; MO_TR = "Moyen-Orient & Caucase › Turquie"; MO_LIB = "Moyen-Orient › Liban"
PH = "Asie du Sud-Est › Philippines"; BR = "Amérique latine & Caraïbes › Brésil"; PE = "Amérique latine & Caraïbes › Pérou"
CARDA = "Cardamome"; PISTA = "Pistache"; EAUROSE = "Eau de fleur d'oranger / de rose"; SEMFINE = "Semoule de blé (fine/moyenne)"
LAITCOND = "Lait concentré sucré / non sucré"; LAITPOUDRE = "Lait en poudre"; COCORAPEE = "Noix de coco râpée"
PLANTAIN = "Plantain (banane à cuire)"; SAFRAN = "Safran (pistils)"; GHEE = "Beurre clarifié / ghee"
BESAN = "Farine de pois chiche (besan)"

# ---------- Asie du Sud ----------
K("rasmalai", "Rasmalai (palets de fromage frais au lait safrané, cardamome et pistache)", "रसमलाई", IN, "D", 2, 6, 40, 20, "€€",
  "Grande casserole large, mousseline ou tissu propre, passoire.",
  "Le dessert indien culte des fêtes et de l'Aïd : des palets tout légers de fromage frais maison, pochés puis gonflés dans "
  "un sirop, qu'on fait ensuite nager dans un lait réduit parfumé au safran et à la cardamome. Froid, c'est un nuage qui "
  "fond en bouche.",
  [f"2 l|de lait entier (pour le fromage frais, chenna)|{LAIT}|3", f"3 c. à s.|de jus de citron|{CIT}|1",
   f"400 g|de sucre (pour le sirop de cuisson)|{SUCRE}|2", "1,5 l|de lait entier (pour le bain safrané)|-|3",
   f"8|gousses de cardamome écrasées|{CARDA}|1", f"1 pincée|de safran|{SAFRAN}|1?",
   f"3 c. à s.|de pistaches concassées (pour servir)|{PISTA}|1", f"1 c. à c.|d'eau de rose (facultatif)|{EAUROSE}|1?"],
  ["**Chenna.** Lait porté à ébullition ; citron versé en filet hors du feu jusqu'à ce qu'il tranche nettement (petit-lait "
   "clair et grains blancs) ; versé dans une mousseline, rincé à l'eau froide pour enlever le goût du citron, égoutté 30 min "
   "pendu, le poids posé dessus pour presser le reste d'eau 20 min : une pâte souple qui ne colle plus aux doigts.",
   "**Pétrir et façonner.** Chenna pétri 8 à 10 min sur un plan lisse jusqu'à ce qu'il devienne brillant et sans grain : "
   "c'est ce pétrissage qui évite que les palets se fendent à la cuisson. Façonné en 14 à 16 boules lisses, légèrement aplaties.",
   "**Pocher.** Sucre et 1 l d'eau portés à ébullition dans une large casserole (les palets doublent de volume : il leur "
   "faut de la place) ; palets déposés, couvercle, 15 à 18 min à bouillon franc sans y toucher : ils gonflent et deviennent "
   "spongieux. Un palet coupé en deux doit être homogène, sans cœur dur.",
   "**Bain safrané.** En parallèle, le second lait réduit de moitié à feu doux 25 min avec la cardamome, en remuant "
   "souvent ; safran et sucre à volonté ajoutés en fin de réduction.",
   "**Assembler.** Palets égouttés (sirop pressé doucement entre deux mains) glissés dans le lait réduit tiède ; eau de "
   "rose. Au moins 3 h au frais, mieux une nuit : ils absorbent le lait et deviennent moelleux.",
   "**Servir.** Bien froid, pistaches concassées sur le dessus."],
  tips=["Le chenna rate si le lait n'a pas vraiment tranché (petit-lait trouble) : ajoute un peu plus de citron et laisse "
        "reposer 2 min avant d'égoutter.", "Des palets qui se fendent à la cuisson = pétrissage trop court ou pâte encore "
        "humide : égoutte et presse davantage la prochaine fois."],
  keep="3 jours au frigo, bien couverts (ne se congèle pas, le fromage frais devient granuleux).", age=2,
  kids="✓ dès 2 ans, en petits morceaux.", cats=["fetes", "vegetarien"], fetes=["Repas de famille"], profil=["sucre"],
  tech=["Faire un fromage frais maison (chenna, paneer, ricotta express)"], credit=C(V("nombeah", "7618266509651184917")))
K("gajar_halwa", "Gajar halwa (halwa de carotte au lait, cardamome et pistache)", "गाजर का हलवा", IN, "D", 1, 6, 15, 45, "€",
  "Grande poêle ou sauteuse large, râpe.",
  "Le halwa de carotte des maisons indiennes en hiver : des carottes râpées longuement mijotées dans le lait jusqu'à "
  "fondre en une pâte dorée, sucrée et parfumée au ghee, à la cardamome et aux fruits à coque. Tiède avec une boule de "
  "glace à la vanille, c'est un classique qui ne rate jamais.",
  [f"1 kg|de carottes|{CAROTTE}|3", f"1 l|de lait entier|{LAIT}|3", f"5 c. à s.|de ghee (ou de beurre clarifié)|{GHEE}|2",
   f"150 g|de sucre|{SUCRE}|2", f"6|gousses de cardamome écrasées|{CARDA}|1",
   f"3 c. à s.|d'amandes et de pistaches concassées|{PISTA}|1", "2 c. à s.|de raisins secs|Raisins secs|1?"],
  ["**Râper.** Carottes épluchées et râpées fin (grosse râpe) : plus elles sont fines, plus le halwa est fondant.",
   "**Mijoter au lait.** Carottes et lait dans une large poêle, à feu moyen, 30 à 35 min en remuant souvent : le lait "
   "s'évapore et les carottes deviennent tendres et presque sèches. Ne pas couvrir, sinon le lait déborde.",
   "**Enrichir.** Ghee ajouté en deux fois, 5 min à feu moyen-vif en remuant sans arrêt : les carottes prennent une "
   "couleur plus profonde et une odeur de caramel ; sucre et cardamome, 5 min de plus jusqu'à ce que le mélange se "
   "détache du fond de la poêle en masse brillante.",
   "**Servir.** Chaud ou tiède, amandes, pistaches et raisins secs par-dessus."],
  tips=["Le halwa est prêt quand une cuillerée tenue debout ne s'effondre pas : avant ça, il est encore trop liquide.",
        "Il épaissit encore en refroidissant : ne le laisse pas trop sécher dans la poêle."],
  keep="5 jours au frigo ; se réchauffe doucement.", age=1, kids="✓ dès 1 an.", cats=["enfants", "vegetarien"],
  fetes=["Repas de famille"], profil=["sucre", "gras"])
K("barfi", "Barfi (carrés de lait condensé, cardamome et pistache)", "बर्फी", IN, "D", 1, 16, 20, 30, "€",
  "Poêle à fond épais, moule carré ou plat beurré.",
  "Les petits carrés fondants qu'on offre pour Diwali et les mariages : du lait en poudre et du lait concentré cuits "
  "ensemble jusqu'à épaissir, parfumés à la cardamome, puis coupés en losanges décorés de pistaches et parfois d'une "
  "fine feuille d'argent comestible (vark).",
  [f"400 g|de lait en poudre|{LAITPOUDRE}|3", f"1 boîte (400 g)|de lait concentré sucré|{LAITCOND}|3",
   f"3 c. à s.|de ghee|{GHEE}|1", f"6|gousses de cardamome moulues|{CARDA}|1",
   f"4 c. à s.|de pistaches concassées|{PISTA}|1"],
  ["**Préparer le moule.** Plat carré de 18 cm chemisé de papier cuisson légèrement beurré.",
   "**Cuire.** Ghee fondu dans une poêle à fond épais, feu doux ; lait en poudre et lait concentré versés en remuant "
   "sans arrêt : la pâte épaissit et se détache des bords en 10 à 12 min. Cardamome incorporée en fin de cuisson.",
   "**Verser.** Pâte étalée dans le moule sur 1,5 cm, lissée à la spatule humide ; pistaches pressées dessus.",
   "**Reposer.** 2 h à température ambiante (ou 45 min au frigo) jusqu'à ce qu'elle soit ferme mais encore souple.",
   "**Découper.** En carrés ou en losanges de 3 cm, couteau légèrement huilé."],
  tips=["La pâte attache vite au fond dès qu'elle épaissit : baisse le feu plutôt que de la quitter des yeux.",
        "Trop cuite, la barfi devient granuleuse : retire-la du feu dès qu'elle se détache nettement des bords."],
  keep="1 semaine à température ambiante, dans une boîte fermée ; 3 semaines au frigo.", age=2,
  kids="✓ dès 2 ans.", cats=["fetes", "vegetarien"], fetes=["Repas de famille"], profil=["sucre"])
K("ladoo", "Ladoo de besan (boulettes de farine de pois chiche, ghee et cardamome)", "बेसन के लड्डू", IN, "D", 1, 18, 20, 25, "€",
  "Poêle à fond épais, grand saladier.",
  "Les boulettes dorées qu'on roule à la main pour toutes les fêtes indiennes : de la farine de pois chiche torréfiée "
  "longuement dans le ghee jusqu'à sentir la noisette, puis liée au sucre glace et façonnée encore tiède.",
  [f"250 g|de farine de pois chiche (besan)|{BESAN}|3", f"150 g|de ghee|{GHEE}|3", f"180 g|de sucre glace|Sucre glace|2",
   f"5|gousses de cardamome moulues|{CARDA}|1", f"3 c. à s.|de pistaches ou d'amandes concassées|{PISTA}|1"],
  ["**Torréfier.** Ghee fondu à feu doux dans une poêle à fond épais ; besan versé en pluie en remuant sans arrêt, "
   "15 à 20 min à feu doux : la farine passe du jaune pâle au doré, sent la noisette grillée et devient granuleuse et "
   "parfumée. C'est l'étape qui fait toute la différence : ne pas la précipiter.",
   "**Refroidir un peu.** Hors du feu, 8 à 10 min, jusqu'à pouvoir y poser la main sans se brûler mais encore tiède.",
   "**Lier.** Sucre glace, cardamome et la moitié des fruits à coque incorporés : pâte sableuse qui se tient quand on la "
   "presse dans le poing.",
   "**Façonner.** Boulettes de 3 cm roulées fermement entre les paumes tant que c'est encore malléable ; reste des "
   "fruits à coque pressés sur le dessus."],
  tips=["Si la pâte ne se tient pas, elle est encore trop chaude ou trop sèche : ajoute une cuillerée de ghee fondu.",
        "Les enfants adorent rouler les boulettes ; se lave les mains, le ghee chaud brûle."],
  keep="2 semaines à température ambiante, dans une boîte fermée.", age=2, kids="✓ dès 2 ans. Les enfants roulent les boulettes tièdes.",
  cats=["fetes", "vegetarien"], fetes=["Repas de famille"], profil=["sucre", "gras"])
K("falooda", "Falooda (vermicelles, sirop de rose, basilic et glace à la vanille)", "فالودہ", IN, "D", 1, 4, 15, 10, "€€",
  "4 grands verres, casserole.",
  "La boisson-dessert fraîche des étés indiens et pakistanais, en couches à mélanger soi-même : vermicelles cuits, "
  "sirop de rose, graines de basilic gonflées, lait froid et une boule de glace à la vanille qui fond doucement dessus.",
  ["80 g|de vermicelles de riz fins|-|2", f"4 c. à s.|de sirop de rose (ou de grenadine)|{EAUROSE}|1",
   f"1 c. à s.|de graines de basilic ou de chia|{VAN}|1?", f"50 cl|de lait entier bien froid|{LAIT}|2",
   "4 boules|de glace à la vanille|-|2", f"2 c. à s.|de pistaches concassées|{PISTA}|1"],
  ["**Graines.** Graines de basilic (ou chia) trempées 15 min dans 10 cl d'eau : elles gonflent et deviennent "
   "translucides, comme de petites perles.",
   "**Vermicelles.** Cuits 3 à 4 min à l'eau bouillante (comme indiqué sur le paquet) jusqu'à tendres, égouttés, "
   "rincés à l'eau froide pour qu'ils ne collent pas.",
   "**Monter les verres.** Dans chaque verre, dans l'ordre : 1 c. à s. de sirop de rose, les graines gonflées égouttées, "
   "les vermicelles, puis le lait froid versé doucement le long de la paroi.",
   "**Finir.** Une boule de glace à la vanille posée sur le dessus, un trait de sirop de rose, pistaches concassées. "
   "Servi avec une longue cuillère pour remonter les couches du fond."],
  tips=["Tout se prépare à l'avance sauf le montage final : vermicelles et graines gonflées se gardent 1 jour au frigo, "
        "séparément.", "Sans sirop de rose, la grenadine ou un sirop de fraise maison font très bien l'affaire."],
  keep="À monter juste avant de servir ; les éléments préparés se gardent 1 jour au frigo séparément.", age=2,
  kids="✓ dès 2 ans (sans glace pour les tout-petits).", cats=["enfants", "vegetarien", "boissons"], profil=["sucre"])

# ---------- Moyen-Orient ----------
K("maamoul", "Maamoul (petits gâteaux fourrés aux dattes ou aux noix, moule à motifs)", "معمول", MO_LIB, "D", 2, 24, 50, 15, "€€",
  "Moule à maamoul (ou fourchette pour le motif), rouleau à pâtisserie.",
  "Les petits gâteaux sablés qu'on façonne en famille pour l'Aïd et Pâques : une pâte fine à la semoule et au beurre "
  "clarifié, fourrée de pâte de dattes ou de noix à la cannelle, démoulée avec son motif et saupoudrée de sucre glace.",
  [f"500 g|de semoule fine|{SEMFINE}|3", f"200 g|de beurre clarifié (ghee) fondu puis refroidi|{GHEE}|3",
   f"1 c. à c.|de levure boulangère sèche|{LEV}|1", f"8 c. à s.|d'eau de fleur d'oranger|{EAUROSE}|1",
   f"300 g|de pâte de dattes (ou de dattes dénoyautées mixées)|Datte (medjool, deglet)|3",
   f"150 g|de noix ou de noix de Grenoble concassées (pour la version aux noix)|Amande (entière, effilée, poudre)|2",
   f"2 c. à c.|de cannelle|{CANN}|1", "4 c. à s.|de sucre glace (pour saupoudrer)|Sucre glace|1"],
  ["**Pâte.** Semoule et beurre clarifié fondu mélangés à la main, couverts, 2 h à température ambiante : la semoule "
   "boit le gras et devient soyeuse. C'est l'étape qu'on ne peut pas accélérer.",
   "**Finir la pâte.** Levure diluée dans l'eau de fleur d'oranger ajoutée à la semoule, pétrie jusqu'à obtenir une "
   "pâte souple qui ne colle pas ; 30 min de repos couverte.",
   "**Farce.** Pâte de dattes ramollie à la main ; ou noix concassées mêlées à la cannelle et un peu de sucre glace.",
   "**Façonner.** Four à 170 °C. Boule de pâte de 25 g creusée en coupelle, une noix de farce au centre, refermée en "
   "boule sans trace de la farce ; pressée dans le moule à motifs ou marquée à la fourchette, démoulée d'un coup sec.",
   "**Cuire.** 15 à 18 min : à peine dorés dessous, encore pâles dessus (ils ne doivent pas brunir). Refroidis "
   "complètement avant de les toucher : ils sont fragiles chauds.",
   "**Finir.** Roulés ou saupoudrés de sucre glace une fois froids."],
  tips=["Chauds, ils s'effritent : attends qu'ils soient complètement froids pour les manipuler.",
        "Les deux farces (dattes, noix) dans la même fournée : on marque différemment chaque moule pour les reconnaître."],
  keep="2 semaines à température ambiante, dans une boîte fermée ; se congèlent crus, farcis, non cuits.", age=2,
  kids="✓ dès 2 ans. Les enfants façonnent et marquent le motif.", cats=["fetes", "vegetarien"],
  fetes=["Ramadan / Aïd", "Pâques orthodoxe"], profil=["sucre", "gras"])
K("qatayef", "Qatayef (petites crêpes pliées, fourrées à la ricotta ou aux noix, sirop)", "قطايف", MO_LIB, "D", 2, 16, 35, 10, "€€",
  "Poêle à blinis ou poêle antiadhésive, pince à ourler (ou les doigts).",
  "Les petites crêpes qu'on prépare chaque soir de Ramadan : une pâte levée cuite d'un seul côté, fourrée de fromage "
  "frais ou de noix, pincée en demi-lune puis frite ou dorée au four, et trempée dans un sirop à l'eau de fleur "
  "d'oranger.",
  [f"250 g|de farine|{F55}|3", f"1 c. à c.|de levure boulangère sèche|{LEV}|1", f"1 c. à c.|de sucre|{SUCRE}|1",
   f"1 c. à c.|de levure chimique|{LEVC}|1", f"30 cl|de lait tiède|{LAIT}|2",
   f"300 g|de ricotta égouttée (ou de noix concassées sucrées et cannelées, pour la version aux noix)|Ricotta|2",
   f"300 g|de sucre (pour le sirop)|{SUCRE}|2", f"3 c. à s.|d'eau de fleur d'oranger|{EAUROSE}|1",
   f"3 c. à s.|de ghee ou d'huile (pour dorer)|{GHEE}|1"],
  ["**Sirop.** Sucre et 25 cl d'eau portés à ébullition 5 min, eau de fleur d'oranger ajoutée hors du feu ; refroidi "
   "complètement (le sirop chaud détremperait les crêpes).",
   "**Pâte.** Farine, sucre, levures et lait tiède fouettés en pâte lisse et fluide (comme une pâte à blinis) ; 45 min "
   "de repos couverte : elle se couvre de petites bulles.",
   "**Cuire d'un côté.** Petites louches dans une poêle chaude non graissée, feu moyen : des bulles crèvent à la "
   "surface et elle sèche dessus sans jamais être retournée. Retirée dès que le dessus n'est plus brillant.",
   "**Fourrer.** Une cuillerée de ricotta (ou de farce aux noix) au centre du côté sec ; pliée en demi-lune, bords "
   "pincés fermement entre les doigts tous les 5 mm : ils ne doivent pas s'ouvrir à la cuisson.",
   "**Dorer.** À la poêle avec le ghee, 2 min par face, ou 12 min au four à 200 °C, jusqu'à bien dorées.",
   "**Servir.** Trempées quelques secondes dans le sirop froid dès la sortie de la poêle, encore chaudes."],
  tips=["Des bords mal pincés s'ouvrent à la cuisson et la farce coule : humidifie légèrement le bord avant de "
        "pincer si la pâte est trop sèche.", "La version aux noix (pas de produit laitier) convient aux repas sans "
        "fromage pendant le Ramadan."],
  keep="2 jours au frigo une fois farcies ; se congèlent crues, farcies, avant cuisson.", age=2,
  kids="✓ dès 2 ans pour manger ; le pliage demande de la patience, dès 6-7 ans.", cats=["fetes", "vegetarien"],
  fetes=["Ramadan / Aïd"], profil=["sucre"])
K("sutlac", "Sütlaç (riz au lait turc gratiné)", "Sütlaç", MO_TR, "D", 1, 6, 15, 40, "€",
  "Casserole, petits plats individuels allant au four.",
  "Le riz au lait turc, plus ferme et plus parfumé que sa version française : du riz rond cuit longuement dans le "
  "lait sucré, lié à la maïzena, versé dans des petits plats et passé sous le grill jusqu'à ce que le dessus se "
  "marque de belles taches dorées.",
  [f"120 g|de riz rond (dessert)|{RIZ}|3", f"1,2 l|de lait entier|{LAIT}|3", f"150 g|de sucre|{SUCRE}|2",
   f"3 c. à s.|de fécule de maïs (maïzena)|Fécule de maïs (maïzena)|1", f"1 c. à c.|de vanille en poudre|{VAN}|1?",
   f"1 pincée|de cannelle (pour saupoudrer)|{CANN}|1?"],
  ["**Précuire le riz.** Riz et 30 cl d'eau portés à ébullition 10 min jusqu'à ce que l'eau soit absorbée : le riz "
   "démarre sa cuisson sans brûler dans le lait.",
   "**Cuire au lait.** Lait ajouté, feu doux, 25 à 30 min en remuant souvent : le riz devient très tendre et le "
   "mélange épaissit légèrement.",
   "**Lier.** Maïzena délayée dans un peu de lait froid, versée en filet en fouettant ; sucre et vanille, 5 min de "
   "plus à feu doux jusqu'à ce que ça nappe franchement la cuillère.",
   "**Gratiner.** Versé dans des petits plats individuels, à peine remplis ; 8 à 10 min sous le grill du four à "
   "forte chaleur, surveillé sans relâche : le dessus se marque de taches brun doré par endroits sans brûler partout.",
   "**Refroidir.** Au moins 2 h au frigo : il raffermit et se tranche net à la cuillère. Cannelle au moment de servir."],
  tips=["Le grill marque très vite : reste devant le four, 30 secondes d'inattention et ça brûle.",
        "Sans grill, un chalumeau de cuisine ou simplement servi non gratiné reste très bon."],
  keep="4 jours au frigo, couvert.", age=1, kids="✓ dès 1 an.", cats=["enfants", "vegetarien"], profil=["sucre"])

# ---------- Philippines ----------
K("halo_halo", "Halo-halo (glace pilée, fruits, gelées, lait concentré et flan)", "Halo-halo", PH, "D", 2, 4, 30, 60, "€€",
  "Mixeur ou robot (pour la glace pilée), 4 grands verres ou coupes.",
  "Le dessert d'été le plus partagé des Philippines : de la glace pilée surmontée d'une mosaïque de fruits, de "
  "gelées colorées, de haricots rouges sucrés et d'un morceau de flan, le tout noyé de lait concentré qu'on verse au "
  "moment de servir et qu'on mélange (« halo-halo » = « mélangé-mélangé »).",
  ["1 kg|de glaçons (ou glace pilée du commerce)|-|3", "1 boîte (400 g)|de macédoine de fruits au sirop (saba, jacquier, noix de coco)|-|2",
   f"200 g|de haricots rouges sucrés en boîte|{POIS}|2?", f"4 c. à s.|de noix de coco râpée|{COCORAPEE}|1",
   f"4|petits morceaux de flan (recette liée) ou de crème caramel|{OEUF}|2?", f"4 c. à s.|de gelée colorée en dés (facultatif)|{SUCRE}|1?",
   f"1 boîte (400 g)|de lait concentré sucré|{LAITCOND}|3", "4 boules|de glace à la vanille ou à l'ube (igname violette)|-|1?"],
  ["**Glace pilée.** Glaçons mixés par à-coups au robot (ou pilés au torchon) jusqu'à une neige fine mais encore "
   "cristalline, pas de la poudre fondue.",
   "**Monter les verres.** Dans chaque grand verre : macédoine égouttée et haricots rouges au fond, puis la glace "
   "pilée tassée en dôme.",
   "**Décorer.** Noix de coco râpée, dés de gelée, morceau de flan et boule de glace disposés sur le dessus, par "
   "zones bien visibles : c'est un dessert qui se regarde avant de se mélanger.",
   "**Servir.** Lait concentré versé généreusement sur le dessus à table, devant les convives ; chacun mélange tout "
   "avec une longue cuillère avant de manger."],
  tips=["La glace pilée fond vite : prépare tous les éléments d'abord, pile la glace en dernier et serre aussitôt.",
        "Sans jacquier ni ube, des fruits frais (mangue, banane) et une glace à la vanille font un halo-halo très "
        "honorable."],
  keep="À monter et servir immédiatement (la glace pilée fond en quelques minutes).", age=2,
  kids="✓ dès 2 ans, sans gelée dure pour les tout-petits (risque de fausse route).", cats=["enfants", "vegetarien"],
  profil=["sucre"])
K("leche_flan", "Leche flan (flan au lait concentré, caramel bien amer)", "Leche flan", PH, "D", 2, 6, 15, 60, "€€",
  "Moule à flan (llanera) ou moule à manqué, bain-marie, cuit-vapeur ou four.",
  "Le flan des Philippines, plus riche et plus dense que le flan espagnol dont il descend : des jaunes d'œufs, du "
  "lait concentré et du lait évaporé cuits à la vapeur sur un caramel volontairement poussé jusqu'à l'amertume, qui "
  "contrebalance la richesse du flan.",
  [f"10|jaunes d'œufs|{OEUF}|3", f"1 boîte (400 g)|de lait concentré sucré|{LAITCOND}|3",
   "1 boîte (410 g)|de lait évaporé (ou de lait entier)|-|3", f"1 c. à c.|de vanille en poudre|{VAN}|1",
   f"180 g|de sucre (pour le caramel)|{SUCRE}|2"],
  ["**Caramel.** Sucre et 3 c. à s. d'eau dans le moule (ou une casserole si le moule ne va pas sur le feu), à sec "
   "sur feu moyen, sans remuer : ambré puis franchement brun-rouge, presque à la limite de brûler (c'est voulu, "
   "l'amertume équilibre le flan) ; versé aussitôt et incliné pour couvrir le fond.",
   "**Appareil.** Jaunes d'œufs battus sans mousser (à la fourchette, pas au fouet électrique) ; lait concentré, "
   "lait évaporé et vanille incorporés en remuant doucement. Passé au chinois pour enlever les filaments de blanc.",
   "**Verser et couvrir.** Appareil versé sur le caramel froid ; moule couvert hermétiquement de papier aluminium "
   "(l'eau de cuisson ne doit jamais toucher le flan).",
   "**Cuire à la vapeur.** 40 à 45 min dans un cuit-vapeur à feu doux (ou au bain-marie au four à 160 °C) : le flan "
   "est pris quand il tremble légèrement au centre sans être liquide.",
   "**Refroidir.** Complètement, puis au moins 4 h au frigo : il se démoule net.",
   "**Démouler.** Bords décollés au couteau fin, assiette posée dessus, retourné d'un geste sec : le caramel coule "
   "sur le flan."],
  tips=["Pas de mousse dans l'appareil = pas de trous dans le flan : on bat les jaunes à la fourchette, jamais au "
        "fouet électrique.", "Un caramel trop clair donne un flan fade : il doit presque sentir la fumée avant d'être "
        "versé."],
  keep="4 jours au frigo, démoulé et couvert.", age=2, kids="✓ dès 2 ans.", cats=["enfants", "vegetarien"],
  fetes=["Repas de famille"], profil=["sucre", "gras"], tech=["Caramel et cuissons du sucre"])
K("bibingka", "Bibingka (gâteau de riz vapeur-four, feuille de bananier et œuf salé)", "Bibingka", PH, "D", 2, 8, 20, 25, "€€",
  "Moule rond chemisé de feuille de bananier (ou de papier cuisson huilé), four.",
  "Le gâteau qu'on vend sur des braises devant les églises pendant les messes de l'Aube de Noël aux Philippines : "
  "une pâte à la farine de riz gluant, cuite entre chaleur douce et dessus gratiné, garnie de tranches de noix de "
  "coco fraîche et parfois d'œuf de cane salé.",
  [f"250 g|de farine de riz gluant|Farine de riz / riz gluant|3", f"1 c. à c.|de levure chimique|{LEVC}|1",
   f"1 pincée|de sel|{SEL}|1", f"2|œufs|{OEUF}|2", f"150 g|de sucre|{SUCRE}|2", f"25 cl|de lait de coco|{COCO}|2",
   f"25 cl|de lait entier|{LAIT}|2", f"60 g|de beurre fondu (et un peu pour le dessus)|{BEURRE}|2",
   f"80 g|de noix de coco fraîche ou râpée réhydratée, en lamelles|{COCORAPEE}|2",
   "1|œuf dur salé (œuf de cane salé, ou œuf de poule dur, en tranches)|Œuf entier (frais)|1?"],
  ["**Pâte.** Farine de riz, levure et sel mélangés ; œufs, sucre, lait de coco, lait et beurre fondu incorporés au "
   "fouet jusqu'à pâte lisse et fluide, sans grumeaux.",
   "**Préparer le moule.** Four à 190 °C, chaleur tournante si possible. Moule chemisé de feuille de bananier "
   "légèrement passée à la flamme (elle s'assouplit et parfume) ou simplement beurré.",
   "**Cuire.** Pâte versée sur 2 cm ; 15 min au four, puis tranches d'œuf salé et de noix de coco disposées sur le "
   "dessus encore mou, un filet de beurre fondu ; 10 min de plus jusqu'à bien doré et ferme au centre.",
   "**Servir.** Tiède, découpé en parts, directement sur sa feuille de bananier."],
  tips=["Sans feuille de bananier, un moule beurré et fariné marche très bien : le goût change un peu, pas la "
        "texture.", "L'œuf salé est optionnel : sans lui, le gâteau reste un très bon gâteau de riz à la noix de coco."],
  keep="2 jours à température ambiante, couvert ; 4 jours au frigo.", age=2, kids="✓ dès 2 ans, sans l'œuf salé pour les plus petits.",
  cats=["enfants", "vegetarien", "fetes"], fetes=["Noël et Nouvel An"], profil=["sucre"])
K("turon", "Turon (banane plantain et jacquier en rouleaux croustillants, caramel)", "Turon", PH, "D", 1, 8, 20, 15, "€",
  "Poêle ou friteuse, galettes de riz ou feuilles de pâte won-ton.",
  "Le beignet de rue le plus vendu des Philippines : des lamelles de banane plantain bien mûre et un peu de jacquier "
  "mûr, roulées dans une fine galette, frites et caramélisées en surface dans le sucre qui fond à la cuisson.",
  [f"4|bananes plantain bien mûres (peau presque noire)|{PLANTAIN}|3",
   "100 g|de jacquier mûr en boîte, égoutté et effiloché (facultatif)|-|1?",
   "8|feuilles de pâte filo ou de brick, coupées en bandes de 10 cm|Pâte filo / feuilles de brick|2",
   f"5 c. à s.|de sucre roux (vergeoise)|{SUCRE}|2", f"50 cl|d'huile de friture (ou 3 c. à s. pour une cuisson à la poêle)|{HN}|2"],
  ["**Préparer.** Plantains épluchés, coupés en deux dans la longueur puis en lamelles de 1 cm ; roulées dans le "
   "sucre roux pour bien les enrober.",
   "**Rouler.** Une lamelle de plantain (et un peu de jacquier effiloché) posée en biais sur une feuille, bords "
   "repliés et roulée serré comme un nem, extrémité scellée avec une goutte d'eau.",
   "**Cuire.** À la poêle avec 3 c. à s. d'huile, feu moyen, 2 à 3 min par face : la pâte dore et le sucre caramélise "
   "en surface en petites plaques brunes et croustillantes. (Ou en friture à 175 °C, 2 min, même résultat plus "
   "uniforme.)",
   "**Servir.** Égouttés sur papier absorbant, tièdes : l'extérieur craque, l'intérieur est fondant et caramélisé."],
  tips=["Le sucre colle et brûle vite : feu moyen, jamais vif, et surveille les deux dernières minutes.",
        "Sans jacquier, le turon de plantain seul est déjà le classique de base — le jacquier est un ajout, pas un "
        "ingrédient obligatoire."],
  keep="Le jour même, recroustillés 5 min au four si besoin.", age=2, kids="✓ dès 2 ans.",
  cats=["enfants", "vegetarien"], profil=["sucre", "gras"])

# ---------- Amérique latine ----------
K("quindim", "Quindim (petit flan brésilien à la noix de coco et aux jaunes d'œufs)", "Quindim", BR, "D", 2, 8, 15, 35, "€€",
  "8 petits moules à muffin ou ramequins, bain-marie, four.",
  "Le petit dessert doré des fêtes brésiliennes : des jaunes d'œufs, du sucre, du beurre et de la noix de coco râpée "
  "cuits au bain-marie jusqu'à former une fine croûte dorée sur un cœur moelleux et très parfumé.",
  [f"12|jaunes d'œufs|{OEUF}|3", f"250 g|de sucre|{SUCRE}|2", f"100 g|de noix de coco râpée|{COCORAPEE}|3",
   f"50 g|de beurre fondu (et un peu pour les moules)|{BEURRE}|2", f"2 c. à s.|de beurre fondu (pour les moules)|{BEURRE}|1"],
  ["**Préparer les moules.** Four à 170 °C, bain-marie prêt. Moules généreusement beurrés (le quindim colle "
   "facilement s'ils ne sont pas assez graissés).",
   "**Appareil.** Jaunes d'œufs battus à la fourchette avec le sucre jusqu'à dissolution (sans mousser) ; noix de "
   "coco râpée et beurre fondu incorporés ; passé au chinois pour une texture bien lisse.",
   "**Cuire.** Versé dans les moules ; cuits au bain-marie 30 à 35 min, eau frémissante, jusqu'à ce que le dessus "
   "soit doré et ferme au toucher, le centre encore tremblant.",
   "**Refroidir et démouler.** 15 min à température ambiante, puis démoulé chaud sur un plat (comme un flan, il se "
   "démoule mieux tiède que froid).",
   "**Servir.** Tiède ou froid, tel quel."],
  tips=["Pas assez beurré, le quindim reste collé au moule : n'économise pas le beurre sur les parois.",
        "Le centre doit rester un peu tremblant à la sortie du four : il finit de prendre en refroidissant."],
  keep="4 jours au frigo.", age=2, kids="✓ dès 2 ans.", cats=["enfants", "vegetarien", "fetes"], profil=["sucre", "gras"])
K("picarones", "Picarones (beignets péruviens à la citrouille et à la patate douce, sirop de chancaca)", "Picarones", PE, "D", 2, 20, 30, 20, "€",
  "Friteuse ou grande casserole, poche à douille ou grande cuillère, écumoire.",
  "Les beignets en forme d'anneau les plus vendus dans les rues de Lima : une pâte levée à la citrouille et à la "
  "patate douce, frite en forme d'anneau grâce à un trou percé au pouce, et noyée dans un sirop de chancaca (sucre de "
  "canne non raffiné) parfumé à la cannelle et aux clous de girofle.",
  [f"400 g|de citrouille ou de potimarron, cuite et écrasée|{SUCRE}|2", "300 g|de patate douce, cuite et écrasée|Patate douce|2",
   f"300 g|de farine|{F55}|2", f"1 c. à c.|de levure boulangère sèche|{LEV}|1", f"1 c. à c.|de cannelle|{CANN}|1",
   f"1 pincée|de sel|{SEL}|1", f"250 g|de sucre roux (vergeoise, à défaut de chancaca)|{SUCRE}|2",
   f"1 bâton|de cannelle (pour le sirop)|{CANN}|1", "2|clous de girofle|Clou de girofle|1?",
   f"1|écorce d'orange ou de citron|{CIT}|1?", f"1 l|d'huile de friture|{HN}|2"],
  ["**Sirop.** Sucre roux, 25 cl d'eau, bâton de cannelle, clous de girofle et écorce d'agrume portés à ébullition "
   "10 min jusqu'à léger épaississement ; réservé tiède.",
   "**Pâte.** Citrouille et patate douce bien écrasées sans morceaux, mélangées à la farine, la levure, la cannelle "
   "et le sel ; pétrie en pâte souple, collante mais qui se tient à la cuillère ; 1 h de repos couverte, à "
   "température ambiante : elle double de volume.",
   "**Façonner et frire.** Huile à 170 °C. Une bonne cuillerée de pâte étalée sur la main mouillée, un trou percé au "
   "centre avec le pouce, glissée délicatement dans l'huile en formant un anneau ; 2 à 3 min par face : doré et "
   "gonflé, l'anneau se tient tout seul.",
   "**Servir.** Égouttés, aussitôt trempés ou arrosés de sirop de chancaca tiède."],
  tips=["La pâte très collante est normale, ne rajoute pas trop de farine sinon les picarones durcissent : mouille-toi "
        "les mains plutôt.", "Sans chancaca, un sirop de sucre roux à la cannelle donne un goût très proche."],
  keep="Le jour même, meilleurs chauds ; se réchauffent 5 min au four.", age=2, kids="✓ dès 2 ans.",
  cats=["enfants", "vegetarien"], profil=["sucre", "gras"], tech=["Frire en sécurité (et double cuisson)"])
