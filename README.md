snapsnare-cli
=

snapsnare-cli, this project, is a commandline tool to interact with snapsnare.

# Table of contents:

* Remarks
* Getting started
* General installation
* Development installation

# Remarks
snapsnare-cli currently supports Python 3.5 and higher.

# Getting started
The snapsnare-cli commandline tool uses the snapsnare-api rest server to interact with snapsnare.
The following commands are available
* jamulus:jammers
* icecast:status

## jamulus:jammers
Retrieves the active jammers in the Jamulus server and stores the result in snapsnare.
In order to retrieve the jammers you need to run this command on the server where the Jamulus server is installed.

Execute the following command to retrieve the active jammers:
```shell
$ snapsnare-cli jamulus:jammers --username admin --password admin --htmlstatus /home/jamulus/status.html
```

options:
- --username, the username to access snapsnare through the snapsnare-api
- --password, the password to access snapsnare
- --htmlstatus, the path to the jamulus html status file


## icecast:status
Retieves the status of the icecast server and stores the result in snapsnare

Execute the following command to retrieve the status of the icecast server:
```shell
$ snapsnare-cli icecast:status --username admin --password admin 
```

options:
- --username, the username to access snapsnare through the snapsnare-api
- --password, the password to access snapsnare


# General installation
The snapsnare-cli uses the snapsnare-api rest server to communicatie with snapsnare.

## configure snapsnare
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

## install snapsnare-cli
```shell
pip3 install git+https://github.com/janripke/snapsnare-cli.git@0.0.3#egg=snapsnare_cli
```

## run snapsnare-cli
```shell
$ snapsnare-cli
snapsnare-cli version 0.0.3
```


# Development installation
The snapsnare-cli uses the snapsnare-api rest server to communicatie with snapsnare.

## configure snapsnare-cli
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

## clone snapsnare-cli
```
git clone https://github.com/janripke/snapsnare-cli.git
```

## run snapsnare-cli
```shell
python3 snapsnare_cli/snapsnare_cli.py
```

## setup snapsnare-cli for development
```shell
$ python3 setup.py develop
```
