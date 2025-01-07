FROM openmmlab/mmdeploy:ubuntu20.04-cuda11.8-mmdeploy1.3.1

#MMSegmentation
#COPY ./ /root/workspace/mmsegmentation/
#ENV FORCE_CUDA="1"
#RUN pip install -r /root/workspace/mmsegmentation/requirements.txt
#RUN pip install --no-cache-dir -e /root/workspace/mmsegmentation

# previous method of local installation fails so fallback to the official method
RUN pip install -U openmim

RUN mim install mmsegmentation
RUN python3 -m pip install ftfy regex

RUN git clone https://github.com/logivations/mmsegmentation.git /mmsegmentation

#MMPretrain
RUN mim install git+https://github.com/logivations/mmpretrain.git
RUN git clone https://github.com/logivations/mmpretrain.git /mmpretrain


RUN mim install git+https://github.com/logivations/mmpose.git
RUN git clone https://github.com/logivations/mmpose.git /mmpose

WORKDIR /mmpose
RUN git checkout v1.3.2-branch_v2

WORKDIR /root/workspace/mmdeploy

