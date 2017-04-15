# upassAutomator
A Python Script to automate the renewal for U-Pass BC

The script automates the process of renewing U-Pass for SFU.  To automate that process, I use Windows Task Scheduler so that it runs the code in the background when my computer is on and is connected to the Internet.

(For UBC and other universities change the “sfu” string to corresponding university abbreviation based on the Upass website.)

The web-scraping API being used here is Selenium.  Note that to have a simulated browser open, you need a webdriver.  (For Google Chrome click here).  If you don’t want a web browser open, use PhantomJS webkit.
