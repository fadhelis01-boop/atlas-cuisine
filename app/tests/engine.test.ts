// Tests du moteur et des règles métier (équivalents TypeScript de bible/test_engine.py + contrôles sur les fiches réelles).
// Lancement : npm test. Les suites sont des modules séparés (audit dév/UX 2026-10-21 §4), exécutés dans l'ordre.
import { passedCount } from "./helpers";
import "./e1-moteur-frigo-imports";
import "./e2-contenu-techniques";
import "./e3-variete-famille";
import "./e4-audit-gourmet";
import "./e5-audit-dev-ux";
import "./e6-variete-idees";
import "./e7-favoris-tiktok";

console.log(`\n${passedCount()} contrôles OK`);
