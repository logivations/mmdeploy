export TAG=openmmlab/mmdeploy:ubuntu20.04-cuda11.8-mmdeploy1.3.1
docker run --gpus=all -v /data:/data -it --rm $TAG
