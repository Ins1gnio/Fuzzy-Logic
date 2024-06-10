"""
Fuzzy c-means (FCM) python code (without Lib.), created for "Fundamental of Intelligent System" Class, BME.
Code algorithm is based on book by Timothy J. Ross (Fuzzy Logic with Engineering Application, pp. 379).
Same as HCM, the U matrix value is randomized using np.random, which can cause error at times if the U matrix not fully randomized,
solution to this, you just need to run the code again. Reducing the c value also helps.
Ignore the error resulting on NaN, which means the center cluster overlapping 1 of the data, division with distance equal to 0.
(c) AS. - 2024
"""

import matplotlib.pyplot as plt
import numpy as np
import math


class main_fcm:
    def __init__(self):
        # generate randomized data
        self.n_dat = 100  # number of data
        self.dat = [[np.random.uniform(0, 10), np.random.uniform(0, 10)] for _ in range(self.n_dat)]

        # test data
        # self.dat = [[1, 6], [4, 4], [7, 4], [5, 5], [0, 4]]
        # self.n_dat = len(self.dat)  # number of data

        self.c = 4      # number of cluster
        self.weight = 2     # fuzzy weight (m')
        self.tolerance = 0.01  # error tolerance each iteration
        self.u = np.zeros((self.c, self.n_dat))
        for i in range(self.n_dat):
            temp = np.random.randint(0, self.c)  # randomize the u matrix
            self.u[temp, i] = 0.999  # value is not 1 to avoid zero division
        print("U matrix initial value:")
        print(self.u)
        self.iter = 0  # no. of iteration
        self.flag = True  # flag use to compare
        self.color = ['r', 'orange', 'g', 'b', 'c', 'm', 'y', 'k', 'Brown', 'ForestGreen']  # color for each cluster

        self.main()  # main prog.
        self.plot()  # scatter plot

    def main(self):
        while self.flag:
            self.iter += 1

            # calculate the center vector (v)
            num = np.matmul(self.power(self.u), self.dat)
            den = [[0 for i in range(1)] for j in range(len(self.u))]
            for i in range(len(self.u)):
                for j in range(len(self.u[0])):
                    den[i][0] += (self.u[i][j]) ** self.weight
            self.v = np.divide(num, den)

            # calculate the distance (d) between each data and center vector
            self.d = [[0 for i in range(len(self.dat))] for j in range(len(self.v))]
            for i in range(len(self.v)):
                for k in range(len(self.dat)):
                    temp = 0
                    for j in range(len(self.dat[0])):
                        temp += (self.dat[k][j] - self.v[i][j]) ** 2
                    self.d[i][k] = np.sqrt(temp)

            # update the u value
            self.u_last = self.u
            self.u = np.zeros((self.c, self.n_dat))
            for i in range(len(self.v)):
                for k in range(len(self.dat)):
                    temp = 0
                    for j in range(len(self.v)):
                        temp += (self.d[i][k] / self.d[j][k]) ** (2 / (self.weight - 1))
                    if math.isnan(temp ** -1):  # division with 0 can be occurred if center cluster overlap 1 of the data
                        self.u[i][k] = 1
                    else:
                        self.u[i][k] = temp ** -1

            print("U matrix iteration no. " + str(self.iter) + " value:")
            print(self.u)

            # compare last iter. u and this iter. u
            self.flag = False
            for i in range(len(self.v)):
                for k in range(len(self.dat)):
                    if np.abs(self.u[i][k] - self.u_last[i][k]) >= self.tolerance:
                        self.flag = True

    def power(self, dat):
        out = []
        for i in range(len(dat)):
            out.append([j ** self.weight for j in dat[i]])
        return out

    def plot(self):
        plt.figure(figsize=(11, 5))
        plt.subplot(1, 2, 1)  # scatter plot data
        plt.title("Randomized Data")
        plt.xlabel("x coordinate")
        plt.ylabel("y coordinate")
        plt.scatter([i[0] for i in self.dat], [i[1] for i in self.dat])

        x_plt = []
        for i in range(self.c):
            x_plt.append([])

        for i in range(len(self.u[0])):
            max = 0
            coord = 0
            for j in range(len(self.u)):
                if self.u[j][i] >= max:
                    max = self.u[j][i]
                    coord = j
            x_plt[coord].append(self.dat[i])
        # print(x_plt)

        ax2 = plt.subplot(1, 2, 2)  # scatter plot data with cluster color
        plt.title("FCM Clustering")
        plt.xlabel("x coordinate")
        plt.ylabel("y coordinate")
        for i in range(self.c):
            x, y = zip(*x_plt[i])
            plt.scatter(x, y, color=self.color[i], label='Cluster ' + str(i))
            plt.scatter(self.v[i][0], self.v[i][1], color=self.color[i], s=50, marker='x')  # center cluster
        ax2.legend()
        plt.show()


if __name__ == '__main__':
    main_fcm()
