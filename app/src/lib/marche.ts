// Guide « Bien choisir, bien rattraper » (audit du chef, 16/10/2026) : ce que regardent un maraîcher, un boucher et un
// poissonnier, ce qu'on peut rattraper (fruit pas mûr ou trop mûr, viande dure, poisson moins frais)… et ce qu'on ne
// rattrape JAMAIS. Repères de professionnels, NON TESTÉS dans la cuisine d'ATLAS (Tome 7 §2). Les noms entre « refs »
// sont les ingrédients du Tome 3 : la fiche du dictionnaire affiche le conseil correspondant.

export interface Choix { name: string; refs: string[]; good: string; avoid: string; tip?: string }
export interface Rayon { id: string; title: string; icon: string; who: string; intro: string; items: Choix[] }

export const RAYONS: Rayon[] = [
  { id: "legumes", title: "Légumes", icon: "carrot", who: "le maraîcher", intro: "Un légume frais est lourd pour sa taille, ferme, brillant, et sa queue ou ses feuilles sont vertes. Le légume de saison, cueilli près de chez toi, a plus de goût et coûte moins cher.",
    items: [
      { name: "Tomate", refs: ["Tomate", "Tomate cerise"], good: "Lourde, parfumée au pédoncule, souple sous le doigt sans être molle ; de juin à septembre.", avoid: "Pâle et dure en hiver, vendue en grappe pour faire « jardin » (la grappe ne dit rien du goût).", tip: "Jamais au frigo : elle perd son parfum. À plat, pédoncule en bas." },
      { name: "Courgette, aubergine", refs: ["Courgette", "Aubergine"], good: "Petite à moyenne, peau tendue et brillante, ferme, pédoncule vert.", avoid: "Peau terne ou ridée, taches molles ; aubergine très grosse (pleine de graines, amère)." },
      { name: "Pommes de terre", refs: ["Pomme de terre"], good: "Fermes, sans germes ni taches vertes ; choisies selon l'usage : chair ferme (vapeur, salade, sautées), farineuse (purée, frites, soupe).", avoid: "Parties vertes ou germées en quantité : la solanine, toxique, s'y concentre.", tip: "Les parties vertes et les germes se retirent largement ; si toute la pomme de terre est verte, on la jette. À l'abri de la lumière, pas au frigo." },
      { name: "Carottes, poireaux, céleri", refs: ["Carotte", "Poireau", "Céleri-branche", "Céleri-rave"], good: "Carottes cassantes (elles font « crac »), fanes fraîches si elles en ont ; poireau au fût blanc long et ferme, feuilles vertes droites.", avoid: "Carottes molles qui plient, poireau jauni ou fendu." },
      { name: "Salades et herbes", refs: ["Salade (laitue, batavia)", "Roquette / mâche", "Persil plat / frisé", "Coriandre fraîche", "Menthe", "Basilic"], good: "Feuilles turgescentes, cœur bien fermé, base de la tige blanche et nette (pas rousse).", avoid: "Feuilles molles, visqueuses ou noircies.", tip: "Herbes : debout dans un verre d'eau comme un bouquet (basilic hors du frigo), ou roulées dans un torchon humide." },
      { name: "Champignons", refs: ["Champignon de Paris", "Shiitake"], good: "Chapeau fermé, ferme, sec au toucher, lamelles claires cachées.", avoid: "Lamelles noires bien ouvertes, chapeau gluant ou taché.", tip: "Dans un sac en papier, pas en barquette filmée : ils transpirent." },
      { name: "Choux, brocoli, chou-fleur", refs: ["Chou-fleur", "Brocoli", "Chou vert / frisé / kale", "Chou blanc / rouge"], good: "Lourd, serré, feuilles qui craquent ; brocoli vert foncé aux bouquets fermés.", avoid: "Brocoli qui jaunit (il fleurit : amer), chou-fleur aux taches brunes étendues." },
      { name: "Oignons, ail, échalotes", refs: ["Oignon jaune", "Oignon rouge", "Ail", "Échalote"], good: "Durs, peau sèche qui craque, lourds.", avoid: "Mous, germés, moisissure noire sous la peau.", tip: "Ail germé : on retire le germe vert (indigeste et amer), la gousse reste bonne." },
      { name: "Avocat", refs: ["Avocat"], good: "Pour aujourd'hui : cède légèrement sous le pouce près du pédoncule. Pour dans 3 jours : ferme.", avoid: "Très mou, creux sous la peau, pédoncule qui part seul en montrant du brun.", tip: "Petit truc de primeur : le pédoncule s'enlève et le dessous est vert = mûr à point ; brun = trop mûr." },
    ] },
  { id: "fruits", title: "Fruits", icon: "strawberry", who: "le maraîcher", intro: "Certains fruits continuent de mûrir après la cueillette (banane, avocat, kiwi, mangue, poire, pêche, abricot, tomate), d'autres jamais (fraise, cerise, raisin, agrumes, ananas, melon, pastèque) : ceux-là s'achètent prêts à manger.",
    items: [
      { name: "Fraises, cerises, petits fruits", refs: ["Fraise", "Cerise / griotte", "Framboise / mûre / myrtille"], good: "Brillants, parfumés à un mètre, colorés jusqu'au pédoncule ; queue verte et fraîche pour les cerises.", avoid: "Barquette tachée de jus au fond, un seul fruit moisi (il contamine les autres).", tip: "Lavés juste avant de manger, jamais avant de ranger." },
      { name: "Melon, pastèque", refs: ["Melon / pastèque"], good: "Melon lourd, parfumé au pédoncule, qui se détache ; pastèque qui sonne creux, tache jaune crème là où elle a reposé au sol.", avoid: "Melon sans odeur (il ne mûrira plus), fendu ou mou." },
      { name: "Agrumes", refs: ["Citron", "Citron vert", "Orange", "Mandarine / clémentine"], good: "Lourds (pleins de jus), peau fine et souple.", avoid: "Légers, peau épaisse et grumeleuse, zones molles.", tip: "Pour utiliser le zeste : agrumes « non traités après récolte »." },
      { name: "Pommes, poires", refs: ["Pomme", "Poire"], good: "Pommes fermes et parfumées ; poire qui cède un peu près de la queue.", avoid: "Meurtrissures étendues, chair farineuse (pomme) ou blette au cœur (poire)." },
      { name: "Bananes, mangues, ananas", refs: ["Banane", "Mangue", "Ananas"], good: "Banane jaune tachetée pour manger, jaune-vert pour dans 3 jours ; mangue qui cède sous le doigt et sent bon au pédoncule ; ananas parfumé à la base, une feuille du centre s'arrache facilement.", avoid: "Ananas qui sent le fermenté, mangue ridée." },
    ] },
  { id: "viandes", title: "Viandes", icon: "steak", who: "le boucher", intro: "Le bon morceau dépend de la cuisson : les morceaux nobles (filet, entrecôte, rumsteck) se saisissent vite ; les morceaux riches en collagène (paleron, joue, jarret, macreuse) doivent mijoter longtemps et deviennent fondants. Se tromper de morceau, c'est la première cause de viande dure.",
    items: [
      { name: "Bœuf", refs: ["Rumsteck", "Entrecôte", "Bavette", "Côte de bœuf", "Paleron", "Joue de bœuf", "Jarret de bœuf", "Macreuse / gîte"], good: "Rouge sombre à rouge vif, persillée de fins filets de gras blanc crème (le goût et le moelleux) ; maturée quelques semaines pour les pièces à griller.", avoid: "Viande qui baigne dans le sang, brune grisâtre, collante, odeur aigre.", tip: "Bourguignon, daube, pot-au-feu : demande « un mélange paleron, joue et macreuse ». À griller : « une bavette ou un rumsteck à point de maturation »." },
      { name: "Viande hachée", refs: ["Bœuf haché", "Agneau haché"], good: "Hachée devant toi chez le boucher, ou en barquette avec le taux de matières grasses (15 % pour les burgers, 5 % pour les sauces).", avoid: "Gris à cœur, odeur aigre, barquette gonflée.", tip: "La plus fragile des viandes : cuisinée le jour même, cuite à cœur pour les enfants (70 °C, plus de rose)." },
      { name: "Agneau, veau", refs: ["Gigot d'agneau", "Épaule d'agneau", "Côtelettes d'agneau", "Escalope de veau", "Épaule / tendron de veau", "Jarret de veau"], good: "Agneau rose vif, gras blanc et ferme ; veau rose très pâle, gras blanc nacré.", avoid: "Gras jaune et mou, viande terne ou sèche sur les bords." },
      { name: "Volailles", refs: ["Poulet entier", "Blanc de poulet", "Cuisse / pilon de poulet", "Dinde (escalope, cuisse, filet)", "Canard : magret, cuisse"], good: "Peau sèche, sans taches ni déchirures, chair ferme et rebondie ; Label Rouge ou fermier pour le goût (poulet élevé plus longtemps, en plein air).", avoid: "Peau collante ou visqueuse, odeur même légère, jus abondant dans la barquette.", tip: "Ne lave pas la volaille : l'eau projette les bactéries dans l'évier ; la cuisson suffit." },
      { name: "Abats", refs: ["Foies / gésiers de volaille", "Langue de bœuf", "Tripes / gras-double de bœuf", "Queue de bœuf"], good: "Très frais, brillants, achetés chez le boucher pour le jour même ou le lendemain.", avoid: "Couleur terne, odeur prononcée.", tip: "Tripes : demande-les « blanchies », le long nettoyage est fait." },
    ] },
  { id: "poissons", title: "Poissons", icon: "fish", who: "le poissonnier", intro: "Un poisson frais sent la mer, l'iode, l'algue : jamais « le poisson ». C'est le produit le plus fragile de ta liste de courses : il s'achète en dernier, voyage au frais et se cuisine dans les 24 heures.",
    items: [
      { name: "Poisson entier", refs: ["Dorade", "Bar / loup", "Maquereau", "Sardine (fraîche / conserve)"], good: "Œil bombé, noir et brillant ; ouïes rouge vif et humides ; peau brillante, écailles bien accrochées ; chair ferme : le doigt ne laisse pas de trace.", avoid: "Œil creux, gris ou laiteux ; ouïes brunes ; peau terne et visqueuse ; ventre mou ou percé.", tip: "Demande-le « vidé, écaillé et levé en filets » : le poissonnier le fait gratuitement, et garde les arêtes pour un fumet si tu les veux." },
      { name: "Filets et pavés", refs: ["Cabillaud / morue fraîche", "Saumon (frais, pavé)", "Colin, lieu noir, merlu", "Thon (frais)"], good: "Chair nacrée, humide sans eau dans la barquette, feuillets serrés, coupe nette.", avoid: "Chair qui se sépare en feuillets, bords secs ou jaunis, liquide laiteux, odeur.", tip: "Le surgelé « pêché-congelé à bord » est souvent plus frais que le « frais » de plusieurs jours : bon choix pour les poissons blancs." },
      { name: "Coquillages", refs: ["Moules", "Palourdes / coques", "Huîtres"], good: "Vivants : coquilles fermées, ou qui se referment quand on les tapote ; lourds (pleins d'eau de mer).", avoid: "Coquille cassée ou ouverte qui ne se referme pas.", tip: "Après cuisson, on jette ceux qui sont restés fermés." },
      { name: "Crevettes, crustacés", refs: ["Crevettes (cuites/crues)"], good: "Crues : grises et translucides, tête bien attachée ; cuites : roses, chair ferme, sans odeur.", avoid: "Tête noire ou qui se détache, chair molle, odeur d'ammoniaque.", tip: "Les crevettes crues vendues « décongelées » ne se recongèlent pas." },
    ] },
];

export interface Rattrapage { id: string; title: string; ok: string; how: string[]; jeter?: string; recipes?: string[] }
export const RATTRAPAGES: Rattrapage[] = [
  { id: "fruit-pas-mur", title: "Fruit pas assez mûr", ok: "Banane, avocat, kiwi, mangue, poire, pêche, abricot, prune, tomate : ils mûrissent encore.",
    how: ["Dans un sac en papier fermé, avec une pomme ou une banane mûre (elles dégagent de l'éthylène, le gaz qui fait mûrir) : 1 à 3 jours à température ambiante.", "Jamais au frigo tant qu'ils ne sont pas mûrs : le froid bloque le mûrissement.", "Fraise, cerise, raisin, agrumes, ananas, melon ne mûriront plus : cuis-les (compote, poêlée au sucre, sirop) ou sers-les en salade avec du sucre et du citron qui les attendrissent.", "Tomates vertes : en chutney, ou panées et frites à l'américaine."],
    recipes: ["compote_pommes_poires"] },
  { id: "fruit-trop-mur", title: "Fruit trop mûr", ok: "Taches brunes, peau ridée, chair molle : il est même meilleur cuisiné, plus sucré et plus parfumé.",
    how: ["Banane noire : banana bread, pancakes, ou épluchée et congelée en rondelles pour les smoothies.", "Pommes et poires : compote, crumble, chutney pour le fromage.", "Fraises, pêches, abricots : coulis mixé, smoothie, confiture minute (fruits + 30 % de sucre, 10 min).", "Avocat très mûr : guacamole, s'il est vert ; les filaments bruns se retirent."],
    jeter: "Moisissure, odeur de vinaigre ou d'alcool (fermentation), chair grise et liquide. Un fruit moisi dans une barquette : on jette les fruits qui le touchent.",
    recipes: ["banana_bread", "smoothie_fruits_abimes", "crumble_pommes_mures", "pancakes_banane_avoine"] },
  { id: "legume-fatigue", title: "Légume fatigué, salade molle, herbes fanées", ok: "Un légume qui a perdu de l'eau n'est pas abîmé.",
    how: ["20 min dans l'eau glacée : salade, herbes, carottes, céleri, radis retrouvent leur croquant.", "Trop mous pour être ranimés : soupe, velouté, purée, sauce tomate, pesto (herbes).", "Fanes de radis et de carottes, tiges d'herbes : pesto ou soupe."],
    jeter: "Partie gluante ou qui sent mauvais, moisissure étendue.", recipes: ["pesto", "minestrone", "chips_epluchures"] },
  { id: "viande-dure", title: "Viande trop dure", ok: "Presque toujours une erreur de morceau ou de cuisson, pas une mauvaise viande.",
    how: ["Morceau à mijoter (paleron, joue, jarret, épaule) encore dur : il n'est pas assez cuit. Continue à frémissement, couvert, 30 à 60 min de plus : il durcit d'abord, puis devient fondant.", "Steak ou rôti trop cuit : tranche-le très finement contre les fibres (perpendiculairement aux lignes de la viande) et nappe-le de sauce ou de beurre fondu ; ou émince-le pour un sauté minute.", "La prochaine fois, avant la cuisson : maillet ou rouleau entre deux films pour les escalopes ; marinade au yaourt (2 à 12 h) ou au kiwi, à l'ananas ou à la papaye râpés (30 min maximum, sinon la viande devient farineuse).", "Volaille sèche : effilochée dans une sauce chaude (crème, tomate, curry), elle retrouve du moelleux.", "Dernier recours : hachée au couteau pour un parmentier, des boulettes ou une farce."],
    jeter: "Une viande dure n'est pas dangereuse ; une viande qui sent l'aigre, colle ou a dépassé sa date l'est : voir « Viande ou volaille à la date limite ».",
    recipes: ["hachis_parmentier", "marinade_tandoori"] },
  { id: "poisson-moins-frais", title: "Poisson pas de première fraîcheur", ok: "Seulement s'il sent encore neutre ou légèrement marin, sans odeur d'ammoniaque, et avant sa date limite : sa chair est un peu molle, il a perdu son éclat. Il reste sain, mais n'est plus bon cru.",
    how: ["Plus de cru ni de cuisson rosée (tartare, ceviche, sushi, mi-cuit) : il se cuit à cœur.", "Cuissons qui pardonnent : en sauce (curry, tajine, à la tomate), en court-bouillon, en papillote avec citron et herbes.", "Émietté après cuisson : croquettes, brandade, parmentier, rillettes.", "Un bain de 10 min dans du lait ou de l'eau citronnée raffermit la chair et atténue le goût fort."],
    jeter: "Odeur d'ammoniaque ou de « poisson » marquée, chair visqueuse ou qui reste creusée sous le doigt, œil enfoncé gris, ouïes brunes, date dépassée. Thon, maquereau, sardine, anchois mal conservés peuvent contenir de l'histamine : la cuisson ne la détruit pas. Un goût piquant ou poivré sur la langue : on recrache et on jette. En cas de doute, on ne rattrape pas un poisson.",
    recipes: ["croquettes_poisson", "brandade"] },
  { id: "viande-douteuse", title: "Viande ou volaille à la date limite", ok: "La date limite de consommation (DLC, « à consommer jusqu'au ») est une limite de sécurité, pas une suggestion.",
    how: ["Avant la date, viande à l'odeur neutre : cuis-la aujourd'hui, à cœur, ou congèle-la tout de suite (le jour de la date au plus tard).", "Congelée la veille de sa date, elle se décongèle au frigo et se cuisine dans les 24 h."],
    jeter: "Date dépassée, odeur aigre ou soufrée, surface collante ou visqueuse, barquette gonflée. Laver une viande douteuse ne la rend pas sûre." },
  { id: "pain-rassis", title: "Pain rassis, biscuits ramollis", ok: "Le pain dur n'est pas abîmé, il a séché.",
    how: ["Pour le manger tel quel : passé sous le robinet 2 secondes, puis 5 min au four à 180 °C ; il redevient croustillant (à manger tout de suite).", "Biscuits, chips, céréales ramollis : 5 min au four à 150 °C.", "Sinon : pain perdu, croûtons, chapelure, panzanella, soupe à l'oignon."],
    jeter: "La moindre moisissure sur du pain de mie ou une brioche (moelleux : la moisissure s'étend à l'intérieur).", recipes: ["pain_perdu", "croutons_chapelure", "panzanella"] },
];

export const LABELS: [string, string][] = [
  ["Label Rouge", "Qualité gustative supérieure contrôlée : pour la volaille, élevage plus long, en plein air, alimentation surtout végétale. Le label qui change le plus le goût d'un poulet."],
  ["AOP / AOC", "Produit d'un terroir précis, fabriqué selon un savoir-faire fixé (comté, lentille verte du Puy, piment d'Espelette)."],
  ["IGP", "Lien avec une région pour au moins une étape (volailles de Loué, pruneaux d'Agen) : plus souple que l'AOP."],
  ["Agriculture biologique (AB)", "Sans pesticides ni engrais de synthèse ; pour les animaux, accès au plein air et alimentation bio. Ne dit rien du goût."],
  ["MSC (poissons sauvages), ASC (élevage)", "Pêche ou aquaculture certifiées durables : un repère simple au rayon poisson."],
  ["« Origine France », « Viande bovine française »", "Né, élevé, abattu en France pour la viande bovine française ; pour le reste, lire où l'animal a été élevé."],
  ["Halal", "Abattage rituel, certifié par un organisme : vérifie le nom du certificateur sur l'étiquette ou demande-le au boucher."],
];

export const PHRASES: [string, string][] = [
  ["Au boucher", "« C'est pour un bourguignon pour six : quels morceaux me conseillez-vous ? » · « Pouvez-vous me le parer et le couper en cubes de 5 cm ? » · « Je voudrais les os pour un bouillon. »"],
  ["Au poissonnier", "« Qu'est-ce qui est arrivé ce matin ? » · « Vous pouvez me le vider, l'écailler et lever les filets ? » · « Je garde les arêtes et la tête pour un fumet. »"],
  ["Au maraîcher", "« C'est pour manger aujourd'hui ou dans trois jours ? » (il choisira les fruits au bon stade) · « Vous auriez des légumes moches ou abîmés moins chers pour une soupe ? »"],
];

export const MALIN: string[] = [
  "Achète les morceaux à mijoter (paleron, joue, macreuse, épaule, cuisses de volaille) : moitié prix des morceaux nobles, plus de goût.",
  "Poissons moins demandés et de saison : maquereau, sardine, lieu noir, merlu, chinchard. Les moules sont parmi les protéines les moins chères.",
  "Un poulet entier coûte moins cher au kilo que les morceaux : rôti le dimanche, bouillon le lundi, restes le mardi.",
  "Légumes de saison et « moches » ; surgelés nature (épinards, petits pois, haricots) : récoltés à maturité, sans perte.",
  "Courses dans l'ordre : épicerie, puis fruits et légumes, puis frais, et poisson et viande en dernier, dans un sac isotherme ; au frigo dès le retour.",
];

/** Le conseil d'achat d'un ingrédient du Tome 3 (affiché sur sa fiche du dictionnaire). */
export function choixOf(ref: string): { c: Choix; who: string } | null {
  for (const r of RAYONS) for (const c of r.items) if (c.refs.includes(ref)) return { c, who: `l'œil ${r.who.startsWith("le ") ? "du " + r.who.slice(3) : "de " + r.who}` };
  return null;
}
