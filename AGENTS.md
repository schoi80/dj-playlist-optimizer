# DJ PLAYLIST OPTIMIZER - PROJECT KNOWLEDGE BASE

**Generated:** 2026-01-16
**Commit:** c523fa1
**Branch:** main

## OVERVIEW
Python library + CLI for optimizing DJ playlists using Google OR-Tools CP-SAT solver. Features harmonic mixing (Camelot Wheel), BPM matching (direct/halftime/doubletime), and Rekordbox integration (DB/XML).

## STRUCTURE
```
.
├── src/dj_playlist_optimizer/   # Core logic (solver, models, integrations)
├── tests/                       # Unit + integration tests (pure pytest, no fixtures)
├── examples/                    # Usage demos (SDK + logging)
└── pyproject.toml               # uv-managed dependencies + tool config
```

## WHERE TO LOOK
| Task | Location | Notes |
|------|----------|-------|
| **Core Solver** | `src/dj_playlist_optimizer/optimizer.py` | Uses `AddCircuit` constraint for TSP-like pathfinding |
| **Data Models** | `src/dj_playlist_optimizer/models.py` | `Track`, `PlaylistResult`, `HarmonicLevel` |
| **BPM Logic** | `src/dj_playlist_optimizer/bpm.py` | Pure functions for BPM compatibility |
| **Harmonic Rules** | `src/dj_playlist_optimizer/camelot.py` | Camelot Wheel math + `KEY_MAPPING` |
| **Rekordbox** | `src/dj_playlist_optimizer/rekordbox.py` | Direct DB read/write + XML export |
| **CLI** | `src/dj_playlist_optimizer/cli.py` | `argparse` entry point + logging setup |

## CODE MAP
| Symbol | Type | Location | Role |
|--------|------|----------|------|
| `PlaylistOptimizer` | Class | `optimizer.py` | Main facade for configuring and running the solver |
| `Track` | Class | `models.py` | Data carrier for ID, Key, BPM, Energy, Duration |
| `HarmonicLevel` | Enum | `models.py` | STRICT, MODERATE, RELAXED compatibility modes |
| `RekordboxLoader` | Class | `rekordbox.py` | Interface for reading playlists from `master.db` |
| `write_rekordbox_xml` | Func | `rekordbox.py` | Generates XML for re-importing optimized lists |

## CONVENTIONS
- **Layout**: `src/` layout with `uv` package manager.
- **Line Length**: **100 chars** (enforced by ruff).
- **Quotes**: Double quotes always.
- **Commits**: Conventional Commits (feat, fix, docs, etc.) enforced by pre-commit.
- **Tests**: Pure `pytest` class-based structure. **NO fixtures**, **NO conftest.py**. Data instantiated inline.

## ANTI-PATTERNS (THIS PROJECT)
- ❌ **Print**: Forbidden in library code (`src/`). Use `logging`. Allowed ONLY in `cli.py`.
- ❌ **Suppression**: No `# type: ignore` or `# noqa`.
- ❌ **Mutable State**: Do not modify `PlaylistStatistics` fields after init.
- ❌ **Direct DB Write**: Avoid writing to Rekordbox DB while the app is open (corruption risk).

## UNIQUE STYLES
- **Solver**: Uses a "dummy node" pattern in `AddCircuit` to find longest paths (TSP variant).
- **Soft Constraints**: "Must Include" logic implemented via massive objective weights (100,000).
- **Versioning**: Hybrid approach. `pyproject.toml` (1.0.0) vs `cli.py` fallback (0.0.0).

## COMMANDS
```bash
# Dev Cycle
uv sync --dev
uv run pytest
uv run ruff check --fix && uv run ruff format
uv run pre-commit run --all-files

# CLI Usage
uv run dj-optimize tracks.json --harmonic-level moderate
uv run dj-optimize --rekordbox --playlist "Techno" --output result.xml
uv run dj-optimize --rekordbox --playlist "Techno" --write-to-db
```

## NOTES
- **Camelot Math**: `1A` and `12A` are adjacent. Code handles circular distance.
- **Halftime BPM**: `128` matches `64`. Asymmetric relationship supported.
- **DB Write Risk**: Direct write requires Rekordbox to be closed to avoid SQLite lock errors.
- **Missing**: No `docs/` dir (README only). No remote CI (local pre-commit only).
