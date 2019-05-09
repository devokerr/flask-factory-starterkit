# Flask Factory Design Pattern + Blueprints + Flask SQLAlchemy [![Scrutinizer Quality Score](https://scrutinizer-ci.com/g/devokerr/flask-factory-starterkit/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/devokerr/flask-factory-starterkit/?branch=master)
[![Scrutinizer Build Status](https://scrutinizer-ci.com/g/devokerr/flask-factory-starterkit/badges/build.png?b=master)](https://scrutinizer-ci.com/g/devokerr/flask-factory-starterkit/?branch=master)

Flask design factory pattern starterkit with blueprints and Flask SQLAlchemy
### Getting Start

First, clone the project:
```sh
$ git clone https://github.com/devokerr/flask-factory-starterkit <my-project>
$ cd <my-project>
```
### Installation

Then install dependencies and check that it works


```sh
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ chmod +x run.sh
```

### DataBase

After done the installation step, setup database for Flask-SQLAlchemy

Change `SQLALCHEMY_DATABASE_URI` in `config.py`:
``` python
import os
class Config(object):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root_password@localhost/database_name'
```
Project use `flask_migrate` package for database migrations. Use this for prepare `flask_migrate`
```sh
flask db init
```
For create or update database models in database use:
```sh
$ flask db migrate
```
### Development
To develop locally run with:
```sh
$ ./run.sh
```
### Todos

 - Write More!

License
----

MIT


