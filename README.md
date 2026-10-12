# sample-target-app

A tiny FastAPI app used as the target repository for the
[issue-crew](https://github.com/<Gourish-Pednekar>/issue-crew) agents.

It ships with deliberately failing tests that describe a feature
(pagination on `GET /users`). The agent's job is to make them pass.

```bash
pip install fastapi httpx pytest
pytest
```

The git tag `baseline-pagination` marks the starting state (failing tests).
