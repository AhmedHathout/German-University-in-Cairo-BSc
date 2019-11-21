from PIL import Image
import numpy as np
import math

def get_kernel_size(sigma):
    return 2 * math.ceil(3 * sigma) + 1

def get_kernel(sigma):
    kernel_size = get_kernel_size(sigma)

    # kernel = np.zeros([[0 for _ in range(kernel_size)] for _ in range(kernel_size)])
    kernel = np.zeros(shape=[kernel_size, kernel_size])

    for i in range(kernel_size):
        x = i - kernel_size // 2
        for j in range(kernel_size):
            y = j - kernel_size // 2

            kernel[i][j] = (-1 / (math.pi * (sigma ** 4))) * \
                           (1 - ((x ** 2 + y ** 2) / (2 * (sigma ** 2)))) * \
                           (math.exp(-1 * (((x ** 2 + y ** 2) / (2 * (sigma ** 2))))))

    return kernel

def detect_edges(numpy_image, sigma, threshold):
    kernel_size = get_kernel_size(sigma)
    half_kernel_size = kernel_size // 2
    kernel = get_kernel(sigma)
    convolved_image = numpy_image.copy()

    for i in range(half_kernel_size, numpy_image.shape[0] - half_kernel_size):
        for j in range(half_kernel_size, numpy_image.shape[0] - half_kernel_size):
            new_pixel = 0
            for k in range(kernel_size):
                x = i + k - half_kernel_size
                for l in range(kernel_size):
                    y = j + l - half_kernel_size
                    new_pixel += kernel[k][l] * numpy_image[x][y]
            convolved_image[i][j] = new_pixel

    for i in range(convolved_image.shape[0] - 1):
        for j in range(convolved_image.shape[1] - 1):
            current_pixel = convolved_image[i][j]
            right_pixel = convolved_image[i][j + 1]
            below_pixel = convolved_image[i + 1][j]

            # if zero_crossing(current_pixel, right_pixel) or zero_crossing(current_pixel, below_pixel):
    _ = 1
    im = Image.fromarray(convolved_image).convert("L")
    im.save("Log_2.jpg.jpeg")


def zero_crossing(pixel1, pixel2):
    return True if pixel1 * pixel2 < 0 else False

def main():
    image = Image.open("./Cameraman.tif")

    numpy_image = np.array(image)
    detect_edges(numpy_image, 2, 0.1)

if __name__ == '__main__':
    main()