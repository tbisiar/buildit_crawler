# buildit_crawler
A simple web crawler.  Given a domain url it should visit all pages within the domain, but not follow the links to external sites such as Google or Twitter

## Getting running
This application was build with python 3.8.1, to manage multiple python installations [pyenv](https://github.com/pyenv/pyenv) is suggested.  By default mac OSX uses python 2.7 so it is essential to make sure that the correct version is being used.

### pyenv setup
Install pyenv using homebrew:
`brew update && brew install pyenv`

Ensure pyenv has access to python 3.8.1
`pyenv install 3.8.1`

Verify python & pip versions:
`python --version` - should return `Python 3.8.1`
`pip --version` - should return something like `pip 20.0.2 from /Users/tbisiar/.pyenv/versions/3.8.1/lib/python3.8/site-packages/pip (python 3.8)`

### Running the tests
The tests can be run from the project base directory with the following command:
`python -m unittest test.crawler_test`

### Running the crawler
The crawler can be run via command line with the following argument to specify the domain to be crawled:
`python app.py -d "wiprodigital.com"`





## TODO
[x] Setup repo

[x] Build initial POC scraper for single site

[] Add tests

[] Expand scraper to follow same-domain links

[] Validate behavior and add more tests (may need to switch to selenium)

[] Dockerize

[] Async

[] Resiliancy

* memory & performance

* logging

* case sensitivity

[] Review and update README.md

[] Validate fresh checkout and run works as desired following README.md
