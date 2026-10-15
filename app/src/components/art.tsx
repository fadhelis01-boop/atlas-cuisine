// Habillage illustré d'ATLAS (Tome 13 §6) : couvertures générées pour les fiches sans photo, bandeau d'accueil
// et bandeaux de rubrique. Tout est en SVG léger (aucune image à télécharger, fonctionne hors connexion) ;
// décoratif uniquement (aria-hidden), le texte reste en HTML pour le contraste et les lecteurs d'écran.
import { useId } from "react";
import type { Recipe } from "../lib/types";
import { norm } from "../lib/text";

/** Teinte de base par grande région (palette « marché » : tomate, safran, pistache, aubergine, océan…). */
export const MACRO_HUE: Record<string, number> = { france: 8, europe_sud: 30, europe_nord: 205, maghreb: 38, afrique: 18, moyen_orient: 44, asie_sud: 28,
  asie_est: 352, asie_sud_est: 150, amerique_nord: 4, amerique_latine: 95, oceanie: 185 };

// Un emoji par plat, déduit du titre (le premier mot-clé trouvé gagne), puis du type de plat.
const BY_WORD: [RegExp, string][] = [
  [/chocolat|brownie|truffe|ganache|brigadeiro|lamington/, "🍫"], [/macaron/, "🍥"], [/croissant|pain au chocolat|chocolatine/, "🥐"], [/bagel/, "🥯"],
  [/cookie|sable|speculoos|biscuit|anzac|alfajor|tuile/, "🍪"], [/glace|sorbet|milk-?shake/, "🍨"], [/beignet|churro|bugne|puff|donut/, "🍩"],
  [/crepe|pancake|blini|gaufre|msemen/, "🥞"], [/tarte|quiche|tourte|flamiche|pissaladiere|tielle/, "🥧"], [/gateau|cake|fraisier|buche|cheesecake|baba|fiadone|quatre-quarts|financier|madeleine|kouign|kougelhopf|canele|basboussa|makrout|kalb/, "🍰"],
  [/creme|flan|panna|pudding|mousse|ile flottante|kheer|riz au lait|teurgoule/, "🍮"], [/caramel|bonbon|sucette|rocher|mendiant|orangette|praline/, "🍬"],
  [/pizza|lahmacun|manakish/, "🍕"], [/burger/, "🍔"], [/taco|enchilada|quesadilla|tostada|burrito/, "🌮"], [/sandwich|bokit|banh mi|pan bagnat|croque|welsh|smorrebrod/, "🥪"],
  [/ramen|pho|nouille|udon|laksa|pancit|chow mein|bo bun|vermicelle/, "🍜"], [/sushi|onigiri|poke/, "🍙"], [/gyoza|ravioli|pierogi|dumpling|jiaozi|bao|nem|samoussa|empanada|fataya|bourek|briouat/, "🥟"],
  [/falafel|kefta|kofta|boulette|polpette|kottbullar/, "🧆"], [/curry|dal|biryani|masala|colombo|cari|rendang|korma|tikka|makhani/, "🍛"],
  [/soupe|veloute|potage|bouillon|harira|chorba|bortsch|minestrone|gaspacho|gazpacho|bisque|garbure|tourin|caldo|lablabi|miso|tom kha/, "🥣"],
  [/salade|taboule|fattouche|coleslaw|som tam|larb|panzanella/, "🥗"], [/pates|spaghetti|lasagne|macaroni|gnocchi|risotto|crozet|spatzle|cacio/, "🍝"],
  [/riz|paella|jollof|thieb|pilaf|tahdig|nasi|bibimbap|mujaddara|koshari/, "🍚"], [/couscous|semoule|tajine|tagine/, "🥘"],
  [/fondue|tartiflette|raclette|aligot|truffade|fromage|gougere|camembert|cheddar|mac and cheese|khachapuri|pao de queijo/, "🧀"],
  [/\boeufs?\b|omelette|chakchouka|shakshuka|menemen|tortilla de patatas|tortilla espanola/, "🍳"], [/frite|patatas|pommes de terre|puree|gratin|sarladaise|stoemp|rosti|poutine/, "🍟"],
  [/poulet|volaille|chicken|nugget|coq|pintade|dinde|yassa|souvlaki|chich/, "🍗"], [/canard|magret|confit/, "🍗"], [/agneau|gigot|souris|navarin|mechoui|dibi|stew/, "🍖"],
  [/boeuf|steak|cote de|entrecote|bourguignon|daube|joue|pot-au-feu|goulash|carbonade|bulgogi|suya|lomo|chili/, "🥩"],
  [/crevette|gambas|scampi/, "🦐"], [/moule|huitre|coque|palourde|saint-jacques/, "🦪"], [/calamar|poulpe|seiche|tielle/, "🦑"],
  [/saumon|thon|cabillaud|morue|bacalhau|poisson|bar |dorade|sole|maquereau|sardine|lieu|brandade|ceviche|gravlax|blaff|amok|kokoda|fish|bouillabaisse/, "🐟"],
  [/pain|baguette|fougasse|focaccia|ciabatta|brioche|bretzel|soda bread|cornbread|naan|pita|chapati|arepa|batbout|mhadjeb/, "🍞"],
  [/sauce|mayo|ketchup|moutarde|aioli|rouille|tartare|bearnaise|hollandaise|pesto|chimichurri|salsa|mojo|romesco|tzatziki|raita|toum|tahini|nuoc|harissa|chutney|pickles|gribiche|pico/, "🥫"],
  [/epice|ras el|garam|curry en poudre|berbere|dukkah|zaatar|nokoss|bouillon cube|bouillon en poudre|marinade/, "🧂"],
  [/the |the$|chai|matcha/, "🍵"], [/cafe|frappe/, "☕"], [/chocolat chaud|lait d.or|lassi|ayran|horchata|smoothie/, "🥛"],
  [/mojito|limonade|citronnade|punch|sangria|agua|ginger|sirop|bissap|jus/, "🍹"],
  [/fraise|framboise|fruits rouges|cerise|clafoutis/, "🍓"], [/pomme|crumble|tatin|chausson|strudel|normande/, "🍎"], [/poire/, "🍐"], [/banane|plantain|alloco|kelewele/, "🍌"],
  [/mangue/, "🥭"], [/citron/, "🍋"], [/orange/, "🍊"], [/peche/, "🍑"], [/ananas/, "🍍"], [/coco/, "🥥"], [/pasteque|halloumi/, "🍉"],
  [/avocat|guacamole|feroce/, "🥑"], [/aubergine|moussaka|caponata|zaalouk|moutabal|imam/, "🍆"], [/carotte/, "🥕"], [/champignon/, "🍄"], [/mais|elote/, "🌽"],
  [/chou|kimchi|endive|poireau|epinard|palak|ndole|sabzi/, "🥬"], [/lentille|haricot|pois chiche|feve|ful|loubia|chana|houmous|feijoada|maharagwe|misir|parippu/, "🥣"],
  [/tomate|gaspacho|pa amb/, "🍅"], [/piment|piri/, "🌶️"], [/olive|tapenade/, "🥗"], [/ail/, "🧄"], [/oignon/, "🧅"], [/courge|potiron|butternut/, "🎃"],
];
const BY_KIND: Record<string, string> = { Pain: "🍞", Sauce: "🥫", Boisson: "🍹", Dessert: "🍰", "Goûter / dessert": "🧁", Entrée: "🥗", Base: "🍯", Accompagnement: "🥔", Plat: "🍲" };

export function dishEmoji(r: Pick<Recipe, "title" | "kind">, special?: string) {
  if (special) return special;
  const t = norm(r.title).replace(/['’]/g, " ");
  for (const [re, e] of BY_WORD) if (re.test(t)) return e;
  return BY_KIND[r.kind] ?? "🍽️";
}

type Motif = "vichy" | "dots" | "bubbles" | "waves" | "wheat" | "leaves" | "stars";
const MOTIF: Record<string, Motif> = { Plat: "vichy", Dessert: "dots", "Goûter / dessert": "stars", Boisson: "bubbles", Sauce: "waves", Base: "waves", Pain: "wheat", Entrée: "leaves", Accompagnement: "leaves" };

function hashOf(s: string) { let h = 0; for (let i = 0; i < s.length; i++) h = (h * 31 + s.charCodeAt(i)) | 0; return Math.abs(h); }

function MotifDefs({ id, motif, ink }: { id: string; motif: Motif; ink: string }) {
  const o = { fill: ink, stroke: ink };
  switch (motif) {
    case "vichy": return <pattern id={id} width="16" height="16" patternUnits="userSpaceOnUse"><rect width="8" height="16" fill={ink} opacity="0.16" /><rect width="16" height="8" fill={ink} opacity="0.16" /></pattern>;
    case "dots": return <pattern id={id} width="14" height="14" patternUnits="userSpaceOnUse"><circle cx="4" cy="4" r="2.2" fill={o.fill} opacity="0.28" /><circle cx="11" cy="11" r="2.2" fill={o.fill} opacity="0.28" /></pattern>;
    case "stars": return <pattern id={id} width="22" height="22" patternUnits="userSpaceOnUse"><path d="M6 2l1.2 3 3 .2-2.3 2 .8 3-2.7-1.7L3.3 10l.8-3L1.8 5.2l3-.2z" fill={o.fill} opacity="0.3" /><circle cx="17" cy="16" r="1.6" fill={o.fill} opacity="0.3" /></pattern>;
    case "bubbles": return <pattern id={id} width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="6" cy="7" r="3.5" fill="none" stroke={o.stroke} strokeWidth="1.2" opacity="0.35" /><circle cx="17" cy="17" r="2" fill="none" stroke={o.stroke} strokeWidth="1" opacity="0.35" /><circle cx="19" cy="5" r="1.2" fill={o.fill} opacity="0.3" /></pattern>;
    case "waves": return <pattern id={id} width="24" height="12" patternUnits="userSpaceOnUse"><path d="M0 6q6-6 12 0t12 0" fill="none" stroke={o.stroke} strokeWidth="1.6" opacity="0.3" /></pattern>;
    case "wheat": return <pattern id={id} width="20" height="20" patternUnits="userSpaceOnUse"><path d="M10 3v14M10 7l-3-2M10 7l3-2M10 11l-3-2M10 11l3-2" fill="none" stroke={o.stroke} strokeWidth="1.3" strokeLinecap="round" opacity="0.3" /></pattern>;
    default: return <pattern id={id} width="26" height="26" patternUnits="userSpaceOnUse"><path d="M5 18c0-7 6-12 13-12-1 7-6 12-13 12z" fill={o.fill} opacity="0.22" /><path d="M5 18L14 10" stroke={o.stroke} strokeWidth="0.8" opacity="0.3" /></pattern>;
  }
}

/** Couverture illustrée : fond dégradé de la région, motif du type de plat, assiette, emoji du plat. */
export function IllustratedCover({ r, emoji }: { r: Recipe; emoji: string }) {
  const uid = useId().replace(/:/g, "");
  const base = MACRO_HUE[r.macro] ?? 20;
  const h = (base + (hashOf(r.id) % 24) - 12 + 360) % 360; // nuance propre à chaque fiche
  const motif = MOTIF[r.kind] ?? "vichy";
  return (
    <div className="ill-cover" aria-hidden="true" style={{ background: `linear-gradient(135deg, hsl(${h} 78% 62%), hsl(${(h + 28) % 360} 68% 44%))` }}>
      <svg className="ill-motif" focusable="false"><defs><MotifDefs id={`m${uid}`} motif={motif} ink="#FFFFFF" /></defs><rect width="100%" height="100%" fill={`url(#m${uid})`} /></svg>
      <svg className="ill-plate" viewBox="0 0 100 100" focusable="false">
        <defs>
          <radialGradient id={`p${uid}`} cx="0.45" cy="0.4" r="0.6">
            <stop offset="0" stopColor="#FFFDF8" /><stop offset="0.8" stopColor="#F6EEDF" /><stop offset="1" stopColor="#E9DCC6" />
          </radialGradient>
        </defs>
        <ellipse cx="53" cy="56" rx="46" ry="42" fill="rgb(0 0 0 / 18%)" />
        <circle cx="50" cy="50" r="46" fill={`url(#p${uid})`} />
        <circle cx="50" cy="50" r="34" fill="none" stroke={`hsl(${h} 50% 55% / 35%)`} strokeWidth="1.6" />
      </svg>
      <span className="ill-emoji">{emoji}</span>
    </div>
  );
}

/** Bandeau d'accueil : planche de cuisine vue du dessus (assiette fumante, herbes, agrumes, piment, épices). */
export function HeroArt() {
  return (
    <svg className="hero-art" viewBox="0 0 360 260" aria-hidden="true" focusable="false">
      <defs>
        <radialGradient id="hplate" cx="0.45" cy="0.4" r="0.65"><stop offset="0" stopColor="#FFFDF8" /><stop offset="0.85" stopColor="#F3E8D4" /><stop offset="1" stopColor="#DCC9A8" /></radialGradient>
        <radialGradient id="hsoup" cx="0.4" cy="0.35" r="0.7"><stop offset="0" stopColor="#F4B23F" /><stop offset="1" stopColor="#C8553D" /></radialGradient>
        <linearGradient id="hboard" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stopColor="#C98B4E" /><stop offset="1" stopColor="#9A6334" /></linearGradient>
      </defs>
      {/* planche */}
      <rect x="150" y="150" width="190" height="96" rx="18" fill="url(#hboard)" transform="rotate(-8 245 198)" opacity="0.95" />
      <circle cx="320" cy="168" r="6" fill="#7A4B24" transform="rotate(-8 245 198)" />
      {/* assiette et soupe */}
      <ellipse cx="168" cy="132" rx="96" ry="90" fill="rgb(0 0 0 / 22%)" />
      <circle cx="160" cy="122" r="92" fill="url(#hplate)" />
      <circle cx="160" cy="122" r="66" fill="url(#hsoup)" />
      <path d="M118 112c14-10 30-4 40 6s28 14 44 2" fill="none" stroke="#FFF2D6" strokeWidth="4" strokeLinecap="round" opacity="0.7" />
      <circle cx="140" cy="140" r="5" fill="#4F7A2B" /><circle cx="176" cy="150" r="4" fill="#4F7A2B" /><circle cx="186" cy="104" r="4.5" fill="#4F7A2B" />
      <path d="M150 96l8 6M170 128l7-5M132 122l-6 6" stroke="#F7E7B0" strokeWidth="3" strokeLinecap="round" />
      {/* vapeur */}
      <g className="steam" fill="none" stroke="#FFF7EA" strokeWidth="5" strokeLinecap="round" opacity="0.85">
        <path d="M138 44c-10-14 10-18 0-32" /><path d="M162 40c-10-14 10-18 0-32" /><path d="M186 44c-10-14 10-18 0-32" />
      </g>
      {/* citron */}
      <circle cx="290" cy="70" r="34" fill="#F3D046" /><circle cx="290" cy="70" r="27" fill="#FBE98A" />
      <g stroke="#F3D046" strokeWidth="3">{[0, 45, 90, 135].map((a) => <line key={a} x1="290" y1="70" x2={290 + 27 * Math.cos((a * Math.PI) / 180)} y2={70 + 27 * Math.sin((a * Math.PI) / 180)} />)}</g>
      {/* piment */}
      <path d="M250 214c30-6 58-24 72-50 3 22-24 58-70 62z" fill="#C8302A" /><path d="M322 164c4-8 10-10 16-8" stroke="#3E7B2C" strokeWidth="5" strokeLinecap="round" fill="none" />
      {/* basilic */}
      <g fill="#3F8A3A">
        <path d="M40 210c-6-26 14-44 36-40-2 24-16 38-36 40z" /><path d="M66 232c4-26 28-34 46-22-10 20-28 28-46 22z" opacity="0.9" />
        <path d="M30 168c8-22 30-26 44-12-14 16-30 18-44 12z" opacity="0.85" />
      </g>
      {/* ail et grains d'épices */}
      <path d="M262 122c-14 0-22 12-18 24 4 10 30 10 34 0 4-12-4-24-16-24z" fill="#F7EEDC" stroke="#D9C7A6" strokeWidth="2" />
      <g fill="#7A3E1D">{[[60, 70], [74, 58], [52, 52], [86, 76], [40, 84], [70, 90]].map(([x, y]) => <circle key={`${x}${y}`} cx={x} cy={y} r="3.4" />)}</g>
      <g fill="#E8A33D">{[[96, 40], [110, 30], [84, 26], [122, 48]].map(([x, y]) => <circle key={`${x}${y}`} cx={x} cy={y} r="2.6" />)}</g>
    </svg>
  );
}

/** Bandeau de rubrique sans photo : couleur et motif propres à la page. */
export function PatternBand({ seed, children }: { seed: string; children: React.ReactNode }) {
  const uid = useId().replace(/:/g, "");
  const h = [8, 30, 150, 205, 352, 44, 95, 280][hashOf(seed) % 8];
  const motifs: Motif[] = ["vichy", "dots", "leaves", "waves", "stars", "wheat", "bubbles"];
  const motif = motifs[hashOf(seed + "m") % motifs.length];
  return (
    <div className="pattern-band" style={{ background: `linear-gradient(120deg, hsl(${h} 62% 34%), hsl(${(h + 35) % 360} 58% 28%))` }}>
      <svg aria-hidden="true" focusable="false"><defs><MotifDefs id={`b${uid}`} motif={motif} ink="#FFFFFF" /></defs><rect width="100%" height="100%" fill={`url(#b${uid})`} /></svg>
      <div className="band-text">{children}</div>
    </div>
  );
}
