# Simple example with FastAPI + sqlmodel + postgresql 

>*Plans: complete, minimalistic template based on external services.     
Focused on performance, less own code and infrastructure.*

## Features 

- Docker with [Postgresql](https://www.postgresql.org) and [FastAPI](http://fastapi.tiangolo.com)  
- [Poetry](https://python-poetry.org) as dependency manager    
- Works well **async** (all, with db)  
- Supported snake_case -> cammelCase conversion 
- Env file parsed by Pydantic    
- **sqlmodel** works well with **FastAPI** & **Pydantic** 
- Structure with **Dependency Injection** (database implementation)    

Build on **Python: 3.9**.    


## Installation and usage 

Create env from template: ```cp example.env .env``` (only once)    
Run: 
<li> poetry install </li>
<li> docker network create db55</li>
<li> docker run -d --name db54 -p 5432:5432 --network=db55 -e POSTGRES_PASSWORD=password postgres -d postgres </li>
<li> docker run -it --rm --network=db55 postgres psql -h db54 -U postgres </li>  
<li> create database sqlmodeldb;</li>
<li> \q</li>
<li> python3 create_database.py</li>
<li>uvicorn main:app --reload</li>
</ul><br />
## TODO 

> Example is complete

- Branche for MongoDB
- More examples with custom response models 
- [Maybe] File handling with external provider (Amazon S3, DO Spaces)    
- [Maybe] Authorization by external provider (Auth0)    

Plans: complete, minimalistic template based on external services.
Focused on performance, less own code and infrastructure.

