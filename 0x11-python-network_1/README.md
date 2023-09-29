# Python - Network #1

This project involved learning how to use the ```urllib``` and requests Python libraries to send and receive HTTP messages to URL's. I practiced sending ```GET``` and ```POST``` ```requests```, fetching ```JSON``` resources, and interacting with API's (the Star Wars API, GitHub API, and Twitter API).
AOA
## Resources
**Read or watch:**

+ [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
+ [Quickstart with Requests package](https://requests.readthedocs.io/en/latest/)
+ [Requests package](https://pypi.org/project/requests/)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
+ How to fetch internet resources with the Python package ```urllib```
+ How to decode ```urllib``` body response
+ How to use the Python package ```requests``` #requestsiswaysimplerthanurllib
+ How to make HTTP ```GET``` request
+ How to make HTTP ```POST/PUT/etc.``` request
+ How to fetch JSON resources
+ How to manipulate data from an external service


## General

+ Allowed editors: ```vi```, ```vim```, ```emacs```
+ All your files will be interpreted/compiled on ```Ubuntu 20.04``` LTS using ```python3 (version 3.8.5)```
+ All your files should end with a new line
+ The first line of all your files should be exactly ```#!/usr/bin/python3```
+ A ```README.md``` file at the root of the repo, containing a description of the repository
+ A ```README.md``` file, at the root of the folder of this project, is mandatory
+ Your code should use the ```pycodestyle (version 2.8.*)```
+ All your files must be executable
+ The length of your files will be tested using ```wc```
+ All your modules should have a documentation ```(python3 -c 'print(__import__("my_module").__doc__)')```
+ You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
+ A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
+ Your code should not be executed when imported ```(by using if __name__ == "__main__":)```


## Tasks 📃

* 0. What's my status? #0

	* 0-hbtn_status.py: Python script that fetches https://intranet.hbtn.io/status.
		* Uses urllib.

* 1. Response header value #0

	* 1-hbtn_header.py: Python script that displays the X-Request-Id response header variable of a request to a given URL.
		* Usage: ./1-hbtn_header.py <URL>
    		* Uses urllib.
* 2. POST an email #0

	* 2-post_email.py: Python script that sends a POST request to a given URL with a given email, and displays the response body.
		* Usage: ./2-post_email.py <URL> <email>.
		* Uses urllib.
* 3. Error code #0

	* 3-error_code.py: Python script sends a request to a given URL and displays the response body.
		* Handles HTTP errors.
		* Uses urllib.
* 4. What's my status? #1

	* 4-hbtn_status.py: Python script that fetches https://intranet.hbtn.io/status.
		* Uses requests.
* 5. Response header value #1

	* 5-hbtn_header.py: Python script that displays the X-Request-Id response header variable of a request to a given URL.
		* Usage: ./5-hbtn_header.py <URL>
 		* Uses requests.
* 6. POST an email #1

	* 6-post_email.py: Python script that sends a POST request to a given URL with a given email, and displays the response body.
		* Usage: ./6-post_email.py <URL> <email>.
		* Uses requests.
* 7. Error code #1

	* 7-error_code.py: Python script sends a request to a given URL and displays the response body.
		* Handles HTTP errors.
		* Uses requests.
* 8. Search API

	* 8-json_api.py: Python script that sends a POST request to http://0.0.0.0:5000/search_user with a letter passed as parameter.
		* Usage: ./8-json_api.py <letter>
		* The letter is sent as the value of the variable q.
		* If no letter is given, sets q="".
		* If the response body is properly formatted and non-empty, displays it as [<id>] <name>.
		* Uses requests.
* 10. My Github!

	* 10-my_github.py: Python script that takes GitHub credentials (username and password) and uses the Github API to display the corresponding ID.
		* Usage: ./10-my_github.py <username> <password>
		* Uses requests.
