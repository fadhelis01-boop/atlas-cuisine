// « Si ça ne se passe pas comme prévu » (Tome 13 §11, audit du débutant) : pour chaque recette, les problèmes les plus
// fréquents et comment les rattraper, choisis d'après ce que la recette contient (gestes, ingrédients, cuissons),
// complétés par les erreurs décrites dans les fiches techniques liées. Rédaction NON TESTÉE en cuisine (Tome 7 §2).
import type { Recipe } from "./types";
import { norm } from "./text";
import { techniqueFor } from "./techniques";

export interface Rescue { problem: string; fix: string; tech?: string }

const CARDS: { when: RegExp; problem: string; fix: string; tech?: string; ing?: boolean }[] = [  // ing : ne regarde que le titre et les ingrédients
  // assaisonnement (toutes les recettes salées)
  { when: /./, problem: "C'est trop salé", fix: "Allonge (crème, lait de coco, eau ou bouillon non salé, tomates), ajoute un féculent cuit sans sel (pommes de terre, riz) ou un peu d'acidité (citron) qui équilibre. La pomme de terre crue « qui absorbe le sel » est un mythe : elle dilue seulement." },
  { when: /./, problem: "C'est fade", fix: "Avant d'ajouter du sel : une pointe d'acide (citron, vinaigre), du gras (beurre, huile d'olive) ou des herbes fraîches réveillent souvent mieux. Goûte à chaque étape, pas seulement à la fin." },
  { when: /piment|harissa|cayenne|sriracha|chili|scotch bonnet|curry/, problem: "C'est trop piquant", fix: "Ajoute du gras ou du laitage (yaourt, crème, lait de coco), un peu de sucre ou de miel, et sers avec riz ou pain. L'eau n'aide pas. La prochaine fois : épépine le piment, ou mets-le entier sans le percer et retire-le." },
  // sauces, liaisons
  { when: /sauce|reduire|reduis|napp|jus|epaissi|veloute|lie\b|lier/, problem: "La sauce est trop liquide", fix: "Laisse réduire à découvert à feu moyen en remuant ; ou lie : 1 c. à c. de maïzena délayée dans 1 c. à s. d'eau froide, versée dans la sauce frémissante, 1 min. Une sauce nappe quand elle couvre le dos d'une cuillère et qu'un doigt y trace un sillon net." },
  { when: /sauce|reduire|reduis|napp|creme/, problem: "La sauce est trop épaisse ou attache", fix: "Ajoute un peu de liquide chaud (bouillon, eau, lait) cuillère par cuillère hors du feu, en fouettant. Si le fond a brûlé, ne gratte pas : transvase sans le fond." },
  { when: /mayonnaise|aioli|emulsion|emulsionn|hollandaise|bearnaise|rouille|toum/, problem: "L'émulsion a tranché (sauce huileuse, en grains)", fix: "Dans un bol propre : 1 jaune (ou 1 c. à c. de moutarde, ou 1 c. à s. d'eau très chaude pour une sauce au beurre), puis la sauce ratée cuillère par cuillère en fouettant. Pour les sauces chaudes au beurre : hors du feu, un glaçon et fouette fort.", tech: "emulsionner" },
  { when: /bechamel|roux|farine.*lait|lait.*farine/, problem: "Il y a des grumeaux", fix: "Fouette énergiquement hors du feu, ou un coup de mixeur plongeant, ou passe au tamis. La prochaine fois : roux chaud + lait froid (ou l'inverse), jamais les deux chauds.", tech: "roux-bechamel" },
  { when: /creme anglaise|a la nappe|creme patissiere|pâtissiere|patissiere|jaunes/, problem: "La crème a tourné ou fait des grumeaux", fix: "Verse-la aussitôt dans un bol froid et mixe 30 s au mixeur plongeant : elle redevient souvent lisse. Pour la crème pâtissière : fouette sans arrêt au moment où elle épaissit." },
  // viandes
  { when: /mijot|bourguignon|daube|ragout|braise|paleron|joue|jarret|epaule|collier|tajine|curry|mafe|colombo|cari/, problem: "La viande mijotée est dure", fix: "Elle n'est pas encore assez cuite : les morceaux à collagène durcissent d'abord puis deviennent fondants. Continue à frémissement (jamais à gros bouillon) 30 à 60 min, en ajoutant du liquide chaud si besoin.", tech: "mijoter" },
  { when: /saisir|saisis|steak|cote de boeuf|magret|entrecote|rumsteck|bavette|onglet/, problem: "La viande a rendu de l'eau et ne dore pas", fix: "Poêle pas assez chaude ou trop remplie. Retire la viande, fais réduire le jus, remets de l'huile, attends que ça fume légèrement, et saisis par petites quantités sans toucher 2 min.", tech: "saisir" },
  { when: /steak|cote de boeuf|magret|entrecote|gigot|roti|carre/, problem: "C'est trop cuit à l'intérieur", fix: "Tranche finement et nappe de sauce ou de beurre fondu ; ou transforme en émincé (wok, sandwich). La prochaine fois : thermomètre et retirer 3-5 °C avant la cible, puis repos.", tech: "cuisson-viande-rouge" },
  { when: /poulet|volaille|dinde|cuisse|blanc de poulet|canard/, problem: "Je ne sais pas si la volaille est cuite", fix: "Pique la partie la plus épaisse : le jus doit être clair, sans rose, et la chair se détacher de l'os. Avec un thermomètre : 74 °C à cœur. Sinon, remets 5-10 min.", tech: "securite-temperatures" },
  // poissons
  { when: /poisson|saumon|cabillaud|dorade|bar\b|sole|lieu|colin|maquereau|thon|lotte/, problem: "Le poisson colle ou se défait", fix: "Il a été retourné trop tôt : il se décolle seul quand la croûte est formée. Pour sauver : finis-le au four 5 min dans la poêle, sans y toucher. Sers en morceaux, nappé de sauce.", tech: "cuissons-poisson" },
  // pâtes, pains, pâtisseries
  { when: /levure boulangere|levure seche|pousse|pointage|petris|brioche|pain|pizza|naan|pita/, problem: "La pâte n'a pas levé", fix: "Pièce trop froide ou levure inactive. Mets-la près d'un radiateur ou dans le four éteint avec un bol d'eau chaude, 30-60 min de plus. Si rien ne bouge en 2 h : levure morte (eau trop chaude ? plus de 40 °C la tue) : recommence avec une levure neuve.", tech: "pointage" },
  { when: /petris|pate a pain|pizza|brioche|pain|naan|pita|msemen|bokit/, problem: "La pâte colle aux mains", fix: "C'est souvent normal au début : pétris 5 min de plus, elle devient lisse. Mains et plan légèrement huilés plutôt que farinés (trop de farine rend le pain sec).", tech: "petrir" },
  { when: /pate a choux|choux|eclair|chouquette|gougere|paris.brest|profiterole/, problem: "Les choux sont retombés", fix: "Ils sont sortis trop tôt ou le four a été ouvert. On ne peut pas les regonfler, mais ils se garnissent quand même (coupés en deux). La prochaine fois : bien dorés jusque dans les fentes, porte fermée, puis 5 min four éteint porte entrouverte.", tech: "pate-a-choux" },
  { when: /gateau|cake|genoise|muffin|brownie|quatre.quarts|madeleine|financier|fondant/, problem: "Le gâteau est cru au centre mais doré dessus", fix: "Couvre d'aluminium et prolonge de 5 à 10 min à 160 °C. Test : une lame plantée au centre ressort sèche (ou avec quelques miettes humides pour un brownie, un fondant)." },
  { when: /gateau|cake|genoise|muffin|madeleine|biscuit|quatre.quarts/, problem: "Le gâteau est sec", fix: "Imbibe-le d'un sirop (1 volume de sucre pour 2 d'eau, chauffés, parfumés) ou sers-le avec une crème anglaise, une compote. La prochaine fois : 5 min de moins, et vérifie la température de ton four (beaucoup chauffent plus qu'affiché)." },
  { when: /pate brisee|pate sucree|tarte|fond de tarte|foncer/, problem: "Le fond de tarte a rétréci ou est détrempé", fix: "Rétréci : la pâte avait été étirée ou n'avait pas assez reposé au froid ; elle reste bonne. Détrempé : cuis le fond à blanc avant de garnir, et dore-le au jaune d'œuf 2 min.", tech: "pate-sucree" },
  { when: /meringue|blancs en neige|monter les blancs|pavlova|macaron/, problem: "Les blancs ne montent pas", fix: "Une trace de jaune ou de gras dans le bol : recommence dans un bol parfaitement propre (essuyé au citron). Une pincée de sel ou quelques gouttes de citron aident.", tech: "separer-oeuf" },
  { when: /caramel/, problem: "Le caramel a cristallisé ou brûlé", fix: "Cristallisé (sable blanc) : ajoute 3 c. à s. d'eau et un trait de citron, chauffe sans remuer jusqu'à ce qu'il refonde. Brûlé (noir, âcre) : il ne se rattrape pas, recommence ; trempe la casserole dans l'eau chaude pour la nettoyer.", tech: "caramel-sucre" },
  { when: /chocolat|ganache|temper/, problem: "Le chocolat a figé en pâte granuleuse", fix: "Une goutte d'eau ou un excès de chaleur. Il ne sert plus pour tempérer, mais ajoute 2-3 c. à s. de crème chaude et mixe : tu obtiens une ganache, parfaite pour un gâteau ou une sauce.", tech: "ganache" },
  { when: /chantilly|creme fleurette|monter la creme|creme montee/, problem: "La chantilly ne monte pas, ou tourne en beurre", fix: "Ne monte pas : crème pas assez froide ou pas assez grasse (30 % minimum) ; mets bol et crème 15 min au congélateur. Tourne en beurre : ajoute 2-3 c. à s. de crème liquide froide et mélange doucement à la spatule.", tech: "creme-chantilly-ganache-montee" },
  // féculents
  { ing: true, when: /\briz\b|risotto|paella|biryani|pilaf/, problem: "Le riz est collant, pâteux ou brûlé au fond", fix: "Collant : il fallait le rincer et ne pas remuer pendant la cuisson ; étale-le sur une plaque, il se raffermit (parfait pour un riz sauté le lendemain). Brûlé au fond : ne racle pas, transvase le dessus. Risotto et paella : un fond qui accroche est voulu (socarrat).", tech: "cuire-riz" },
  { ing: true, when: /pates|spaghetti|nouilles|lasagne|gnocchi|udon|ramen/, problem: "Les pâtes collent entre elles", fix: "Pas assez d'eau ou pas remuées au début. Passe-les sous l'eau chaude puis mélange avec la sauce et une louche d'eau de cuisson. La prochaine fois : 1 L d'eau pour 100 g, remuer la première minute.", tech: "cuire-pates" },
  { when: /frire|friture|frites|beignet|tempura|pane|chapelure/, problem: "La friture est grasse et molle", fix: "Huile pas assez chaude ou bain trop chargé : la température chute. Remonte à 175-180 °C, fais de petites quantités, égoutte sur une grille. Les frites : double cuisson (150 °C puis 180 °C).", tech: "frire" },
  // œufs
  { when: /oeufs? (poches?|mollets?|durs?)|omelette|brouill|oeuf parfait|oeufs? cocotte/, problem: "L'œuf est trop cuit (jaune sec, bord vert)", fix: "Pour un œuf dur : plonge-le dans l'eau glacée dès la fin du minuteur. Pour une omelette ou des œufs brouillés : retire du feu quand c'est encore un peu coulant, la chaleur termine.", tech: "oeufs-temperatures" },
  // légumes
  { when: /legumes|courgette|aubergine|poivron|ratatouille|tian|gratin/, problem: "Les légumes rendent de l'eau, le plat est aqueux", fix: "Sale-les et laisse-les dégorger 20 min (aubergines, courgettes, concombre), ou fais-les revenir à feu vif en premier pour évaporer l'eau. Pour un gratin déjà cuit : 10 min de plus à découvert." },
  { when: /four|enfourn|gratin|rotir|roti\b/, problem: "Le dessus brûle mais l'intérieur n'est pas cuit", fix: "Couvre d'une feuille d'aluminium, baisse le four de 20 °C et prolonge la cuisson. Ton four chauffe sans doute plus qu'affiché : un petit thermomètre de four (quelques euros) évite ce piège. Place le plat au milieu du four, pas en haut." },
  { when: /moules?|coques|palourdes|bulots/, problem: "Des coquillages restent fermés", fix: "Ne les force pas : jette ceux qui restent fermés après cuisson (ils étaient morts avant). Avant cuisson, jette aussi ceux qui sont ouverts et ne se referment pas quand on les tape.", tech: "moules-coquillages" },
  { when: /fromage|gruyere|comte|cheddar|mozzarella|raclette|fondue|reblochon|parmesan|feta|chevre/, ing: true, problem: "Le fromage devient huileux ou en grumeaux", fix: "Il a trop chauffé ou trop vite. Hors du feu, ajoute une cuillère de liquide froid (lait, vin blanc ou citron) et un peu de maïzena délayée, et remue doucement. Pour gratiner : four chaud et peu de temps, fromage râpé ajouté à la fin." },
  { when: /carotte|haricots verts|brocoli|chou|courgette|petits pois|epinard|poireau|navet|legumes/, ing: true, problem: "Les légumes sont trop durs ou réduits en purée", fix: "Trop durs : couvre et prolonge de quelques minutes avec un fond d'eau. Trop cuits : transforme-les en velouté ou en purée. La prochaine fois : coupe-les de taille égale et goûte-les à la pointe du couteau (elle doit entrer sans forcer)." },
  { when: /oignon/, problem: "Les oignons brûlent au lieu de fondre", fix: "Baisse le feu, ajoute une cuillère d'eau et une pincée de sel, couvre 5 min. Des oignons noirs sont amers : retire-les et recommence, ça vaut la peine." },
];

/** Problèmes probables pour cette recette, du plus spécifique au plus général (6 au plus), plus ceux des techniques liées. */
export function rescueFor(r: Recipe, max = 6): Rescue[] {
  const text = norm([r.title, r.steps.join(" "), r.ingredients.map((l) => l.label).join(" "), r.techniques.join(" ")].join(" "));
  const ingText = norm([r.title, r.ingredients.map((l) => `${l.label} ${l.ref ?? ""}`).join(" ")].join(" "));
  const sweet = r.role === "dessert" || r.role === "boisson";
  const title = norm(r.title + " " + r.origin);
  const scored: (Rescue & { score: number })[] = [];
  for (const c of CARDS) {
    if (sweet && /sale|fade|piquant/.test(norm(c.problem))) continue;
    if (!c.when.test(c.ing ? ingText : text)) continue;
    // le plus spécifique d'abord : la carte qui correspond au nom du plat, puis aux techniques de la fiche ; sel et fadeur en dernier
    const score = (c.when.test(title) ? 3 : 0) + (c.tech && r.techniques.some((t) => techniqueFor(t)?.id === c.tech) ? 2 : 0) - (/trop salé|fade/.test(c.problem) ? 5 : 0);
    scored.push({ problem: c.problem, fix: c.fix, tech: c.tech, score });
  }
  scored.sort((a, b) => b.score - a.score);
  const out: Rescue[] = scored.map(({ score: _s, ...x }) => x);
  const seen = new Set(out.map((o) => o.tech).filter(Boolean));
  for (const label of r.techniques) {
    const t = techniqueFor(label);
    if (!t || seen.has(t.id)) continue;
    seen.add(t.id);
    for (const e of t.errors.slice(0, 1)) out.push({ problem: `${t.name} : erreur fréquente`, fix: e, tech: t.id });
  }
  return out.slice(0, max);
}
