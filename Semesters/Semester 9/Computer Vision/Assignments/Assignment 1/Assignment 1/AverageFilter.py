from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from IntegralImage import get_integral_image

def average_filter(image, filter_size):
    integral_image = get_integral_image(image)

    image = np.array(image)

    filtered_image = np.array(image) # Another copy that will be modified

    c = filter_size // 2

    for i in range(c, image.shape[0] - c):
        for j in range(c, image.shape[1] - c):

            k = integral_image[i + c][j + c]

            x = 0
            if i - c - 1 >= 0 and j - c - 1>= 0:
                x = integral_image[i - c - 1][j - c - 1]

            z = 0
            if j - c - 1 >= 0:
                z = integral_image[i][j - c] - 1

            y = 0
            if i - c - 1 >= 0:
                y = integral_image[i - c - 1][j]
            filtered_image[i][j] = (k + x - z - y) // (filter_size ** 2)

    im = Image.fromarray(filtered_image)
    im = im.convert("L")
    return im

image = Image.open("./Cameraman_noise.bmp")
average_filter(image, 3).save("Camera_Filt_3.jpg")
average_filter(image, 5).save("Camera_Filt_5.jpg")