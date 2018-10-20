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
<p>
```bash
pip3 install flask
pip3 freeze > requirements.txt
```

</p>
</details>

* Write [server.py](server.py) and [test.py](test.py) and make sure it passes the tests
<details>
<p>
```bash
python3 test.py
```

</p>
</details>

* Create [travis](.travis.yml) config file with the appropriate information about the tests and commit to repo
<details>
<p>
```yaml
language: python
python:
  - '3.5'
install:
  - pip3 install -r requirements.txt
script:
  - python3 test.py
```

</p>
</details>

* Go to [travis-ci.org](hhttps://travis-ci.org/) and [heroku.com](https://heroku.com/) and sync repo on both sites
<details>
<p>
Now you can add the travis _build status_ lab to the readme

</p>
</details>

* Install `travis` and `heroku` CLI
<details>
<p>
```bash
apt-get install ruby && gem install travis
snap install --classic heroku
```

</p>
</details>

* Login in both services
<details>
<p>
```bash
heroku login
travis login
```

</p>
</details>

* Generate Heroku authentication token, encrypt it with Travis and automatically write it down on [travis](.travis.yml) config file and complete it
<details>
<p>
```bash
travis encrypt $(heroku auth:token) --add deploy.api_key
```

</p>
</details>

* Ensure there is at least one [dynos](https://www.heroku.com/dynos) assigned to heroku app
<details>
<p>
```bash
heroku ps:scale web=1 --app de0acloud
```

</p>
</details>

* Commit, push and it's done! Now it should go through travis tests and automatically be deployed on heroku if passing
