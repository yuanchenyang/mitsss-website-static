# Setup instructions on Athena (first build)

Clone website:
```
$ cd /mit/mitsss
$ git clone https://github.com/yuanchenyang/mitsss-website-static.git
$ cd mitsss-website-static
```

Set up virtualenv:
```
$ virtualenv -p python3 env
$ source env/bin/activate
```

Install dependencies:
```
$ pip3 install -r requirements.txt
```

Build website:
```
$ make html
```

Set up permissions for output directory:
```
$ add consult
$ fsr sa output system:anyuser rl
$ cd /mit/mitsss
$ ln -s mitsss-website-static/output/ www
$ fs sa www system:anyuser rl
```

# To rebuild after pushing new changes to github
```
$ cd /mit/mitsss/mitsss-website-static
$ git pull
$ source env/bin/activate
$ make html
```
