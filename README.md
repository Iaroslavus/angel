Python 3.5.2




Install virtual frame buffer:
::
    $ sudo apt-get install xvfb
    $ sudo apt-get install chromium-browser

Get appropriate version of chrome driver from: http://chromedriver.storage.googleapis.com/index.html

Unzip the chromedriver.zip

Move the file to /usr/bin directory
::
    $ sudo mv chromedriver /usr/bin
Goto /usr/bin directory and you would need to run
::
    $ cd /
    $ cd /usr/bin
    $ chmod a+x chromedriver


Create virtual environment for project
::
    $ virtualenv -p python3 angel_env
    $ . ./angel_env/bin/activate


Install python libs to virtual environment
::
    (angel_env)$ cd facebook
    (angel_env)$ pip install -r requirements.txt


Before run script You need to set a "config.json" file with your email and password for correct login.
::
    (angel_env)$ cp config.json.example config.json

and add your auth-data
::
    {
        "email": "YOUREMAIL",
        "pass": "YOURPASSWORD"
    }

Run script
::
    (angel_env)$ python inbound.py
