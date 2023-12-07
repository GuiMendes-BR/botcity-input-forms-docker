from botcity.web import By


class RpaChallengeLocators():
    """The RpaChallengeLocators class defines all locators from rpa challenge. Each locator has to be a tuple
    """
    b_input_forms = (By.XPATH, "//a[text() = 'Input Forms']")
    b_download_excel = (By.XPATH, "//a[text() = ' Download Excel ']")
    b_start = (By.XPATH, "//button[text()='Start']")
    i_first_name = (By.XPATH, "//label[text()='First Name']/../input")
    i_last_name = (By.XPATH, "//label[text()='Last Name']/../input")
    i_company_name = (By.XPATH, "//label[text()='Company Name']/../input")
    i_role_in_company = (By.XPATH, 
        "//label[text()='Role in Company']/../input")
    i_address = (By.XPATH, "//label[text()='Address']/../input")
    i_email = (By.XPATH, "//label[text()='Email']/../input")
    i_phone_number = (By.XPATH, "//label[text()='Phone Number']/../input")
    b_sumbit = (By.XPATH, "//input[@type='submit']")
