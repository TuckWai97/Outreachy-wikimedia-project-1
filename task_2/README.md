# Addressing the Lusophone technological wishlist proposals - Task 2
## Objective of the task: Create a Python script to get and print the status code of the response of a list of URLs from a .csv file.

Your python code needs to get the urls from the file and print their status code in the following format:

`(STATUS CODE) URL`

e.g. `(200) https://www.nytimes.com/1999/07/04/sports/women-s-world-cup-sissi-of-brazil-has-right-stuff-with-left-foot.html`

### Setup on your local machine:
1. Clone using git clone from my repo (jump to next step if you already do it in Outreachy-wikimedia-project-1/task_1)
   ```bash
   git clone https://github.com/TuckWai97/Outreachy-wikimedia-project-1.git
   ```
2. Change directory to Outreachy-wikimedia-project-1/task_2
    ```bash
    cd Outreachy-wikimedia-project-1/task_2
    ```
3. Create a virtual environment to isolate project dependencies
   ```bash
   python -m venv env
   ```
4. Activate your virtual environment

   - For Windows
      - If use command.exe
        ```bash
        \env\Scripts\activate.bat
        ```
       - Powershell
         ```bash
          \env\Scripts\Activate.ps1
          ```
> 'env' is your previous created virtual environment name. *Note:* You can refer to documentation her for more detail: https://docs.python.org/3/tutorial/venv.html

5. Use pip to install requests library 
   ```
   python -m pip install requests
   ```
6. Run python script:
   ```
   python status_code_url.py
   ```

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

### Some findings and guesses:
- for `request.get`, if added with `timeout`, I attempted 10,15,20 , it will causes the url that started with `https://web.archive.org` to have `ReadTimeout` exception error instead of `200` as `(OK)` for status code due to insufficient time to complete the HTTP request, so I not using it, but according to 
-  `https://www.ussoccer.com/news/womens-national-team/2009/07/remembering-99-sissi.aspx` has `ConnectionError` instead of `404`- `(Not Found)` status code when running with the same code, which I verified it should be `404`-`(Not Found)` by browsing the website.
- For `https://www.socceramerica.com/publications/article/93014/california-storm-captures-fourth-wpsl-championship.html` from output,it is `ConnectionError` ,but when I browsing to the website , it can be viewed but just need to login using account.
- For `https://www.uefa.com/teamsandplayers/players/player=250107154/profile`, from one run, it was `502`-`(Bad Gateway)`status code, which is ***means that the server, while working as a gateway to get a response needed to handle the request, got an invalid response*** but I able to get `404` at my another run, which is quite weird to me.
- `https://www.corinthians.com.br/noticias/ver/60537`, it was observed as `Page not found` which should be `404` status code when loading the website using the url, but I got once as `ConnectionError` and another run as `403`-`(Forbidden)` status code, which is the ***client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource***.
- `https://avai.com.br/novo/julia-bianchi-dedicou-primeiro-gol-do-brasileirao-2020-ao-avo/`, it was observer as `Page not found` when browsing that should be `404`, but the output from code shown as `ConnectionError`.
- `https://dibradoras.com.br/2020/12/05/time-de-tradicao-no-feminino-avai-kindermann-tem-craques-formadas-em-casa/` is able to viewed via browser, but output from code is `406`, which is ***response is sent when the web server, after performing server-driven content negotiation, doesn't find any content that conforms to the criteria given by the user agent***.
- Majority of the url has status code `200`- `OK` as Successful response, followed by `403`- `(Forbidden)`, `404`- `(Not Found)` and `ConnectionError`.

### Code explanation:
instead of using str.format() method requires more manual effort,
#  "{}" to mark where a variable will be substituted and also need to provide information to be formatted
# for example line 40, "({}) {}.format(status_code, url)"
