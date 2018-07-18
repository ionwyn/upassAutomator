# upassAutomator

The script automates the process of renewing U-Pass for SFU. 
An automated script run the automated process, in the Windows Task Scheduler. Every time the computer turns on, and internet connection is available, the script performs the auto-renewal.

Making the script Compatible for other Greater Vancouver universities (UBC)
1.  Replace the “sfu” string to corresponding university abbreviation based on the Upass website

# Technical-Toolkit:
1. Selenium-  Web-scraping API  

# Requirements:
1. Python installed on your device
2. Webdriver
  a) To have a simulated browser open. Check the link for chrome
  b) If you don’t want a web browser open, use PhantomJS webkit.
