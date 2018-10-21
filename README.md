# Flask, Travis and Heroku example

Small project developing a python Flask server and automatically testing it on Travis-IC and deploying to Heroku only if passing the tests.

## Build status

[![Build Status](https://travis-ci.org/gomezportillo/de0acloud.svg?branch=master)](https://travis-ci.org/gomezportillo/de0acloud)

## Heroku URL

[https://de0acloud.herokuapp.com/](https://de0acloud.herokuapp.com/)

If its down just wait ~20 seconds for the heroku dynos to wake up.

## Small dev tutorial

* Install dependecies (in this case just flask) and output them to [requirements.txt](requrements.txt) file
<details>

```bash
pip3 install flask
pip3 freeze | grep "Flask" > requirements.txt
```
</details>

* Write [server.py](server.py) and [test.py](test.py) and make sure it passes the tests
<details>

```bash
python3 test.py
```
</details>

* Create [travis](.travis.yml) config file with the appropriate information about the tests and commit to repo
<details>

```yaml
language: python
python:
  - '3.5'
install:
  - pip3 install -r requirements.txt
script:
  - python3 test.py
```
</details>

* Go to [travis-ci.org](hhttps://travis-ci.org/) and [heroku.com](https://heroku.com/) and sync repo on both sites
<details>

Now you can add the travis _build status_ lab to the readme
</details>

* Install `travis` and `heroku` CLI
<details>

```bash
apt-get install ruby && gem install travis
snap install --classic heroku
```
</details>

* Login in both services
<details>

```bash
heroku login
travis login
```
</details>

* Generate Heroku authentication token, encrypt it with Travis and automatically write it down on [travis](.travis.yml) config file and complete it
<details>

```bash
travis encrypt $(heroku auth:token) --add deploy.api_key
```
</details>

* Ensure there is at least one [dynos](https://www.heroku.com/dynos) assigned to heroku app
<details>

```bash
heroku ps:scale web=1 --app de0acloud
```
</details>

* Commit, push and it's done! Now it should go through travis tests and automatically be deployed on heroku if passing
