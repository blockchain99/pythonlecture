* [Building Docker Images](https://stackify.com/docker-build-a-beginners-guide-to-building-docker-images/docker-build-a-beginners-guide-to-building-docker-images/)
1.  <span style="color:red">Docker containers</span> are instances of  <span style="color:yellow">Docker images</span> , whether running or stopped. In fact, the major difference between Docker containers and images is that containers have a writable layer.
 ![docker container](docker_img.png)
    * When you create a Docker container, you’re adding a writable layer on top of the Docker image. You can run many Docker containers from the same Docker image. You can see a Docker container as an instance of a Docker image. 
2. <span style="color:yellow">Dockerfile</span> as “a text document that contains all the commands a user could call on the command line to assemble an image.”

3. Original step to web app.
* We start by installing the express generator as follows:
``$ npm install express-generator -g``

* Next, we scaffold our application using the following command:
``$ express docker-app``

* Now we install package dependencies:
``$ npm install``

* Start the application with the command below:( http://localhost:3000)
``$ npm start``

4. Above steps can be replaced by Dockerfile 
* .dockerignore
```
.git
.gitignore
node_modules
npm-debug.log
Dockerfile*
docker-compose*
README.md
LICENSE
.vscode
```
* Dockerfile
```
# Filename: Dockerfile 
FROM node:10-alpine
<!-- WORKDIR /usr/src/app -->
WORKDIR /media/ys/hdd2/docker-app/src/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```
5. Build Docker images
    * ``$ docker build .``
* tagging the name we want.(ex. ys/node-server)
    * `` $ docker build -t ys/node-serve . ``
* we can see the image just built
    * ``$ docker images``
 6. Running a Docker image
 * `` $ docker run -p80:3000 ys/node-serve ``
    * -p argument to specify what port on the host machine to map the port the app is listening on in the container. Now you can access your app from your browser on https://localhost.
    * To run the container in a detached mode, you can supply argument -d 
    * `` $ docker run -d -p80:3000 ys/node-serve ``

7. Pushing a Docker image to Docker repository
```
With your Docker Hub credentials ready, you need only to log in with your username and password.

$ docker login
Retag the image with a version number:

$ docker tag yourusername/example-node-app yourdockerhubusername/example-node-app:v1
Then push with the following:

$ docker push abiodunjames/example-node-app:v1
If you’re as excited as I am, you’ll probably want to poke your nose into what’s happening in this container, and even do cool stuff with Docker API.

You can list Docker containers:

$ docker ps
And you can inspect a container:

$ docker inspect <container-id>
You can view Docker logs in a Docker container:

$ docker logs <container-id>
And you can stop a running container:

$ docker stop <container-id>
```
***********************
* remove docker iamges
    * ``$ docker images -a``
* you can pass their ID or tag to docker rmi
    * ``$ docker rmi Image Image``

* remove container
    * ``$ docker ps -a``
    * ``$ docker rm ID_or_Name ID_or_Name``
    * ``$ docker run --rm image_name`` (run & remove)
    * ``$ docker rm -v container_name``
****************************************
* How does one add something new to an already existing docker image?

Create a Dockerfile which uses the existing image as base image and add the required installation packages or modules you want inside the image using RUN command

Dockerfile should be somewhat like this :
```
FROM <existing image name>
RUN apt-get update && pip install tensorflow
```
Then again build the new image using the command:
```
$ docker build -t <image-name>:<tag> .
```
*****************************************
* [tf2.0](https://levelup.gitconnected.com/5-important-changes-coming-with-tensorflow-2-0-e6bb172c5fdf)
* [tf official tf2 migrate guide](https://www.tensorflow.org/guide/migrate)
* [tf2 example](https://towardsdatascience.com/tensorflow-2-0-create-and-train-a-vanilla-cnn-on-google-colab-c7a0ac86d61b)