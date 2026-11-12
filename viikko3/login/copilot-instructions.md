# Copilot instructions for `viikko3/login`

## Project scope

The application described here is the Flask project in `viikko3/login`. Run
the commands below from that directory.

## Build, run, and test commands

This project uses `uv` and requires Python 3.14 or newer (`pyproject.toml`
declares `requires-python = ">=3.14"`).

```bash
# Create/update the environment from the lock file
uv sync

# Start the Flask application on http://localhost:5001
uv run python src/index.py

# Run all tests
uv run robot src/tests

```

There is no configured Python unit-test suite in `src/tests` and no separate
lint command in `pyproject.toml`. The browser tests use Robot Framework,
`robotframework-browser`, and the Browser Batteries package. A running
application is required for the browser tests; the test support includes
`POST /tests/reset` to clear the in-memory users between scenarios.

## Architecture and request flow

- `src/index.py` is the development entry point. It imports the Flask `app`
  from `src/app.py` and starts it on all interfaces at port 5001.
- `src/app.py` owns HTTP routes, form extraction, redirects, flashed error
  messages, and the application-wide `user_service` and `user_repository`
  instances. GET routes render templates; POST routes delegate validation and
  persistence to the service and redirect on success or failure.
- `src/services/user_service.py` contains the domain rules for registration
  and authentication. `UserService` depends on a repository instance, which
  makes the service usable with a substitute repository in isolated tests.
  `UserInputError` represents invalid registration/login input and
  `AuthenticationError` represents failed credentials.
- `src/repositories/user_repository.py` is an in-memory repository. The module
  level `user_repository` is shared by the Flask app, so users disappear when
  the process restarts. The reset route calls `delete_all()` for browser-test
  isolation.
- `src/entities/user.py` is the plain `User` data object. Passwords are
  currently stored as provided; preserve this behavior unless a task
  explicitly changes the authentication model.
- `src/templates/` contains the Jinja templates. `layout.html` supplies the
  common document shell; page templates extend it and display flashed
  messages on the login and registration forms.
- `browser/` contains the end-to-end Robot Framework suites and shared
  resources. `src/AppLibrary.py` provides Robot-facing HTTP helpers such as
  resetting state and creating users.

## Repository-specific conventions

- Keep application imports relative to the `src` runtime layout: commands are
  run from `viikko3/login`, with `src` on the import path when starting
  `src/index.py`.
- Keep route handlers thin. Put registration and credential rules in
  `UserService`, and put user collection operations in `UserRepository`.
- Use the existing singleton wiring (`user_repository` and `user_service`) for
  the running application. Inject a repository through `UserService(...)` when
  testing service behavior.
- User-facing failures are surfaced by raising a service exception, catching
  it at the route boundary, flashing `str(error)`, and redirecting back to the
  relevant form. Preserve the established error messages when changing
  validation.
- Registration currently requires a non-empty username and password, a
  username of at least three characters, a password of at least eight
  characters, and a unique username. Keep duplicate checks in the service and
  repository consistent.
- Successful registration redirects to `/welcome`; successful login redirects
  to `/ohtu`; logout is a POST and redirects to `/login`.
- Browser-test state is deliberately process-local. Use `/tests/reset` in test
  setup rather than relying on test order or a persistent database.
