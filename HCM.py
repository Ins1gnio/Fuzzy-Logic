"""
Hard c-means python code (without Lib.), created for "Fundamental of Intelligent System" Class, BME.
Code algorithm is based on book byy Timothy J. Ross (Fuzzy Logic with Engineering Application, pp. 371)
U matrix value is randomized using np.random, which can cause error at times if the U matrix not fully randomized,
solution to this, you just need to run the code again. Reducing the c value also helps.
(c) AS. - 2024
"""

import matplotlib.pyplot as plt
import numpy as np

class main_hcm:
    def __init__(self):
        # generate randomized data
        self.n_dat = 100  # number of data
        self.dat = [[np.random.uniform(0, 100), np.random.uniform(0, 100)] for _ in range(self.n_dat)]

        # static test data
        # self.dat = [[1, 1], [1, 2], [2, 1], [6, 7], [6, 6], [7, 7], [3, 2], [0, 5], [6, 7], [8, 9], [10, 1], [10, 6]]     # 2d data value
        # self.n_dat = len(self.dat)      # number of data

        self.c = 5      # number of cluster
        self.u = np.zeros((self.c, self.n_dat))
        for i in range(self.n_dat):
            temp = np.random.randint(0, self.c)     # randomize the u matrix
            self.u[temp, i] = 1
        print("U matrix initial value:")
        print(self.u)
        self.iter = 0       # no. of iteration
        self.flag = True    # flag use to compare
        self.color = ['r', 'orange', 'g', 'b', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']      # color for each cluster

        self.main()     # main prog.
        self.plot()     # scatter plot

    def main(self):
        while self.flag:
            self.iter += 1
            # calculate the center vector (v)
            num = np.matmul(self.u, self.dat)
            den = [[0 for i in range(1)] for j in range(len(self.u))]
            for i in range(len(self.u)):
                for j in range(len(self.u[0])):
                    den[i][0] += self.u[i][j]
            self.v = np.divide(num, den)

            # calculate the distance (d) between each data and center vector
            self.d = [[0 for i in range(len(self.dat))] for j in range(len(self.v))]
            for i in range(len(self.v)):
                for k in range(len(self.dat)):
                    temp = 0
                    for j in range(len(self.dat[0])):
                        temp += (self.dat[k][j] - self.v[i][j]) ** 2
                    self.d[i][k] = np.sqrt(temp)

            # find the closest center vector of each data --> using min. value of the distance (d)
            self.u_last = self.u
            self.u = np.zeros((self.c, self.n_dat))
            self.d_t = list(zip(*self.d))
            for j in range(len(self.d_t)):
                idx = self.d_t[j].index(min(self.d_t[j]))
                self.u[idx, j] = 1
            print("U matrix iteration no. " + str(self.iter) + " value:")
            print(self.u)

            # compare last iter. u and this iter. u
            self.flag = False
            for i in range(self.c):
                for j in range(self.n_dat):
                    if self.u[i, j] != self.u_last[i, j]:
                        self.flag = True

    def plot(self):
        plt.figure(figsize=(11, 5))
        plt.subplot(1, 2, 1)    # scatter plot data
        plt.title("Randomized Data")
        plt.xlabel("x coordinate")
        plt.ylabel("y coordinate")
        plt.scatter([i[0] for i in self.dat], [i[1] for i in self.dat])

        idx = [0] * len(self.u[0])
        x_plt = []
        for i in range(self.c):
            x_plt.append([])

        for i in range(len(self.u[0])):
            for j in range(len(self.u)):
                if self.u[j][i] == 1:
                    idx[i] = j
                    x_plt[j].append(self.dat[i])
        print(x_plt)

        ax2 = plt.subplot(1, 2, 2)  # scatter plot data with cluster color
        plt.title("HCM Clustering")
        plt.xlabel("x coordinate")
        plt.ylabel("y coordinate")
        for i in range(self.c):
            x, y = zip(*x_plt[i])
            plt.scatter(x, y, color=self.color[i], label='Cluster ' + str(i))
            plt.scatter(self.v[i][0], self.v[i][1], color=self.color[i], s=50, marker='x')  # center cluster
        print(self.v)
        ax2.legend()
        plt.show()

main_hcm()