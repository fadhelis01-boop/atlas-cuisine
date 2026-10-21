import { toast } from "./toast";

/** Envoie un lien : feuille de partage du téléphone, sinon copie dans le presse-papiers. */
export async function sendLink(title: string, text: string, url: string) {
  try {
    if (navigator.share) await navigator.share({ title, text, url });
    else { await navigator.clipboard.writeText(`${text}\n${url}`); toast("Lien copié : colle-le dans un message"); }
  } catch { /* partage annulé */ }
}
/** Télécharge un fichier texte (agenda, carnet…). */
export function downloadText(name: string, text: string, type: string) {
  const url = URL.createObjectURL(new Blob([text], { type }));
  const a = document.createElement("a"); a.href = url; a.download = name; a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}
