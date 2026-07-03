# 2026-06-30 — Project start

`cairn` begins: a distributed key/value store built from scratch in Python, grown over four phases — single-node storage engine, Raft replication, production hardening, end-to-end design synthesis. Each phase has binary exit criteria; each ships a design doc and a write-up.

**Done**
- Created the project and this build log.

**Next**
- Sketch the Phase 1 storage-engine design in `docs/design/`: Bitcask-style append-only log + in-memory hash index, on-disk record format, and the crash-recovery story (what happens to a half-written record on `kill -9`).
- Ground the design in DDIA 2e Ch. 3 and the original Bitcask paper before writing code.

This log gets a dated entry every week — what shipped, what's still fuzzy, next week's single item. Declared pauses beat silent gaps.
