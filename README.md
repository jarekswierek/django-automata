# django-automata

Web application for fast create Django project parts e.g. CRUD Views

# RUN APP

1. Install Docker and docker-compose

https://docs.docker.com/engine/installation/linux/ubuntu/#install-using-the-repository

```
pip install docker-compose==1.10.0
```

2. Add docker to group

```
sudo usermod -aG docker ${USER}
```

3. Set django-automata and run

```
git clone git@github.com:jarekswierek/django-automata.git
cd django-automata
docker-compose build
docker-compose up
```

Application will be available on **localhost:8000**

# sources

- background: freepptbackgrounds.net 
