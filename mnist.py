#!/usr/bin/env python3

import scipy.io as sio
from collections import namedtuple

MNIST = namedtuple("MNIST", ["trainX", "trainY", "testX", "testY"])

def load():
    r = sio.loadmat("mnist.mat")
    return MNIST(trainX=r["trainX"], trainY=r["trainY"], testX=r["testX"], testY=r["testY"])

if __name__ == "__main__":
    x = load()
    assert x.trainX.shape == (60000, 784)
    assert x.trainY.shape == (1, 60000)
    assert x.testX.shape == (10000, 784)
    assert x.testY.shape == (1, 10000)
