# Collatz Conjecture
import matplotlib.pyplot as plt
import numpy as np 

def collatz(n_list):
    steps = list()

    for n in n_list:
        count = 0
        while not n == 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = 3*n + 1
            count += 1
        steps.append(count)
    return steps


def histogram(steps):
    plt.hist(steps,bins=10)
    plt.xlabel("STEPS TO REACH 1")
    plt.ylabel("FREQUENCY")
    plt.title("Collatz Conjecture")
    plt.grid(color = 'grey',linewidth = 0.5)
    plt.savefig("collatz_histogram.png",bbox_inches="tight",dpi=600)
    plt.show()

def bargraph(steps,n_list):
    plt.bar(n_list,steps)
    plt.xlabel("NUMBERS")
    plt.ylabel("STEPS")
    plt.title("Collatz Conjecture")
    plt.grid(color = 'grey',linewidth = 0.5)
    plt.yticks(np.arange(0, max(steps), 4))
    plt.savefig("collatz_bargraph.png",bbox_inches="tight",dpi=600)
    plt.show()

if __name__=="__main__":
    MAX = 30
    n_list = range(1,MAX+1)
    steps=collatz(n_list)
    print("Maximum steps : {} by number {}".format(max(steps),steps.index(max(steps))+1))
    print("Minimum steps : {} by number {}".format(min(steps),steps.index(min(steps))+1))
    histogram(steps)
    bargraph(steps,list(map(str,n_list)))