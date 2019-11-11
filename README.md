# Restrict Service

This repo contains a small service

The service is responible for restricting JSON documents based on rules regarding regional restrictions, sourceId's and premium subscriptions (entitlements).

## Running locally

```
$ git clone git@github.com:skivis/restrict_service.git
$ cd restrict_service
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Once the requirements are installed, run the server:

```
$ python manager.py runserver
```