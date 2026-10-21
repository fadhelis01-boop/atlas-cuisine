import { Component, type ReactNode } from "react";
import { logError } from "../lib/errlog";

/** Une erreur dans une page ne doit pas effacer toute l'application : message clair, retour à l'accueil, rechargement. */
export default class ErrorBoundary extends Component<{ children: ReactNode; resetKey: string }, { error: Error | null }> {
  state = { error: null as Error | null };
  static getDerivedStateFromError(error: Error) { return { error }; }
  componentDidUpdate(prev: { resetKey: string }) { if (prev.resetKey !== this.props.resetKey && this.state.error) this.setState({ error: null }); }
  componentDidCatch(error: Error) { console.error("ATLAS :", error); logError(location.hash || "/", error); }
  render() {
    if (!this.state.error) return this.props.children;
    return (
      <main className="page" id="contenu" tabIndex={-1}>
        <h1>Oups, cette page a un souci</h1>
        <p>Le reste d'ATLAS fonctionne. Tu peux revenir en arrière, aller à l'accueil ou recharger.</p>
        <div className="row">
          <button className="btn" onClick={() => history.back()}>← Retour</button>
          <a className="btn ghost" href="#/">Accueil</a>
          <button className="btn ghost" onClick={() => location.reload()}>Recharger</button>
        </div>
        <details className="small"><summary>Détail technique</summary><pre>{String(this.state.error.message)}</pre></details>
      </main>
    );
  }
}
