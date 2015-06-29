The module should work with Python 2.4, 2.5, 2.6, 2.7. I haven't yet put together a version for Python 3.


# Do I have it installed? #

If you have preprocess.py installed you should be able to do this:

```
$ python -c "import preprocess; print('yes')"
yes
```


# What version do I have installed? #

```
$ python -c "import preprocess; print(preprocess.__version__)"
...your installed version...
```


# How do I install of upgrade? #

Install with **one** of the following methods.

  * Install **with pip** (if you have it):

> `pip install preprocess`

> More on `pip` [here](http://pip.openplans.org/).

  * Install **with easy\_install** (if you have it):

> `easy_install preprocess`

> See good instructions here for installing easy\_install (part of setuptools) [here](http://turbogears.org/2.0/docs/main/DownloadInstall.html#setting-up-setuptools).

  * **Basic** (aka old school) installation:
    1. download the latest `preprocess-$version.zip`
    1. unzip it
    1. run `python setup.py install` in the extracted directory

> For example, for version 1.1.2:
```
wget -q http://preprocess.googlecode.com/files/preprocess-1.1.2.zip
unzip preprocess-1.1.2.zip
cd preprocess-1.1.2
python setup.py install
```