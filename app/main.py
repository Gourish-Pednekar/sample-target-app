from fastapi import FastAPI

app = FastAPI()
USERS = [{"id": i, "name": f"user{i}"} for i in range(1, 26)]


@app.get("/users")
def list_users():
    return USERS