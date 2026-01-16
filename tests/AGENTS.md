# AGENTS.md - tests/

## OVERVIEW
Pure `pytest` suite for unit and integration testing. Prioritizes isolation and explicit data setup over shared state.

## CONVENTIONS
- **No Fixtures**: Do not use `conftest.py` or `@pytest.fixture`. Instantiate `Track` objects and data inline within test methods.
- **Class-Based**: Group related tests in classes (e.g., `TestBpmCompatible`).
- **Explicit Assertions**: Use `with pytest.raises(Error, match="...")` for precise error validation.

## ANTI-PATTERNS
- ❌ **Shared State**: No global variables or module-level setup.
- ❌ **Mocking Internal Logic**: Prefer testing against real `Track` and `Optimizer` objects where possible.
- ❌ **DB Dependency**: Do not run tests that require a live Rekordbox database connection (mock the loader if necessary).
