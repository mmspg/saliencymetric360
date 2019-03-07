# Source code

File `quality_metrics.py` contains two functions implemented in Python
to compute WS-PSNR and VA-PSNR

```
wspsnr(im_true,im_test,range=(235-16))
    Compute WS-PSNR
    im_true - original omnidirctional image in equirectangular format
    im_test - tested omnidirctional image in equirectangular format
    ragne - dynamic range of pixel values, default is [16,235]
```

```
vapsnr(im_true,im_test,saliency_map,range=(235-16))
    Compute VA-PSNR, Visual Attention PSNR
    im_true - original omnidirctional image in equirectangular format
    im_test - tested omnidirctional image in equirectangular format
    saliency_map - saliency map for the tested image
    ragne - dynamic range of pixel values, default is [16,235]
```
