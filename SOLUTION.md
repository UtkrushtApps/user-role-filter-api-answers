# Solution Steps

1. Set up the FastAPI project structure with an 'app' directory containing module files: main.py, models.py, schemas.py, and database.py.

2. Define the SQLAlchemy async engine and session in app/database.py, connecting to the PostgreSQL database using env variables for Docker compatibility.

3. In app/models.py, define the User model with id, username, role, and status fields, mapped to the users table.

4. In app/schemas.py, define a Pydantic model UserOut matching User for API responses, with orm_mode enabled.

5. In app/main.py, initialize FastAPI and implement the /users GET endpoint.

6. For /users, accept optional 'role' and 'status' query parameters. Use Query for description and parameter parsing.

7. Build a SQLAlchemy async SELECT query that applies both role and status filters (if provided), combining them with .where() so they are ANDed together.

8. Use SQLAlchemy’s async session as a dependency to execute the query and fetch all User objects matching the filters.

9. Return the list of users as Pydantic models using response_model=List[UserOut] for FastAPI automatic validation and serialization.

10. Create requirements.txt with all necessary dependencies (FastAPI, uvicorn, asyncpg, SQLAlchemy[asyncio], pydantic).

11. Write a Dockerfile to containerize the FastAPI application.

12. Write a docker-compose.yml to orchestrate both the FastAPI app and the PostgreSQL database for local development/testing.

13. With this setup, the /users endpoint will accurately filter users by both role and status, using proper SQLAlchemy query composition and PostgreSQL async integration.

