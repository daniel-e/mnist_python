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
