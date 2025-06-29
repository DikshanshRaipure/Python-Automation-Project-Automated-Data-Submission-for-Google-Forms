# Python-Automation-Project-Automated-Data-Submission-for-Google-Forms

## Google Form Auto-Filler Python Script
Hey! 👋
This project is a Python script I built to automate filling out Google Forms using data from a CSV file. It’s especially useful if you have a big list of entries and need to submit them all to a form that doesn’t require sign-in and allows unlimited responses.
### What Does It Do?
- Reads a test.csv file in the project folder, where each row is a set of answers you want to submit.
- Converts each row into a Python dictionary so it’s easy to work with programmatically.
- Uses Selenium (a Python tool for browser automation) to open Google Chrome and load the Google Form.
- For each entry in the CSV, the script automatically fills in all the form fields and submits the form.
- Repeats this process until all entries from your CSV are submitted—no manual copy-pasting needed!
### How Does It Work?
- The script uses the Pandas library to read and process the CSV data.
- Each column in your CSV matches a question in the Google Form.
- For every row, the script:
  - Opens the form in Chrome.
  - Fills each field using the correct XPath (the unique path to each form input).
  - Clicks the submit button.
  - Waits a bit, then moves on to the next entry.
- At the end, you can close the browser with a simple key press.
### Why Did I Build This?
I wanted to learn more about Python automation, especially how to handle real-world data and automate boring, repetitive tasks. This project helped me practice:
- Data manipulation with Pandas
- Web automation with Selenium
- Writing clean, reusable scripts for data-driven workflows
### Who Is This For?
Anyone who needs to bulk-submit data to a Google Form (like for surveys, registrations, or data collection) and wants to save time. You just need a CSV file with your data and a Google Form that’s open to all (no sign-in required).
Feel free to fork, use, or improve this script!
### Remember, you need to change the form link and all the XPATHS according to your use case
