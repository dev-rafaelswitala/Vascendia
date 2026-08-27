# Vascendia

Plattform zum Tracken von Challenges, Sessions, Goals und Analytics — mit Clean Architecture im Backend und Feature-basiertem Frontend.

## Projektstruktur

```
Vascendia/
├── backend/
│   ├── pyproject.toml
│   ├── src/challenge_myself/
│   │   ├── domain/           # Entities, Value Objects
│   │   ├── application/      # Use Cases / Services
│   │   ├── infrastructure/   # DB, externe APIs
│   │   ├── presentation/     # HTTP (FastAPI)
│   │   ├── config/
│   │   └── main.py
│   └── tests/
├── frontend/
│   ├── src/
│   │   ├── app/              # App-Shell, Routing
│   │   ├── features/         # challenges, sessions, goals, analytics
│   │   ├── components/
│   │   ├── api/
│   │   └── types/
│   └── tests/
├── contracts/
│   └── openapi.yaml          # API-Vertrag (Single Source of Truth)
├── config/
│   ├── .env.example
│   └── docker/
├── scripts/
└── docker-compose.yml
```

## Erste Schritte

### 1. Setup

```powershell
# Alles installieren (Frontend + Backend venv)
npm run setup
```

Oder manuell:

```powershell
cd frontend && npm install
cd ..\backend
python -m venv .venv
.\.venv\Scripts\pip install -e ".[dev]"
```

### 2. Umgebungsvariablen

```powershell
copy config\.env.example .env
copy config\.env.example frontend\.env
```

### 3. Entwicklung starten

Zwei Terminals:

```powershell
# Terminal 1 — Backend (Port 8000)
npm run dev:backend

# Terminal 2 — Frontend (Port 5173)
npm run dev:frontend
```

Oder mit dem Dev-Script (startet Backend in neuem Fenster):

```powershell
npm run dev
```

- Frontend: [http://localhost:5173](http://localhost:5173)
- Backend API: [http://localhost:8000/api/v1/health](http://localhost:8000/api/v1/health)
- OpenAPI Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

## VS Code

Öffne `vascendia.code-workspace` — du siehst Frontend, Backend und Contracts als separate Ordner.

## Docker (Production)

```powershell
docker compose up --build
```

- Frontend: [http://localhost:8080](http://localhost:8080)
- Backend: [http://localhost:8000](http://localhost:8000)

## Tests

```powershell
# Frontend
npm run test

# Backend
npm run test:backend
```

## CI/CD (GitHub Actions)

Bei Push/PR auf `main` oder `develop`:

| Job | Prüfungen |
|-----|-----------|
| **frontend** | typecheck, lint, test, build |
| **backend** | ruff, pytest |
| **docker** (main) | Backend- + Frontend-Image bauen |

## API-Vertrag

Der Vertrag liegt in `contracts/openapi.yaml`. Backend-Routen und Frontend-Typen sollten daran ausgerichtet werden.

## Architektur-Hinweise

**Backend (Clean Architecture):**
- `domain/` — reine Geschäftslogik, keine Framework-Abhängigkeiten
- `application/` — Use Cases orchestrieren Domain
- `infrastructure/` — Persistenz, externe Dienste
- `presentation/http/` — FastAPI Routes, Schemas, Middleware

**Frontend (Feature-Slices):**
- `features/challenges`, `sessions`, `goals`, `analytics` — je Feature eigene UI + Logik
- `api/` — HTTP-Client zum Backend
- `types/` — TypeScript-Typen (an OpenAPI angelehnt)

## Lizenz

MIT — siehe [LICENSE](./LICENSE).
