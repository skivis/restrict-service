# Restrict Service

This repo contains a small service

The service is responible for restricting JSON documents based on rules regarding regional restrictions, source_ids and premium subscriptions d.

## Running locally

```
$ git clone git@github.com:skivis/restrict_service.git
$ cd restrict_service
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Once the requirements are installed, run the server:

```
$ python manager.py runserver
```