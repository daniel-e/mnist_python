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

print(data.trainX.shape)
print(data.trainY.shape)
print(data.testX.shape)
print(data.testY.shape)
```

When you're running the code for the first time mnistdb will download
the MNIST database of handwritten digits from the Internet. The database
will be stored in `~/.mnistdb` so that does not need to download the
database for subsequent calls.