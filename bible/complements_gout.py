# -*- coding: utf-8 -*-
"""Audit gourmet (21/10/2026) §4.2, « assaisonnement plat » : les plats sans aucun élément acide (citron, vinaigre, tomate,
laitage fermenté, cornichon, vin, moutarde, fruit acide, fermenté) reçoivent l'acidité que leur cuisine leur donne.
C'est soit dans la recette (citron vert d'un curry, vinaigre des lentilles), soit à table (salade vinaigrée d'un gratin,
pickles d'un teriyaki, concombre vinaigré coréen). Les acides choisis ne portent ni trace d'alcool, ni
sulfites, ni poisson au référentiel : un filet de citron ne doit pas changer les badges d'un plat.

Un plat dont la tradition refuse l'acide est listé dans SANS_ACIDE avec sa raison : on ne trahit pas une recette pour un
contrôle. Une ligne marquée « ? » est facultative. Rien n'est testé en cuisine (Tome 7 §2).

ACIDE : id → (ligne d'ingrédient au format K, phrase ajoutée à la fin de la dernière étape, ou "" si les étapes en parlent déjà)
SALADE : plats servis avec une salade verte (accompagnement relié, ajouté aux courses)
"""

CIDRE = "Vinaigre de cidre"  # sans trace d'alcool ni sulfites au référentiel (le vinaigre de vin, de riz, de xérès en portent)
SALADE_VINAIGRETTE = ("1 c. à s.|de vinaigre de cidre (vinaigrette de la salade)|" + CIDRE + "|1?",
                      "À table, une salade verte à la vinaigrette : son acidité équilibre le fromage et la béchamel.")
PICKLES = ("2 c. à s.|de vinaigre de cidre (concombre en pickles rapides)|" + CIDRE + "|1?",
           "À côté, un concombre en fines tranches, 10 min dans le vinaigre avec une pincée de sucre et de sel : il coupe le laqué.")
KIMCHI = ("2 c. à s.|de vinaigre de cidre (concombre vinaigré, oi muchim)|" + CIDRE + "|1?",
          "À côté, comme en Corée, un concombre en fines rondelles avec le vinaigre, une pincée de sucre et de sésame : son acidité répond à la sauce sucrée-salée. Le kimchi y va aussi (il contient souvent du poisson).")

ACIDE = {
    # Afrique, Amériques
    "ndole": ("1|citron, en quartiers (à table)|Citron|1?", "Un quartier de citron à table, pour qui aime : il allège la richesse de l'arachide."),
    "arroz_con_pollo": ("1|citron vert, en quartiers|Citron vert|1?", "Un quartier de citron vert pressé sur chaque assiette réveille le riz."),
    "empanadas": ("2 c. à s.|de vinaigre de cidre (salsa criolla)|" + CIDRE + "|1?",
                  "À table, une salsa criolla : oignon et tomate en petits dés, vinaigre, huile, sel ; elle tranche sur la farce."),
    "burger_vegetarien_haricots": ("2 c. à s.|de vinaigre de cidre (oignon rouge mariné)|" + CIDRE + "|1?", "L'oignon rouge émincé, 10 min dans le vinaigre avec une pincée de sel et de sucre : rose, croquant et acidulé, il équilibre la galette."),
    "dinde_roti_farcie": ("100 g|de canneberges séchées (sauce, avec le jus d'une orange)|Canneberges séchées|1?",
                          "La sauce aux canneberges de Thanksgiving : 100 g de canneberges, le jus d'une orange, 2 c. à s. de sucre, 10 min à frémissement : elle fait briller la dinde."),
    "gumbo_poulet": ("1|citron, en quartiers|Citron|1?", "À table, des quartiers de citron et une sauce piquante, comme en Louisiane : quelques gouttes suffisent."),
    "muffins_oeufs_legumes": ("200 g|de tomates cerises, pour servir|Tomate cerise|1?", "Avec quelques tomates cerises : leur acidité allège l'œuf et le fromage."),
    "plov": ("3|tomates (salade achichuk)|Tomate|1?", "À côté, la salade achichuk : tomates et oignon en fines lamelles, sel, poivre ; sa fraîcheur équilibre le riz gras."),
    # Asie
    "char_siu_poulet": PICKLES,
    "poulet_teriyaki": PICKLES,
    "saumon_teriyaki": PICKLES,
    "congee_riz": ("1 c. à c.|de vinaigre de cidre, à table|" + CIDRE + "|1?", "Quelques gouttes de vinaigre à table, à la chinoise (le vinaigre noir, si tu en as)."),
    "nouilles_sautees_boeuf": ("1 c. à c.|de vinaigre de cidre|" + CIDRE + "|1?", "Un trait de vinaigre au dernier moment réveille la sauce (le vinaigre noir chinois, si tu en as)."),
    "dubu_jorim": KIMCHI,
    "galbi_jjim": KIMCHI,
    "japchae": KIMCHI,
    "tempura_legumes_crevettes": ("1|citron, en quartiers|Citron|1?", "Un quartier de citron et une pincée de sel fin, comme au Japon, pour qui préfère à la sauce."),
    "udon_sautees_legumes": ("1 c. à c.|de vinaigre de cidre|" + CIDRE + "|1?", "Un trait de vinaigre avec la sauce, hors du feu : plus net."),
    "yaki_udon": ("1 c. à s.|de gingembre mariné (gari)|Gingembre mariné (gari)|1?", "Un peu de gingembre mariné dessus, comme au Japon : il coupe le gras."),
    "yakitori": ("1|citron, en quartiers|Citron|1?", "Un quartier de citron à côté, comme dans les izakaya."),
    "curry_legumes_coco": ("½|citron vert|Citron vert|1", "Un filet de citron vert au moment de servir réveille le lait de coco."),
    "curry_vert_tofu_legumes": ("½|citron vert|Citron vert|1", "Un filet de citron vert à la fin : la sauce gagne en relief."),
    "pad_kra_pao_poulet": ("½|citron vert|Citron vert|1?", "À table, à la thaïe : piment frais émincé dans un peu de jus de citron vert et de sauce soja."),
    "gratin_chou_fleur_lentilles": ("½|citron|Citron|1?", "Un filet de citron sur chaque assiette réveille le curry et le lait de coco."),
    # Europe
    "cevapi": ("1 c. à s.|de vinaigre de cidre (ajvar)|" + CIDRE + "|1", "Les poivrons mixés avec le vinaigre et un filet d'huile : c'est l'ajvar, acidulé et doux."),
    "cordon_bleu_dinde": ("1|citron, en quartiers|Citron|1?", "Un quartier de citron à presser, comme pour une escalope viennoise."),
    "spaetzle_fromage": ("1 c. à s.|de vinaigre de cidre (salade verte)|" + CIDRE + "|1?", "Avec une salade verte bien vinaigrée, comme en Souabe : elle tranche le fromage."),
    "cocido_madrileno_version": ("200 g|de sauce tomate (pour les légumes)|Coulis / passata / tomates pelées|1?", "À Madrid, les légumes se servent avec un peu de sauce tomate chaude."),
    "frittata_courgettes": ("½|citron (salade de roquette)|Citron|1?", "Avec une salade de roquette au citron et à l'huile d'olive : fraîche et vive."),
    "orecchiette_brocoli_ail": ("½|citron (zeste et jus)|Citron|1?", "Un peu de zeste et de jus de citron à la fin avive le brocoli."),
    "polenta_champignons_creme": ("½|citron|Citron|1?", "Un filet de citron sur les champignons en fin de cuisson leur donne du relief."),
    "risotto_courge_sauge": ("½|citron|Citron|1?", "Quelques gouttes de citron avec le parmesan équilibrent la douceur de la courge."),
    "brandade": ("½|citron|Citron|1?", "Quelques gouttes de citron dans la brandade avant de gratiner, au goût."),
    "chou_braise_saucisses": ("1 c. à s.|de vinaigre de cidre|" + CIDRE + "|1", "Un trait de vinaigre de cidre à la fin : le chou garde sa douceur et gagne du relief."),
    "lentilles_saucisses": ("1 c. à s.|de vinaigre de cidre (ou de vin)|" + CIDRE + "|1", "Hors du feu, un trait de vinaigre dans les lentilles : c'est le geste des bouchons lyonnais."),
    "poulet_basse_temp": ("½|citron (dans le jus)|Citron|1?", "Quelques gouttes de citron dans le jus, au dernier moment, le rendent plus net."),
    "couscous_express_legumes": ("½|citron|Citron|1?", "Un filet de citron sur la semoule, pour qui aime."),
    "mechoui_four": ("1|citron (salade méchouia)|Citron|1?", ""),
    "falafels": ("1|citron (sauce tahini)|Citron|1", "La sauce : 3 c. à s. de tahini, le jus du citron, de l'eau froide cuillère par cuillère, sel ; fouettée, elle devient crémeuse et pâle."),
}
# les plats français gratinés ou fromagers : salade verte vinaigrée à table
for _id in ("crepes_salees_enfants", "croque_monsieur", "endives_jambon_dinde", "gratin_macaronis", "galette_complete", "galettes_sarrasin_champignons",
            "pain_perdu_sale", "croquettes_restes", "souffle_fromage", "omelette_fines_herbes", "toasts_champignons_oeuf", "truffade", "nuggets_maison"):
    ACIDE[_id] = SALADE_VINAIGRETTE
SALADE = [i for i, v in ACIDE.items() if v in (SALADE_VINAIGRETTE,)] + ["spaetzle_fromage", "frittata_courgettes"]
# lignes complémentaires (la sauce des falafels demande aussi son tahini)
EXTRA = {"burger_vegetarien_haricots": ["1 pincée|de sucre (oignon mariné)|Sucre blanc / roux / cassonade / vergeoise|1?"],
         "falafels": ["3 c. à s.|de tahini (sauce)|Tahini (purée de sésame)|1"],
         "dinde_roti_farcie": ["1|orange (jus, sauce aux canneberges)|Orange|1?", "2 c. à s.|de sucre (sauce aux canneberges)|Sucre blanc / roux / cassonade / vergeoise|1?"]}

SANS_ACIDE = {
    "cacio_e_pepe": "Trois ingrédients : un acide casserait la crème de pecorino. À Rome, la salade qui suit apporte la fraîcheur.",
    "spaghetti_carbonara": "La liaison œuf-pecorino est le plat ; un acide la trancherait. La fraîcheur vient de la salade qui suit.",
    "spaghetti_aglio_olio": "Ail, huile, piment : la recette tient en trois saveurs, la tradition n'y ajoute rien.",
    "gnocchi_maison": "Beurre noisette et sauge : la douceur est voulue.",
    "tortilla_espanola": "Œufs, pommes de terre, oignon : la tortilla se mange telle quelle, souvent avec du pain à la tomate.",
    "cabillaud_vapeur_gingembre": "Poisson vapeur cantonais : le goût repose sur le poisson, le gingembre et la cébette ; un acide les masquerait.",
    "onigiri": "En-cas de riz : la tradition cache parfois une prune salée acidulée (umeboshi) au centre, à ajouter si tu en trouves.",
    "ramen_shoyu": "Bouillon shoyu : la profondeur vient du bouillon et du soja, la tradition n'ajoute pas d'acide.",
    "cornish_pasty": "Chausson du mineur, mangé à la main : la tradition ne l'accompagne de rien.",
    "irish_stew": "Ragoût blanc irlandais : douceur voulue de l'agneau, de l'oignon et des pommes de terre.",
    "axoa_veau": "Veau et piment doux d'Espelette : une douceur voulue, servie avec des pommes de terre.",
    "pissaladiere": "Oignons confits, anchois, olives : le sel des anchois répond à la douceur des oignons.",
    "dafina": "Mijoté du shabbat, doux et épicé, cuit toute la nuit : la tradition n'y met pas d'acide.",
    "rechta_poulet": "Plat blanc algérois à la cannelle, doux par tradition.",
    "rfissa": "Fenugrec, ras el-hanout, lentilles : saveur chaude voulue, sans acide.",
    "tajine_agneau_pruneaux": "Sucré-salé du tajine aux pruneaux : le miel et le fruit tiennent la place de l'acide.",
    "sapasui": "Vermicelles sautés samoans, simples par tradition (soja, gingembre).",
}
