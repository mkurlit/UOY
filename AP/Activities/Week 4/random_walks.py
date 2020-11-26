import seaborn as sns
import numpy as np 
import matplotlib.pyplot as plt

class RandomWalks:

    def __init__(self, cap, no_iter, no_test):
        self.cap = cap 
        self.no_iter = no_iter
        self.no_test = no_test
    
    def single_walk(self):
        position = 0
        trace = np.array([])
        while abs(position)<self.cap and trace.size <= self.no_iter:
            position+=np.random.choice([-1,1])
            trace = np.append(trace, position)
        return trace 
    
    def multiple_walks(self):
        walks_hist = np.array([])
        for wlk in range(self.no_test):
            walks_hist = np.append(walks_hist, self.single_walk().size)
        return walks_hist
    
    def draw_histogram(self):
        sns.histplot(self.multiple_walks(), kde = True)
        plt.show()

    def draw_walks(self):
        walks = []
        for t in range(self.no_test):
            walks.append(np.array(self.single_walk()))
        sns.lineplot(data = walks, dashes = False)
        plt.show()
        #return walks

test = RandomWalks(7, 200, 10000)
test.draw_histogram()