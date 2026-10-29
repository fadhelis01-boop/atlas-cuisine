# -*- coding: utf-8 -*-
"""Vague 8 (fin) · Auteurs des favoris du 29/10/2026 : goûters, entrées, bases et deux plats végétariens tirés de leurs
vidéos les plus enregistrées (@dinewithtwo, @food.by.ibtissam, @chez.zakia77, @chefsquare, @hoplabretz,
@lardoise_porto_vecchio, @chesterfoodies). Fiches réécrites et créditées. NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *
from recipes_v6_tiktok_plats import C

DINDE_J = "Jambon de dinde / de poulet"; CHEVRE = "Chèvre (frais, bûche)"; LC = "Lait concentré sucré / non sucré"

# ———————————————————————————————— plats végétariens
K("fromage_pane_pommes_terre_paprika", "Petit fromage pané croustillant et pommes de terre rôties au paprika fumé", "Fromage pané", "France › Cuisine du quotidien", "P", 1, 4, 20, 35, "€", "Plaque, 3 assiettes creuses, poêle.",
  "Un petit fromage à croûte fleurie (type Caprice des Dieux ou camembert) pané deux fois et doré à la poêle : croustillant dehors, coulant dedans. Avec des quartiers de pommes de terre rôtis au paprika fumé et une salade à la vinaigrette moutardée.",
  ["2|petits fromages à croûte fleurie (200 g chacun)|Camembert / brie|3", f"1 kg|de pommes de terre|{PDT}|3", f"2 c. à c.|de paprika fumé|{PFUME}|1", f"2|œufs|{OEUF}|2", "80 g|de chapelure|Chapelure|2", f"3 c. à s.|de farine|{F55}|1", f"5 c. à s.|d'huile|{HN}|1", "1|salade verte|Salade (laitue, batavia)|1", "1 c. à s.|de vinaigre de cidre (+ 1 c. à c. de moutarde)|Vinaigre de cidre|1", f"1 c. à s.|de confiture d'airelles ou de figues (facultatif)|Confiture / gelée|1?"],
  ["**Pommes de terre.** En quartiers, 2 c. à s. d'huile, paprika fumé, sel ; 35 min à 210 °C, retournées à mi-cuisson : dorées, tendres au cœur.",
   "**Paner.** Fromages coupés en deux (ou entiers), bien froids ; farine, œuf battu, chapelure, puis une 2e fois œuf et chapelure : aucune faille, sinon il coule ; 15 min au congélateur.",
   "**Dorer.** 3 c. à s. d'huile, feu moyen, 2 à 3 min par face : chapelure dorée, fromage qui se bombe sans percer.",
   "**Servir.** Tout de suite, avec les pommes de terre, la salade vinaigrée et la confiture."],
  keep="Le jour même.", age=3, cats=["vegetarien", "enfants"], profil=["gras", "acide"],
  credit=C(("@food.by.ibtissam", "https://www.tiktok.com/@food.by.ibtissam/video/7538090775851044118")))

# ———————————————————————————————— entrées
K("boules_pomme_terre_mozzarella", "Boules de pommes de terre croustillantes au cœur de mozzarella", "Boules de purée à la mozzarella", "France › Cuisine du quotidien", "E", 1, 16, 30, 20, "€", "Casserole, poêle profonde ou friteuse, 3 assiettes creuses.",
  "Une purée bien sèche relevée d'ail et de parmesan, roulée autour d'un dé de mozzarella, panée et frite : croustillante, filante au milieu. Idéal pour finir un reste de purée ; une sauce yaourt-citron à côté.",
  [f"700 g|de pommes de terre farineuses|{PDT}|3", "125 g|de mozzarella (bien égouttée) en dés|Mozzarella / burrata|3", f"40 g|de parmesan râpé|{PARM}|1", f"1|gousse d'ail|{AIL}|1", f"2|œufs (1 pour la purée)|{OEUF}|2", "100 g|de chapelure|Chapelure|2", f"3 c. à s.|de farine|{F55}|1", f"1/2|botte de persil ou de ciboulette|{PERSIL}|1", f"150 g|de yaourt + ½ citron (sauce)|{YAO}|1", f"50 cl|d'huile de friture|{HN}|1"],
  ["**Purée.** Pommes de terre cuites à l'eau salée 20 min, bien égouttées, 2 min dans la casserole sur le feu : elles fument et sèchent ; écrasées avec parmesan, ail râpé, 1 œuf, herbes, sel ; refroidie.",
   "**Former.** 16 boules, un dé de mozzarella au centre, bien refermées ; farine, œuf battu, chapelure.",
   "**Frire.** 3 min à 175 °C, par petites quantités : bien dorées ; égouttées. (Au four : 20 min à 210 °C, badigeonnées d'huile.)",
   "**Sauce.** Yaourt, jus de citron, sel, herbes : à côté."],
  keep="Le jour même.", age=3, cats=["vegetarien", "enfants", "fetes"], fetes=["Apéritif dînatoire"], profil=["gras", "acide"], tech=["Frire en sécurité"],
  credit=C(("@food.by.ibtissam", "https://www.tiktok.com/@food.by.ibtissam/video/7545509166832520470")))
K("soupe_froide_concombre_zaatar", "Soupe froide de concombre à l'orange, au zaatar et à la fleur d'oranger", "Soupe froide marocaine au concombre", "Afrique du Nord › Maroc", "E", 1, 4, 15, 60, "€", "Mixeur, passoire fine.",
  "Une soupe glacée des jours de canicule : concombre mixé avec du jus d'orange et de citron, quelques gouttes de fleur d'oranger, servie très froide avec un filet d'huile d'olive et du zaatar.",
  ["2|concombres|Concombre|3", "2|oranges (jus) + quelques suprêmes|Orange|2", f"1|citron|{CIT}|2", "1 c. à c.|d'eau de fleur d'oranger|Eau de fleur d'oranger|1", "1 c. à s.|de zaatar|Zaatar|2", f"2 c. à s.|d'huile d'olive|{HO}|1", f"100 g|de yaourt grec (facultatif)|{GREC}|1?", f"1 pincée|de sel|{SEL}|1"],
  ["**Mixer.** Concombres épluchés à moitié (une peau sur deux), épépinés, jus d'orange et de citron, sel, 1 min : très lisse ; passés au tamis pour une soupe soyeuse.",
   "**Parfumer.** Fleur d'oranger, goutte à goutte : elle doit se deviner, pas dominer.",
   "**Refroidir.** 1 h au frigo au moins : bien glacée.",
   "**Servir.** Une cuillerée de yaourt, suprêmes d'orange, huile d'olive, zaatar."],
  keep="1 jour au frigo.", age=1, cats=["vegetarien", "express"], profil=["leger", "acide"],
  credit=C(("@chefsquare", "https://www.tiktok.com/@chefsquare/video/7657215735797714209")))
K("veloute_epluchures_asperges", "Velouté d'épluchures et de talons d'asperges (anti-gaspi)", "Velouté d'asperges anti-gaspi", "France › Anti-gaspi", "E", 1, 4, 15, 30, "€", "Casserole, mixeur, passoire fine.",
  "Les épluchures et les bouts durs des asperges blanches ou vertes, qu'on jette d'habitude, cuits avec une pomme de terre et un oignon : mixés et filtrés, ils donnent un velouté très parfumé. Pendant que les asperges elles-mêmes servent à un autre plat.",
  ["400 g|d'épluchures et talons d'asperges (1 kg d'asperges)|Asperge|3", f"1|pomme de terre|{PDT}|2", f"1|oignon|{OIG}|1", f"20 g|de beurre|{BEURRE}|1", "80 cl|d'eau ou de bouillon de légumes|Bouillon cube légumes|2", f"10 cl|de crème|{CL}|1", f"1/2|citron|{CIT}|1", f"1/2|botte de ciboulette|Ciboulette|1?"],
  ["**Suer.** Oignon émincé, beurre, 5 min : translucide.",
   "**Cuire.** Épluchures, talons coupés en morceaux, pomme de terre en dés, bouillon ; 25 min à frémissement : talons tendres.",
   "**Mixer et filtrer.** 2 min au mixeur ; passé au tamis fin en pressant : on retire les fibres ; velouté lisse.",
   "**Finir.** Crème, sel, quelques gouttes de citron : il se réveille ; ciboulette."],
  keep="2 jours au frigo ; se congèle.", age=1, cats=["vegetarien"], profil=["leger"], zw=[("Épluchures d'asperges", "c'est tout le velouté.")],
  credit=C(("@hoplabretz", "https://www.tiktok.com/@hoplabretz/video/7640778072173710624")))

# ———————————————————————————————— goûters et desserts
K("smores_cookie_bars", "Barres cookie s'mores (biscuit, chocolat, guimauve grillée)", "S'mores cookie bars", "Amérique du Nord › États-Unis", "G", 1, 16, 20, 30, "€€", "Moule carré de 20 cm, papier cuisson.",
  "La vidéo la plus enregistrée de tous les profils lus cette semaine : une pâte à cookie en deux couches, du chocolat et des guimauves au milieu, et des guimauves dorées sous le gril sur le dessus, comme au feu de camp. Un fond de biscuits graham remplacé par des petits-beurre.",
  [f"170 g|de beurre fondu|{BEURRE}|2", f"200 g|de sucre (150 g de cassonade + 50 g de blanc)|{SUCRE}|2", f"1|œuf + 1 jaune|{OEUF}|2", f"250 g|de farine|{F55}|3", f"1/2 c. à c.|de bicarbonate|Bicarbonate de soude|1", "100 g|de petits-beurre écrasés|Biscuits (spéculoos, sablés)|2", "150 g|de chocolat au lait en carrés|Chocolat au lait|2", "150 g|de guimauves sans gélatine de porc (bœuf ou végétales)|-|3", "100 g|de pépites de chocolat|Pépites de chocolat|1"],
  ["**Pâte.** Beurre fondu tiède, sucres, 1 min ; œuf et jaune : lisse et brillant ; farine, bicarbonate, sel, la moitié des petits-beurre, pépites : pâte souple.",
   "**Monter.** Moitié de la pâte tassée au fond du moule chemisé ; carrés de chocolat, la moitié des guimauves coupées en deux ; reste de pâte en morceaux aplatis par-dessus, sans tout couvrir.",
   "**Cuire.** 25 min à 175 °C : bords dorés, centre encore un peu mou.",
   "**Griller.** Reste des guimauves et des biscuits dessus, 2 à 3 min sous le gril en surveillant : guimauves gonflées et dorées (elles brûlent vite) ; 2 h de repos avant de couper au couteau huilé."],
  tips=["Guimauves : la plupart contiennent de la gélatine de porc ; lire l'étiquette (gélatine bovine, halal, ou agar-agar)."],
  keep="4 jours dans une boîte fermée.", age=3, cats=["enfants", "fetes"], fetes=["Anniversaire"], profil=["sucre", "chocolat"],
  credit=C(("@dinewithtwo", "https://www.tiktok.com/@dinewithtwo/video/7577405039552073015"), ("@dinewithtwo", "https://www.tiktok.com/@dinewithtwo/video/7577765944013933837")))
K("moelleux_chocolat_poele", "Moelleux au chocolat cuit à la poêle (sans four)", "Gâteau à la poêle", "France › Cuisine du quotidien", "G", 1, 4, 10, 25, "€", "Poêle antiadhésive de 20 cm avec couvercle.",
  "Le gâteau des studios sans four : une pâte au chocolat très simple cuite à couvert sur feu très doux, qui monte comme au four. Fondant au centre si on l'arrête tôt.",
  [f"100 g|de chocolat noir|{CHOCO}|3", f"80 g|de beurre|{BEURRE}|2", f"2|œufs|{OEUF}|2", f"80 g|de sucre|{SUCRE}|2", f"50 g|de farine|{F55}|2", f"1/2 c. à c.|de levure chimique|{LEVC}|1", f"1 pincée|de sel|{SEL}|1"],
  ["**Fondre.** Chocolat et beurre, 1 min au micro-ondes puis remués : lisse.",
   "**Pâte.** Œufs et sucre fouettés 1 min : mousseux ; chocolat ; farine, levure, sel : pâte lisse.",
   "**Cuire.** Poêle beurrée et farinée (ou papier cuisson au fond), pâte versée ; couvercle, feu le plus doux, 20 à 25 min sans ouvrir les 15 premières : dessus pris, centre qui tremble à peine.",
   "**Démouler.** 10 min de repos, retourné sur une assiette."],
  keep="2 jours sous cloche.", age=1, cats=["enfants", "express"], profil=["sucre", "chocolat"],
  credit=C(("@chez.zakia77", "https://www.tiktok.com/@chez.zakia77/video/7495057814730116374")))
K("fleurs_pommes_feuilletees", "Fleurs de pommes feuilletées (roses de pommes)", "Roses de pommes", "France › Cuisine du quotidien", "D", 1, 6, 25, 40, "€", "Moule à 6 muffins, casserole, mandoline (facultative).",
  "De fines lamelles de pomme attendries, alignées sur une bande de pâte feuilletée tartinée de confiture, roulées en rose et cuites dans un moule à muffins. Un dessert qui fait de l'effet avec trois fois rien.",
  ["2|pommes rouges|Pomme|3", f"1|citron (jus)|{CIT}|2", "1|pâte feuilletée|Pâte feuilletée (prête)|3", "2 c. à s.|de confiture d'abricot|Confiture / gelée|2", f"10 g|de beurre fondu|{BEURRE}|1", f"1 c. à s.|de sucre glace|Sucre glace|1", f"1 pincée|de cannelle (facultatif)|{CANN}|1?"],
  ["**Attendrir.** Pommes épépinées non épluchées, en demi-rondelles de 2 mm ; eau et jus de citron, 3 min au micro-ondes (ou 2 min à frémissement) : souples, elles plient sans casser ; séchées.",
   "**Bandes.** Pâte en 6 bandes de 5 cm ; confiture tiédie étalée, cannelle.",
   "**Rouler.** Lamelles posées en chevauchant sur le bord haut, peau qui dépasse ; bas de la bande replié dessus ; roulé sans serrer ; dans le moule beurré.",
   "**Cuire.** 35 à 40 min à 190 °C (papier aluminium dessus après 20 min si les pétales brunissent) : pâte dorée jusqu'au cœur ; beurre fondu au pinceau, sucre glace."],
  keep="Le jour même.", age=1, cats=["enfants"], profil=["sucre"],
  credit=C(("@chefsquare", "https://www.tiktok.com/@chefsquare/video/7569199130191400214"), ("@chefsquare", "https://www.tiktok.com/@chefsquare/video/7525477011914083606")))
K("dampfnudeln", "Dampfnudeln (petits pains cuits à la vapeur, dessous caramélisé, sauce vanille)", "Dampfnudeln", "France › Grand Est › Alsace", "D", 2, 8, 30, 120, "€", "Sauteuse à fond épais avec couvercle bien hermétique.",
  "La spécialité d'Alsace du Nord et du Palatinat : des boules de pâte levée cuites dans une sauteuse couverte, dans un fond de lait, de beurre et de sucre. La vapeur les gonfle, le fond caramélise et leur fait une croûte croustillante. Avec une compote ou une crème anglaise.",
  [f"500 g|de farine|{F45}|3", f"20 cl|de lait tiède (+ 15 cl pour la cuisson)|{LAIT}|2", f"7 g|de levure boulangère sèche|{LEV}|1", f"60 g|de sucre (+ 1 c. à s.)|{SUCRE}|1", f"1|œuf|{OEUF}|1", f"80 g|de beurre (50 g dans la pâte)|{BEURRE}|2", f"1 pincée|de sel|{SEL}|1", "1|compote de pommes (ou crème anglaise)|SUB:compote_pommes_poires|2"],
  ["**Pâte.** Farine, sucre, levure, sel ; lait tiède et œuf ; pétrie 8 min ; 50 g de beurre mou, 3 min : lisse et élastique ; 1 h à couvert : doublée.",
   "**Bouler.** 8 boules bien serrées, 20 min de repos sous un torchon.",
   "**Cuire.** Dans la sauteuse : 15 cl de lait, 30 g de beurre, 1 c. à s. de sucre, une pincée de sel ; boules dedans ; couvercle fermé (un torchon humide autour s'il fuit) ; 20 à 25 min à feu moyen-doux SANS OUVRIR : elles retombent si on soulève.",
   "**Le signal.** Quand le liquide est évaporé, on entend un léger grésillement et ça sent le caramel : le dessous est doré et croustillant ; feu coupé, 2 min ; servies chaudes avec la compote."],
  tips=["Version salée du Palatinat : avec une soupe de pommes de terre."], keep="Le jour même (réchauffées, elles perdent leur croûte).", age=1, cats=["enfants"], profil=["sucre"], tech=["Pétrir une pâte riche"],
  credit=C(("@hoplabretz", "https://www.tiktok.com/@hoplabretz/video/7626681920893750550")))

# ———————————————————————————————— boulangerie
K("buns_fromage_dinde", "Buns fourrés fromage-dinde à la moutarde (façon boulangerie industrielle, en mieux)", "Bun's maison", "France › Cuisine du quotidien", "Pa", 2, 10, 40, 155, "€", "Robot ou saladier, plaque.",
  "Des petits pains briochés moelleux fourrés d'un mélange de fromage râpé, de jambon de dinde, de crème et de moutarde, comme ceux du rayon boulangerie du supermarché, mais sans additifs. Pour le goûter salé, la boîte à déjeuner ou l'apéritif.",
  [f"500 g|de farine T45|{F45}|3", f"25 cl|de lait tiède|{LAIT}|2", f"8 g|de levure boulangère sèche|{LEV}|1", f"20 g|de sucre|{SUCRE}|1", f"1|œuf (+ 1 jaune pour dorer)|{OEUF}|1", f"70 g|de beurre mou|{BEURRE}|2", f"200 g|de fromage râpé (comté, emmental)|{GRUY}|3", f"4|tranches de jambon de dinde|{DINDE_J}|2", f"2 c. à s.|de crème fraîche|{CF}|1", f"1 c. à s.|de moutarde|{DIJON}|1"],
  ["**Pâte.** Farine, sucre, 10 g de sel, levure ; lait et œuf ; pétrie 5 min ; beurre mou par morceaux, 10 min : souple, se décolle du bol ; 1 h 30 à couvert : doublée.",
   "**Farce.** Fromage, jambon en petits dés, crème, moutarde, poivre : pâte épaisse.",
   "**Façonner.** 10 pâtons de 85 g étalés en disques ; une cuillerée de farce au centre ; bords ramenés et pincés, soudure dessous ; sur la plaque ; 45 min : bien gonflés.",
   "**Cuire.** Jaune d'œuf au pinceau, 18 à 20 min à 180 °C : dorés, dessous qui sonne creux."],
  tips=["Version d'origine : jambon blanc de porc. Version végétarienne : champignons poêlés à la place du jambon."], keep="2 jours dans un sac ; se congèlent cuits.", age=1, cats=["enfants", "pique_nique"], profil=["gras"], tech=["Pétrir une pâte riche"],
  credit=C(("@chesterfoodies", "https://www.tiktok.com/@chesterfoodies/video/7633451982224755991")))

# ———————————————————————————————— bases et sirops
K("lait_concentre_sucre_maison", "Lait concentré sucré maison (lait réduit au sucre)", "Lait concentré sucré", "France › Cuisine du quotidien", "Ba", 1, 1, 5, 50, "€", "Casserole à fond épais, spatule.",
  "L'astuce de grand-mère la plus enregistrée de tous les profils lus : du lait entier et du sucre réduits très doucement jusqu'à une crème épaisse et blonde qui remplace le lait concentré en boîte dans les gâteaux, les flans et le café.",
  [f"1 l|de lait entier|{LAIT}|3", f"200 g|de sucre|{SUCRE}|3", f"20 g|de beurre (facultatif, pour le brillant)|{BEURRE}|1?", "1/2|gousse de vanille (facultatif)|Vanille (gousse)|1?"],
  ["**Dissoudre.** Lait et sucre (et la gousse fendue) dans la casserole, à feu moyen en remuant : le sucre fond, ça frémit.",
   "**Réduire.** Feu doux, 45 à 50 min à petits frémissements, en remuant toutes les 5 min et en raclant le fond : il ne doit pas accrocher ; il passe de blanc à ivoire.",
   "**Le signal.** Il reste environ 30 cl et il nappe la cuillère (le doigt laisse une trace nette) ; beurre ; il épaissit encore en refroidissant.",
   "**Conserver.** En bocal ébouillanté, refroidi puis au frigo."],
  tips=["Prolongé 15 min de plus, il devient une confiture de lait (dulce de leche)."], keep="10 jours au frigo.", age=1, cats=[], profil=["sucre"],
  credit=C(("@chez.zakia77", "https://www.tiktok.com/@chez.zakia77/video/7484609893937499414")))
K("mayonnaise_sans_oeuf", "Mayonnaise sans œuf au lait de soja (au mixeur plongeant)", "Mayonnaise sans œuf", "France › Cuisine du quotidien", "S", 1, 6, 5, 0, "€", "Mixeur plongeant, verre haut et étroit.",
  "Une mayonnaise ferme sans œuf, pour les allergies ou les menus végétaliens : la protéine du lait de soja fait l'émulsion. Tout dans un verre, un coup de mixeur, prête en une minute.",
  ["5 cl|de lait de soja nature (non sucré), froid|Lait de soja|3", f"15 cl|d'huile de tournesol, froide|{HN}|3", f"1 c. à c.|de moutarde|{DIJON}|2", "1 c. à c.|de vinaigre de cidre (ou de jus de citron)|Vinaigre de cidre|2", f"1 pincée|de sel|{SEL}|1"],
  ["**Mettre en verre.** Lait de soja, moutarde, vinaigre, sel au fond ; huile par-dessus ; 1 min d'attente : les couches se séparent.",
   "**Mixer.** Mixeur posé au fond, en marche, sans bouger 10 s : la mayonnaise se forme en dessous ; on remonte lentement : tout prend.",
   "**Ajuster.** Plus ferme : un filet d'huile en mixant ; plus souple : 1 c. à c. d'eau.",
   "**Goûter.** Sel et vinaigre rectifiés ; en pot fermé au frigo, elle raffermit encore en 1 h."],
  tips=["Avec de l'aquafaba (eau de pois chiches, même quantité) à la place du soja : même méthode.", "Le lait d'avoine ou d'amande ne prend pas : c'est la protéine du soja qui fait tenir."],
  keep="5 jours au frigo.", age=1, cats=["vegetarien"], profil=["gras", "acide"],
  credit=C(("@lardoise_porto_vecchio", "https://www.tiktok.com/@lardoise_porto_vecchio/video/7585143044287270146")))
K("sirop_fraise_maison", "Sirop de fraise maison (fraises et sucre, 15 minutes)", "Sirop de fraise", "France › Cuisine du quotidien", "B", 1, 12, 15, 15, "€", "Casserole, passoire fine, bouteille.",
  "Un sirop au vrai goût de fraise, sans colorant ni arôme : des fraises bien mûres (même un peu abîmées) cuites quelques minutes avec le sucre, puis filtrées sans écraser. Dans l'eau, le lait, sur un yaourt ou une glace.",
  ["500 g|de fraises bien mûres|Fraise|3", f"350 g|de sucre|{SUCRE}|3", "25 cl|d'eau|-|2", f"1/2|citron (jus)|{CIT}|2"],
  ["**Cuire.** Fraises équeutées et coupées, sucre, eau ; à frémissement 10 min : les fraises pâlissent, le liquide devient rouge vif.",
   "**Filtrer.** Passoire fine, 15 min sans presser : le sirop reste limpide (la pulpe sert sur un yaourt).",
   "**Finir.** Jus de citron ; 2 min d'ébullition : sirop qui nappe.",
   "**Conserver.** En bouteille ébouillantée, refroidi, au frigo ; une part pour six d'eau fraîche."],
  keep="3 semaines au frigo.", age=1, cats=["enfants"], profil=["sucre", "acide"], zw=[("Fraises trop mûres", "c'est le meilleur usage ; la pulpe filtrée va sur un yaourt.")],
  credit=C(("@lardoise_porto_vecchio", "https://www.tiktok.com/@lardoise_porto_vecchio/video/7653866812949531936")))
