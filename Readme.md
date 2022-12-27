# Guide on how to use this repository

## AdaIN
### Download models
Download [decoder.pth](https://drive.google.com/file/d/1bMfhMMwPeXnYSQI6cDWElSZxOxc6aVyr/view?usp=sharing)/[vgg_normalized.pth](https://drive.google.com/file/d/1EpkBA2K2eYILDSyPTt0fztz59UjAIpZU/view?usp=sharing) and put them under `models/`.

### Sanity check
Use `--content` and `--style` to provide the respective path to the content and style image.
Run the following code to test 
```
CUDA_VISIBLE_DEVICES=<gpu_id> python tests/test_AdaIN.py --content tests/input/cornell.jpg --style tests/style/woman_with_hat_matisse.jpg
```

# Short descriptions of the modules used
# Texformer: 3D Human Texture Estimation from a Single Image with Transformers
This code adapts the official implementation of ["3D Human Texture Estimation from a Single Image with Transformers", ICCV 2021 (Oral)](http://arxiv.org/abs/2109.02563)

## References
[1] ["3D Human Pose, Shape and Texture from Low-Resolution Images and Videos", IEEE Transactions on Pattern Analysis and Machine Intelligence, 2021.](https://arxiv.org/abs/2103.06498)

[2] ["3D Human Shape and Pose from a Single Low-Resolution Image with Self-Supervised Learning", ECCV, 2020](https://arxiv.org/abs/2007.13666)

[3] ["SMPL: A Skinned Multi-Person Linear Model", SIGGRAPH Asia, 2015](https://files.is.tue.mpg.de/black/papers/SMPL2015.pdf)

[4] ["Learning Spatial and Spatio-Temporal Pixel Aggregations for Image and Video Denoising", IEEE Transactions on Image Processing, 2020.](https://arxiv.org/abs/2101.10760)

[5] ["Learning Factorized Weight Matrix for Joint Filtering", ICML, 2020](http://proceedings.mlr.press/v119/xu20f.html)

[6] ["Style normalization and restitution for generalizable person re-identification", CVPR, 2020](https://arxiv.org/abs/2005.11037)

[7] ["3D Human Texture Estimation from a Single Image with Transformers", ICCV 2021 (Oral)](http://arxiv.org/abs/2109.02563)

[8] ["Arbitraty Style Transfer in Real-time with Adaptive Instance Normalization", ICCV 2017 (Oral)](https://arxiv.org/abs/1703.06868)

