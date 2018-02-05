Setup instructions on Athena:

Clone website:
$ cd /mit/mitsss
$ git clone https://github.com/yuanchenyang/mitsss-website-static.git
$ cd mitsss-website-static

Set up virtualenv:
$ virtualenv -p python3 env
$ source env/bin/activate

Install dependencies:
$ pip3 install -r requirements.txt

Build website:
$ make html

Set up permissions for output directory:
$ add consult
$ fsr sa output system:anyuser rl
$ cd /mit/mitsss
$ ln -s mitsss-website-static/output/ www
$ fs sa www system:anyuser rl
