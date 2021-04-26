snapsnare-cli
=

snapsnare-cli, this project, synchronises jamulus server activities with the snapsnare database.


Table of contents:

* Remarks
* Getting started
  * general installation
  * development installation

# Remarks
snapsnare-cli currently supports Python 3.5 and higher.

# Getting started
snapsnare consists of 2 parts, a commandline interface, this tool, and a postgresql database.
When you want to use snapsnare-cli it is recommended that you follow the instructions described in the general installation section.


## General installation
snapsnare-cli depends on the snapsnare database. 
Before you start the installation of snapsnare-cli it is recommended you execute these [installation instructions](https://github.com/janripke/snapsnare-db/blob/main/README.md) first.

### configure snapsnare
For safety reasons the snapsnare database credentials are stored on your local machine. 
To be more exact under ~/.snapsnare/snapsnare-ds.json

create the snapsnare-ds.json in ~/.snapsnare folder: paste the following into this file:
```python
{
  "type": "postgresql",
  "host": "localhost",
  "db": "snapsnare",
  "username": "snapsnare_owner",
  "password": "snapsnare_owner"
}
```

### install snapsnare-cli
```shell
pip3 install git+https://github.com/janripke/snapsnare-cli.git@0.0.1-dev0#egg=snapsnare_cli
```

### run snapsnare-cli
```shell
$ snapsnare-cli
snapsnare-cli version 0.0.1-dev0
```


## Development installation
snapsnare-cli depends on the snapsnare database. 
Before you start the installation of snapsnare it is recommended you execute these [installation instructions](https://github.com/janripke/snapsnare-db/blob/main/README.md) first.

### configure snapsnare-cli
For safety reasons the snapsnare database credentials are stored on your local machine. 
To be more exact under ~/.snapsnare/snapsnare-ds.json

create the snapsnare-ds.json in ~/.snapsnare folder: paste the following into this file:
```python
{
  "type": "postgresql",
  "host": "localhost",
  "db": "snapsnare",
  "username": "snapsnare_owner",
  "password": "snapsnare_owner"
}
```

### clone snapsnare-cli
```
git clone https://github.com/janripke/snapsnare-cli.git
```

### run snapsnare-cli
```shell
python3 snapsnare_cli/snapsnare_cli.py
```

### setup snapsnare-cli for development
```shell
$ python3 setup.py develop
```


