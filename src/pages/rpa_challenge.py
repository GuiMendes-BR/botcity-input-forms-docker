from pages.base_page import BasePage
from locators.rpa_challenge_locators import RpaChallengeLocators
from botcity.plugins.files import BotFilesPlugin
from botcity.plugins.excel import BotExcelPlugin
from pandas import DataFrame, Series
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import subprocess

from selenium import webdriver

from time import sleep

import os
import shutil

from settings.config import config

import logging
logger = logging.getLogger(__name__)

class RpaChallengePage(BasePage):
    def __init__(self, bot):
        super().__init__(bot)
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--headless=new')
        # WINDOW_SIZE = "1280,800",
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')
        # chrome_options.add_argument('--disable-gpu')
        # chrome_options.add_argument('--remote-debugging-port=9222')
        # chrome_options.add_argument("--window-size=1920,1080")
        
        # self.bot.options = chrome_options
        # self.bot.start_browser()
        # self.bot.browse(str(config.rpa_challenge_url))
        # os.system("export DISPLAY=$HOST_IP:99")
        # self.driver = Driver(uc=True, browser='chrome', headed=True, no_sandbox=True)

        #option = webdriver.ChromeOptions()
        #self.driver = webdriver.Chrome(options = option)
        
        # ## use the following where appropriate within your loop
        # with open("ss.txt", "w") as outfile:
        #     subprocess.call("top -n1", shell=True, stdout=outfile)
            
        # with open("ss.txt", "r") as outfile:
        #     print(outfile.read())
        
        # sleep(60)
        
        # ## use the following where appropriate within your loop
        # with open("zzz.txt", "w") as outfile:
        #     subprocess.call("top -n1", shell=True, stdout=outfile)
            
        # with open("zzz.txt", "r") as outfile:
        #     print(outfile.read())
        
        
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
        self.driver.get(str(config.rpa_challenge_url))
        

    def select_challenge(self) -> None:
        """This function selects the current challenge
        """ 
        logger.info("Clicking on Input Forms...")
        self.click(RpaChallengeLocators.b_input_forms)

    def _clean_downloads_folder(self) -> None:
        """This function deletes the download folder and then creates it again
        """
        logger.info("Cleaning downloads folder...")
        folder = config.downloads_folder

        if os.path.exists(folder):
            logger.debug(f"Removing folder {folder}")
            shutil.rmtree(folder)
        os.makedirs(folder)
        

    def download_file(self) -> DataFrame:
        """This function downloads the excel file from the challange and returns it as a DataFrame

        Returns:
            DataFrame: DataFrame containing the content of the excel file
        """
        logger.info("Starting file download...")
        self._clean_downloads_folder()

        files_plugin = BotFilesPlugin()
        excel_plugin = BotExcelPlugin()

        with files_plugin.wait_for_file(directory_path=config.downloads_folder, file_extension=".xlsx", timeout=300000):
            logger.info("Clicking on download file...")
            self.click(RpaChallengeLocators.b_download_excel)
            logger.info("Waiting download finish...")
        file = files_plugin.get_last_created_file(
            directory_path=config.downloads_folder, file_extension=".xlsx")

        excel_plugin.read(file)

        # Convert the excel file to dataframe and set the first line as columns
        df = excel_plugin.as_dataframe()
        df.columns = df.iloc[0]
        return df[1:]

    def start_challenge(self) -> None:
        """This function starts the challenge timer
        """
        logger.info("Starting challenge...")
        self.click(RpaChallengeLocators.b_start)

    def fill_in_user(self, row: Series) -> None:
        """This function inserts one user in the RpaChallenge

        Args:
            row (Series): Row containing the user data (can be used when looping the DataFrame)
        """
        logger.info(f"Filling in user {row['First Name']} {row['Last Name ']}")
        self.send_keys(RpaChallengeLocators.i_first_name, row["First Name"])
        self.send_keys(RpaChallengeLocators.i_last_name, row["Last Name "])
        self.send_keys(RpaChallengeLocators.i_company_name,
                       row["Company Name"])
        self.send_keys(RpaChallengeLocators.i_role_in_company,
                       row["Role in Company"])
        self.send_keys(RpaChallengeLocators.i_address, row["Address"])
        self.send_keys(RpaChallengeLocators.i_email, row["Email"])
        self.send_keys(RpaChallengeLocators.i_phone_number,
                       row["Phone Number"])

        self.click(RpaChallengeLocators.b_sumbit)
