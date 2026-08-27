# Vascendia

Monorepo für die Vascendia-Webanwendung mit React, TypeScript, Vite, Docker und GitHub Actions.

## Projektstruktur

```
Vascendia/
├── apps/
│   └── web/                 # React + TypeScript + Vite (Hauptanwendung)
├── packages/
│   ├── ui/                  # Wiederverwendbare UI-Komponenten
│   ├── config/              # Gemeinsame TypeScript-Konfiguration
│   └── types/               # Gemeinsame TypeScript-Typen
├── docker/
│   └── web/                 # Production-Docker-Image (Node → Nginx)
├── .github/
│   └── workflows/           # CI/CD-Pipelines
├── docker-compose.yml
├── vascendia.code-workspace # VS Code Multi-Root-Workspace
└── package.json             # npm Workspaces (Root)
```

## Voraussetzungen

- Node.js >= 20
- npm >= 10
- Docker (optional, für Production-Builds)
- Visual Studio Code (empfohlen)

## Erste Schritte

```bash
# Abhängigkeiten installieren
npm install

# Entwicklungsserver starten
npm run dev
```

Die App läuft dann unter [http://localhost:5173](http://localhost:5173).

## Wichtige Befehle

| Befehl | Beschreibung |
|--------|--------------|
| `npm run dev` | Vite-Dev-Server starten |
| `npm run build` | Production-Build aller Workspaces |
| `npm run typecheck` | TypeScript prüfen |
| `npm run lint` | Linting (oxlint) |
| `npm run test` | Tests ausführen |
| `npm run preview` | Production-Build lokal previewen |

Einzelne Workspace-Befehle:

```bash
npm run dev -w web
npm run build -w web
```

## VS Code

Öffne das Projekt am besten über die Workspace-Datei:

```
vascendia.code-workspace
```

Damit siehst du Root, Web-App und Shared Packages als separate Ordner in der Seitenleiste.

Empfohlene Extensions werden automatisch vorgeschlagen (Oxc, Prettier).

## Docker (Production)

Für Development nutze `npm run dev` direkt auf dem Host — das ist schneller als Docker.

Docker ist für reproduzierbare Production-Builds gedacht:

```bash
# Image bauen
docker build -f docker/web/Dockerfile -t vascendia-web .

# Oder mit docker compose
docker compose up --build
```

Die App ist dann unter [http://localhost:8080](http://localhost:8080) erreichbar.

## GitHub CI/CD

Beim Push oder Pull Request auf `main` / `develop` läuft automatisch:

1. `npm ci` — saubere Installation
2. TypeScript-Prüfung
3. Linting
4. Tests
5. Build

Auf `main` wird zusätzlich ein Docker-Image gebaut (ohne Push in eine Registry — das kann später ergänzt werden).

### Ersten Push machen

Das Repository ist bereits mit GitHub verbunden:

```bash
git add .
git commit -m "chore: initialize monorepo with React, Docker and CI"
git push origin main
```

Danach siehst du unter **GitHub → Actions** die laufenden Pipelines.

## Git Flow (optional)

Für strukturierte Branch-Entwicklung:

```bash
git flow init
```

Typische Einstellungen:

- Production: `main`
- Development: `develop`
- Features: `feature/`
- Releases: `release/`
- Hotfixes: `hotfix/`

Beispiel:

```bash
git flow feature start login
# ... arbeiten ...
git flow feature finish login
```

## Shared Packages nutzen

In `apps/web` sind bereits angebunden:

```typescript
import type { AppName } from '@vascendia/types'
import { Button } from '@vascendia/ui'
```

Neue Komponenten gehören in `packages/ui`, gemeinsame Typen in `packages/types`.

## Lizenz

MIT — siehe [LICENSE](./LICENSE).
