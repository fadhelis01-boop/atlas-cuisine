import { dismiss, useToasts } from "../lib/toast";
import { href } from "../lib/router";

export default function Toasts() {
  const list = useToasts();
  if (!list.length) return null;
  return (
    <div className="toasts" role="status" aria-live="polite">
      {list.map((t) => (
        <div key={t.id} className="toast">
          <span>{t.text}</span>
          {t.link && <a href={href(t.link.to)} onClick={() => dismiss(t.id)}>{t.link.label}</a>}
          {t.undo && <button type="button" onClick={() => { t.undo!(); dismiss(t.id); }}>Annuler</button>}
        </div>
      ))}
    </div>
  );
}
