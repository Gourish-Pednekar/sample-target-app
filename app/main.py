from fastapi import FastAPI, HTTPException, Response

app = FastAPI()
USERS = [{"id": i, "name": f"user{i}"} for i in range(1, 26)]


@app.get("/users")
def list_users(page: int = 1, limit: int = 10, response: Response = None):
    """Return a paginated list of users.

    Query parameters:
    - **page**: page number (1-based). Defaults to 1. Values less than 1 are rejected with 422.
    - **limit**: number of items per page. Defaults to 10. Must be between 1 and 100 inclusive.
    """
    # Validate pagination parameters
    if page < 1:
        raise HTTPException(status_code=422, detail="Invalid page value")
    if limit < 1 or limit > 100:
        raise HTTPException(status_code=422, detail="Invalid limit value")

    # Set total count header
    response.headers["X-Total-Count"] = str(len(USERS))

    start = (page - 1) * limit
    end = start + limit
    return USERS[start:end]
