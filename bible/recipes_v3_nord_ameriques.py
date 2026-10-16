# -*- coding: utf-8 -*-
"""Vague 4 · Audit du chef (16/10/2026) : Europe du Nord, centrale et de l'Est, Amérique du Nord, Amérique latine & Caraïbes :
les plats du catalogue du Tome 4 encore sans fiche. Règle D21 pour le porc, variantes sans alcool « à tester ». NON TESTÉES (Tome 7 §2)."""
from recipes_v2_base import *

UK = "Europe du Nord › Royaume-Uni"; DE = "Europe du Nord › Allemagne"; AT = "Europe du Nord › Autriche"; CH = "Europe du Nord › Suisse"
RU = "Europe du Nord › Russie"; NL = "Europe du Nord › Pays-Bas"; BE = "Europe du Nord › Belgique"; BK = "Europe du Nord › Balkans"
US = "Amérique du Nord › États-Unis"; QC = "Amérique du Nord › Canada › Québec"; MX = "Amérique latine › Mexique"; BRS = "Amérique latine › Brésil"
VB = ("Sans alcool", ["alcohol"], {"Vin blanc": [("Bouillon d'os maison (bœuf/volaille)", 0.8), ("Citron", 0.1)]}, "Vin blanc → **bouillon + un trait de citron**. **À tester**.")

K("cottage_pie", "Cottage pie (hachis de bœuf anglais)", "Cottage pie", UK, "P", 1, 6, 30, 30, "€", "Cocotte, plat à gratin.",
  "Bœuf haché mijoté avec carottes, petits pois et sauce brune, sous une purée dorée striée à la fourchette : le réconfort britannique du dimanche soir.",
  ["600 g|de bœuf haché|Bœuf haché|3", "1 kg|de pommes de terre|Pomme de terre|3", f"2|carottes|{CAROTTE}|1", "150 g|de petits pois|Petits pois / pois gourmands|1", f"1|oignon|{OIG}|1", f"2 c. à s.|de concentré de tomate|{CONC}|1", "2 c. à s.|de sauce Worcestershire|Sauce Worcestershire|1", f"30 cl|de bouillon|Bouillon cube bœuf|1", f"40 g|de beurre|{BEURRE}|1", f"15 cl|de lait|{LAIT}|1"],
  ["**Garniture.** Oignon et carottes 5 min ; viande 8 min ; concentré, sauce, bouillon ; 20 min : épais ; petits pois.", "**Purée.** Pommes de terre écrasées avec beurre et lait chaud, sel.",
   "**Gratiner.** Viande, purée striée à la fourchette ; 200 °C, 30 min : les stries dorent."], age=1, cats=["enfants"], fetes=["Repas de famille"])

K("yorkshire_puddings", "Yorkshire puddings", "Yorkshire pudding", f"{UK} › Yorkshire", "A", 2, 12, 10, 25, "€", "Moule à muffins, four très chaud.",
  "Une pâte à crêpe versée dans de l'huile fumante : elle gonfle en petites couronnes croustillantes et creuses. L'accompagnement du rôti du dimanche.",
  [f"3|œufs|{OEUF}|3", f"140 g|de farine|{F55}|3", f"20 cl|de lait|{LAIT}|2", f"6 c. à s.|d'huile neutre|{HN}|2", f"1 pincée|de sel|{SEL}|0"],
  ["**Pâte.** Œufs, farine, lait, sel : lisse ; 30 min de repos.", "**Chauffer.** 1 c. à c. d'huile par alvéole, 10 min à 230 °C : l'huile doit fumer.",
   "**Cuire.** Pâte versée vite au tiers ; 20-25 min sans ouvrir : très gonflés et dorés. Servis avec le jus du rôti."], age=1, cats=["enfants"], fetes=["Noël"])

K("sticky_toffee_pudding", "Sticky toffee pudding", "Sticky toffee pudding", f"{UK} › Lake District", "D", 1, 8, 25, 35, "€€", "Moule carré, casserole.",
  "Gâteau moelleux aux dattes, nappé d'une sauce caramel au beurre : le dessert des pubs anglais, à servir chaud avec de la crème.",
  ["200 g|de dattes dénoyautées|Datte (medjool, deglet)|3", f"175 g|de farine|{F55}|2", f"80 g|de beurre|{BEURRE}|2", "150 g|de sucre muscovado (ou cassonade)|Sucre muscovado|2", f"2|œufs|{OEUF}|2", "1 c. à c.|de bicarbonate|Bicarbonate de soude|1", f"1 c. à c.|de levure chimique|{LEVC}|1", f"20 cl|de crème|{CL}|2"],
  ["**Dattes.** Hachées, 25 cl d'eau bouillante et le bicarbonate, 10 min : elles fondent.", "**Pâte.** Beurre et 100 g de sucre crémés, œufs, farine, levure, dattes ; 180 °C, 30-35 min.",
   "**Sauce.** 50 g de sucre, 30 g de beurre et la crème, 3 min de frémissement : caramel. Sur le gâteau chaud."], age=1, fetes=["Noël"], profil=["sucre"])

K("lohikeitto", "Lohikeitto (soupe de saumon finlandaise)", "Lohikeitto", "Europe du Nord › Finlande", "So", 1, 4, 15, 25, "€€", "Faitout.",
  "Saumon, pommes de terre, poireau, crème et beaucoup d'aneth dans un bouillon clair : la soupe des lacs finlandais, douce et complète.",
  ["500 g|de saumon sans peau|Saumon (frais, pavé)|3", "500 g|de pommes de terre|Pomme de terre|2", "1|poireau|Poireau|1", f"20 cl|de crème|{CF}|2", "1 bouquet|d'aneth|Aneth|2", "1 l|de fumet ou d'eau|Fumet de poisson maison|1"],
  ["**Base.** Poireau fondu 5 min au beurre ; pommes de terre en dés, fumet, 15 min : tendres.", "**Saumon.** En cubes, 5 min à frémissement : opaque.", "**Finir.** Crème, aneth haché, sel, poivre."],
  age=1, profil=["poisson"])

K("rosti", "Rösti", "Rösti", f"{CH} › Berne", "A", 1, 4, 15, 25, "€", "Poêle anti-adhésive.",
  "Pommes de terre cuites la veille, râpées grossièrement et dorées en galette épaisse au beurre : croustillante dehors, fondante dedans.",
  ["800 g|de pommes de terre (cuites la veille, à chair ferme)|Pomme de terre|3", f"40 g|de beurre (ou beurre clarifié)|{BEURRE}|2", f"1 pincée|de sel|{SEL}|1", f"1 pincée|de poivre|{POIVRE}|0"],
  ["**Râper.** Pommes de terre froides épluchées, gros trous ; sel, poivre.", "**Dorer.** Beurre, galette tassée légèrement, feu moyen, 12 min sans toucher : croûte dorée.",
   "**Retourner.** Sur une assiette, glisse dans la poêle avec un peu de beurre, 10 min. Avec un œuf au plat ou un émincé."], age=1, cats=["enfants", "vegetarien"])

K("wiener_schnitzel", "Wiener Schnitzel (escalope viennoise)", "Wiener Schnitzel", f"{AT} › Vienne", "P", 2, 4, 25, 10, "€€€", "Grande poêle, 3 assiettes.",
  "Escalope de veau aplatie, panée et frite dans beaucoup de beurre : la panure gonfle et se détache en vagues dorées. Citron et salade de pommes de terre.",
  ["4|escalopes de veau|Escalope de veau|3", f"60 g|de farine|{F55}|1", f"2|œufs|{OEUF}|2", "120 g|de chapelure fine|Chapelure|2", f"100 g|de beurre clarifié (ou huile + beurre)|Beurre clarifié / ghee|2", f"1|citron|{CIT}|1"],
  ["**Aplatir.** Escalopes à 4 mm entre deux films.", "**Paner.** Farine, œuf battu, chapelure sans tasser (c'est ce qui permet de souffler).",
   "**Frire.** Beurre clarifié sur 1 cm, chaud ; 2-3 min par face en arrosant et en secouant la poêle : la panure ondule et dore. Citron."],
  age=3, tech=["paner à l'anglaise"])

K("boeuf_stroganov", "Bœuf Stroganov", "Befstroganov", f"{RU} › Saint-Pétersbourg", "P", 1, 4, 20, 15, "€€€", "Poêle, sauteuse.",
  "Lanières de bœuf saisies, oignons et champignons dans une sauce crème aigre à la moutarde et au paprika : rapide et chic.",
  ["600 g|de rumsteck ou filet|Rumsteck|3", "250 g|de champignons|Champignon de Paris|2", f"1|oignon|{OIG}|1", f"20 cl|de crème|{CF}|2", f"1 c. à s.|de moutarde|{DIJON}|1", f"1 c. à c.|de paprika|{PAPRIKA}|1", f"½|citron|{CIT}|1", f"20 g|de beurre|{BEURRE}|1"],
  ["**Saisir.** Bœuf en lanières, poêle fumante, en 2 fois, 1 min : saisi dehors, rose dedans ; réservé.", "**Sauce.** Oignon et champignons 6 min ; paprika, crème, moutarde, citron, 2 min.",
   "**Finir.** Bœuf et son jus 1 min (ne pas recuire : il durcit). Avec riz ou pâtes."], age=3, tech=["saisir"])

K("pelmeni", "Pelmeni (raviolis russes au bœuf)", "Pelmeni", f"{RU} › Sibérie", "P", 3, 6, 75, 10, "€", "Rouleau, verre (emporte-pièce).",
  "Petits raviolis farcis de bœuf et d'oignon, pochés et servis avec beurre fondu, crème aigre et aneth. Se congèlent crus : le repas d'avance par excellence.",
  [f"400 g|de farine|{F55}|3", f"1|œuf|{OEUF}|1", "400 g|de bœuf haché|Bœuf haché|3", f"1|oignon râpé|{OIG}|2", f"40 g|de beurre|{BEURRE}|1", f"15 cl|de crème|{CF}|1", "1 c. à s.|d'aneth|Aneth|1"],
  ["**Pâte.** Farine, œuf, 18 cl d'eau, sel : pétrie lisse ; 30 min sous un bol.", "**Former.** Pâte très fine, disques de 6 cm, une noisette de farce (viande, oignon, sel, poivre, 2 c. à s. d'eau froide) ; plie en demi-lune, puis rejoins les pointes.",
   "**Pocher.** Eau bouillante salée, 5 min après qu'ils remontent. Beurre, crème, aneth."], age=3, cats=["enfants"], keep="Congelés crus à plat, puis en sac : 3 mois ; cuisson directe 8 min.")

K("cevapi", "Ćevapi (petites saucisses grillées des Balkans)", "Ćevapi", f"{BK} › Bosnie", "P", 1, 4, 20, 10, "€€", "Gril, plancha ou poêle-gril.",
  "Petits boudins de bœuf et d'agneau hachés à l'ail et au bicarbonate (pour la tendreté), grillés, dans un pain plat avec oignon cru et ajvar.",
  ["400 g|de bœuf haché|Bœuf haché|3", "200 g|d'agneau haché|Agneau haché|2", f"2 gousses|d'ail|{AIL}|1", "½ c. à c.|de bicarbonate|Bicarbonate de soude|1", f"1 c. à c.|de paprika|{PAPRIKA}|1", "4|pains plats|Pain pita / libanais|2", "1|oignon rouge|Oignon rouge|1", f"2|poivrons grillés (ajvar express)|{POIVRON}|1?"],
  ["**Mélanger.** Viandes, ail, bicarbonate, paprika, sel, 5 cl d'eau ; pétris 3 min : collant ; 1 h au frais.", "**Former.** Boudins de 8 cm, gros comme un doigt.", "**Griller.** 8 min en tournant : dorés. Dans le pain, oignon émincé, poivrons mixés."],
  age=3, fetes=["Barbecue d'été"])

K("sarmale_boeuf", "Sarmale (chou farci roumain, version bœuf)", "Sarmale", "Europe du Nord › Roumanie", "P", 2, 6, 60, 120, "€€", "Grande cocotte.",
  "Feuilles de chou roulées autour d'une farce viande-riz, mijotées longtemps dans une sauce tomate : le plat des fêtes roumaines. Ici en version bœuf (D21), sans porc.",
  ["1|gros chou vert ou blanc|Chou blanc / rouge|3", "600 g|de bœuf haché|Bœuf haché|3", f"100 g|de riz rond|Riz rond / sushi|2", f"2|oignons|{OIG}|1", f"400 g|de tomates pelées|{PELEES}|2", f"1 c. à c.|de paprika fumé|{PFUME}|1", "1 c. à s.|d'aneth|Aneth|1", f"20 cl|de crème|{CF}|1?"],
  ["**Feuilles.** Chou entier évidé du trognon, 5 min dans l'eau bouillante : les feuilles se détachent souples ; côte centrale amincie.", "**Rouler.** Farce viande, riz cru, oignon fondu, paprika, sel ; une cuillerée par feuille, côtés repliés, roulé serré.",
   "**Mijoter.** Lit de chou émincé, sarmale serrées, tomates, eau à hauteur ; couvert, 2 h à feu très doux (ou four 160 °C). Crème et aneth."], age=3, fetes=["Noël", "Repas de famille"])

K("sachertorte_simple", "Sachertorte simplifiée", "Sachertorte", f"{AT} › Vienne", "D", 3, 10, 50, 45, "€€", "Moule 22 cm, casserole, thermomètre (glaçage).",
  "Le gâteau au chocolat de l'hôtel Sacher : génoise chocolatée, fine couche de confiture d'abricot et glaçage brillant. Version maison simplifiée.",
  ["150 g|de chocolat noir|Chocolat noir|3", f"120 g|de beurre|{BEURRE}|2", f"6|œufs|{OEUF}|3", f"120 g|de sucre|{SUCRE}|2", f"120 g|de farine|{F55}|2", "200 g|de confiture d'abricot|Confiture / gelée|2", "100 g|de chocolat noir (glaçage)|Chocolat noir|2", f"10 cl|de crème|{CL}|1"],
  ["**Pâte.** Chocolat et beurre fondus ; jaunes ; blancs montés avec le sucre, incorporés en alternance avec la farine.", "**Cuire.** 170 °C, 40-45 min : la lame ressort presque sèche ; refroidi.",
   "**Monter.** Coupé en deux, confiture chaude entre et dessus ; ganache brillante (chocolat + crème chaude) versée d'un coup, lissée en un seul geste."],
  age=3, cats=["enfants"], fetes=["Anniversaire"], profil=["chocolat", "sucre"], tech=["monter des blancs", "ganache"])

K("waterzooi_poulet", "Waterzooi de poulet (Gand)", "Gentse waterzooi", f"{BE} › Gand", "P", 1, 4, 25, 40, "€€", "Cocotte.",
  "Poulet poché avec poireaux, carottes et céleri, bouillon lié à la crème et au jaune d'œuf : la soupe-plat douce et dorée de Gand.",
  [f"4|cuisses de poulet|{CUISSE}|3", "2|poireaux|Poireau|2", f"3|carottes|{CAROTTE}|2", "2 branches|de céleri|Céleri-branche|1", f"3|pommes de terre|{PDT}|2", f"20 cl|de crème|{CF}|2", f"2|jaunes d'œuf|Jaune d'œuf|1", f"1 c. à s.|de persil|{PERSIL}|1"],
  ["**Pocher.** Poulet dans 1,2 l d'eau salée, 30 min ; effiloché.", "**Légumes.** En julienne et pommes de terre en dés dans le bouillon, 15 min.", "**Lier.** Crème + jaunes avec une louche de bouillon, versés hors du feu en remuant ; poulet, persil."],
  age=1, cats=["enfants"])

K("stamppot_boerenkool", "Stamppot au chou kale et saucisse fumée", "Boerenkoolstamppot", f"{NL}", "P", 1, 4, 15, 30, "€", "Faitout.",
  "Purée de pommes de terre écrasée avec du chou kale, servie avec une saucisse fumée et un puits de jus : l'hiver néerlandais. Saucisse de volaille fumée par défaut.",
  ["1 kg|de pommes de terre|Pomme de terre|3", "500 g|de chou kale|Chou vert / frisé / kale|3", "4|saucisses fumées de volaille|Saucisse de bœuf / de veau / de volaille|2", f"10 cl|de lait|{LAIT}|1", f"30 g|de beurre|{BEURRE}|1", f"1 c. à c.|de moutarde|{DIJON}|1?"],
  ["**Cuire ensemble.** Pommes de terre en morceaux et kale émincé par-dessus, eau salée, 20 min.", "**Écraser.** Égouttés, beurre, lait chaud : purée grossière verte ; poivre, muscade.", "**Saucisses.** Chauffées 10 min à l'eau frémissante ; moutarde."],
  age=1, cats=["enfants"])

K("poffertjes", "Poffertjes (mini-crêpes hollandaises)", "Poffertjes", NL, "G", 1, 4, 15, 45, "€", "Poêle à blinis ou poêle, poche ou cuillère.",
  "Petites crêpes gonflées à la levure, servies avec beurre et sucre glace : le goûter des fêtes foraines néerlandaises.",
  [f"200 g|de farine (moitié sarrasin possible)|{F55}|3", f"5 g|de levure boulangère|{LEV}|2", f"1|œuf|{OEUF}|2", f"30 cl|de lait tiède|{LAIT}|2", f"30 g|de beurre|{BEURRE}|1", "3 c. à s.|de sucre glace|Sucre glace|1"],
  ["**Pâte.** Tout mélangé, 45 min au chaud : bulles.", "**Cuire.** Petites noisettes de pâte dans la poêle beurrée moyenne ; retournées à la fourchette quand le dessus sèche (1 min).", "**Servir.** Beurre, sucre glace."],
  age=1, cats=["enfants", "brunch"], profil=["sucre"])

K("kartoffelsalat", "Kartoffelsalat (salade de pommes de terre souabe)", "Schwäbischer Kartoffelsalat", f"{DE} › Souabe", "A", 1, 6, 20, 25, "€", "Casserole, saladier.",
  "Pommes de terre tièdes arrosées de bouillon chaud, vinaigre et oignon : elles boivent la sauce et deviennent fondantes, sans mayonnaise.",
  ["1 kg|de pommes de terre à chair ferme|Pomme de terre|3", "20 cl|de bouillon chaud|Bouillon cube légumes|2", f"1|oignon|{OIG}|1", f"3 c. à s.|de vinaigre de cidre|{CIDRE}|1", f"4 c. à s.|d'huile|{HN}|1", f"1 c. à c.|de moutarde|{DIJON}|1", "1 c. à s.|de ciboulette|Ciboulette|1"],
  ["**Cuire.** Pommes de terre en robe des champs, 20 min ; pelées tièdes, en rondelles fines.", "**Arroser.** Bouillon chaud, oignon haché, vinaigre, moutarde, sel ; 20 min : la sauce est bue.", "**Finir.** Huile, ciboulette ; tiède avec des saucisses ou une escalope."],
  age=1, cats=["vegetarien"], fetes=["Barbecue d'été"])

# ——— Amérique du Nord ———
K("buttermilk_fried_chicken", "Poulet frit au babeurre", "Buttermilk fried chicken", f"{US} › Sud", "P", 2, 4, 25, 20, "€€", "Casserole profonde, thermomètre.",
  "Poulet mariné une nuit dans le babeurre épicé (il devient très tendre), enrobé de farine assaisonnée et frit : croustillant du Sud des États-Unis.",
  [f"8|morceaux de poulet|{CUISSE}|3", "50 cl|de babeurre (ou lait + citron)|Babeurre|3", f"200 g|de farine|{F55}|2", f"2 c. à c.|de paprika|{PAPRIKA}|1", "1 c. à c.|de poudre d'ail|Poudre d'ail / d'oignon|1", f"1 pincée|de piment de Cayenne|{CAYENNE}|1", "1,5 l|d'huile de friture|Huile d'arachide|2"],
  ["**Mariner.** Poulet dans le babeurre salé et pimenté, une nuit au frais.", "**Enrober.** Farine + épices + sel ; poulet égoutté roulé dedans, en pressant ; 15 min de repos (la croûte tient mieux).",
   "**Frire.** 160 °C, 12-15 min en retournant : doré profond, 74 °C à cœur ; égoutté sur grille."], age=3, cats=["enfants"], tech=["frire en sécurité"])

K("clam_chowder", "Clam chowder (chaudrée de palourdes de Nouvelle-Angleterre)", "New England clam chowder", f"{US} › Nouvelle-Angleterre", "So", 2, 4, 25, 25, "€€", "Faitout.",
  "Soupe crémeuse aux palourdes, pommes de terre, oignon et céleri, liée au lait : servie à Boston dans un pain rond. Lard en option (version sans porc par défaut).",
  ["1 kg|de palourdes (ou 2 boîtes)|Palourdes / coques|3", f"3|pommes de terre|{PDT}|2", f"1|oignon|{OIG}|1", "2 branches|de céleri|Céleri-branche|1", f"40 cl|de lait|{LAIT}|2", f"15 cl|de crème|{CL}|1", f"30 g|de beurre|{BEURRE}|1", f"20 g|de farine|{F55}|1", "80 g|de lardons (facultatif)|Lardons|1?"],
  ["**Ouvrir.** Palourdes 4 min couvertes avec 20 cl d'eau ; décortiquées ; jus filtré.", "**Base.** (Lardons) oignon, céleri au beurre 5 min ; farine 1 min ; jus, pommes de terre en dés, 15 min.",
   "**Finir.** Lait, crème, palourdes, 3 min sans bouillir ; poivre. Biscuits salés ou pain."], age=6, profil=["poisson"],
  var=[("Sans porc", ["pork"], {"Lardons": [("Lardons de dinde / de volaille fumés", 1.0)]}, "Lardons → **lardons de dinde fumés**, ou rien. **À tester**.")])

K("gumbo_poulet", "Gumbo au poulet et aux crevettes", "Chicken & shrimp gumbo", f"{US} › Louisiane", "P", 3, 6, 40, 60, "€€", "Grande cocotte en fonte.",
  "Le plat créole de La Nouvelle-Orléans : un roux cuit jusqu'à la couleur du chocolat, la « sainte trinité » oignon-céleri-poivron, poulet, saucisse fumée, crevettes et gombo. Saucisse de volaille par défaut.",
  [f"60 g|de farine|{F55}|2", f"6 c. à s.|d'huile|{HN}|2", f"6|cuisses de poulet désossées|{CUISSE}|3", "300 g|de crevettes|Crevettes (cuites/crues)|2", "250 g|de saucisse fumée de volaille|Saucisse de bœuf / de veau / de volaille|2", f"1|oignon|{OIG}|1", "2 branches|de céleri|Céleri-branche|1", f"1|poivron vert|{POIVRON}|1", "2 c. à c.|de mélange cajun|Mélange cajun|2", "1,2 l|de bouillon|Bouillon cube volaille|2"],
  ["**Roux brun.** Farine + huile, feu moyen-doux, 20-25 min en remuant sans arrêt : couleur chocolat au lait, odeur de noisette (s'il noircit ou sent le brûlé : recommence).",
   "**Trinité.** Oignon, céleri, poivron dans le roux, 8 min ; épices, bouillon chaud en fouettant.", "**Mijoter.** Poulet en morceaux, saucisse (et 150 g de gombos si tu en trouves), 45 min ; crevettes 3 min. Riz blanc."],
  age=6, profil=["epice"], tech=["faire un roux"])

K("jambalaya", "Jambalaya au poulet et chorizo de bœuf", "Jambalaya", f"{US} › Louisiane", "P", 1, 6, 25, 30, "€€", "Cocotte.",
  "Le riz créole tout-en-un : poulet, chorizo, crevettes, trinité de légumes, tomates et épices cajun, cuits ensemble jusqu'à ce que le riz boive tout.",
  [f"350 g|de riz long|{RIZ}|3", f"4|cuisses de poulet désossées|{CUISSE}|3", "150 g|de chorizo de bœuf ou de volaille|Chorizo de bœuf ou de volaille|2", "200 g|de crevettes|Crevettes (cuites/crues)|1?", f"1|oignon|{OIG}|1", f"1|poivron|{POIVRON}|1", "2 branches|de céleri|Céleri-branche|1", f"400 g|de tomates pelées|{PELEES}|1", "2 c. à c.|de mélange cajun|Mélange cajun|2", "70 cl|de bouillon|Bouillon cube volaille|2"],
  ["**Dorer.** Poulet en morceaux et chorizo, 6 min ; légumes 5 min ; épices.", "**Cuire.** Riz 1 min, tomates, bouillon ; couvert 20 min à feu doux sans remuer.", "**Finir.** Crevettes posées dessus, 5 min couvert ; cébette."],
  age=6, profil=["epice"])

K("tourtiere_quebec", "Tourtière du Lac-Saint-Jean (version bœuf-veau)", "Tourtière", f"{QC} › Lac-Saint-Jean", "P", 2, 8, 40, 60, "€€", "Moule à tourte profond, four.",
  "La tourte de Noël québécoise : viandes hachées épicées (clou de girofle, cannelle, sarriette) et pommes de terre dans une pâte brisée. Ici bœuf et veau, sans porc.",
  ["2|pâtes brisées|Pâte brisée / sablée (prête)|3", "500 g|de bœuf haché|Bœuf haché|3", "300 g|de veau haché (ou dinde)|Épaule / tendron de veau|2", f"2|pommes de terre|{PDT}|2", f"1|oignon|{OIG}|1", f"½ c. à c.|de cannelle|{CANN}|1", "1 pincée|de clou de girofle moulu|Clou de girofle|1", "1 c. à c.|de sarriette ou thym|Sarriette / marjolaine|1", f"1|œuf (dorure)|{OEUF}|1"],
  ["**Farce.** Viandes, oignon, épices, sel, 30 cl d'eau, 30 min à petit feu ; pommes de terre cuites écrasées dedans : farce liée ; refroidie.", "**Monter.** Pâte, farce, couvercle soudé, cheminée, dorure.",
   "**Cuire.** 200 °C 15 min puis 180 °C 45 min : dorée. Avec du ketchup aux fruits ou des betteraves marinées."], age=3, fetes=["Noël"])

K("pate_chinois", "Pâté chinois (Québec)", "Pâté chinois", QC, "P", 1, 6, 20, 30, "€", "Plat à gratin.",
  "Trois étages : bœuf haché à l'oignon, maïs en crème et en grains, purée de pommes de terre : le plat de cantine le plus aimé du Québec.",
  ["600 g|de bœuf haché|Bœuf haché|3", "400 g|de maïs (grains + crème de maïs)|Maïs doux|3", "1 kg|de pommes de terre|Pomme de terre|3", f"1|oignon|{OIG}|1", f"30 g|de beurre|{BEURRE}|1", f"15 cl|de lait|{LAIT}|1", f"1 c. à c.|de paprika|{PAPRIKA}|0"],
  ["**Viande.** Oignon et bœuf 10 min, sel, poivre.", "**Étages.** Viande, maïs (la moitié mixée avec un peu de lait = crème de maïs), purée beurrée.", "**Gratiner.** 200 °C, 30 min, paprika : doré. Ketchup à table."],
  age=1, cats=["enfants"])

K("tarte_sucre_quebec", "Tarte au sucre du Québec", "Tarte au sucre", QC, "D", 1, 8, 15, 35, "€", "Moule à tarte.",
  "Une garniture de cassonade (ou sirop d'érable), crème et un peu de farine, cuite dans une pâte brisée : fondante et caramélisée, la tarte des cabanes à sucre.",
  ["1|pâte brisée|Pâte brisée / sablée (prête)|3", "200 g|de cassonade|Sucre blanc / roux / cassonade / vergeoise|3", f"25 cl|de crème|{CL}|2", f"2 c. à s.|de farine|{F55}|1", f"1|œuf|{OEUF}|1", "2 c. à s.|de sirop d'érable (facultatif)|Sirop d'agave / d'érable|1?"],
  ["**Garniture.** Cassonade, farine, crème, œuf, sirop : lisse.", "**Cuire.** Pâte foncée, garniture ; 180 °C, 35 min : prise sur les bords, encore tremblotante au centre.", "**Refroidir.** 2 h : elle se raffermit."],
  age=1, fetes=["Noël"], profil=["sucre"])

K("dinde_roti_farcie", "Dinde rôtie farcie (Thanksgiving / Noël)", "Roast turkey", US, "P", 3, 10, 60, 210, "€€€", "Grand plat à rôtir, thermomètre, ficelle.",
  "Dinde rôtie lentement et arrosée, farce au pain, céleri et sauge, sauce au jus : le grand rôti de Thanksgiving et de Noël, sans stress grâce au thermomètre.",
  ["1|dinde de 4 à 5 kg|Dinde (escalope, cuisse, filet)|3", "300 g|de pain rassis|Pain rassis (réservé)|2", f"2|oignons|{OIG}|1", "3 branches|de céleri|Céleri-branche|1", "10 feuilles|de sauge|Sauge|1", f"120 g|de beurre|{BEURRE}|2", "50 cl|de bouillon|Bouillon cube volaille|2", f"2 c. à s.|de farine|{F55}|1"],
  ["**Farce.** Oignons et céleri fondus au beurre, pain en dés, sauge, bouillon pour humidifier, sel ; farce tiède dans la cavité (sans tasser), le reste en plat à part.",
   "**Rôtir.** Peau beurrée et salée ; 165 °C, environ 40 min par kg, arrosée toutes les 30 min, couverte d'aluminium si elle dore trop : 74 °C dans la cuisse et au centre de la farce.",
   "**Reposer et saucer.** 30 min sous aluminium ; jus dégraissé, farine, bouillon, 5 min de fouet : sauce lisse."],
  age=1, fetes=["Noël", "Repas de famille"], tech=["rôtir une volaille", "températures à cœur"])

# ——— Amérique latine & Caraïbes ———
K("pozole_pollo", "Pozole au poulet (pozole verde simplifié)", "Pozole de pollo", f"{MX} › Guerrero", "So", 2, 6, 30, 60, "€€", "Faitout, mixeur.",
  "Le bouillon mexicain des fêtes : poulet effiloché, grains de maïs, sauce verte aux tomatilles et piment, et la garniture qu'on ajoute à table (chou, radis, citron vert). Poulet par défaut (D21).",
  [f"6|cuisses de poulet|{CUISSE}|3", "500 g|de maïs (ou hominy en conserve)|Maïs doux|3", "300 g|de tomatilles (ou tomates vertes)|Tomatille / nopal|2", f"2|piments verts|{PIMENT}|1", f"1 bouquet|de coriandre|{CORI}|2", f"1|oignon|{OIG}|1", "6|radis|Radis rose|1", "¼|chou|Chou blanc / rouge|1", f"2|citrons verts|{CITV}|1"],
  ["**Bouillon.** Poulet, oignon, 2 l d'eau salée, 40 min ; effiloché.", "**Sauce verte.** Tomatilles, piments, coriandre pochés 5 min puis mixés ; versés dans le bouillon avec le maïs, 20 min.",
   "**Servir.** Poulet dans les bols, bouillon ; à table : chou émincé, radis, citron vert, origan."], age=6, fetes=["Repas de famille"], profil=["epice"])

K("mole_poblano_simple", "Poulet au mole poblano simplifié", "Mole poblano", f"{MX} › Puebla", "P", 3, 6, 50, 60, "€€", "Cocotte, mixeur puissant.",
  "La sauce la plus célèbre du Mexique : piments séchés, épices, fruits secs, graines et un peu de chocolat, mixés et cuits longuement. Version simplifiée en 2 heures.",
  [f"6|cuisses de poulet|{CUISSE}|3", "4|piments séchés (ancho, guajillo)|Piments ancho / chipotle / guajillo / pasilla|3", "40 g|de chocolat noir|Chocolat noir|2", "40 g|d'amandes|Amande (entière, effilée, poudre)|1", "30 g|de raisins secs|Raisins secs|1", "2 c. à s.|de sésame|Sésame (blanc/noir)|1", f"2|tomates|{TOM}|1", f"1|oignon|{OIG}|1", f"½ c. à c.|de cannelle|{CANN}|1", "1 tranche|de pain rassis|Pain rassis (réservé)|1"],
  ["**Poulet.** Poché 40 min dans 1,5 l d'eau salée ; bouillon gardé.", "**Base.** Piments épépinés grillés 30 s à sec puis trempés 20 min ; oignon, tomates, amandes, raisins, sésame, pain dorés à la poêle.",
   "**Mole.** Tout mixé avec 50 cl de bouillon et les épices ; cuit 20 min en remuant, chocolat : sauce épaisse, brillante, brun rouge. Poulet nappé, sésame, riz."],
  age=6, fetes=["Repas de famille"], profil=["epice", "chocolat"])

K("moqueca", "Moqueca de poisson (Bahia)", "Moqueca baiana", f"{BRS} › Bahia", "P", 1, 4, 20, 25, "€€", "Cocotte (idéalement en terre).",
  "Poisson blanc et crevettes mijotés dans le lait de coco, tomate, poivrons, coriandre et un peu d'huile de palme : le ragoût de Bahia.",
  ["600 g|de poisson blanc ferme|Cabillaud / morue fraîche|3", "200 g|de crevettes|Crevettes (cuites/crues)|2", "40 cl|de lait de coco|Lait de coco / crème de coco|3", f"2|tomates|{TOM}|1", f"1|poivron|{POIVRON}|1", f"1|oignon|{OIG}|1", f"2|citrons verts|{CITV}|1", f"1 bouquet|de coriandre|{CORI}|1", "1 c. à s.|d'huile de palme rouge (ou paprika)|Huile de palme rouge|1?"],
  ["**Mariner.** Poisson en morceaux, citron vert, ail, sel, 15 min.", "**Étager.** Oignon, poivron, tomate en rondelles, poisson, crevettes ; lait de coco, huile de palme.", "**Mijoter.** Couvert 15 min sans remuer ; coriandre. Riz blanc."],
  age=3, profil=["poisson"])

K("causa_limena", "Causa limeña (purée froide au poulet)", "Causa limeña", "Amérique latine › Pérou › Lima", "E", 2, 6, 40, 60, "€€", "Cercle ou moule à cake, film.",
  "Couches de purée de pommes de terre jaune au citron vert et au piment, garnies de poulet-mayonnaise et d'avocat : l'entrée froide de Lima, très graphique.",
  ["1 kg|de pommes de terre à chair jaune|Pomme de terre|3", f"2|citrons verts|{CITV}|2", "1 c. à s.|de pâte d'aji amarillo (ou ½ poivron jaune mixé + piment)|Aji amarillo|1?", f"200 g|de poulet cuit|{BLANC_P}|2", "4 c. à s.|de mayonnaise|SUB:mayonnaise|2", "1|avocat|Avocat|2", f"2|œufs durs|{OEUF}|1", f"4 c. à s.|d'huile|{HN}|1"],
  ["**Purée.** Pommes de terre écrasées, citron vert, huile, aji, sel : purée ferme et jaune ; froide.", "**Monter.** Moule filmé : purée, poulet à la mayonnaise, avocat en tranches, purée.", "**Servir.** 1 h au frais, démoulé, œuf dur, olives."],
  age=3, fetes=["Apéritif dînatoire"])

K("ajiaco", "Ajiaco de Bogotá (soupe poulet-maïs-pommes de terre)", "Ajiaco santafereño", "Amérique latine › Colombie › Bogotá", "So", 1, 6, 25, 60, "€€", "Faitout.",
  "Soupe épaisse de poulet, trois sortes de pommes de terre (dont une qui fond et lie), épis de maïs et herbe guasca (thym/origan) ; crème et câpres à table.",
  [f"4|cuisses de poulet|{CUISSE}|3", "1,2 kg|de pommes de terre (farineuses et fermes)|Pomme de terre|3", "2|épis de maïs (ou 300 g de grains)|Maïs doux|2", f"1|oignon|{OIG}|1", f"1 c. à c.|d'origan|Origan frais / sec|1", f"10 cl|de crème|{CF}|1", "1 c. à s.|de câpres|Câpres|1", "1|avocat|Avocat|1?"],
  ["**Bouillon.** Poulet, oignon, 2 l d'eau salée, 35 min ; effiloché.", "**Pommes de terre.** Les farineuses en fines rondelles (elles fondent), les fermes en morceaux ; maïs en tronçons, origan ; 30 min.", "**Servir.** Poulet remis ; crème, câpres, avocat à table."],
  age=1, cats=["enfants"])

K("moros_y_cristianos", "Moros y cristianos (riz aux haricots noirs cubain)", "Moros y cristianos", "Amérique latine › Cuba", "A", 1, 6, 15, 30, "€", "Cocotte.",
  "Riz cuit avec les haricots noirs et leur jus, oignon, poivron, cumin et origan : le riz noir et blanc qui accompagne toute la cuisine cubaine.",
  [f"300 g|de riz|{RIZ}|3", "400 g|de haricots noirs avec leur jus|Haricots rouges / noirs|3", f"1|oignon|{OIG}|1", f"1|poivron vert|{POIVRON}|1", f"2 gousses|d'ail|{AIL}|1", f"1 c. à c.|de cumin|{CUMIN}|1", f"1 c. à c.|d'origan|Origan frais / sec|1", f"1|feuille de laurier|{LAURIER}|0"],
  ["**Sofrito.** Oignon, poivron, ail 6 min ; cumin, origan.", "**Cuire.** Riz rincé, haricots et leur jus complétés d'eau (1,5 fois le volume du riz), laurier, sel ; couvert 20 min à feu doux.", "**Reposer.** 10 min, égrené à la fourchette."],
  age=1, cats=["vegetarien"])

K("platanos_maduros", "Plátanos maduros (bananes plantains caramélisées)", "Plátanos maduros", "Amérique latine › Caraïbes", "A", 1, 4, 5, 10, "€", "Poêle.",
  "Plantains très mûrs (peau noire) en tranches épaisses, poêlés jusqu'à caraméliser : sucrés-salés, l'accompagnement des Caraïbes et d'Amérique centrale.",
  ["3|bananes plantains très mûres (peau noire)|Plantain (banane à cuire)|3", f"3 c. à s.|d'huile|{HN}|1", f"1 pincée|de sel|{SEL}|1"],
  ["**Couper.** En biais, tranches de 1,5 cm.", "**Poêler.** Huile moyenne, 3-4 min par face : brun caramel, fondant au cœur.", "**Servir.** Une pincée de sel ; avec riz et haricots, ou en dessert avec un peu de crème."],
  age=1, cats=["enfants", "vegetarien"])

K("tres_leches", "Gâteau tres leches", "Pastel de tres leches", "Amérique latine › Mexique", "D", 1, 10, 30, 240, "€€", "Moule rectangulaire, batteur.",
  "Un biscuit léger imbibé de trois laits (concentré sucré, concentré non sucré, crème) et couvert de chantilly : mouillé, frais, très populaire de Mexico à Miami.",
  [f"5|œufs|{OEUF}|3", f"150 g|de sucre|{SUCRE}|2", f"150 g|de farine|{F55}|2", f"1 c. à c.|de levure chimique|{LEVC}|1", "1 boîte (397 g)|de lait concentré sucré|Lait concentré sucré / non sucré|3", "1 boîte (410 g)|de lait concentré non sucré|Lait concentré sucré / non sucré|2", f"20 cl|de crème|{CL}|2", f"1 pincée|de cannelle|{CANN}|1?"],
  ["**Biscuit.** Blancs montés avec le sucre, jaunes, farine et levure incorporées ; 180 °C, 25 min ; piqué partout à la fourchette.", "**Imbiber.** Les trois laits mélangés (garde 20 cl de crème pour la chantilly), versés lentement sur le gâteau tiède ; 4 h au frais.",
   "**Couvrir.** Chantilly, cannelle ; servi froid."], age=1, cats=["enfants"], fetes=["Anniversaire"], profil=["sucre"], tech=["monter des blancs"])

K("churrasco_chimichurri", "Churrasco et chimichurri", "Churrasco con chimichurri", "Amérique latine › Argentine", "P", 1, 4, 15, 15, "€€€", "Barbecue ou poêle-gril.",
  "Pièce de bœuf grillée au gros sel sur la braise, tranchée et arrosée de chimichurri persil-ail-vinaigre-piment : l'asado argentin à la maison.",
  ["1 kg|de bavette, entrecôte ou rumsteck|Bavette|3", "6 c. à s.|de chimichurri|SUB:chimichurri|3", f"1 c. à c.|de gros sel|{SEL}|1", f"4|pommes de terre (au four)|{PDT}|1?"],
  ["**Tempérer.** Viande sortie 30 min avant ; gros sel juste avant de griller.", "**Griller.** Braise très chaude, 4-5 min par face pour une bavette (52 °C à cœur saignant, 56 °C à point).", "**Reposer et trancher.** 8 min sous aluminium, tranché contre les fibres ; chimichurri."],
  age=3, fetes=["Barbecue d'été"], tech=["cuisson d'une pièce de bœuf"])

K("poulet_jerk", "Poulet jerk jamaïcain", "Jerk chicken", "Amérique latine › Jamaïque", "P", 1, 4, 20, 45, "€€", "Barbecue ou four.",
  "Poulet longuement mariné dans la pâte jerk (piment, piment de la Jamaïque, thym, cébette, gingembre) et grillé jusqu'à noircir par endroits : fumé, épicé, parfumé.",
  [f"8|morceaux de poulet|{CUISSE}|3", "6 c. à s.|de marinade jerk|SUB:marinade_jerk|3", f"2|citrons verts|{CITV}|1", f"300 g|de riz (riz et pois)|{RIZ}|1?"],
  ["**Mariner.** Poulet incisé, frotté de marinade, une nuit au frais (au moins 4 h).", "**Cuire.** Barbecue à feu indirect, couvercle fermé, 40 min en retournant, puis 5 min au-dessus des braises : noirci par endroits ; ou four 200 °C 40 min puis gril.", "**Servir.** Citron vert ; riz et haricots, plantains."],
  age=6, fetes=["Barbecue d'été"], profil=["epice"])
