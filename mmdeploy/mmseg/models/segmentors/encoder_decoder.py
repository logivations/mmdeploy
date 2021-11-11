import torch.nn.functional as F
from mmseg.ops import resize

from mmdeploy.core import FUNCTION_REWRITER


@FUNCTION_REWRITER.register_rewriter(
    func_name='mmseg.models.segmentors.EncoderDecoder.simple_test')
def encoder_decoder__simple_test(ctx, self, img, img_meta, **kwargs):
    """Rewrite `simple_test` for default backend.

    Support configured dynamic/static shape for model input and return
    segmentation map as Tensor instead of numpy array.

    Args:
        ctx (ContextCaller): The context with additional information.
        self: The instance of the original class.
        img (Tensor | List[Tensor]): Input image tensor(s).
        img_meta (dict): Dict containing image's meta information
            such as `img_shape`.

    Returns:
        torch.Tensor: Output segmentation map pf shape [N, 1, H, W].
    """
    x = self.extract_feat(img)
    seg_logit = self._decode_head_forward_test(x, img_meta)
    seg_logit = resize(
        input=seg_logit,
        size=img_meta['img_shape'],
        mode='bilinear',
        align_corners=self.align_corners)
    seg_logit = F.softmax(seg_logit, dim=1)
    seg_pred = seg_logit.argmax(dim=1)
    # our inference backend only support 4D output
    seg_pred = seg_pred.unsqueeze(1)
    return seg_pred
