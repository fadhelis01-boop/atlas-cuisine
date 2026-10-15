// Lexique du débutant (Tome 13 §11) : les mots de cuisine employés dans les étapes, expliqués en une phrase,
// avec la fiche technique quand elle existe. Repéré automatiquement dans chaque étape.
import { norm } from "./text";

export interface Term { term: string; def: string; tech?: string }

export const GLOSSAIRE: (Term & { rx: RegExp })[] = [
  { term: "Ciseler", rx: /\bcisel/, def: "Couper en tout petits dés réguliers (oignon, échalote) ou en fines lanières (herbes).", tech: "ciseler-oignon" },
  { term: "Émincer", rx: /\bemince|\bemincer/, def: "Couper en tranches fines et régulières.", tech: "emincer" },
  { term: "Julienne", rx: /julienne/, def: "Bâtonnets très fins (2 mm) de légumes.", tech: "emincer" },
  { term: "Faire revenir / suer", rx: /fais( les)? revenir|faire revenir|suer|fondre l.oignon|oignons? fondus?/, def: "Cuire doucement dans un peu de matière grasse : « suer » sans coloration (translucide), « revenir » jusqu'à légèrement doré.", tech: "faire-revenir" },
  { term: "Saisir", rx: /\bsaisi/, def: "Cuire à feu très vif quelques minutes pour former une croûte dorée, sans cuire le cœur.", tech: "saisir" },
  { term: "Déglacer", rx: /deglac/, def: "Verser un liquide dans la poêle chaude et gratter les sucs collés au fond : ils font le goût de la sauce.", tech: "deglacer" },
  { term: "Réduire", rx: /\bredui|\breduis|\breduire/, def: "Faire bouillir doucement à découvert pour évaporer l'eau : la sauce épaissit et le goût se concentre.", tech: "reduire" },
  { term: "Napper / à la nappe", rx: /napp|a la nappe/, def: "Une sauce nappe quand elle recouvre le dos d'une cuillère et qu'un doigt y trace un sillon net.", tech: "creme-anglaise" },
  { term: "Mijoter", rx: /mijot/, def: "Cuire longtemps à petits frémissements (quelques bulles), couvercle posé.", tech: "mijoter" },
  { term: "Frémissement", rx: /fremi/, def: "L'eau ou la sauce bouge à peine, quelques petites bulles : juste avant l'ébullition.", tech: "mijoter" },
  { term: "Braiser", rx: /brais/, def: "Cuire à couvert avec peu de liquide, longtemps, après avoir saisi.", tech: "mijoter" },
  { term: "Pocher", rx: /\bpoch/, def: "Cuire dans un liquide frémissant (jamais bouillant) : œufs, poisson, volaille, poires.", tech: "oeufs-cuissons" },
  { term: "Blanchir", rx: /blanchi/, def: "Légumes : plonger quelques minutes dans l'eau bouillante salée puis dans l'eau glacée. Jaunes et sucre : fouetter jusqu'à ce que le mélange pâlisse." },
  { term: "Écumer", rx: /ecum/, def: "Retirer avec une cuillère la mousse grise qui monte à la surface d'un bouillon.", tech: "bouillon" },
  { term: "Nacrer", rx: /nacr/, def: "Riz : le faire revenir sec dans la matière grasse jusqu'à ce qu'il devienne translucide. Poisson : cuit juste à point, chair encore brillante au centre.", tech: "cuissons-poisson" },
  { term: "Mariner", rx: /marin/, def: "Laisser tremper viande, poisson ou légumes dans un mélange parfumé (huile, acide, épices) avant cuisson.", tech: "attendrir-viande" },
  { term: "Saumure", rx: /saumure/, def: "Eau salée (souvent sucrée) où l'on laisse tremper la viande pour qu'elle reste juteuse.", tech: "attendrir-viande" },
  { term: "Dégorger", rx: /degorg/, def: "Saler un légume (aubergine, concombre) pour lui faire rendre son eau ; ou faire tremper des coquillages pour qu'ils rejettent le sable.", tech: "degorger-dessaler" },
  { term: "Dessaler", rx: /dessal/, def: "Faire tremper un produit très salé (morue) dans l'eau froide changée plusieurs fois.", tech: "degorger-dessaler" },
  { term: "Torréfier", rx: /torref|toaste/, def: "Griller à sec épices, graines ou fruits secs jusqu'à ce qu'ils sentent bon.", tech: "torrefier" },
  { term: "Monder / peler à vif", rx: /monder|a vif/, def: "Retirer la peau (tomate ébouillantée 30 s) ou la peau et la membrane blanche d'un agrume.", tech: "degorger-dessaler" },
  { term: "Émulsionner / monter", rx: /emulsion|monte(r|z)? (la mayonnaise|au beurre|l.huile)|en filet/, def: "Mélanger énergiquement deux éléments qui ne se mélangent pas (huile et jaune) en versant l'huile en mince filet.", tech: "emulsionner" },
  { term: "Monter (blancs, crème)", rx: /monte(r|s|z)? (les )?blancs|en neige|crem\w* montee|chantilly/, def: "Fouetter pour incorporer de l'air : blancs en neige, crème fouettée.", tech: "separer-oeuf" },
  { term: "Bec d'oiseau", rx: /bec d.oiseau/, def: "Repère de texture : en relevant le fouet ou la spatule, la pâte ou la meringue forme une pointe qui se courbe.", tech: "pate-a-choux" },
  { term: "Ruban", rx: /\bruban/, def: "La pâte fouettée coule de la spatule en un ruban continu qui reste un instant à la surface.", tech: "biscuits-base" },
  { term: "Incorporer délicatement", rx: /incorpor/, def: "Mélanger à la spatule en soulevant, du centre vers les bords, pour ne pas faire retomber l'air.", tech: "incorporer" },
  { term: "Beurre pommade", rx: /pommade|beurre mou/, def: "Beurre ramolli à température ambiante jusqu'à la consistance d'une crème.", tech: "pate-sucree" },
  { term: "Sabler", rx: /sabl/, def: "Frotter farine et beurre froid entre les doigts jusqu'à obtenir un sable.", tech: "pate-brisee" },
  { term: "Foncer", rx: /\bfonce|\bfoncer/, def: "Garnir un moule de pâte, bien dans les angles, sans l'étirer.", tech: "pate-brisee" },
  { term: "Cuire à blanc", rx: /a blanc/, def: "Cuire un fond de tarte vide (avec des billes ou des haricots secs) avant de le garnir.", tech: "pate-sucree" },
  { term: "Dorer (dorure)", rx: /dorure/, def: "Badigeonner d'œuf battu (ou de lait) au pinceau pour une croûte brillante." },
  { term: "Bain-marie", rx: /bain.marie/, def: "Cuire ou fondre dans un récipient posé sur (ou dans) de l'eau chaude, pour une chaleur douce.", tech: "bain-marie" },
  { term: "Pétrir", rx: /petri/, def: "Travailler la pâte (pousser, replier) pour développer le gluten : elle devient lisse et élastique.", tech: "petrir" },
  { term: "Pointage / pousse", rx: /pointage|\bpousse\b|apprets?|lever/, def: "Repos de la pâte levée : elle gonfle sous l'action de la levure.", tech: "pointage" },
  { term: "Rabats", rx: /rabat/, def: "Étirer un bord de la pâte et le replier sur elle-même, tout autour : remplace le pétrissage.", tech: "pointage" },
  { term: "Façonner / bouler", rx: /faconn|boul(er|e serree)/, def: "Donner sa forme à la pâte (boule, baguette) en la tendant.", tech: "faconner" },
  { term: "Grigner / scarifier", rx: /grign|scarif|entaill/, def: "Inciser la pâte avant cuisson pour qu'elle s'ouvre joliment.", tech: "vapeur-four" },
  { term: "Tourage", rx: /tourage|tour (simple|double)/, def: "Plier plusieurs fois une pâte autour du beurre pour créer des feuillets.", tech: "pate-levee-feuilletee" },
  { term: "Tempérer", rx: /temper/, def: "Chocolat : fondre, refroidir puis réchauffer à des températures précises pour qu'il soit brillant et cassant.", tech: "temperer-chocolat" },
  { term: "Macaronner", rx: /macaronn/, def: "Mélanger la meringue au mélange amande-sucre jusqu'à ce qu'il coule en ruban brillant.", tech: "macarons" },
  { term: "Confire", rx: /confi(t|re|s)\b/, def: "Cuire très lentement dans une graisse ou un sirop, à petite température.", tech: "confire" },
  { term: "Flamber", rx: /flamb/, def: "Enflammer un alcool chauffé versé sur un plat. Optionnel, jamais sous une hotte allumée.", tech: "deglacer" },
  { term: "Dessécher (pâte à choux)", rx: /dessech/, def: "Remuer la pâte sur le feu 1 à 2 min pour en évaporer l'eau.", tech: "pate-a-choux" },
  { term: "Repos de la viande", rx: /repos \d|laisse reposer|repose \d/, def: "Laisser la viande cuite quelques minutes sous aluminium : les jus se répartissent, elle reste juteuse.", tech: "cuisson-viande-rouge" },
  { term: "Al dente", rx: /al dente/, def: "Pâtes ou riz cuits mais qui résistent légèrement sous la dent.", tech: "cuire-pates" },
  { term: "Gratiner", rx: /gratin/, def: "Passer au four très chaud ou sous le gril pour dorer le dessus." },
  { term: "Chinois / filtrer", rx: /chinois|filtre/, def: "Passer un liquide dans une passoire fine pour retirer les morceaux." },
  { term: "Mirepoix / brunoise", rx: /mirepoix|brunoise/, def: "Légumes coupés en dés : gros (mirepoix, pour les fonds) ou très petits (brunoise).", tech: "emincer" },
];

/** Mots de cuisine employés dans un texte (étapes d'une recette). */
export function termsIn(text: string): Term[] {
  const n = norm(text);
  return GLOSSAIRE.filter((t) => t.rx.test(n)).map(({ term, def, tech }) => ({ term, def, tech }));
}
