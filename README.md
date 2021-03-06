# mnistdb

mnistdb is a library which loads the
[MNIST database of handwritten digits](http://yann.lecun.com/exdb/mnist/)
into numpy arrays.

## Install

    pip install mnistdb

## Running

```Python
import mnistdb.io as mio

data = mio.load()

# shape of data
assert x.trainX.shape == (60000, 784)
assert x.trainY.shape == (60000,)
assert x.testX.shape == (10000, 784)
assert x.testY.shape == (10000,)

# With the parameter scaled=True all pixel values are
# scaled into the interval [0,1]

data = mio.load(scaled=True)
```

When you're running the code for the first time mnistdb will download
the MNIST database of handwritten digits from the Internet. The database
will be stored in `~/.mnistdb` so that does not need to download the
database for subsequent calls.

If you want one-hot encoded labels call `load` with the parameter
`one_hot=True`.

```Python
import mnistdb.io as mio

n = mio.load()
o = mio.load(one_hot=True)

# print the labels of the first five training examples
print(n.trainY[range(5)])

# print the one-hot encoded labels of the first five training examples
print(o.trainY[range(5), :])
```

The output is:

```
[5 0 4 1 9]
[[ 0.  0.  0.  0.  0.  1.  0.  0.  0.  0.]
 [ 1.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  1.  0.  0.  0.  0.  0.]
 [ 0.  1.  0.  0.  0.  0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.  0.  0.  0.  0.  1.]]
```

