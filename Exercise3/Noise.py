import numpy as np
import cv2



def add_Gaussion_Noise(img, mean, sigma):
    NoiseImg = img.copy()
    #NoiseImg = random.gauss(mean, sigma)
    cv2.randn(NoiseImg, mean, sigma)
    cv2.add(img, NoiseImg, NoiseImg)
    return NoiseImg

def add_Salt_Pepper_Noise(img, pa, pb):
    SPNoise = img.copy()
    BlackNum=int(pa * img.shape[0] * img.shape[1])
    WhiteNum=int(pb * img.shape[0] * img.shape[1])
    for i in range(BlackNum):
        X=np.random.randint(0,img.shape[0]-1)
        Y=np.random.randint(0,img.shape[1]-1)
        SPNoise[X,Y]=0
    for i in range(WhiteNum):
        X=np.random.randint(0,img.shape[0]-1)
        Y=np.random.randint(0,img.shape[1]-1)
        SPNoise[X,Y]=255
    return SPNoise

if __name__ =='__main__':
    image = cv2.imread("Lenna.png")
    cv2.imshow("Original",image)
    grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray", grayimg)
    
    mean = 0
    sigma = 20
    pa = 0.01
    pb = 0.01
    
    gaussNoiseImg = add_Gaussion_Noise(grayimg, mean, sigma)
    cv2.imshow("Gauss Noise", gaussNoiseImg)
    
    boxfilter_img1 = cv2.boxFilter(gaussNoiseImg, -1, (3,3))
    cv2.imshow("Box Filter on Gauss", boxfilter_img1)
    
    gaussfilter_img1 = cv2.GaussianBlur(gaussNoiseImg, (3,3), 1.5, 3)
    cv2.imshow("GaussianBlur on Gauss", gaussfilter_img1)
    
    medianfilter_img1 = cv2.medianBlur(gaussNoiseImg, 5)
    cv2.imshow("MedianBlur on Gauss", medianfilter_img1)
    
    saltPepperImg = add_Salt_Pepper_Noise(grayimg, pa, pb)
    cv2.imshow("Salt&Pepper Noise",saltPepperImg)
    
    boxfilter_img2 = cv2.boxFilter(saltPepperImg, -1, (3,3))
    cv2.imshow("Box Filter on Salt&Pepper", boxfilter_img2)
    
    gaussfilter_img2 = cv2.GaussianBlur(saltPepperImg, (3,3), 1.5, 3)
    cv2.imshow("GaussianBlur on Salt&Pepper", gaussfilter_img2)
    
    medianfilter_img2 = cv2.medianBlur(saltPepperImg, 5)
    cv2.imshow("MedianBlur on Salt&Pepper", medianfilter_img2)
    
    cv2.waitKey(0)