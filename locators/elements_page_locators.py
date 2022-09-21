

class TextBoxPageLocators:

    #form fields
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName-label']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail-label']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "input[id='currentAddress-label']")
    PERMANENT_ADRESS = (By.CSS_SELECTOR, "input[id='permanentAddress-label']")
    SUBMIT = (By.CSS_SELECTOR, "input[id='submit']")

    #created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, '#output #permanentAddress')