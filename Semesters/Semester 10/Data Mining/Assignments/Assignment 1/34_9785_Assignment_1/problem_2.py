import pandas as pd
import matplotlib.pyplot as plt
from numpy import linalg

string_columns = ["HomeTeam", "AwayTeam", "FTR"]
def read_data():
    df = pd.read_excel("./EPL.xlsx")

    df.dropna(how="all", inplace=True)
    return df

def get_covariance_matrix(df: pd.DataFrame):
    df = df.drop(columns=string_columns)
    df2 = df - df.mean()
    return df2.transpose().dot(df2) / (df.shape[0] - 1)

def get_eigenvector(covariance_matrix: pd.DataFrame):
    return linalg.eig(covariance_matrix)

def project_data(original_data_input: pd.DataFrame, eigenvectors):
    projected_data = [original_data_input.drop(columns=string_columns).dot(eigenvector) for eigenvector in eigenvectors]

    differences = []
    for number, pc in enumerate(projected_data):
        Hs = []
        As = []

        for i in range(len(pc)):
            point = pc[i]
            ftr = original_data_input.iloc[i]["FTR"]
            if ftr == "H":
                Hs.append(point)
            else:
                As.append(point)

        plt.hist(Hs, bins=10, color="red")
        plt.hist(As, bins=10, color="blue")
        plt.savefig("Proj_PC%d.png" %(number + 1))
        plt.clf()
        # plt.figure()
        hs_df = pd.DataFrame(Hs)
        as_df = pd.DataFrame(As)

        differences.append(abs(hs_df.mean() - as_df.mean()))
    plt.scatter(["PC_%d" % (i + 1) for i in range(len(eigenvectors))],
                differences)
    plt.savefig("Distance.png")


if __name__ == '__main__':
    df = read_data()
    covariance_matrix = get_covariance_matrix(df)
    eigenvalues, eigenvector = get_eigenvector(covariance_matrix)
    project_data(df, eigenvector)