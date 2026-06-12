# shiny-waffle08 — Research tool for researchers

ResearchMate (working name) is a web application to help researchers discover, summarize, organize, and export academic literature quickly. This repository will host the code and documentation for the project.

## Project vision

Researchers need a fast, reliable way to move from discovery to insight: discover relevant papers, extract metadata and text from PDFs, generate concise AI summaries, keep organized collections with notes, and export citations.

## MVP (minimum viable product)

Core features to implement first:
- Metadata search across academic sources (arXiv, CrossRef, Semantic Scholar)
- PDF upload + text extraction + metadata extraction (DOI/title/author)
- AI-powered single-paper summary (short + bullet points)
- Save/bookmark papers into projects/collections
- Export citation (BibTeX/RIS)
- Basic notes/annotation per paper
- User accounts (OAuth: ORCID / GitHub / Google)

Nice-to-have (later):
- Semantic search via embeddings (vector DB)
- Collaborative collections + commenting
- Automated literature mapping and clustering
- In-browser PDF viewer with highlights

## Recommended tech stack

- Frontend: Next.js (React) — Vercel-friendly
- Backend: FastAPI (Python) — good for ML/embedding workflows
- DB: PostgreSQL (Supabase or managed Postgres)
- Vector DB (future): Pinecone / Weaviate / Supabase Vector
- Embeddings / LLMs: OpenAI (or local/alternative providers)
- Storage: S3-compatible (Supabase Storage, AWS S3)
- Worker queue: Celery / RQ for PDF ingestion and indexing
- CI/CD: GitHub Actions

## Repository structure (planned)

- /web - Next.js frontend
- /api - FastAPI backend
- /workers - background jobs (PDF processing, embeddings)
- /infra - deployment scripts, docker-compose, k8s manifests (optional)

## Getting started (placeholder)

This repository is being initialized with documentation and planning files. Once the codebase is scaffolded, this section will include steps to run locally, example env variables, and deployment notes.

## DevPost / Hackathon readiness

See DEVPOST_TEMPLATE.md for a ready-to-fill DevPost submission template and a media checklist (screenshots, demo video, live demo links).

## Contributing

- Use issues to propose features or report bugs.
- Use the project board for milestone planning.
- Follow the development roadmap in ROADMAP.md.

## Next steps (what I'll create next if you want):
1. Scaffold the Next.js frontend with a landing page and sample search UI.
2. Scaffold the FastAPI backend with auth stubs and a PDF upload endpoint.
3. Add a simple demo dataset and UI to show search + summary workflows.

If you'd like, I can scaffold the frontend and backend starters now. Which would you prefer I create first? (frontend / backend / README + plan only)
