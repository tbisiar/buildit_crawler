# buildit_crawler
A simple web crawler.

The crawler should be limited to one domain. Given a starting URL – say http://wiprodigital.com - it should visit all pages within the domain, but not follow the links to external sites such as Google or Twitter.

The output should be a simple structured site map (this does not need to be a traditional XML sitemap - just some sort of output to reflect what your crawler has discovered) showing links to other pages under the same domain, links to external URLs, and links to static content such as images for each respective page.

Please provide a README.md file that explains how to build, test, and run your solution. Also, detail anything further that you would like to achieve with more time.

Once done, please make your solution available on Github and forward the link. Where possible please include your commit history to provide visibility of your thinking and working practice.

What you need to share with us
* A working crawler as per requirements above
* A README.md explaining:
  * How to build and run your solution (including any required installations)
  * Reasoning and describe any trade offs
  * Explanation of what could be done with more time
* Project builds / runs / tests as per instruction


## Getting running
This application was build with python 3.8.1, to manage multiple python installations [pyenv](https://github.com/pyenv/pyenv) is suggested.  By default mac OSX uses python 2.7 so it is essential to make sure that the correct version is being used.

### pyenv setup
Install pyenv using homebrew:

    brew update && brew install pyenv

Ensure pyenv has access to python 3.8.1
    
    pyenv install 3.8.1

Verify python & pip versions (should return `Python 3.8.1`
 and `pip 20.0.2 from /Users/xxxxx/.pyenv/versions/3.8.1/lib/python3.8/site-packages/pip (python 3.8)`):

    python --version

    pip --version
    
### pip install
To run the application the python libraries must be installed locally:

    pip install -r requirements.txt


### Running the tests
The tests can be run from the project base directory with the following command:

    python -m unittest test.crawler_test

### Running the crawler
The crawler can be run via command line with the following argument to specify the domain to be crawled:

    python app.py -d "wiprodigital.com"





## TODO
[x] Setup repo

[x] Build initial POC scraper for single site

[] Expand scraper to follow same-domain links

[] Validate behavior and add more tests (may need to switch to selenium)

[] Dockerize

[] Flask endpoint/output

[] Async

[] Resiliancy

* memory & performance

  * Need datastore?

* logging

* case sensitivity

[] Review and update README.md

[] Validate fresh checkout and run works as desired following README.md
