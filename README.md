# cairn — building a distributed key/value store from scratch

[![CI](https://github.com/Zhan017/cairn/actions/workflows/ci.yml/badge.svg)](https://github.com/Zhan017/cairn/actions/workflows/ci.yml)

> Building a replicated, fault-tolerant key/value store from the storage engine up — in Python, in the open — to develop first-principles depth in distributed systems and backend engineering.

**Status:** 🟡 Phase 0 — walking skeleton · Started June 2026 · Language: Python

> *A cairn is a stack of stones that marks a trail — durable markers you can retrace your way back through. Fitting for a log-structured store with a crash-recovery story.*

## Why this exists

I'm deliberately building the layer beneath the systems I use every day. `cairn` grows in four phases — a single-node storage engine, a from-scratch Raft implementation, production hardening, and a documented end-to-end design — each one closing the gap between "it works" and "I know exactly *why* it works." Notes, design docs, and write-ups live in [`/docs`](./docs).

Everything is implemented **once, here, in Python**. I use MIT 6.5840 as curriculum (lectures, the Raft paper, lab specs as a design reference), not as Go labs to submit — my own test harness is the grader.

**Why Python for a storage engine?** Because the goal is first-principles understanding of the algorithms and failure modes, and Python (my strongest language) maximizes iteration speed toward that goal. Performance claims will be scoped honestly as "defensible for Python," with absolute numbers published rather than hidden — owning the trade-off is part of the exercise.

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
```

```python
from cairn.store import InMemoryStore

store = InMemoryStore()
store.put(b"hello", b"world")
store.get(b"hello")  # b"world"
```

The `InMemoryStore` is the walking skeleton. Phase 1 replaces it with an append-only log + hash index (Bitcask-style) and a real crash-recovery story — behind a stable interface.

## Roadmap

The project doubles as my learning roadmap. Each phase ships something real, verified by binary exit criteria (not just a checkbox).

**Phase 1 — Storage engine**
- Bitcask-style engine: append-only log + in-memory hash index + segment compaction + working crash recovery
- Design doc: on-disk format & recovery
- *Exit:* a `kill -9` mid-write test recovers 100% of acknowledged writes, 20/20 runs
- *Stretch (year 2):* an LSM-tree (memtable + SSTables + compaction)

**Phase 2 — Distributed core**
- Raft in Python: leader election, log replication, persistence, snapshots
- Linearizable KV layer on top of Raft
- Own test harness: partition injection, kill/restart, unreliable-network simulation
- Design doc: replication & consensus
- *Exit:* Raft passes the harness 50 consecutive runs; a scripted demo survives a leader kill + healed partition with no lost acked write
- *Stretch (year 2):* sharding for horizontal scale

**Phase 3 — Production hardening**
- Metrics (Prometheus), structured logs, distributed tracing (OpenTelemetry)
- SLOs + load tests + fault injection
- Performance pass (p50 / p95 / p99) with `py-spy` / `cProfile`
- Runbook + reliability doc
- *Exit:* a dashboard that visibly tells the story of a killed node; a load test with a defensible p99

**Phase 4 — Synthesis**
- End-to-end system design doc
- Benchmarks I can defend
- Public write-up series + announce

## Structure (grows over time)

```
cairn/
├── cairn/          # the package: storage engine, raft, kv service
│   ├── __init__.py
│   └── store.py    # Phase 0 seed → Phase 1 Bitcask engine
├── tests/          # unit tests + (Phase 2) the fault-injection harness
├── docs/
│   ├── design/     # design docs, one per phase
│   └── log/        # dated build-log entries / posts
├── .github/workflows/ci.yml
├── pyproject.toml
├── LICENSE
└── README.md
```

## Build log

- **2026-07-03** — Split into its own repo; Python walking skeleton + CI. See [`docs/log`](./docs/log).
- **2026-06-30** — Project started. Phase 0 setup underway.

## License

MIT — see [LICENSE](./LICENSE).
