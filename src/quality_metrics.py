

import numpy as np
from skimage import transform as tran


# WS-PSNR

def generate_ws(i,j,M,N):
    return np.cos( (j+0.5-N/2)*np.pi/N )

def wsmse(im_true,im_test):
    N,M = np.shape(im_true)
    i = np.arange(1,M+1)
    j = np.arange(1,N+1)
    ii, jj = np.meshgrid(i, j)
    # Genarate weight matrix for WS-PSNR
    w = generate_ws(ii,jj,M,N)
    return np.sum( np.multiply((im_true-im_test)**2,w) ) / np.sum(w)

def wspsnr(im_true,im_test,range=(235-16)):
    '''Compute WS-PSNR [1]
    im_true - original omnidirctional image in equirectangular format
    im_test - tested omnidirctional image in equirectangular format
    ragne - dynamic range of pixel values, default is [16,235]
    [1] https://ieeexplore.ieee.org/abstract/document/7961186
    '''
    max_i = range
    return 20*np.log10(max_i)-10*np.log10(wsmse(im_true,im_test,w))


# VA-PSNR
def vamse(im_true,im_test,saliency_map):
    N,M = np.shape(im_true)
    W = tran.resize(saliency_map, np.shape(im_test), mode='reflect',
                    anti_aliasing=False)
    return np.sum( np.multiply((im_true-im_test)**2,W) ) / np.sum(W)

def vapsnr(im_true,im_test,saliency_map,range=(235-16)):
    '''Compute VA-PSNR, Visual Attention PSNR
    im_true - original omnidirctional image in equirectangular format
    im_test - tested omnidirctional image in equirectangular format
    saliency_map - saliency map for the tested image
    ragne - dynamic range of pixel values, default is [16,235]
    '''
    max_i = range
    return 20*np.log10(max_i)-10*np.log10(vamse(im_true,im_test,w))
