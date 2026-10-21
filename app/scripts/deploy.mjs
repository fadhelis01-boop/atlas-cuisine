// Publie la version compilée (dist/) sur la branche gh-pages du dépôt GitHub.
// Usage : npm run deploy   (construit puis publie)
//
// Publication incrémentale (audit dév/UX 2026-10-21 §2.6) : on garde une copie de gh-pages AVEC son historique dans
// .deploy/ (ignoré par Git). Seuls les fichiers modifiés partent ; avant, une branche neuve poussée en force renvoyait
// toutes les photos à chaque publication. Premier lancement : une copie complète de gh-pages est téléchargée une fois.
import { execSync } from "node:child_process";
import { cpSync, existsSync, readdirSync, rmSync, writeFileSync } from "node:fs";

const run = (cmd, cwd = ".") => execSync(cmd, { cwd, stdio: "inherit" });
const out = (cmd, cwd = ".") => execSync(cmd, { cwd }).toString().trim();
let remote = out("git remote get-url origin");
// dans l'automatisation GitHub (ajout de recettes) : on publie avec le jeton fourni par GitHub Actions
if (process.env.GITHUB_TOKEN) remote = remote.replace("https://", `https://x-access-token:${process.env.GITHUB_TOKEN}@`);
const DIR = ".deploy";

if (!existsSync("dist/index.html")) { console.error("dist/ est vide : lance d'abord « npm run build »."); process.exit(1); }
writeFileSync("dist/.nojekyll", ""); // GitHub Pages sert tel quel

const hasBranch = out(`git ls-remote --heads ${remote} gh-pages`).length > 0;
if (existsSync(`${DIR}/.git`)) {
  run(`git fetch --depth 1 ${remote} gh-pages`, DIR);
  run("git reset -q --hard FETCH_HEAD", DIR);
} else {
  rmSync(DIR, { recursive: true, force: true });
  if (hasBranch) run(`git clone -q --depth 1 --single-branch --branch gh-pages ${remote} ${DIR}`);
  else { run(`git init -q -b gh-pages ${DIR}`); }
}

// le contenu publié devient exactement dist/ : on retire tout sauf .git, puis on recopie
for (const n of readdirSync(DIR)) if (n !== ".git") rmSync(`${DIR}/${n}`, { recursive: true, force: true });
cpSync("dist", DIR, { recursive: true });

run("git add -A", DIR);
if (!out("git status --porcelain", DIR)) { console.log("Rien de neuf à publier."); process.exit(0); }
const who = (k) => { try { return out(`git config ${k}`); } catch { return k === "user.name" ? "atlas-bot" : "atlas-bot@users.noreply.github.com"; } };
run(`git -c user.name="${who("user.name")}" -c user.email="${who("user.email")}" commit -q -m "Publication ${new Date().toISOString()}"`, DIR);
console.log(`Envoi : ${out("git diff --stat HEAD~1 --shortstat", DIR) || "première publication"}`);
run(`git push -q ${remote} HEAD:gh-pages`, DIR);
console.log("Publié sur la branche gh-pages.");
