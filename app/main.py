from fastapi import FastAPI, Query, Response

app = FastAPI()
USERS = [{"id": i, "name": f"user{i}"} for i in range(1, 26)]


@app.get("/users")
def list_users(
    response: Response,
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
):
    """Return a paginated list of users.

    Query parameters:
    - **page**: page number (1-based). Defaults to 1. Must be >= 1.
    - **limit**: number of items per page. Defaults to 10. Must be >= 1 and <= 100.
    """
    # Set total count header
    response.headers["X-Total-Count"] = str(len(USERS))

    start = (page - 1) * limit
    end = start + limit
    return USERS[start:end]
