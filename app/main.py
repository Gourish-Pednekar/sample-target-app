from fastapi import FastAPI, Query

app = FastAPI()
USERS = [{"id": i, "name": f"user{i}"} for i in range(1, 26)]


@app.get("/users")
def list_users(page: int = Query(1, ge=1), limit: int = Query(10, ge=1)):
    """Return a paginated list of users.

    Args:
        page: The page number (1-indexed). Defaults to 1.
        limit: Number of users per page. Defaults to 10.
    """
    start = (page - 1) * limit
    end = start + limit
    return USERS[start:end]
