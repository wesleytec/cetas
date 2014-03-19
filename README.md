cetas
=====

A animal database writen using Django.

Environment
-----------

This project uses [virtualenv](https://pypi.python.org/pypi/virtualenv) and to make your life easer I recomend you to use [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/).

Get code
--------

```
cd .virtualenvs/
git clone https://github.com/wesleytec/cetas.git
cd cetas
virtualenv .
workon cetas
```

After this initial project setup what you need to get start working in this
project next time is to execute:

```
workon cetas
cdvirtualenv
```

Requirements
------------

```
pip install -r requirements.txt
```

Configuration
-------------

Running development server
--------------------------

```
python manage.py runserver
```

Open your browser [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

Running tests
-------------

