# analystic-starter

Python + Pydantic + Pandas + DuckDB, managed with [uv](https://docs.astral.sh/uv/).

## Run

```bash
uv run main.py
```

## Use

- Dependencies live in `pyproject.toml`. Add more with `uv add <package>`.
- `uv run <script.py>` automatically uses the project's `.venv` — no manual activation needed.
- Delete `.venv` anytime; `uv run` recreates it from `uv.lock`.
