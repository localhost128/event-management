# Event Management

To run project
```
git clone https://github.com/localhost128/event-management.git
cd event-management
```
make .env file from .env.example
```
docker build . -t event-management
docker volume create django_db
docker run --rm -v django_db:/app event-management python src/manage.py migrate
docker run -p 8000:8000 -v django_db:/app event-management
```

OpenAPI shcema on /api/schema/
Swagger UI on /api/schema/swagger-ui/
Redoc on  /api/schema/redoc/
