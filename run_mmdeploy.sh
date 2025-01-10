export TAG=quay.io/logivations/ml_all:LS_mmdeploy_1.3.1
docker run --gpus=all -v /data:/data -it --rm $TAG
