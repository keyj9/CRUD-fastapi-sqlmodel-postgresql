Simple example with FastAPI + sqlmodel + postgresql
Plans: complete, minimalistic template based on external services.
Focused on performance, less own code and infrastructure.

Features
Docker with postgres
Poetry as dependency manager
Works well async (all, with db)
Supported snake_case -> cammelCase conversion
Env file parsed by Pydantic
Structure with Dependency Injection (database implementation)
Build on Python: 3.9.

Installation and usage
Create env from template: cp example.env .env (only once)
RUN:
docker network create db55
docker run -d --name db54 -p 5432:5432 --network=db55 -e POSTGRES_PASSWORD=password postgres -d postgres:alpine
docker run -it --rm --network=55 postgres:alpine psql -h db54 -U postgres

TODO
Example is completely and works very well. In the future probably I add more.

Branche for MongoDB
More examples with custom response models
[Maybe] File handling with external provider (Amazon S3, DO Spaces)
[Maybe] Authorization by external provider (Auth0)