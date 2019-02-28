import pandas as pd
import matplotlib.pyplot as plt
from numpy import linalg

def read_data():
    df = pd.read_csv(filepath_or_buffer="./Data.txt", delimiter=" ")

    df.columns = ["x", "y"]
    df.dropna(how="all", inplace=True)
    return df

def get_covariance_matrix(df: pd.DataFrame):
    df2 = df - df.mean()
    return df2.transpose().dot(df2) / (df.shape[0] - 1)

def get_eigenvector(covariance_matrix: pd.DataFrame):
    return linalg.eig(covariance_matrix)

def project_data(original_data_input: pd.DataFrame, eigenvectors):
    output_data1 = original_data_input.dot(eigenvectors[0])
    output_data2 = original_data_input.dot(eigenvectors[1])

    output_data = pd.DataFrame([output_data1, output_data2]).transpose()
    pd.set_option('display.max_rows', 1000)
    plt.scatter(original_data_input["x"], original_data_input["y"])
    plt.quiver([5], [5],
        [eigenvector[0] * 100 for eigenvector in eigenvectors],
        [eigenvector[1] * 100 for eigenvector in eigenvectors])
    plt.savefig("Data_PCA.png")

    with open("Data_result.txt", "w") as f:
        f.write("PC1 = %s\n"
                "PC2 = %s\n\n"
                "Projected Data:-\n%s" % (eigenvectors[0], eigenvectors[1], output_data))

if __name__ == '__main__':
    df = read_data()
    covariance_matrix = get_covariance_matrix(df)
    eigenvalues, eigenvector = get_eigenvector(covariance_matrix)
    project_data(df, eigenvector)
