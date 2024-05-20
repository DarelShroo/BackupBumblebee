## Setting Up the API Project

To set up the API project, you'll need to have Docker installed on your system. Follow these steps:

1. Navigate to the `api/` directory of the project in your terminal or command line.

2. Once in the `api/` folder, run the following command to build and bring up the Docker containers:

    ```bash
    docker-compose up -d --build
    ```

    This command will build the necessary images and bring up the containers in the background (`-d`). The `--build` option ensures that the images are rebuilt before bringing up the containers.

3. Once the containers are up and running, you can access the API backend at [http://localhost:5000/](http://localhost:5000/) and the frontend at [http://localhost:8080/](http://localhost:8080/).

That's it! The API project is now up and running, and you can start using it.

### Possible Errors
- **Error Reading Preface from Client**: If you encounter the following error message: 

    ```
    2024/05/20 11:14:10 http2: server: error reading preface from client //./pipe/docker_engine: file has already been closed
    ```

    To resolve this issue on Windows, restart and run Docker Desktop as an administrator.