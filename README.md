# VERSIONS

- Node - 21.2.0
- NPM - 10.2.3
- Python 3.12.0
- Django - 3.2.9
- Docker - 4.25.2
- Sass - 1.69.5 (using brew)

# Sources

https://nsgov.github.io/patternlibrary/

# INSTALLATION/RUNNING

    Assuming all of the above versions have been correctly installed and configured:
    - Download and install Docker
    - Download and install python3
    - Clone the repo into a directory of your choosing (todoapp is a sample name): git clone https://github.com/AK-Rosen/todoapp.git todoapp
    - Navigate to the root of the project where the Dockerfile lives
    - Run `docker build -t todoapp .`
    - Then run `docker run -p 8000:8000 todoapp`
    - In any browser, navigate to `http://localhost:8000/`
    - The application should be running

# Unit Tests

    A few unit tests ship with this code. They cover the following scenarios
    - Verify that the main list of lists page is reachable
    - Verify that a successful redirect occurs when a list is created/deleted
    - Verify Items can be viewed
    - Verify that creating/updating/deleting items correctly redirets to respective pages
    - To execute the tests, navigate to the directory where manage.py is located
    - run docker ps to get the docker container ID
    - run docker exec -it "container ID" /bin/bash
    - run `python3 manage.py test todo_app.tests`
