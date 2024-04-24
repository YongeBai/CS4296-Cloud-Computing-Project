DOCKER_FILE_NAME="Dockerfile"
DOCKER_IMAGE_NAME="llmbenchmark_image"
DOCKER_CONTAINER_NAME="llmbenchmark_container"

# Check if docker container exists. If exists, remove it.
if [ ! -z "$(docker ps -a -q -f name=$DOCKER_CONTAINER_NAME)" ]; then
    echo "Removing existing container: $DOCKER_CONTAINER_NAME"
    docker rm $DOCKER_CONTAINER_NAME
fi

# # Check if docker image exists. If exists, remove it.
# if [ ! -z "$(docker images -q $DOCKER_IMAGE_NAME)" ]; then
#     echo "Removing existing image: $DOCKER_IMAGE_NAME"
#     docker rmi $DOCKER_IMAGE_NAME
# fi

# Build docker image
docker build -t $DOCKER_IMAGE_NAME -f $DOCKER_FILE_NAME .

# Run docker container to start bash
docker run --rm -it --name $DOCKER_CONTAINER_NAME --gpus all -v $(pwd):/usr/app --env-file .env $DOCKER_IMAGE_NAME bash

