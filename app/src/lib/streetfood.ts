// Rubrique Street food (audit « cuisinier expert de la street food », 12/11/2026, bible/AUDIT_STREET_FOOD_2026-11-12.md).
// La street food n'était qu'un filtre sur les titres : elle a maintenant ses familles, ses gestes de cuisinier de rue,
// ses soirées toutes faites. Les fiches sont choisies à la main (un mot du titre ne suffit pas : « crêpes Suzette »).
import { RECIPE_BY_ID } from "./data";
import type { Recipe } from "./types";

export interface Famille { id: string; label: string; icon: string; sub: string; ids: string[] }

export const FAMILLES: Famille[] = [
  { id: "sandwichs", label: "Sandwichs, pains garnis et burgers", icon: "burger", sub: "À la main, dans un papier.", ids: [
    "banh_mi", "pan_bagnat", "bokit_volaille", "tacos_lyonnais", "shawarma_poulet", "tombik_doner", "kebab_poulet_pain_maison", "adana_kebab",
    "souvlaki_poulet", "chich_taouk", "bocadillo_tortilla", "sandwich_merguez_orientale", "katsu_sando", "tamago_sando", "pain_charge_cameroun",
    "croque_monsieur", "burger_maison", "islak_burger", "hot_honey_chicken_burger", "bao_poulet", "bao_burger_bulgogi", "vada_pav", "pav_bhaji",
    "hot_dog_maison", "philly_cheesesteak", "choripan", "sabich", "balik_ekmek", "tantuni", "roujiamo_boeuf", "zapiekanka", "currywurst_volaille"] },
  { id: "galettes", label: "Tacos, galettes et crêpes de rue", icon: "taco", sub: "Cuites à la minute sur la plaque.", ids: [
    "tacos_al_pastor", "birria_res", "quesadillas_haricots_fromage", "arepas", "pupusas_frijol_queso", "tlayuda", "sopes", "crepes_bretonnes",
    "galette_saucisse_volaille", "socca", "manakish_zaatar", "lahmacun", "msemen", "mahjouba", "piadina", "jianbing", "dan_bing", "rolex_ouganda",
    "okonomiyaki", "banh_xeo", "roti_canai", "kottu_roti", "doubles_trinidad", "langos"] },
  { id: "fritures", label: "Fritures, chaussons et beignets salés", icon: "pot", sub: "Huile au thermomètre, papier absorbant.", ids: [
    "frites_maison", "poutine", "salchipapa", "fish_and_chips", "falafels", "tameya", "accras_morue", "akara_niebe", "acaraje", "coxinha", "arancini",
    "suppli", "panzerotti", "samoussas_legumes", "pastels_thon", "fataya", "empanadas", "jamaican_patty", "alloco", "kelewele", "nems_poulet",
    "pakoras", "korokke", "corn_dog_coreen_pain_mie", "chips_crevettes", "poulet_sel_poivre", "takoyaki", "panisse", "brik_oeuf", "bourek_algerien",
    "borek_fromage", "karantika"] },
  { id: "grillades", label: "Brochettes et grillades", icon: "steak", sub: "Sur la braise, la plancha ou le gril du four.", ids: [
    "suya", "suya_poulet", "tsire_agneau", "dibi", "yakitori", "tsukune", "satay_poulet", "anticuchos", "poulet_jerk", "elote", "esquites", "eomuk_tang"] },
  { id: "bouchees", label: "Raviolis, bouchées et bols de rue", icon: "chopsticks", sub: "Vapeur, wok et petits bols.", ids: [
    "gyoza", "xiao_long_bao", "momo_legumes", "dumplings_vapeur_legumes", "ha_kao", "kimbap", "onigiri", "tteokbokki", "pad_thai", "char_kway_teow",
    "som_tam", "pani_puri", "kumpir"] },
  { id: "sucre", label: "Le sucré de rue", icon: "cupcake", sub: "Beignets, gaufres et douceurs des marchés.", ids: [
    "churros", "liege_gaufres", "gaufres", "crepes_froment_sucre", "puff_puff", "mandazi", "sfenj", "bambalouni", "loukoumades", "taiyaki", "hotteok",
    "kkwabaegi", "egg_waffle", "martabak_manis", "tanghulu", "trdelnik", "kunefe", "jalebi", "pasteis_nata", "beignets_banane_cameroun", "bretzels"] },
];

export const STREET_IDS = new Set(FAMILLES.flatMap((f) => f.ids));
export const isStreetFood = (r: Recipe) => STREET_IDS.has(r.id);
export const streetRecipes = (f: Famille) => f.ids.map((id) => RECIPE_BY_ID[id]).filter(Boolean);

/** Soirées « street food » à la maison : trois à quatre plats qui se complètent et se préparent ensemble. */
export const SOIREES: { title: string; for: string; ids: string[] }[] = [
  { title: "Soirée tacos", for: "Une plaque, une marinade la veille, tout le monde garnit.", ids: ["tacos_al_pastor", "esquites", "churros"] },
  { title: "Marché de nuit asiatique", for: "Vapeur, wok et une douceur qui craque.", ids: ["gyoza", "jianbing", "takoyaki", "tanghulu"] },
  { title: "Kebab-frites maison", for: "La viande la veille, les frites en deux bains.", ids: ["kebab_poulet_pain_maison", "frites_maison", "bambalouni"] },
  { title: "Street food d'Afrique de l'Ouest", for: "Le gril, la friture et le piment à part.", ids: ["suya", "alloco", "akara_niebe", "puff_puff"] },
  { title: "Stand de foire", for: "Pour les enfants : tout se mange avec les doigts.", ids: ["hot_dog_maison", "salchipapa", "egg_waffle"] },
  { title: "Apéro des quais", for: "Marseille, Rome et Istanbul sur la même table.", ids: ["panisse", "suppli", "balik_ekmek", "kunefe"] },
];

/** Les gestes du cuisinier de rue, adaptés à la maison. */
export const GESTES: [string, string][] = [
  ["Friture", "Thermomètre obligatoire : 160 °C pour cuire (frites, gros beignets), 175-180 °C pour dorer, 185-190 °C pour recroustiller. Jamais plus d'un tiers de la casserole rempli d'huile, petites quantités à la fois."],
  ["Double cuisson", "Frites, poulet frit, beignets épais : une première cuisson qui cuit, une seconde à 185 °C qui croustille. C'est le secret des stands."],
  ["Plaque et plancha", "Préchauffe 10 min à vide : la viande doit chanter dès qu'elle touche. Une poêle en fonte remplace la plancha."],
  ["Mise en place", "Sur un stand, tout est coupé, mariné et rangé avant le premier client : fais pareil, la cuisson dure ensuite quelques minutes."],
  ["Sauces maison", "Sauce blanche, samouraï, chimichurri, nước chấm, sauce piment : préparées la veille, elles sont meilleures et sans additifs."],
  ["Le pain", "Toujours toasté côté mie (poêle, gril) : il ne se détrempe pas sous la garniture."],
];

/** La sécurité, là où la street food maison se rate le plus. */
export const SECURITE_STREET: string[] = [
  "Huile chaude : casserole lourde sur un feu arrière, manche tourné vers l'intérieur, enfants à distance. Si l'huile prend feu : couvercle et feu coupé, jamais d'eau.",
  "Une huile de friture se garde filtrée, au frais et à l'abri de la lumière, 5 à 6 utilisations au plus ; jetée si elle fume à 170 °C, sent le rance ou mousse.",
  "Viande hachée, volaille, saucisses : cuites à cœur (70 à 74 °C), même dans un sandwich pressé.",
  "Ce qui attend sur la table : moins de 2 h à température ambiante ; au-delà, au frigo. Ce qui est servi chaud reste au-dessus de 63 °C (four à 80 °C).",
  "Sauces à l'œuf cru (mayonnaise maison) : au frais jusqu'au service, pas pour les enfants de moins de 6 ans ni les femmes enceintes.",
];
