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
    - Clone the repo into a directory of your choosing (todoapp is a sample name): git clone https://github.com/AK-Rosen/todoapp.git todoapp
    - Navigate to the root of the project where the Dockerfile lives
    - Run `docker build -t todoapp .`
    - Then run `docker run -p 8000:8000 todoapp`
    - In any browser, navigate to `http://localhost:8000/`
    - The application should be running
