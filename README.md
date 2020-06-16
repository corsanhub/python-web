# python-web
Simple Python HTTP server

## Description
*python-Web* is a simple web server created in Bash & Python, which provides static content originating from a directory within the **file system**. Meaning, publishing the directory content.

## Getting started
For getting python-web example working, just clone the project like this:
```
git clone https://github.com/corsanhub/python-web.git
```
Then you must change to the directory python-web
```
cd python-web
```

The project contains two simple web sites namely: site1 and site2. There is one directory per site in the project.

Each site is composed by:
* An html web page
* A javascript file
* An image used for the background
* A favicon 

## Start server
For starting one of the included examples you should run the start command providing the directory name to be served and a port where the content will be published.

Eg.
```
bin/start site1 6080

bin/start site2 6090
```

*Note:* During http server execution, standard output is redirected to the nohup.out file

To see it, run this command:
```
tail -f nohup.out
```

## Navigating sites
Running sites can be seen in a browser using next url's:

[link to site1!](http://localhost:6080)

[link to site2!](http://localhost:6090)

*Note:* When starting a server, files and directories contained can be browsed and seen as they are in the file system Eg.

[link to files in site1!](http://localhost:6080/files/)

[link to files in site2!](http://localhost:6090/files/)

## Stop server
For stopping a running site run the stop command providing the directory name to be served and a port where the content is currently published.

Eg.
```
bin/stop site1 6080

bin/stop site2 6090
```

## Query for running sites
Current running sites can be retrieved runnig next command:
```
bin/list
```