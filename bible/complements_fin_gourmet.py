# -*- coding: utf-8 -*-
"""Audit « fin gourmet, cuisine française » (12/11/2026, AUDIT_FIN_GOURMET_FRANCE_2026-11-12.md). Appliqué par
export_app_data.py :
- ETAPES / ASTUCES : les grands classiques régionaux réduits à 3 étapes télégraphiques, réécrits au niveau étalon
  (geste, temps, repère visuel ou température) — mêmes ingrédients.
- accords() : un accord mets-vin régional et un accord sans alcool pour chaque plat, entrée et dessert français qui
  n'en avait pas (la mention Evin est affichée par l'application).
- region() : noms de régions unifiés (« Bourgogne » et « Franche-Comté » → « Bourgogne-Franche-Comté ») et une rubrique
  pour les bases françaises sans région."""

ETAPES = {
 "moules_marinieres": [
  "**Laver.** Moules grattées et ébarbées (le filament tiré vers la charnière), rincées à grande eau ; celles qui sont cassées ou restent ouvertes quand on les tapote sont jetées.",
  "**Suer.** Grande cocotte, beurre, échalotes ciselées, 2 min à feu moyen : translucides, sans couleur ; laurier.",
  "**Ouvrir.** Vin blanc, feu vif ; moules, couvercle, 5 à 6 min en secouant la cocotte deux fois : toutes ouvertes, la chair orange et gonflée.",
  "**Servir.** Persil haché, poivre du moulin (pas de sel : l'eau des moules l'est) ; celles restées fermées jetées ; le jus au fond de la cocotte (sable) laissé, le reste versé dessus ; frites ou pain."],
 "sole_normande": [
  "**Préparer.** Filets parés, salés, roulés peau à l'intérieur ; moules grattées et ouvertes 4 min à couvert dans 5 cl de cidre, jus filtré gardé.",
  "**Pocher.** Plat beurré, échalote ciselée, filets serrés, reste du cidre et jus des moules ; papier sulfurisé au contact ; four 180 °C 10 à 12 min : chair blanche, nacrée, qui se défait à la pression.",
  "**Champignons.** Émincés, une noix de beurre et un trait de jus de cuisson, 5 min : blancs et brillants.",
  "**Sauce.** Jus de cuisson réduit de moitié, crème, 3 min : nappante ; hors du feu, le jaune battu : elle épaissit et brille, sans bouillir.",
  "**Dresser.** Filets sur assiettes chaudes, champignons, moules décortiquées autour, sauce, persil."],
 "bouchees_reine": [
  "**Pocher.** Poulet en dés de 2 cm dans le bouillon frémissant, 10 min : blanc à cœur ; bouillon filtré gardé.",
  "**Champignons.** En quartiers, 10 g de beurre, un trait de citron, 5 min à couvert : ils restent blancs et rendent un jus, ajouté au bouillon.",
  "**Velouté.** Roux blanc (20 g de beurre, farine, 2 min sans couleur), 40 cl de bouillon chaud en fouettant, 5 min : il nappe ; crème, 2 min.",
  "**Lier.** Hors du feu, le jaune battu avec une cuillère de sauce, puis dans la casserole : sauce suprême, brillante ; poulet et champignons dedans, sel, poivre blanc, un trait de citron.",
  "**Garnir.** Croustades 8 min à 180 °C (chapeau à part), remplies à ras, chapeau posé ; aussitôt (la pâte ramollit vite)."],
 "blanquette_poulet": [
  "**Pocher.** Poulet en gros morceaux, eau froide à hauteur, porté à frémissement et écumé ; carottes en tronçons, oignon, bouquet, sel ; 25 min à frémissement : la chair se détache.",
  "**Champignons.** Quartiers, une noix de beurre, citron, 5 min à couvert : blancs.",
  "**Velouté.** Roux blanc (beurre et farine, 2 min sans couleur), 50 cl de bouillon filtré chaud en fouettant, 10 min à feu doux : il nappe la cuillère ; jus des champignons.",
  "**Lier.** Crème et jaune battus, une louche de sauce chaude dedans, puis tout dans la casserole hors du feu : jamais d'ébullition après (elle tranche) ; jus de citron.",
  "**Réunir.** Poulet, carottes, champignons réchauffés 3 min à feu très doux dans la sauce ; riz pilaf ou riz blanc."],
 "choucroute_mer": [
  "**Rincer.** Choucroute crue rincée deux fois à l'eau froide, pressée à la main : moins acide.",
  "**Braiser.** Beurre, oignon émincé 5 min ; chou, genièvre, fumet, poivre ; couvert, feu doux 35 à 40 min en remuant : tendre, encore légèrement croquant, presque sec.",
  "**Pocher.** Poissons en gros morceaux (le haddock dessalé 15 min dans le lait), dans un fond de fumet frémissant, 6 à 8 min ; crevettes les 2 dernières minutes : chair nacrée au cœur.",
  "**Dresser.** Choucroute en dôme sur plat chaud, poissons et crevettes autour, pommes vapeur, beurre blanc chaud à part."],
 "baeckeoffe_volaille": [
  "**Mariner (la veille).** Viandes en cubes de 4 cm avec oignons émincés, ail, bouquet garni et le vin ; filmé, 12 à 24 h au frigo.",
  "**Couches.** Terrine à baeckeoffe ou cocotte beurrée : pommes de terre en rondelles de 5 mm, viandes et légumes (carottes, poireau en rondelles), pommes de terre ; sel et poivre à chaque couche.",
  "**Mouiller.** Marinade versée, eau ou bouillon à mi-hauteur.",
  "**Luter.** Couvercle soudé d'un boudin de pâte (200 g de farine, 12 cl d'eau) : la vapeur reste dedans ; four 160 °C 3 h.",
  "**Servir.** Croûte cassée à table (le parfum s'échappe), dans la terrine ; une salade verte."],
 "truffade": [
  "**Trancher.** Pommes de terre à chair ferme en lamelles de 3 mm, épongées ; tome en fines lamelles.",
  "**Poêler.** Graisse de canard (et lardons), pommes de terre, ail écrasé ; feu moyen 20 à 25 min en retournant souvent : dorées, tendres, quelques-unes écrasées ; sel avec mesure (la tome est salée).",
  "**Filer.** Tome ajoutée hors du feu vif, mélangée à la spatule 2 à 3 min : elle fond et file en rubans.",
  "**Galette.** 3 min sans toucher à feu moyen : dessous doré ; retournée d'un coup sur le plat ; persil, salade verte."],
 "pissaladiere": [
  "**Confire.** Oignons émincés fin, huile, thym, sel, couvert, feu très doux 45 min à 1 h en remuant : fondants, blond pâle, jamais grillés ; découvert 10 min pour sécher.",
  "**Étaler.** Pâte à pizza en rectangle de 5 mm sur plaque huilée, bords légèrement relevés.",
  "**Garnir.** Oignons tièdes jusqu'au bord, anchois en croisillons, une olive dans chaque losange, un filet d'huile.",
  "**Cuire.** Four 220 °C, 20 min : pâte croustillante dessous, oignons à peine dorés aux pointes ; tiède ou froide."],
 "magret_cerises": [
  "**Quadriller.** Peau entaillée en croisillons serrés sans toucher la chair ; magrets sortis 20 min avant ; sel sur la chair.",
  "**Fondre la peau.** Poêle froide, côté peau, feu moyen 8 à 10 min : la graisse fond, la peau devient fine et dorée ; graisse vidée en cours (gardée pour des pommes de terre).",
  "**Chair.** Retournés, 3 à 4 min : 54 °C à cœur (rosé) ; 8 min de repos sous aluminium, peau dessus.",
  "**Sauce.** Poêle dégraissée, miel, 1 min (il caramélise), balsamique, cerises, 4 à 5 min : sirupeuse, cerises entières ; jus de repos dedans.",
  "**Trancher.** En biais, 1 cm, fleur de sel, poivre, sauce."],
 "quenelles_nantua_simple": [
  "**Panade.** Lait, 50 g de beurre, sel à ébullition ; farine d'un coup, dessécher 2 min : la pâte se décolle ; refroidie.",
  "**Farce.** Poisson sans arête mixé froid, panade, œufs un à un, 30 g de beurre mou, sel, muscade : lisse et élastique ; 2 h au frigo (elle se raffermit).",
  "**Pocher.** Quenelles moulées à deux cuillères mouillées, dans l'eau salée frémissante (jamais bouillante), 8 à 10 min : elles remontent et gonflent ; égouttées sur un torchon.",
  "**Sauce Nantua.** Carapaces revenues au beurre 5 min, concentré 1 min, crème, 10 min ; passée au chinois en pressant ; crevettes décortiquées dedans.",
  "**Gratiner.** Quenelles dans un plat beurré, nappées ; four 200 °C 15 min : elles doublent de volume, la sauce bouillonne ; aussitôt (elles retombent)."],
 "flamiche_maroilles": [
  "**Foncer.** Pâte dans le moule beurré, piquée, 15 min au frais ; cuite à blanc 10 min à 190 °C (papier et billes) : le fond ne sera pas détrempé.",
  "**Oignon.** Émincé, fondu 10 min dans une noix de beurre : doux, blond.",
  "**Appareil.** Œufs battus avec la crème, poivre (pas de sel : le maroilles est salé) ; oignon étalé sur la pâte, appareil versé.",
  "**Fromage.** Maroilles en tranches épaisses avec la croûte (grattée si elle est collante), posé en rosace.",
  "**Cuire.** Four 200 °C 25 min : gonflée, dorée, le fromage coule ; tiède, avec une salade d'endives."],
 "croque_monsieur": [
  "**Beurrer.** Tranches de pain de mie beurrées sur une face (dehors), comme pour un sandwich grillé.",
  "**Monter.** Face non beurrée : une fine couche de béchamel, jambon plié à la taille du pain, un peu d'emmental, l'autre tranche.",
  "**Napper.** Béchamel épaisse sur le dessus, emmental râpé jusqu'au bord.",
  "**Cuire.** Four 200 °C 8 min (le dessous dore), puis 3 min sous le grill : bouillonnant, doré par plaques ; 2 min avant de couper. Avec un œuf au plat dessus : croque-madame."],
 "tielle_setoise": [
  "**Sauce.** Huile, oignons et ail fondus 10 min ; calamars en lanières, 5 min ; tomates, paprika, piment, sel ; 30 min à découvert : très épaisse, presque sèche (sinon la pâte se détrempe) ; refroidie.",
  "**Foncer.** Deux tiers de la pâte étalés à 5 mm dans un moule huilé de 24 cm, bords qui dépassent.",
  "**Fermer.** Garniture froide, couvercle de pâte, bords roulés ensemble en cordon serré ; un petit trou au centre.",
  "**Cuire.** Dessus badigeonné du jus rouge de la sauce ; four 200 °C 40 min : pâte dorée et ferme ; tiède ou froide, comme à Sète."],
 "bourride_setoise": [
  "**Bouillon.** Poireau, oignon, fenouil émincés, zeste d'orange, 1 L d'eau salée, poivre ; 15 min de frémissement.",
  "**Pocher.** Poisson en tronçons épais, 8 à 10 min à frémissement : chair nacrée ; réservé au chaud, couvert.",
  "**Lier.** Dans une casserole hors du feu : aïoli et jaunes ; le bouillon filtré chaud versé peu à peu en fouettant.",
  "**Épaissir.** À feu très doux en tournant, sans bouillir (elle tranche), 3 à 4 min : la sauce nappe la cuillère.",
  "**Servir.** Pain grillé frotté d'ail au fond des assiettes, poisson, sauce par-dessus."],
 "petit_sale_lentilles": [
  "**Dessaler.** Petit salé dans l'eau froide, porté à ébullition 5 min ; égoutté, rincé.",
  "**Mijoter.** Eau froide à hauteur, oignon piqué, bouquet, poivre (pas de sel) ; 1 h à frémissement, écumé.",
  "**Lentilles.** Rincées, dans la cocotte avec les carottes en rondelles et du bouillon de cuisson à hauteur, 25 à 30 min : tendres, entières, presque tout le liquide absorbé.",
  "**Goûter.** Seulement maintenant : le sel du petit salé suffit souvent.",
  "**Servir.** Viande tranchée sur les lentilles, moutarde forte à table, un trait de vinaigre dans les lentilles."],
 "tomates_farcies": [
  "**Évider.** Chapeaux coupés, pulpe retirée à la cuillère et hachée ; intérieur salé, tomates retournées 15 min : elles rendent leur eau.",
  "**Farce.** Viande, oignon et ail hachés, persil, pain trempé dans le lait et pressé, œuf, sel (10 g par kg), poivre : mélangée à la main, liée.",
  "**Remplir.** Farce en dôme, chapeaux posés.",
  "**Riz.** Riz cru au fond du plat avec la pulpe hachée et 20 cl d'eau, sel ; tomates dessus, filet d'huile.",
  "**Cuire.** Four 180 °C 50 min à 1 h : farce à 70 °C, tomates fripées et rôties, riz tendre et confit du jus."],
 "axoa_veau": [
  "**Hacher.** Veau en petits dés de 5 mm au couteau (la texture de l'axoa), ou hachage gros chez le boucher.",
  "**Fondre.** Huile, oignons émincés, poivrons en lanières, ail, 12 à 15 min à feu moyen : très tendres, sans brûler.",
  "**Saisir.** Viande, feu vif, 5 min en remuant : elle grise et rend son eau, qui s'évapore.",
  "**Mijoter.** Espelette, sel, bouillon ; 30 min à petit feu, couvert : la viande est tendre, la sauce courte.",
  "**Servir.** Avec des pommes de terre vapeur et un peu de piment d'Espelette en plus."],
 "saint_jacques_poelees": [
  "**Purée.** Panais pelés en morceaux, lait et eau à hauteur, sel, 20 min : très tendres ; mixés avec 20 g de beurre et un peu de liquide : lisse et soyeuse.",
  "**Sécher.** Noix rincées rapidement, corail retiré (ou gardé), épongées sur papier, 15 min au frigo à découvert : bien sèches, elles dorent.",
  "**Saisir.** Poêle fumante, huile, noix posées en cercle, 1 min 30 sans toucher : croûte dorée ; retournées, 1 min ; beurre, arrosage 20 s : cœur nacré, translucide.",
  "**Servir.** Sur la purée chaude, fleur de sel, quelques gouttes de citron, beurre de cuisson."],
}
ASTUCES = {
 "sole_normande": ["Le jaune s'ajoute hors du feu : la sauce ne doit plus bouillir."],
 "bouchees_reine": ["La sauce suprême se prépare la veille ; les croustades se garnissent au dernier moment."],
 "blanquette_poulet": ["Une blanquette ne colore jamais : roux blanc, légumes non revenus, sauce ivoire."],
 "choucroute_mer": ["Le beurre blanc se tient 30 min au bain-marie tiède, pas plus chaud."],
 "baeckeoffe_volaille": ["La version d'origine mêle porc, bœuf et agneau ; ici bœuf et agneau."],
 "truffade": ["Une tome fraîche d'Auvergne (tome de cantal) file ; un cantal affiné, non."],
 "pissaladiere": ["Les oignons confits se préparent la veille."],
 "magret_cerises": ["Cerises surgelées : ajoutées encore congelées, 2 min de plus."],
 "quenelles_nantua_simple": ["À Lyon, le brochet est roi ; le cabillaud donne une quenelle plus douce."],
 "flamiche_maroilles": ["Le maroilles sent fort cru, beaucoup moins cuit."],
 "croque_monsieur": ["Un pain de mie de la veille absorbe moins la béchamel."],
 "tielle_setoise": ["La sauce doit être froide et épaisse : chaude, elle ramollit la pâte."],
 "bourride_setoise": ["La lotte est la reine de la bourride ; le cabillaud convient."],
 "petit_sale_lentilles": ["Les lentilles vertes du Puy restent entières : pas de trempage."],
 "tomates_farcies": ["Les tomates de fin d'été, charnues, tiennent la cuisson."],
 "axoa_veau": ["L'axoa se réchauffe très bien : il est meilleur le lendemain."],
 "saint_jacques_poelees": ["Achète des noix « fraîches, non trempées » : les noix gorgées d'eau ne dorent pas."],
 "moules_marinieres": ["Des moules de bouchot de la Baie du Mont-Saint-Michel (AOP) : petites, pleines, sucrées."],
 "pissaladiere_": [],
}
ASTUCES.pop("pissaladiere_")

# ---------------------------------------------------------------- accords mets-vins régionaux
# (vin rouge, vin blanc ou rosé) par région, et un accord sans alcool du terroir
_REG = [
 ("Bourgogne", "un bourgogne rouge (pinot noir, Mercurey ou Givry)", "un chablis ou un mâcon blanc", "jus de raisin de pinot noir ; eau pétillante au cassis"),
 ("Franche-Comté", "un côtes-du-jura rouge (poulsard)", "un côtes-du-jura blanc ou un vin jaune", "jus de pomme fermier"),
 ("Alsace", "un pinot noir d'Alsace", "un riesling ou un pinot gris d'Alsace", "jus de pomme-rhubarbe ; bière sans alcool"),
 ("Grand Est", "un pinot noir d'Alsace", "un riesling d'Alsace ou un champagne brut", "jus de pomme-rhubarbe"),
 ("Provence", "un bandol rouge", "un rosé de Provence ou un cassis blanc", "citronnade au thym ; jus de raisin muscat"),
 ("Corse", "un patrimonio rouge (niellucciu)", "un patrimonio blanc (vermentinu)", "jus de clémentine corse"),
 ("Nouvelle-Aquitaine", "un bordeaux (médoc, saint-émilion) ou un madiran", "un entre-deux-mers ou un jurançon sec", "jus de raisin rouge ; thé noir glacé"),
 ("Occitanie", "un corbières, un fitou ou un cahors", "un picpoul-de-pinet", "jus de raisin blanc ; sirop de violette à l'eau pétillante"),
 ("Auvergne-Rhône-Alpes", "un beaujolais (morgon, fleurie) ou une mondeuse de Savoie", "un apremont ou une roussette de Savoie", "jus de pomme de Savoie ; eau pétillante au sirop de génépi sans alcool"),
 ("Bretagne", "un cidre brut fermier", "un muscadet sur lie", "cidre sans alcool ou jus de pomme pétillant"),
 ("Normandie", "un cidre ou un poiré fermier", "un cidre brut", "jus de pomme pétillant de Normandie"),
 ("Hauts-de-France", "une bière de garde", "une bière blanche", "bière sans alcool ; jus de pomme"),
 ("Pays de la Loire", "un chinon ou un saumur-champigny", "un muscadet ou un savennières", "jus de pomme ; eau pétillante citronnée"),
 ("Centre-Val de Loire", "un chinon ou un bourgueil", "un sancerre ou un vouvray sec", "jus de raisin blanc"),
 ("Île-de-France", "un côtes-du-rhône", "un bourgogne aligoté", "jus de raisin ; eau pétillante citronnée"),
 ("Outre-mer", "un ti-punch ou une bière locale (avec modération)", "un ti-punch ou une bière locale (avec modération)", "jus de goyave ; citron vert, sirop de canne et eau pétillante"),
]
_GEN = {  # sans région : selon le plat
 "viande_rouge": ("un côtes-du-rhône ou un bordeaux", "jus de raisin rouge ; thé noir fumé"),
 "poisson": ("un muscadet ou un chablis", "eau pétillante citronnée ; jus de pomme"),
 "dessert_choco": ("un banyuls ou un maury (vin doux)", "lait chocolaté froid ; jus de raisin noir"),
 "dessert": ("un muscat de Beaumes-de-Venise ou un sauternes", "jus de pomme pétillant ; thé parfumé"),
 "autre": ("un bourgogne blanc ou un côtes-du-rhône", "eau pétillante citronnée ; jus de pomme fermier"),
}

def accords(d):
    """(alcool, sans_alcool) ajoutés à un plat, une entrée ou un dessert français qui n'en a pas."""
    reg = d["region"]
    if not reg.startswith("France") or d.get("kind") not in ("Plat", "Entrée", "Dessert"):
        return None
    # pas de vin conseillé avec la cuisine des enfants, les desserts simples ni les plats express de tous les jours
    if any(x in reg for x in ("enfants", "Desserts simples", "Anti-gaspi", "Cuisine du quotidien", "Food fusion")):
        return None
    prof = set(d.get("profil") or [])
    labels = " ".join((x[1] or "") + " " + (x[2] or "") for x in d["ing"]).lower()
    sweet = d["kind"] == "Dessert"
    if sweet:
        key = "dessert_choco" if "chocolat" in labels else "dessert"
        return [_GEN[key][0]], [_GEN[key][1]]
    fish = "poisson" in prof
    for name, rouge, blanc, sa in _REG:
        if name in reg:
            vin = blanc if fish or "leger" in prof and "viande_rouge" not in prof else rouge
            return [vin], [sa]
    key = "viande_rouge" if "viande_rouge" in prof else "poisson" if fish else "autre"
    return [_GEN[key][0]], [_GEN[key][1]]

# ---------------------------------------------------------------- régions françaises unifiées
_REGION_FIX = {"France › Bourgogne": "France › Bourgogne-Franche-Comté", "France › Franche-Comté": "France › Bourgogne-Franche-Comté"}

def region(d):
    r = d["region"]
    for a, b in _REGION_FIX.items():
        if r == a or r.startswith(a + " ›"):
            return b + r[len(a):]
    if r.strip() == "France":
        return "France › Cuisine de base"
    return r
