# Copilot instructions

## Commands

Run these commands from `viikko4/tdd-ostoskori`:

```bash
# Run all tests
uv run pytest src/tests

# Run one test method
uv run pytest src/tests/ostoskori_test.py -k test_ostoskorin_hinta_ja_tavaroiden_maara_alussa
```

The project targets Python 3.14 (`.python-version`) and uses `uv` with the locked
development dependency set in `uv.lock`. Pytest is the only configured
development tool; no lint command is defined in `pyproject.toml`.

## Architecture

This is a small shopping-cart domain model implemented as flat modules under
`src/`:

- `tuote.py` defines `Tuote`, a product with a name and unit price.
- `ostos.py` defines `Ostos`, a product line item. It owns the quantity,
  prevents quantity from becoming negative, and calculates line-item price.
- `ostoskori.py` defines `Ostoskori`, the cart aggregate. Its public operations
  manage products and expose item count, total price, and cart contents.
- `src/tests/ostoskori_test.py` contains the cart behavior tests. Tests use
  `unittest.TestCase` but are executed by pytest.

The application entry point is not implemented; changes should focus on the
domain classes and their tests.

## Repository conventions

- Keep the domain vocabulary and public method names in Finnish (`Tuote`,
  `Ostos`, `Ostoskori`, `hinta`, `lukumaara`, etc.).
- Modules are imported directly by name (for example, `from tuote import
  Tuote`), so preserve the current flat-module layout and run tests from the
  project root.
- Product prices and quantities are represented as integers. `Ostos.hinta()`
  derives its result from the current quantity and product price rather than
  storing a separate line total.
- Add behavior tests alongside the existing test module and preserve its
  `unittest` style unless there is a concrete reason to change it.
- Tests executed with uv run pytest
- Code of ostos.py and tuote.py should not be changed
- Tests should not be edited unless explicitly asked
- Always implement absolutely minimal code that makes the tests pass
