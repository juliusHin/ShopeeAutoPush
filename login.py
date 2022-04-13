from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Imports for general selenium functionality.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


import time
import getpass
import datetime
import os
import sys
import platform

driver = webdriver.Chrome(ChromeDriverManager().install())

