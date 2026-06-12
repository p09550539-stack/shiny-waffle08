# Roadmap

This is an example 4-week roadmap for building the MVP. Adjust timelines to your availability or hackathon duration.

Week 0 — Planning & repo setup
- Finalize project name and tech choices
- Create GitHub repo files (README, LICENSE, issue templates)
- Create project board and issues for first milestones

Week 1 — Core infra & frontend scaffold
- Initialize Next.js app (basic pages: Home, Projects, Paper Detail)
- Initialize FastAPI backend with basic auth stub
- Provision Postgres (local docker or Supabase)
- Add CI skeleton (GitHub Actions)

Week 2 — Ingestion & search
- Implement PDF upload endpoint and worker to extract text
- Implement metadata extraction (CrossRef / DOI lookup)
- Basic metadata search API (title/author/abstract)
- Paper detail view showing extracted metadata

Week 3 — AI summaries & exports
- Integrate LLM API for single-paper summarization
- Add BibTeX/RIS export for saved papers
- UI for saving/bookmarking papers into collections

Week 4 — Polish & deploy
- Deploy frontend (Vercel) and backend (Render / Fly / Cloud Run)
- Create demo data and demo account
- Record 60-90s demo video and screenshots for DevPost
- Final bugfixes and UX polish

Future milestones
- Add vector embeddings & semantic search
- Add collaboration features (shared collections)
- Improve PDF viewer with highlights and annotations
