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
snapsnare consists of 2 parts, a commandline interface, this tool, and the snapsnare-api rest server


## General installation
The snapsnare-cli uses the snapsnare-api rest server to communicatie with snapsnare.

### configure snapsnare
The endpoint of the snapsnare-api rest server used by snapsnare-cli is stored on your local machine
To be more exact in ~/.snapsnare/snapsnare.json

In this example it is assumed that the snapsnare-api rest server is running on your localhost and uses port 5001
create the snapsnare.json file in ~/.snapsnare folder: paste the following into this file:
```python
{
  "snapsnare-api": {
    "endpoint": "http://localhost:5001"
  }
}
```

### install snapsnare-cli
```shell
pip3 install git+https://github.com/janripke/snapsnare-cli.git@0.0.3#egg=snapsnare_cli
```

### run snapsnare-cli
```shell
$ snapsnare-cli
snapsnare-cli version 0.0.3
```


## Development installation
The snapsnare-cli uses the snapsnare-api rest server to communicatie with snapsnare.

### configure snapsnare-cli
The endpoint of the snapsnare-api rest server used by snapsnare-cli is stored on your local machine
To be more exact in ~/.snapsnare/snapsnare.json

In this example it is assumed that the snapsnare-api rest server is running on your localhost and uses port 5001
create the snapsnare.json file in ~/.snapsnare folder: paste the following into this file:
```python
{
  "snapsnare-api": {
    "endpoint": "http://localhost:5001"
  }
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


