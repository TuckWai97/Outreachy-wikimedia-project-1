# Addressing the Lusophone technological wishlist proposals - Task 2
## Objective of the task: Create a Python script to get and print the status code of the response of a list of URLs from a .csv file.

Your python code needs to get the urls from the file and print their status code in the following format:

`(STATUS CODE) URL`

e.g. `(200) https://www.nytimes.com/1999/07/04/sports/women-s-world-cup-sissi-of-brazil-has-right-stuff-with-left-foot.html`

Instructions:



### Brief explanation:

There are 2 functions in the script:
1. `get_status_code` function is used to get response status code from HTTP request.
2. `catch_status_code_exception_error` function has `try` and `except` statement to handle the response status code exception in case the HTTP request is not successful with 4 exceptions from HTTP request library as below:
    - Connection Error
    - URLRequired
    - ReadTimout
    - TooManyRedirects

### How it works:      
-  Open the csv file in `r` read mode, using `reader` method from `csv` library to read the csv file, use `for` loop to iterate through each row of csv file and stores as list
   - for each row
      - assign index 0 as the url in csv file is in first column, calls `catch_status_code_exception_error` function which in turn will call `get_status_code` function to get status code and get a formatted string literal in format of `(status_code) url` , finally print out as output.

### Some findings:
- for `request.get`, if added with `timeout`, I attempted 10,15,20 , it will causes the url that started with `https://web.archive.org` to have `ReadTimeout` exception error instead of `200` as `OK` for status code due to insufficient time to complete the HTTP request, so I not using it, but according to 
-  `https://www.ussoccer.com/news/womens-national-team/2009/07/remembering-99-sissi.aspx` has `ConnectionError` instead of `404 Not Found` status code when running with the same code, which I verified it should be `404` by browsing the website.
- `https://www.socceramerica.com/publications/article/93014/california-storm-captures-fourth-wpsl-championship.html` I get `ConnectionError` ,but when I browsing to the website , it can be viewed but just need to login using account.
