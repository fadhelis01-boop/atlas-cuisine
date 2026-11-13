# -*- coding: utf-8 -*-
"""Audit des manques TikTok (13/11/2026, AUDIT_MANQUES_TIKTOK_2026-11-13.md §5, priorité 4) : les tendances les plus
vues qui ne sont pas liées à une région précise, toutes nées ou relancées sur TikTok. Recherche TikTok bloquée
(erreur serveur) pendant toute cette vague : aucune fiche créditée, à faire dans une passe ultérieure.
NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

US = "Amérique du Nord › États-Unis"; MX = "Amérique latine & Caraïbes › Mexique"; KR = "Asie de l'Est › Corée"
CHEDDAR = "Cheddar"; CORNICHON = "Cornichon"; BABEURRE = "Babeurre"; BOUDOIRS = "Boudoirs / biscuits cuillère"
RAMEN = "Nouilles ramen"; ANCHO = "Piments ancho / chipotle / guajillo / pasilla"; PISTA = "Pistache"

K("smash_burger", "Smash burger (steak haché écrasé à la plancha, bords caramélisés)", "Smash burger", US, "P", 1, 4, 10, 10, "€€",
  "Plancha ou grande poêle très chaude, spatule plate large, papier cuisson.",
  "La méthode qui a relancé le burger sur TikTok : une boule de bœuf haché écrasée d'un coup sec sur une plaque "
  "brûlante, pour maximiser la surface qui caramélise. Fin, très croustillant sur les bords, juteux au centre.",
  [f"400 g|de bœuf haché (15 à 20 % de matières grasses)|{HACHE}|3", "4|pains à burger moelleux|Brioche|2",
   f"4 tranches|de cheddar|{CHEDDAR}|2", f"1|oignon, émincé très fin|{OIG}|1", f"8|tranches de cornichon|{CORNICHON}|1",
   f"4 c. à s.|de sauce burger (mayonnaise, ketchup, un peu de moutarde)|Mayonnaise industrielle|1", f"-|sel, poivre|{SEL}|1"],
  ["**Plancha brûlante.** Poêle ou plancha chauffée à feu vif plusieurs minutes, jusqu'à fumer légèrement : c'est "
   "la chaleur qui fait la croûte, pas le temps.",
   "**Bouler.** Bœuf haché divisé en 4 boules lâches de 100 g, sans trop les travailler (sinon le burger devient "
   "dense).",
   "**Écraser.** Chaque boule posée sur la plaque chaude, écrasée d'un coup sec à la spatule (ou au fond d'une "
   "casserole) jusqu'à 1 cm d'épaisseur et 12 cm de diamètre, en une seule fois ; salée, poivrée, 90 secondes.",
   "**Retourner.** Bords bien bruns et craquants, un peu de sang qui perle sur le dessus ; retourné une seule "
   "fois, fromage posé aussitôt dessus, 60 à 90 secondes de plus : le fromage fond, le centre reste juteux.",
   "**Monter.** Pain légèrement grillé, sauce sur les deux faces, steak-fromage, oignon émincé, cornichons, "
   "chapeau du pain. Servi aussitôt."],
  tips=["Écraser une seule fois, fort et net : appuyer plusieurs fois fait perdre le jus.",
        "Deux fines galettes empilées valent mieux qu'une grosse : plus de surface caramélisée."],
  keep="À manger aussitôt (le burger se tasse en refroidissant).", age=3, kids="✓ dès 3 ans.",
  cats=["enfants", "express"], profil=["gras"])
K("dalgona_coffee", "Dalgona coffee (café fouetté mousseux sur lait glacé)", "달고나 커피", KR, "B", 1, 2, 10, 0, "€",
  "Fouet électrique ou shaker, 2 grands verres.",
  "La boisson qui a occupé tout le monde pendant les confinements : du café soluble, du sucre et de l'eau chaude "
  "fouettés longuement jusqu'à une mousse couleur caramel, posée en nuage sur un verre de lait bien froid.",
  [f"4 c. à s.|de café soluble|-|2", f"4 c. à s.|de sucre|{SUCRE}|1", f"4 c. à s.|d'eau chaude|{EAU}|1",
   f"40 cl|de lait entier bien froid (et des glaçons)|{LAIT}|2"],
  ["**Fouetter.** Café soluble, sucre et eau chaude dans un bol ; fouettés 3 à 5 min au fouet électrique (ou "
   "énergiquement à la main, 8 à 10 min) jusqu'à une mousse épaisse, couleur caramel clair, qui se tient en pic "
   "souple sur le fouet.",
   "**Monter.** Glaçons et lait froid dans chaque verre.",
   "**Poser.** La mousse de café déposée délicatement à la cuillère sur le lait, en dôme, sans la mélanger.",
   "**Servir.** Avec une longue cuillère : on mélange soi-même à table, en regardant les deux couleurs se mêler."],
  tips=["La mousse ne monte pas sans café soluble (le café moulu ne fonctionne pas, il n'a pas la bonne "
        "structure).", "Sans fouet électrique, ça marche aussi à la main, juste plus long et plus fatigant pour "
        "le bras."],
  keep="La mousse se garde 1 h à température ambiante avant de s'affaisser ; à préparer juste avant de servir.",
  age=6, kids="Avec de la chicorée ou un café très dilué pour les enfants, dès 6 ans.", cats=["boissons"],
  profil=["sucre"])
K("butter_board", "Butter board (planche de beurre tartiné, miel et herbes, à tremper)", "Butter board", US, "E", 1, 6, 10, 0, "€€",
  "Une grande planche ou un plat plat, un petit couteau à tartiner.",
  "L'apéritif qui a explosé sur TikTok : du beurre très mou étalé en vagues sur toute une planche, arrosé de "
  "miel, parsemé d'herbes et de fleur de sel, avec du pain chaud à tremper directement dedans.",
  [f"250 g|de beurre doux, bien mou|{BEURRE}|3", f"3 c. à s.|de miel|{MIEL}|2",
   f"2 c. à s.|d'herbes fraîches ciselées (thym, persil, ciboulette)|{PERSIL}|1", f"1 c. à c.|de fleur de sel|{SEL}|1",
   f"1 c. à c.|de piment en poudre ou de paprika fumé (facultatif)|{PFUME}|1?", "1|baguette ou pain de campagne, chaud|Baguette tradition|2"],
  ["**Étaler.** Beurre très mou étalé directement sur la planche à la spatule, en vagues et en creux (pas lisse : "
   "le relief retient le miel et les herbes).",
   "**Garnir.** Miel versé en filet dans les creux ; herbes ciselées, fleur de sel et paprika parsemés sur le "
   "dessus.",
   "**Servir.** Aussitôt, avec le pain chaud coupé en tranches ou en morceaux à côté, pour tremper directement "
   "dans le beurre."],
  tips=["Le beurre doit vraiment être mou (sorti 1 h avant) : froid, il ne s'étale pas en vagues et se déchire.",
        "Selon la saison : zeste d'agrume et romarin en hiver, basilic et tomates séchées en été."],
  keep="À préparer et manger dans l'heure (le beurre regraisse en refroidissant trop).", age=2,
  kids="✓ dès 2 ans, sans piment.", cats=["enfants", "vegetarien", "express"], profil=["gras", "sucre"])
K("chaffle", "Chaffle (gaufre minute au fromage, sans farine)", "Chaffle", US, "P", 1, 2, 5, 8, "€",
  "Petit gaufrier (ou poêle antiadhésive).",
  "La gaufre expresse devenue virale chez ceux qui réduisent le pain : juste un œuf et du fromage râpé, cuits "
  "dans un gaufrier jusqu'à dorés et croustillants, pour un sandwich ou un petit-déjeuner salé sans farine.",
  [f"2|œufs|{OEUF}|2", f"120 g|de mozzarella ou de cheddar râpé|{CHEDDAR}|2", f"1 c. à c.|de levure chimique (facultatif, pour plus de tenue)|{LEVC}|1?"],
  ["**Mélanger.** Œufs battus avec le fromage râpé (et la levure si utilisée) : pâte assez liquide, parsemée de "
   "fromage.",
   "**Cuire.** Gaufrier chaud et légèrement huilé ; moitié de la pâte versée, couvercle fermé, 3 à 4 min : bien "
   "doré et ferme, le fromage a croustillé sur les bords.",
   "**Servir.** Tiède, nature, en sandwich (jambon-fromage) ou avec un œuf au plat par-dessus."],
  tips=["Sans gaufrier : à la poêle antiadhésive, comme une petite omelette épaisse, 2 min par face.",
        "Une pointe d'ail en poudre ou de herbes de Provence dans la pâte change agréablement le goût."],
  keep="Le jour même, recroustillé 2 min au four ou au grille-pain.", age=2, kids="✓ dès 2 ans.",
  cats=["enfants", "express", "brunch"], profil=["gras"])
K("baked_oats", "Baked oats (avoine cuite au four façon gâteau, banane et cannelle)", "Baked oats", US, "D", 1, 1, 5, 20, "€",
  "Petit plat à four individuel ou ramequin.",
  "Le petit-déjeuner viral qui ressemble à un gâteau mais se mange à la cuillère : de l'avoine, une banane "
  "écrasée, un œuf et du lait, cuits au four jusqu'à ce que le dessus soit doré et le centre encore moelleux.",
  [f"50 g|de flocons d'avoine|Avoine (flocons)|3", "1|banane mûre, écrasée|Banane|3", f"1|œuf|{OEUF}|2",
   f"10 cl|de lait|{LAIT}|2", f"1 c. à c.|de levure chimique|{LEVC}|1", f"1/2 c. à c.|de cannelle|{CANN}|1",
   "4 carrés|de chocolat noir (facultatif)|Chocolat noir|1?"],
  ["**Mélanger.** Tous les ingrédients fouettés ensemble dans le plat de cuisson lui-même (un seul récipient "
   "sale) : pâte assez liquide, homogène.",
   "**Garnir.** Carrés de chocolat enfoncés dans la pâte si utilisés.",
   "**Cuire.** Four à 190 °C, 18 à 22 min : le dessus est doré et ferme, le centre reste moelleux et à peine "
   "tremblant.",
   "**Servir.** Tiède, directement dans son plat, à la cuillère."],
  tips=["Se prépare la veille au soir dans le plat, cuit le matin directement sorti du frigo (2 à 3 min de plus).",
        "Avec des myrtilles ou des pépites de chocolat à la place de la banane : toujours la même base."],
  keep="2 jours au frigo, réchauffé quelques secondes.", age=1, kids="✓ dès 1 an.", cats=["enfants", "vegetarien", "brunch"],
  profil=["sucre"])
K("birria_ramen", "Birria ramen (bouillon de bœuf aux piments mexicains, nouilles ramen)", "Birria ramen", MX, "P", 2, 4, 25, 180, "€€",
  "Cocotte, mixeur, casserole pour les nouilles.",
  "La fusion la plus virale des dernières années : le bouillon profond et épicé de la birria mexicaine (bœuf "
  "longuement mijoté aux piments séchés) servi sur des nouilles ramen plutôt que dans des tacos, avec les mêmes "
  "quartiers de citron vert et d'oignon cru pour relever.",
  [f"1 kg|de paleron ou de joue de bœuf, en gros morceaux|Paleron|3", f"4|piments séchés (ancho, guajillo)|{ANCHO}|2",
   f"4 gousses|d'ail|{AIL}|1", f"1|oignon|{OIG}|1", f"2|tomates|{TOM}|2", f"1 c. à c.|de cumin|{CUMIN}|1",
   f"2|feuilles de laurier|{LAURIER}|1", f"2|paquets de nouilles ramen fraîches|{RAMEN}|2",
   f"2|citrons verts|Citron vert|1", f"1/2|oignon rouge, en fines lamelles (pour servir)|{OIG}|1",
   f"1/2 bouquet|de coriandre|{CORI}|1"],
  ["**Piments.** Épépinés, trempés 15 min dans l'eau chaude jusqu'à souples, puis mixés avec un peu de leur eau, "
   "l'ail, l'oignon et les tomates : une pâte lisse et rouge sombre.",
   "**Mijoter.** Bœuf doré en cocotte, pâte de piments ajoutée, cumin et laurier, couvert d'eau à hauteur ; "
   "2 h 30 à 3 h à petits bouillons couverts, jusqu'à ce que la viande s'effiloche à la fourchette.",
   "**Effilocher.** Bœuf retiré, effiloché grossièrement à deux fourchettes ; bouillon dégraissé en surface si "
   "besoin et goûté, rectifié en sel.",
   "**Nouilles.** Cuites 2 à 3 min à l'eau bouillante selon le paquet, égouttées.",
   "**Servir.** Nouilles au fond du bol, bœuf effiloché par-dessus, bouillon chaud versé dessus ; oignon rouge, "
   "coriandre et quartiers de citron vert pour chacun, à presser soi-même."],
  tips=["Le bouillon se prépare très bien la veille, il ne fait que gagner en profondeur ; les nouilles se cuisent "
        "au dernier moment.", "Sans piments séchés mexicains : un mélange de paprika fumé et d'un peu de piment "
        "d'Espelette donne une couleur et un goût proches, en moins complexe."],
  keep="Bouillon et viande, 3 jours au frigo ou 2 mois au congélateur ; nouilles cuites au moment.", age=4,
  kids="✓ dès 4 ans, bouillon moins pimenté pour eux.", cats=[], profil=["epice", "gras", "acide"])
K("chocolat_dubai", "Chocolat façon Dubaï (tablette pistache et kadaïfi croustillant)", "Dubai chocolate", "Moyen-Orient & Caucase › Émirats arabes unis", "D", 2, 8, 25, 30, "€€€",
  "Moule à tablette ou moule à cake, bain-marie.",
  "La tablette devenue phénomène mondial sur TikTok en 2024 : une coque de chocolat, une farce de pâte de "
  "pistache et de cheveux d'ange (kadaïfi) dorés au beurre jusqu'à croustillants, recouverte d'une seconde couche "
  "de chocolat.",
  [f"400 g|de chocolat au lait ou noir, en pastilles|{CHOCO}|3", f"150 g|de pâte de pistache (ou de pistaches mixées avec un peu d'huile neutre)|{PISTA}|3",
   "100 g|de cheveux d'ange (kadaïfi), ou à défaut de pâte filo émincée très finement|Pâte filo / feuilles de brick|3",
   f"40 g|de beurre|{BEURRE}|2", f"2 c. à s.|de pistaches concassées (pour le décor)|{PISTA}|1"],
  ["**Dorer le kadaïfi.** Cheveux d'ange (ou pâte filo émincée en fils très fins) effilochés à la main pour les "
   "séparer, dorés à sec à la poêle avec le beurre, 6 à 8 min en remuant sans arrêt : couleur caramel, bien "
   "croustillants. Refroidis complètement.",
   "**Tempérer le chocolat.** Chocolat fondu au bain-marie doucement, sans dépasser 45 °C ; refroidi en remuant "
   "jusqu'à 28-29 °C puis légèrement réchauffé à 31-32 °C (ou simplement fondu puis utilisé tiède, pour une "
   "version moins technique mais qui blanchira un peu en séchant).",
   "**Première couche.** Fine couche de chocolat versée et étalée dans le moule, remontée sur les bords au "
   "pinceau ; 10 min au frigo pour qu'elle fige.",
   "**Farce.** Kadaïfi doré refroidi mélangé à la pâte de pistache : pâte épaisse et croustillante, étalée sur le "
   "chocolat figé.",
   "**Refermer.** Reste du chocolat versé par-dessus, lissé ; pistaches concassées sur le dessus ; 30 min au "
   "frigo jusqu'à bien ferme.",
   "**Démouler.** D'un coup sec, tranché en carrés ou en barres."],
  tips=["Sans tempérage précis, le chocolat garde un peu moins de croquant et peut légèrement blanchir en "
        "séchant : ça reste très bon, juste moins parfait visuellement.", "Le kadaïfi doit être complètement "
        "froid avant de le mélanger à la pâte de pistache, sinon elle devient huileuse."],
  keep="2 semaines au frigo, dans une boîte hermétique (le kadaïfi ramollit à l'air libre).", age=3,
  kids="✓ dès 3 ans.", cats=["vegetarien", "fetes"], profil=["sucre", "gras"])
K("cinnamon_rolls", "Cinnamon rolls (brioches roulées à la cannelle, glaçage au fromage frais)", "Cinnamon rolls", US, "G", 2, 12, 30, 150, "€€",
  "Rouleau à pâtisserie, plat à four, robot ou pétrissage à la main.",
  "Les roulés moelleux du brunch américain, viraux pour leur cœur qui s'étire en spirale de cannelle fondue, "
  "nappés tièdes d'un glaçage au fromage frais qui fond un peu en coulant dans les plis.",
  [f"500 g|de farine|{F55}|3", f"7 g|de levure boulangère sèche|{LEV}|2", f"30 cl|de lait tiède|{LAIT}|2",
   f"70 g|de sucre|{SUCRE}|2", f"1|œuf|{OEUF}|1", f"80 g|de beurre fondu|{BEURRE}|2", f"1 pincée|de sel|{SEL}|1",
   f"100 g|de beurre mou (pour la farce)|{BEURRE}|2", f"100 g|de sucre roux (vergeoise, pour la farce)|{SUCRE}|2",
   f"2 c. à s.|de cannelle (pour la farce)|{CANN}|1", f"100 g|de fromage à tartiner (pour le glaçage)|Fromage à tartiner / fondu|2",
   f"80 g|de sucre glace (pour le glaçage)|Sucre glace|1", f"3 c. à s.|de lait (pour le glaçage)|{LAIT}|1"],
  ["**Pâte.** Levure diluée dans le lait tiède, 5 min ; farine, sucre, œuf, beurre fondu et sel ajoutés, pétris "
   "8 à 10 min jusqu'à pâte souple et élastique ; 1 h de repos couverte dans un endroit tiède : elle double de "
   "volume.",
   "**Étaler.** Pâte étalée en grand rectangle de 40 x 30 cm sur un plan fariné.",
   "**Farce.** Beurre mou étalé sur toute la surface ; sucre roux et cannelle mélangés, saupoudrés dessus.",
   "**Rouler.** Enroulé serré dans le sens le plus long, en boudin ; coupé en 12 tronçons de 3 cm au fil de "
   "cuisine ou au couteau bien aiguisé.",
   "**Lever et cuire.** Tronçons posés serrés dans un plat beurré, espacés d'1 cm (ils vont encore gonfler) ; "
   "30 min de pousse supplémentaire ; four à 180 °C, 20 à 25 min : dorés dessus, encore moelleux au centre.",
   "**Glacer.** Fromage à tartiner, sucre glace et lait fouettés en glaçage fluide ; versé sur les rouleaux "
   "encore tièdes, aussitôt."],
  tips=["Coupés au fil de cuisine (glissé sous le boudin et croisé par-dessus) plutôt qu'au couteau : ils ne "
        "s'écrasent pas.", "Se préparent la veille jusqu'à la levée finale, gardés au frigo une nuit ; sortis "
        "1 h avant de cuire pour qu'ils reviennent à température."],
  keep="2 jours à température ambiante, couverts ; se congèlent cuits, sans le glaçage.", age=2,
  kids="✓ dès 2 ans. Les enfants étalent la farce et roulent.", cats=["enfants", "vegetarien", "brunch"],
  fetes=["Repas de famille"], profil=["sucre", "gras"])
K("red_velvet_cake", "Red velvet cake (gâteau rouge cacao, glaçage au fromage frais)", "Red velvet cake", US, "D", 2, 10, 30, 35, "€€",
  "2 moules à manqué de 20 cm, fouet électrique.",
  "Le gâteau américain à la couleur spectaculaire et au goût tout en douceur : une mie rouge sombre à peine "
  "cacaotée, acidulée par le babeurre et le vinaigre, entre deux couches d'un glaçage au fromage frais bien "
  "crémeux.",
  [f"300 g|de farine|{F55}|3", f"2 c. à s.|de cacao en poudre non sucré|Cacao en poudre non sucré|2",
   f"1 c. à c.|de bicarbonate de soude|Bicarbonate de soude|1", f"1 pincée|de sel|{SEL}|1",
   f"300 g|de sucre|{SUCRE}|2", f"20 cl|d'huile neutre|{HN}|2", f"2|œufs|{OEUF}|2",
   f"24 cl|de babeurre (ou lait + citron)|{BABEURRE}|2", f"1 c. à c.|de vinaigre blanc|{CIDRE}|1",
   f"1 c. à c.|de vanille en poudre|{VAN}|1", f"1 c. à c.|de colorant alimentaire rouge (facultatif)|-|1?",
   f"250 g|de fromage à tartiner|Fromage à tartiner / fondu|3", f"100 g|de beurre mou (glaçage)|{BEURRE}|2",
   f"150 g|de sucre glace (glaçage)|Sucre glace|2"],
  ["**Pâte.** Farine, cacao, bicarbonate et sel tamisés ensemble. Dans un autre saladier : sucre et huile "
   "fouettés, œufs incorporés un à un, puis babeurre, vinaigre, vanille et colorant.",
   "**Mélanger.** Ingrédients secs incorporés en trois fois au mélange liquide, à la spatule, juste assez pour "
   "homogénéiser : ne pas trop travailler, sinon le gâteau durcit.",
   "**Cuire.** Four à 175 °C. Répartie dans les deux moules beurrés et chemisés ; 25 à 30 min : un cure-dent "
   "piqué au centre ressort sec.",
   "**Refroidir.** Complètement sur une grille avant de glacer, sinon le glaçage fond.",
   "**Glaçage.** Fromage à tartiner, beurre mou et sucre glace fouettés ensemble jusqu'à lisse et aéré.",
   "**Monter.** Un disque de gâteau, glaçage étalé généreusement, second disque posé dessus, reste du glaçage "
   "sur le dessus et les bords."],
  tips=["Sans colorant, le gâteau reste très bon mais prend une teinte brun-rouge naturelle plutôt que rouge "
        "vif : c'est une question d'apparence, pas de goût.", "Le vinaigre et le babeurre réagissent avec le "
        "bicarbonate pour une mie bien aérée : ne pas les sauter."],
  keep="4 jours au frigo, glacé.", age=2, kids="✓ dès 2 ans.", cats=["enfants", "vegetarien", "fetes"],
  fetes=["Anniversaire"], profil=["sucre", "gras"])
K("trifle_anglais", "Trifle anglais (génoise au sherry, crème pâtissière, fruits et chantilly en verrine)", "Trifle", "Europe du Nord › Royaume-Uni", "D", 2, 8, 30, 0, "€€",
  "Grand bol en verre (pour voir les couches), fouet.",
  "Le dessert des fêtes anglaises, monté en couches dans un grand bol transparent pour qu'on en voie l'empilement : "
  "génoise ou boudoirs imbibés, confiture, fruits, crème pâtissière et une chantilly généreuse, parfois réveillés "
  "d'un trait de sherry.",
  [f"200 g|de boudoirs ou de génoise toute prête, en morceaux|{BOUDOIRS}|3", f"6 c. à s.|de confiture de framboise ou de fraise|Confiture / gelée|2",
   "3 c. à s.|de jus d'orange (ou de sherry pour la version adulte)|Orange|1", f"50 cl|de crème pâtissière (recette liée ou toute prête)|{LAIT}|3",
   "300 g|de framboises et de fraises (fraîches ou surgelées)|Fraise|3", f"30 cl|de crème fleurette bien froide|{CL}|2",
   f"2 c. à s.|de sucre glace|Sucre glace|1", f"3 c. à s.|d'amandes effilées, torréfiées (pour le décor)|Amande (entière, effilée, poudre)|1?"],
  ["**Base.** Boudoirs tassés au fond du grand bol, confiture étalée dessus, jus d'orange (ou sherry) versé "
   "pour bien les imbiber.",
   "**Fruits.** Framboises et fraises réparties sur la base imbibée, en réservant quelques-unes pour le dessus.",
   "**Crème.** Crème pâtissière froide versée en couche égale par-dessus les fruits, lissée.",
   "**Chantilly.** Crème fleurette bien froide montée en chantilly ferme avec le sucre glace ; étalée en dernière "
   "couche, en vagues à la cuillère.",
   "**Finir.** Fruits réservés et amandes torréfiées sur le dessus.",
   "**Reposer.** Au moins 2 h au frigo avant de servir : les couches se tiennent mieux et les saveurs se "
   "mêlent."],
  tips=["Un grand bol transparent est presque la moitié du plaisir : c'est un dessert qui se montre à table "
        "avant d'être mangé.", "La version aux enfants se fait avec du jus d'orange ; celle des adultes, avec un "
        "trait de sherry ou de porto dans la base."],
  var=[("Sans alcool", ["alcohol"], {}, "Déjà proposée en version jus d'orange par défaut ici ; le sherry est une option pour les adultes, jamais la base.")],
  keep="2 jours au frigo, couvert.", age=2, kids="✓ dès 2 ans, version au jus d'orange.", cats=["enfants", "vegetarien", "fetes"],
  fetes=["Noël et Nouvel An"], profil=["sucre", "gras"])
K("corn_ribs", "Corn ribs (épis de maïs taillés en côtes, épices et beurre)", "Corn ribs", US, "A", 1, 4, 15, 15, "€",
  "Couteau bien aiguisé (ou un maillet pour amorcer), four ou friteuse.",
  "L'accompagnement qui a fasciné TikTok par sa seule découpe : un épi de maïs fendu en quartiers qui se "
  "recourbent à la cuisson comme des travers de porc miniatures, rôtis avec du beurre et des épices, à manger "
  "avec les doigts.",
  [f"4|épis de maïs frais (ou surgelés, décongelés)|-|3", f"4 c. à s.|de beurre fondu|{BEURRE}|2",
   f"1 c. à c.|de paprika fumé|{PFUME}|1", f"1/2 c. à c.|d'ail en poudre|{AIL}|1", f"-|sel|{SEL}|1",
   f"2 c. à s.|de parmesan râpé (facultatif)|{PARM}|1?", "1|citron vert (pour servir)|Citron vert|1?"],
  ["**Fendre.** Épis coupés en tronçons de 6 cm ; chaque tronçon fendu en quartiers dans la longueur au gros "
   "couteau (amorcer le centre avec la pointe, puis presser fermement : c'est la découpe qui demande le plus "
   "d'attention, les grains sont durs).",
   "**Enrober.** Quartiers roulés dans le beurre fondu, le paprika, l'ail en poudre et le sel.",
   "**Cuire.** Four à 220 °C, 15 à 18 min (ou friteuse à 190 °C, 6 à 8 min) : les grains dorent et les quartiers "
   "se recourbent légèrement vers l'extérieur en refroidissant, comme des travers.",
   "**Servir.** Parmesan râpé et un trait de citron vert dessus, aussitôt, à manger avec les doigts."],
  tips=["La découpe est le seul geste délicat : un couteau large et bien aiguisé, et presser d'un coup sec "
        "plutôt que de scier.", "Les enfants adorent le format mais pas forcément la découpe : à leur confier "
        "déjà fendus."],
  keep="Le jour même, recroustillés 5 min au four.", age=3, kids="✓ dès 3 ans, en tronçons plus petits.",
  cats=["enfants", "vegetarien", "express"], profil=["gras"])
K("cronut", "Cronut (viennoiserie frite façon croissant-donut, glaçage et sucre)", "Cronut", US, "G", 3, 10, 60, 180, "€€€",
  "Rouleau à pâtisserie, emporte-pièces ronds (deux tailles), friteuse ou grande casserole.",
  "L'hybride né à New York et devenu culte sur les réseaux : une pâte feuilletée levée façon croissant, détaillée "
  "en anneaux, frite plutôt que cuite au four, glacée et décorée comme un donut. Un croissant qui a la légèreté "
  "feuilletée et le croustillant de la friture.",
  [f"500 g|de pâte à croissant (recette liée, ou pâte feuilletée levée toute prête)|{F55}|3",
   f"1 l|d'huile de friture|{HN}|3", f"150 g|de sucre glace|Sucre glace|2", f"3 c. à s.|de lait|{LAIT}|1",
   f"1 c. à c.|de vanille en poudre|{VAN}|1", f"2 c. à s.|de vermicelles en sucre ou de pépites colorées (facultatif)|{SUCRE}|1?"],
  ["**Détailler.** Pâte à croissant étalée sur 1 cm ; anneaux détaillés à l'emporte-pièce (grand cercle de "
   "9 cm, petit cercle de 3 cm au centre) ; posés sur du papier cuisson, 30 min de pousse à température "
   "ambiante.",
   "**Frire.** Huile à 170 °C ; anneaux frits délicatement, 2 à 3 min par face jusqu'à bien dorés et gonflés : "
   "ils doublent presque de volume, le feuilletage se détache en couches visibles.",
   "**Égoutter.** Sur une grille, 10 min : ils doivent complètement refroidir avant d'être glacés, sinon le "
   "glaçage fond et coule sans accrocher.",
   "**Glacer.** Sucre glace, lait et vanille fouettés en glaçage lisse et épais ; cronuts trempés face dessus "
   "dans le glaçage, décorés aussitôt de vermicelles avant qu'il ne fige."],
  tips=["Une huile pas assez chaude donne un cronut gorgé de gras et pas assez gonflé : vérifie la température "
        "au thermomètre plutôt qu'à l'œil.", "Les chutes de pâte (centres et bords) se frient aussi, en petites "
        "bouchées à glacer pareillement."],
  keep="Le jour même, meilleur à peine tiède ; se ramollit vite.", age=3, kids="✓ dès 3 ans.",
  cats=["enfants", "vegetarien", "fetes"], profil=["sucre", "gras"])
