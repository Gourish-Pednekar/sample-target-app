# sample-target-app

A tiny FastAPI app used as the target repository for the
[issue-crew](https://github.com/Gourish-Pednekar/issue-crew) agents.

It ships with deliberately failing tests that describe features to build
(pagination, input validation and a total-count header on `GET /users`).
The agent's job is to make them pass.

```bash
pip install fastapi httpx pytest
pytest
```

`pytest.ini` puts the project root on the import path, so plain `pytest` works.

## Baselines (git tags)

Each tag marks a starting state with failing tests. Agents start from one of these.

| Tag                   | What the tests ask for                                                                                            | Expected on a fresh checkout |
| --------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| `baseline-pagination` | `page` and `limit` query params on `GET /users`                                                                   | 3 failed                     |
| `baseline-validation` | Pagination already works; invalid `page`/`limit` must return 422 and the response needs an `X-Total-Count` header | 3 failed, 4 passed           |

Reset the app code to a baseline before a run:

```bash
git checkout baseline-validation -- app/main.py
pytest
```

## Solutions written by the crew

Each agent run is saved on its own branch so the history stays comparable:

| Branch                            | Produced by                                                                                                                    |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `run3-validation-crew-v1`         | Crew v1 (Planner/Coder/Tester)                                                                                                 |
| `run4-validation-crew-v2`         | Crew v2 (adds Reviewer and Supervisor)                                                                                         |
| `run5-validation-crew-v2-sandbox` | Crew v2 with tests run in the Docker sandbox                                                                                   |
| `crew/issue-1-1792077192`         | Crew v2 via `issue_to_pr.py` from GitHub issue #1 (PR #2, closed unmerged). Not asked for in the issue: it caps `limit` at 100 |

`main` always stays at the failing baseline.
