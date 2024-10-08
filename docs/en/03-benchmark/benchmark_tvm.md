# Test on TVM

## Supported Models

| Model             | Codebase       |                                       Model config                                       |
| :---------------- | :------------- | :--------------------------------------------------------------------------------------: |
| RetinaNet         | MMDetection    |    [config](https://github.com/open-mmlab/mmdetection/tree/master/configs/retinanet)     |
| Faster R-CNN      | MMDetection    |   [config](https://github.com/open-mmlab/mmdetection/tree/master/configs/faster_rcnn)    |
| YOLOv3            | MMDetection    |       [config](https://github.com/open-mmlab/mmdetection/tree/master/configs/yolo)       |
| YOLOX             | MMDetection    |      [config](https://github.com/open-mmlab/mmdetection/tree/master/configs/yolox)       |
| Mask R-CNN        | MMDetection    |    [config](https://github.com/open-mmlab/mmdetection/tree/master/configs/mask_rcnn)     |
| SSD               | MMDetection    |        [config](https://github.com/open-mmlab/mmdetection/tree/main/configs/ssd)         |
| ResNet            | MMPretrain     |       [config](https://github.com/open-mmlab/mmpretrain/tree/main/configs/resnet)        |
| ResNeXt           | MMPretrain     |       [config](https://github.com/open-mmlab/mmpretrain/tree/main/configs/resnext)       |
| SE-ResNet         | MMPretrain     |      [config](https://github.com/open-mmlab/mmpretrain/tree/main/configs/seresnet)       |
| MobileNetV2       | MMPretrain     |    [config](https://github.com/open-mmlab/mmpretrain/tree/main/configs/mobilenet_v2)     |
| ShuffleNetV1      | MMPretrain     |    [config](https://github.com/open-mmlab/mmpretrain/tree/main/configs/shufflenet_v1)    |
| ShuffleNetV2      | MMPretrain     |    [config](https://github.com/open-mmlab/mmpretrain/tree/main/configs/shufflenet_v2)    |
| VisionTransformer | MMPretrain     | [config](https://github.com/open-mmlab/mmpretrain/tree/main/configs/vision_transformer)  |
| FCN               | MMSegmentation |      [config](https://github.com/open-mmlab/mmsegmentation/tree/master/configs/fcn)      |
| PSPNet            | MMSegmentation |    [config](https://github.com/open-mmlab/mmsegmentation/tree/master/configs/pspnet)     |
| DeepLabV3         | MMSegmentation |   [config](https://github.com/open-mmlab/mmsegmentation/tree/master/configs/deeplabv3)   |
| DeepLabV3+        | MMSegmentation | [config](https://github.com/open-mmlab/mmsegmentation/tree/master/configs/deeplabv3plus) |
| UNet              | MMSegmentation |     [config](https://github.com/open-mmlab/mmsegmentation/tree/master/configs/unet)      |

The table above list the models that we have tested. Models not listed on the table might still be able to converted. Please have a try.

## Test

- Ubuntu 20.04
- tvm 0.9.0

|                                                        mmpretrain                                                         | metric | PyTorch |  TVM  |
| :-----------------------------------------------------------------------------------------------------------------------: | :----: | :-----: | :---: |
|           [ResNet-18](https://github.com/open-mmlab/mmpretrain/blob/main/configs/resnet/resnet18_8xb32_in1k.py)           | top-1  |  69.90  | 69.90 |
|      [ResNeXt-50](https://github.com/open-mmlab/mmpretrain/blob/main/configs/resnext/resnext50-32x4d_8xb32_in1k.py)       | top-1  |  77.90  | 77.90 |
| [ShuffleNet V2](https://github.com/open-mmlab/mmpretrain/blob/main/configs/shufflenet_v2/shufflenet-v2-1x_16xb64_in1k.py) | top-1  |  69.55  | 69.55 |
|    [MobileNet V2](https://github.com/open-mmlab/mmpretrain/tree/main/configs/mobilenet_v2/mobilenet-v2_8xb32_in1k.py)     | top-1  |  71.86  | 71.86 |

<!-- |     [Vision Transformer](https://github.com/open-mmlab/mmpretrain/blob/main/configs/vision_transformer/vit-base-p16_ft-64xb64_in1k-384.py)     | top-1  |  85.43  | 84.01 | -->

|                                        mmdet(\*)                                        | metric | PyTorch | TVM  |
| :-------------------------------------------------------------------------------------: | :----: | :-----: | :--: |
| [SSD](https://github.com/open-mmlab/mmdetection/tree/master/configs/ssd/ssd300_coco.py) | box AP |  25.5   | 25.5 |

\*: We only test model on ssd since dynamic shape is not supported for now.

|                                                           mmseg                                                            | metric | PyTorch |  TVM  |
| :------------------------------------------------------------------------------------------------------------------------: | :----: | :-----: | :---: |
|     [FCN](https://github.com/open-mmlab/mmsegmentation/tree/master/configs/fcn/fcn_r50-d8_512x1024_40k_cityscapes.py)      |  mIoU  |  72.25  | 72.36 |
| [PSPNet](https://github.com/open-mmlab/mmsegmentation/tree/master/configs/pspnet/pspnet_r50-d8_512x1024_80k_cityscapes.py) |  mIoU  |  78.55  | 77.90 |
