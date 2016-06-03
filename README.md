# andandand

Python wsgi application that serves configured endpoints and does healthchecks on them, and returns appropriately.

## Usecase

Most loadbalancers let you have one endpoint for the healthcheck. But, you may have multiple applications, and want to put the node in and out of rotation.

You may have a check for:

* Main app
* Secondary app
* Basic file to know if I should be in the loadbalancer or not

If any of those fails, andandand returns a 500. If all succeed, 200.

## Usage

Setup your configuraion like this:
* endpoint/
* * app (newline separated list of urls, generally localhost-based)
* * otherapp (newline separated list of urls)
* otherapp/
* * app (newline separated list of urls)

Run andandand with uwsgi:

```
uwsgi --chdir2 example-configuration/ --http :8000 --wsgi-file andandand/wsgi.py --processes 4 --threads 2
```

And hit the endpoints at: `http://localhost:8000/healthcheck/(endpoint,otherendpoint)`

*Ideally, use chroot insead of chdir2 if you are root.*

## Nifty features

* It's simple.
* Doesn't need reloads for configuration changes.
