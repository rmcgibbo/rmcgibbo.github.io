title: Faster PyYAML Parsing with LibYAML
date: 2013-05-23 23:20
comments: true
tags: msmbuilder
slug: faster-yaml-parsing-with-libyaml


This morning, [Christian](https://github.com/schwancr) submitted a great
[pull request](https://github.com/SimTk/msmbuilder/pull/199) to speed up YAML
parsing in MSMBuilder using LibYAML. In MSMBuilder,
we use a YAML file to save the "project", which is keeps the path to all of
the files associated with an MSMBuilder project, such as the different
trajectories, and a PDB for the protein's topology.

YAML is convenient here: being easily editable plain text, it makes it pretty
easy to check what's in your project, and perform simple tasks like splitting
a project in two, without needing any libraries or programming. But there's
one big disadvantage: it can be really really slow to load a large project
file. Although it's not usually the rate limiting step, it's still really
annoying.

Using the LibYAML parser (written in C) can speed up the reading significantly.
To see if your python installation is linked against LibYAML, try the following
command.

``` bash
python -c "from yaml import CLoader"
```

If this blows up with an ImportError, then LibYAML isn't installed. If the
commands runs just fine, then you've already got LibYAML.

## Installing LibYAML

To install LibYAML, you can either build it from source or use a package manager.
If you've got `sudo` privileges, you can easily install LibYAML from source,
following the directions from [here](http://pyyaml.org/wiki/LibYAML), with:

``` bash
wget http://pyyaml.org/download/libyaml/yaml-0.1.4.tar.gz
tar -xzvf yaml-0.1.4.tar.gz
cd yaml-0.1.4
./configure
make
sudo make install
```

If you're on a machine without `sudo` privileges, use a `--prefix` flag with
`configure` to install the library in user-space. You'll probably also have to
add the new library directory to `LD_LIBRARY_PATH` (or `DYLD_LIBRARY_PATH` on mac).

If you access to a package manager like `apt-get` on ubuntu, then you can
install LibYAML with the command `sudo apt-get install libyaml-dev`. On a centos
system, you should be able to get LibYAML with `sudo yum install libyaml-devel`.

## Rebuilding PyYAML with the C Bindings

If you've installed LibYAML with the default location (either by compiling from
source without --prefix, or using your package manager), then you can rebuild PyYAML
with the LibYAML bindings by just reinstalling it through pip with `pip install pyyaml --upgrade --force`.

Otherwise, download the source package from [pypi](https://pypi.python.org/pypi/PyYAML)
and edit the `setup.cfg` file to point to the lib and include directories of your
LibYAML installation. I configured LibYAML with `--prefix=$HOME/opt/yaml`, so
uncommented lines 7 and 10 of `setup.cfg`, and edited them to read

``` bash
# List of directories to search for 'yaml.h' (separated by ':').
include_dirs=/usr/local/include:../../include:/home/rmcgibbo/opt/yaml/include

# List of directories to search for 'libyaml.a' (separated by ':').
library_dirs=/usr/local/lib:../../lib:/home/rmcgibbo/opt/yaml/lib
```

And then rebuilt the package with

``` bash
python setup.py --with-libyaml install
```
