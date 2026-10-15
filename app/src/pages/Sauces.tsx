import { ImportRow } from "../components/video";
import { useState } from "react";
import { useImportLibrary, RECIPES } from "../lib/data";
import { useProfile } from "../lib/store";
import { Chip, Grid, Page, RecipeCard, Section, useVisible } from "../components/ui";

// « Sauce Builder » (Tome 1 §11.3) : base → profil → aromates ; proportions, étapes et conservation calculées.
type Base = "oeuf" | "aquafaba" | "yaourt" | "tomate" | "tahini" | "huile";
const BASES: Record<Base, { label: string; ing: string[]; how: string; keep: number; warn?: string; allergens: string[] }> = {
  oeuf: { label: "Mayonnaise (œuf)", ing: ["1 jaune d'œuf très frais", "1 c. à c. de moutarde", "180 ml d'huile de tournesol", "1 c. à c. de citron", "1 pincée de sel"], how: "Fouette jaune, moutarde, citron et sel, puis l'huile goutte à goutte et en filet.", keep: 3, warn: "Œuf cru : pas pour les jeunes enfants, femmes enceintes, personnes fragiles (prends la base aquafaba ou yaourt).", allergens: ["Œufs", "Moutarde"] },
  aquafaba: { label: "Mayonnaise sans œuf (aquafaba)", ing: ["3 c. à s. d'aquafaba (jus de pois chiches)", "1 c. à c. de moutarde", "150 ml d'huile de tournesol", "1 c. à c. de citron", "1 pincée de sel"], how: "Au mixeur plongeur : aquafaba, moutarde, citron et sel au fond d'un bocal étroit, l'huile par-dessus, mixe en remontant lentement.", keep: 3, allergens: ["Moutarde"] },
  yaourt: { label: "Sauce au yaourt", ing: ["200 g de yaourt grec", "1 c. à s. d'huile d'olive", "1 c. à c. de citron", "1 pincée de sel"], how: "Mélange à la cuillère.", keep: 4, allergens: ["Lait"] },
  tomate: { label: "Base tomate (type ketchup)", ing: ["200 g de ketchup maison ou 2 c. à s. de concentré + 100 g de passata", "1 c. à s. de vinaigre de cidre", "1 c. à c. de sucre"], how: "Mélange ; pour une sauce chaude, fais frémir 10 min.", keep: 14, allergens: [] },
  tahini: { label: "Sauce tahini (sésame)", ing: ["3 c. à s. de tahini", "1 citron (jus)", "4 à 6 c. à s. d'eau froide", "1 pincée de sel"], how: "Fouette tahini et citron (ça épaissit), puis l'eau cuillère par cuillère jusqu'à une sauce nappante.", keep: 5, allergens: ["Sésame"] },
  huile: { label: "Vinaigrette (huile)", ing: ["1 c. à s. de vinaigre de cidre", "1 c. à c. de moutarde", "3 c. à s. d'huile", "1 pincée de sel"], how: "Dissous le sel dans le vinaigre, ajoute moutarde et huile, secoue en bocal.", keep: 7, allergens: ["Moutarde"] },
};
const PROFILS: Record<string, { label: string; add: string[] }> = {
  doux: { label: "Doux", add: [] },
  releve: { label: "Relevé (type algérienne, samouraï)", add: ["1 c. à c. de harissa maison (à ajuster)", "1 c. à s. de concentré de tomate", "½ c. à c. de paprika"] },
  fume: { label: "Fumé (type barbecue)", add: ["1 c. à c. de paprika fumé", "1 c. à c. de miel", "1 c. à c. de ketchup maison"] },
  acidule: { label: "Acidulé", add: ["1 c. à s. de jus de citron en plus", "le zeste d'½ citron"] },
  curry: { label: "Curry", add: ["1 c. à c. de curry en poudre", "1 c. à c. de miel"] },
};
const AROMATES: Record<string, { label: string; add: string; keepMax?: number; warn?: string }> = {
  ail: { label: "Ail", add: "½ gousse d'ail pressée", keepMax: 4 },
  herbes: { label: "Herbes fraîches", add: "1 c. à s. d'herbes ciselées (ciboulette, persil, coriandre)", keepMax: 3 },
  cornichons: { label: "Cornichons, câpres", add: "1 c. à s. de cornichons et câpres hachés" },
  oignon: { label: "Oignon, échalote", add: "1 c. à s. d'échalote hachée très fin", keepMax: 2 },
  piment: { label: "Piment frais", add: "½ piment frais épépiné et haché", warn: "Piquant : pas pour les jeunes enfants." },
  fromage: { label: "Parmesan", add: "1 c. à s. de parmesan râpé" },
};

function Builder() {
  const p = useProfile();
  const [base, setBase] = useState<Base>(p.allergens.includes("OE") ? "aquafaba" : "oeuf");
  const [prof, setProf] = useState("doux");
  const [aro, setAro] = useState<string[]>(["ail"]);
  const b = BASES[base];
  const keep = Math.min(b.keep, ...aro.map((a) => AROMATES[a].keepMax ?? 99));
  const conflicts = b.allergens.filter((a) => p.allergens.some((x) => ({ OE: "Œufs", MO: "Moutarde", LA: "Lait", SE: "Sésame" } as Record<string, string>)[x] === a));
  return (
    <div className="card pad builder">
      <h3>1. Base</h3>
      <div className="chips">{(Object.keys(BASES) as Base[]).map((k) => <Chip key={k} on={base === k} onClick={() => setBase(k)}>{BASES[k].label}</Chip>)}</div>
      <h3>2. Profil</h3>
      <div className="chips">{Object.entries(PROFILS).map(([k, v]) => <Chip key={k} on={prof === k} onClick={() => setProf(k)}>{v.label}</Chip>)}</div>
      <h3>3. Aromates</h3>
      <div className="chips">{Object.entries(AROMATES).map(([k, v]) => <Chip key={k} on={aro.includes(k)} onClick={() => setAro(aro.includes(k) ? aro.filter((x) => x !== k) : [...aro, k])}>{v.label}</Chip>)}</div>
      <div className="builder-out">
        <h3>Ta sauce</h3>
        <ul>{[...b.ing, ...PROFILS[prof].add, ...aro.map((a) => AROMATES[a].add)].map((x) => <li key={x}>{x}</li>)}</ul>
        <p><strong>Comment :</strong> {b.how} Ajoute ensuite {[...PROFILS[prof].add, ...aro.map((a) => AROMATES[a].add)].length ? "le reste et mélange ; goûte et ajuste (le piquant augmente au repos)" : "rien d'autre : c'est prêt"}. 15 min au frais avant de servir.</p>
        <p><strong>Conservation :</strong> {keep} jour{keep > 1 ? "s" : ""} au frigo (≤ 4 °C), en bocal propre et fermé, étiqueté avec la date.</p>
        {b.warn && <p className="warn-text">⚠️ {b.warn}</p>}
        {aro.map((a) => AROMATES[a].warn && <p key={a} className="warn-text">⚠️ {AROMATES[a].warn}</p>)}
        {conflicts.length > 0 && <p className="bad-text">⛔ Contient {conflicts.join(", ")}, exclu(s) de ton profil.</p>}
        <p className="small">Allergènes de la base : {b.allergens.join(", ") || "aucun"}. Aucun additif : la conservation vient du froid, de l'acidité et du sel. Pas d'huile aromatisée à l'ail conservée longtemps (botulisme).</p>
      </div>
    </div>
  );
}

export default function Sauces() {
  const IMPORT_LIBRARY = useImportLibrary();
  const list = useVisible(RECIPES.filter((r) => r.cats.includes("sauces")));
  const tiktok = IMPORT_LIBRARY.filter((i) => i.cat === "sauces" || i.cat === "fait_maison");
  return (
    <Page photo="rubrique/sauces" title="Sauces maison" sub="Au plus simple, sans additif ni conservateur : mayonnaise, algérienne, samouraï, sauce blanche, barbecue, ketchup… et les frites qui vont avec." back="/explorer">
      <div className="card pad charte">
        <strong>La charte ATLAS des sauces</strong> : aucun E-numéro, conservateur, exhausteur ou arôme artificiel ; 8 ingrédients maximum, trouvables en supermarché ; une durée de conservation honnête ; une version sans œuf quand c'est possible ; sans porc et sans alcool garantis (vinaigre de cidre plutôt que de vin pour les profils stricts).
      </div>
      <Grid>{list.map((r) => <RecipeCard key={r.id} r={r} />)}</Grid>
      <Section title="Crée ta sauce (Sauce Builder)"><Builder /></Section>
      {tiktok.length > 0 && (
        <Section title={`Tes favoris TikTok : sauces et fait maison (${tiktok.length})`}>
          <ul className="links-list">{tiktok.map((i) => <ImportRow key={i.url} i={i} />)}</ul>
        </Section>
      )}
    </Page>
  );
}
