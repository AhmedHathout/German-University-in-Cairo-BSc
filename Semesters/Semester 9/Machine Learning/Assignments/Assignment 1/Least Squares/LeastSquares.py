import os
from PIL import Image
import numpy as np

num_of_classes = 10

def read_images(folder: str, add_ones=True):
    np_images = [[] for filename in os.listdir(folder) if filename.endswith(".jpg")]

    for filename in os.listdir(folder):
        if filename.endswith(".jpg"):
            index = int(filename.split(".")[0]) - 1
            image = Image.open(os.path.join(folder, filename))
            np_image = np.array(image).flatten()

            if add_ones:
                np_image = np.append(np_image, 1)

            del np_images[index]
            np_images.insert(index, np_image)

    with open(os.path.join(folder, "Labels.txt"), "r") as f:
        labels = [int(label.strip()) for label in f.readlines()]

    return np_images, labels

def least_squares_w():
    training_folder = "./Train"

    np_images, labels = read_images(folder=training_folder)
    np_images_transposed = np.transpose(np_images)

    x_t_x_1_x_t = np.dot(np.linalg.pinv(np.dot(np_images_transposed, np_images)), np_images_transposed)

    ws = []
    for i in range (num_of_classes):
        t = []
        for j in range(len(labels)):
            if i == labels[j]:
                t.append(1)
            else:
                t.append(-1)

        w = np.dot(x_t_x_1_x_t, t)
        ws.append(w)

    return np.array(ws)

def get_confusion_matrix():

    # The rows correspond to the weights of a classifier for each number
    ws = least_squares_w()

    test_folder = "./Test"
    test_images, test_labels = read_images(folder=test_folder)

    ys = []
    for w in ws:
        row_ys = [] # Classification of all the test images with the classifier having weights w
        for test_image in test_images:
            y = np.dot(np.transpose(w), test_image) # Classification of test_image using the classifier with weights w
            row_ys.append(y)
        ys.append(row_ys)

    ys_transposed = np.array(ys).transpose()

    normalisation_matrix = []
    for i in range(len(ys_transposed)):
        normalisation_matrix.append(np.zeros(10).tolist())
        max_index = 0

        for j in range(len(ys_transposed[i])):
            if ys_transposed[i][j] > ys_transposed[i][max_index]:
                max_index = j

        normalisation_matrix[i][max_index] += 1

    confusion_matrix = [[0 for _ in range(num_of_classes)] for _ in range(num_of_classes)]
    for i in range(len(normalisation_matrix)):
        for j in range(len(normalisation_matrix[0])):
            if normalisation_matrix[i][j] == 1:
                confusion_matrix[i // 20][j] += 1
                break

    return confusion_matrix

with open("Confusion Marix.csv", "w") as f:
    confusion_matrix = get_confusion_matrix()

    str_confusion_matrix = "Real Value \\ Predicted Value,"
    str_confusion_matrix += ",".join([str(cls) for cls in range(num_of_classes)]) + "\n"
    for i, row in enumerate(confusion_matrix):
        str_confusion_matrix += str(i) + ","
        for num in row:
            str_confusion_matrix += str(int(num)) + ", "

        str_confusion_matrix += "\n"

    f.write(str_confusion_matrix)



