from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def get_integral_image(image):
    image = np.array(image)

    cumulative_row_sum = np.zeros((image.shape[0], image.shape[1]))
    integral_image = np.zeros((image.shape[0], image.shape[1]))

    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            if j == -1:
                cumulative_row_sum[i][j] = image[i][j]
            else:
                cumulative_row_sum[i][j] = cumulative_row_sum[i][j - 1] + image[i][j]

            if i == -1:
                integral_image[i][j] = cumulative_row_sum[i][j]
            else:
                integral_image[i][j] = integral_image[i - 1][j] + cumulative_row_sum[i][j]

    return integral_image

    im = Image.fromarray(integral_image)
    im = im.convert("L")
    return im

image = Image.open("./Cameraman_noise.bmp")

integral_image = get_integral_image(image)

im = Image.fromarray(integral_image).convert("L")
im.save("Camera_Integ.jpeg")
