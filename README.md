# VERSIONS

- Node - 21.2.0
- NPM - 10.2.3
- Python 3.12.0
- Django - 3.2.9
- Docker - 4.25.2
- Sass - 1.69.5 (using brew)

# INSTALLATION/RUNNING

    Assuming all of the above versions have been correctly installed and configured:
    - clone the repo into a directory of your choosing (todoapp is a sample name): git clone https://github.com/AK-Rosen/todoapp.git todoapp
    - Navigate to the root of the project where the Dockerfile lives
    - run `docker build -t todoapp .`
    - then run `docker run -p 8000:8000 todoapp`
    - in any browser, navigate to `http://localhost:8000/`
    - the application should be running

# Original app source

https://realpython.com/django-todo-lists/#step-1-set-up-your-virtual-environment-and-django
