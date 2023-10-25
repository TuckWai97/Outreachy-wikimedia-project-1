# Addressing the Lusophone technological wishlist proposals - Task 1

## Objective of the task: Create a JavaScript script to manipulate a json object and print it in a human legible format.

Your javascript code needs to get the data from the data variable and print them into the HTML element with #results ID in the following format:

Article "ARTICLE TITLE" (Page ID PAGEID) was created at MONTH DAY, YEAR.

e.g. Article "André Baniwa" (Page ID 6682420) was created at September 12, 2021

### Setup on your local machine:
1. Clone using git clone from my repo
   ```bash
   git clone https://github.com/TuckWai97/Outreachy-wikimedia-project-1.git
   ```
2. Navigate to the `Outreachy-wikimedia-project-1/task_1` folder using file explorer, then double click on the `Task 1 - Intern.html` file, the html content will show up in a browser.

### How it works:

- `formatDate()` function is used to format the date using `toLocaleDateString` method by using `en-US` as `locale` parameter as it uses `month-day-year` order and customized using `options` parameter on `month`, `year` and `day`  to return the specific form of formatted date string.
- `displayData` function to display the final output.Inside the function, it uses the `forEach()` method to access the `data` array in `line 16 to 29`, it will be executed once to get the each element of `data` array in ascending index order and stores in `eachArticle`, literally it means **for each item(eachArticle) will store each line that with properties `page_Id`, `creation_date` and `title` that was in `data` array.**
  - for each time/loop, `outputText` will format the output in the form of `Article "ARTICLE TITLE" (Page ID PAGEID) was created at MONTH DAY, YEAR.` by using value inside placeholders, which are embedded expressions delimited by dollar sign and curly braces,`${}` and the whole string is wrapped with  backtick characters, "``" to create template literals for embed expressions and variables inside a string, which in this case, `title`, `page_id`, `formattedDate` value will subtitute to the placeholder,"${}" respectively.
 - Back to the main program, the `results` HTML ID with `resultElement` variable will have each paragraph element, `outputText` with format required as in the task ,printing it out by calling `displayData` function.
 
