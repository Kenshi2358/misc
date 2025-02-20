A Dockerfile defines the steps to build and create a custom Docker image.  
Once that image is built, you can run containers from it.  
A container is a runtime instance of an image.  

To kick off a Dockerfile and create a custom Docker image, the docker build command needs to be ran.  
This command looks for a file in your current directory called “Dockerfile” and follows that.  
Once done, you’ll have your own custom environment.  
Then you can run your existing docker image for future runs with the docker-compose up command.  

The docker-compose up command looks for a docker-compose.yml file in the current directory.  
It then executes those commands to run that image and any other service listed as a new container.  
The docker-compose.yml file defines and manages multi-container Docker applications.  

In addition, docker-compose up also creates a network for the services defined in the .yml file.  
All services are connected to this network, allowing them to communicate with each other using their service names as host names.  

To check your docker version, type: docker --version  

<h2>To create a docker build:</h2>

Open Docker Desktop. Open a new terminal, cd to the directory of the repo containing your DockerFile.  
Then type: `docker build -t <image_name> .`  
The -t command stands for tag  

<h2>To start up a docker image:</h2>

Open Docker Desktop. Open a new terminal, cd to the directory of the repo you want to work with.  
Activate any virtual environment you need.  

To see what version you’re under, type:  
`docker-compose --version`

Then from the terminal, type:
`docker-compose up`

When you run docker-compose up, docker will look for a .yml file.  
If found, it will start up all docker containers available in the .yml file.  

To start up a docker container with an interactive terminal, type:  
`docker-compose up --detach`  
This also works:  
`docker-compose up -d`

To take down a docker container, type:  
`docker-compose down`

To see the current status of running processes, navigate to your .yml file’s directory. Then type:  
`docker-compose ps`
