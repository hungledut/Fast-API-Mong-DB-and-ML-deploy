# HungLV_FastAP

## Installation ⚡️
### Requires
- Python 3.9

Install with poetry:
~~~
pip install poetry
poetry install
~~~

Create `.env` file as `.venv`

**WARNING**: 
- When run application in local: `MONGO_DETAILS=mongodb://localhost:27017`
- When run application with docker-compose (not yet public port): `MONGO_DETAILS=mongodb://mongodb:27017`

## Deployment app ⛄️
Run FastAPI:
~~~
uvicorn app.main:app --reload
~~~

## Tree directory 🌗 
~~~
app                                    
├─ config                              
│  └─ database.py                      
├─ logger                              
│  ├─ logger.log                       
│  └─ logger.py                        
├─ models                              
│  └─ user_model.py                    
├─ routes                              
│  ├─ login_routes.py                  
│  └─ users_routes.py                  
├─ schemas                             
│  └─ user_schema.py                   
├─ main.py                             
├─ security.py                         
└─ __init__.py           
~~~
              
