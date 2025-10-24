# apiprofile

A small Django REST API that returns a simple user profile and a (random) cat fact.

This project contains a single app, `apiprof`, which exposes one endpoint that returns
the project's owner information together with a timestamp and a cat fact fetched from an external API.

## What it does
- Endpoint: `GET /me/`
- Response: JSON with keys `status`, `user`, `timestamp`, and `fact`.

Example response:

```
{
  "status": "success",
  "user": {
    "email": "you@example.com",
    "name": "Your Name",
    "stack": "Your Stack"
  },
  "timestamp": "2025-10-24T12:34:56.789Z",
  "fact": "A short cat fact pulled from an external API."
}
```

## Requirements
- Python 3.8+ (project was created with Django 5.x)
- The project's Python dependencies are listed in `requirements.txt`.

## Quick start (Windows PowerShell)

Open PowerShell and run the following from the project root (`apiprofile`):

```powershell
# create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# install dependencies
pip install -r requirements.txt

# apply migrations (uses the bundled sqlite3 DB by default)
python manage.py migrate

# run the development server
python manage.py runserver

# then open or curl http://127.0.0.1:8000/me/
```

## Configuration

The project reads a `.env` file (via python-dotenv) for a few simple profile settings.
If not provided, sensible defaults are used.

Environment variables used:
- `MY_EMAIL` — email shown in the profile (default: `default@example.com`)
- `MY_NAME` — name shown in the profile (default: `Default Name`)
- `MY_STACK` — tech stack string (default: `Default Stack`)
- `CAT_FACTS_API_URL` — URL of the external cat-fact service (defaults to `https://catfact.ninja/fact`)

Tip: create a `.env` file in the project root with values like:

```
MY_EMAIL=you@example.com
MY_NAME=Your Name
MY_STACK=Python, Django
CAT_FACTS_API_URL=https://catfact.ninja/fact
```

## Notes
- The `apiprof` app's `ProfileView` always returns HTTP 200 with a `status: "success"` body. If the external cat fact fetch fails, a fallback message is returned in the `fact` field.
- Database: `db.sqlite3` is included and used by default for local development.
- There are no models defined in `apiprof/models.py` in this project — the app is focused on presenting the profile endpoint.

## Next steps / suggestions
- Add documentation or an OpenAPI schema for the endpoint.
- Add tests for the view (mock the external cat fact API).
- Add CI to run linting and tests.

---
Created automatically by a helper script. If anything in this README is inaccurate, open `apiprof/views.py` and `apiprofile/urls.py` to inspect route and response structure.
