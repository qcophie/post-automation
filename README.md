# post-automation
Effortlessly schedule and publish posts to multiple social media platforms using this highly efficient solution built with Python/Django, Docker, Pytest, and Django Rest Framework. Experience seamless automation and improve your online presence with this cutting-edge repository

Youtube Video: https://youtu.be/FYleHEkw8Lc

## Perquisites
- docker
- docker-compose
- .env file in the project root dir

create a superuser
```
  docker exec -it container_id python manage.py createsuperuser
```

run your local server on port 8000 with flag --build (optional)
```
  docker-compose up --build
```

*PS: for more commands, refer to docker-commands.txt found in the project root dir*
