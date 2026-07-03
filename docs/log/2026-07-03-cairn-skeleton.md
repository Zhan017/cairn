# 2026-07-03 — Own repo + Python walking skeleton

Moved the flagship into its own public repo (`cairn`, split out of my private roadmap repo) and gave it a spine to grow on.

**Done**
- Chose the name **cairn** — a stack of stones marking a trail; a fitting image for a log-structured store you can retrace after a crash.
- Stood up the Python package skeleton: `cairn/store.py` with an `InMemoryStore` (get/put/delete over `bytes`), a table-driven test suite, `pyproject.toml`, and MIT `LICENSE`.
- Wired up CI (GitHub Actions: `ruff` + `pytest` on Python 3.11+) so the repo is green from commit one — not 100% docs.

**Why a throwaway in-memory store?**
It's the walking skeleton: a correct, tested interface to build CI and the package layout around. Phase 1 replaces it with the real Bitcask-style engine (append-only log + hash index + crash recovery) behind the same `get/put/delete` interface — and the tests here become the invariants that engine must also satisfy.

**Next**
- Sketch the Phase 1 on-disk format + recovery design in `docs/design/` (use the template), grounded in DDIA Ch. 3 and the Bitcask paper.
