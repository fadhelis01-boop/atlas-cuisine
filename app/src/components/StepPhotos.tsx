import etapesJson from "../data/etapes.json";
import { Credit, Photo, photoOf } from "./photo";

// Photos de gestes et d'étapes (illustrations/etapes_*.py) : sous licence libre, choisies une à une.
// Clé « technique/<id> » ou « recette/<id> » → liste de { k: clé de photo, c: légende }.
const ETAPES = etapesJson as unknown as Record<string, { k: string; c: string }[]>;
export const stepPhotosOf = (key: string) => (ETAPES[key] ?? []).filter((x) => photoOf(x.k));

/** Galerie numérotée, légendée et créditée ; rien si aucune photo n'existe pour ce sujet. */
export default function StepPhotos({ subject, title }: { subject: string; title: string }) {
  const list = stepPhotosOf(subject);
  if (!list.length) return null;
  return (
    <section className="section">
      <div className="section-head"><h2>{title}</h2></div>
      <ol className="step-photos">
        {list.map((x, i) => (
          <li key={x.k}>
            <figure>
              <div className="thumb43"><Photo k={x.k} alt={x.c} sizes="(min-width: 900px) 300px, 80vw" /></div>
              <figcaption><strong>{i + 1}.</strong> {x.c}<Credit k={x.k} note={false} /></figcaption>
            </figure>
          </li>
        ))}
      </ol>
    </section>
  );
}
