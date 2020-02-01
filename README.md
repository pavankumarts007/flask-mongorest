# Flask- Mogo Loggger

the flask app consists of two apis 
* addlog - for creating log with source as compulsary field
* logs - for accessing log entries

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The application requires Python 3.x, PIP3, Virtualenv and MongoDb 

```
sudo apt install python3
pip install virtualenv
```

### Installing

A step by step series of examples that tell you how to get a development env running

Clone the application
```
git clone URL
```

create python virtualenv and install python packages

```
cd flask_mongorest
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

create settings.py pr copy settings_copy.py and alter the configs

```
cp settings_copy.py settings.py
```

## Running the tests

alter configs in settings.py for test environment
```
cd flask_mongorest
virtualenv env
source env/bin/activate
python app.py
python test.py
```


## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Python](https://www.python.org/) - Programming Language
* [mongoengine](http://mongoengine.org/) - The web framework used
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Microservice Web development lib


