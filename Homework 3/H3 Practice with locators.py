# 1. Find the most optimal locators for Create Account (Registration) page elements:

# Amazon link - "navigation icon"
# $x("//a[@class='a-link-nav-icon']")
# By.CSS_SELECTOR, "a.a-link-nav-icon"
# $$("a.a-link-nav-icon")

# Heading - "Create Account"
# $x("//h1[@class='a-spacing-small']")
# By.CSS_SELECTOR, "h1.a-spacing-small"
# $$("h1.a-spacing-small")

# Input Element - "Your name"
# $x("//input[@id='ap_customer_name']")
# By.ID, 'ap_customer_name'
# $$("#ap_customer_name")

# Input Element - "Email"
# $x("//input[@id='ap_email']")
# By.ID, 'ap_email'
# $$("#ap_email")

# Input Element - "Password"
# $x("//input[@id='ap_password']")
# By.ID, 'ap_password'
# $$("#ap_password")


# Input Element - "Reenter password"
# $x("//input[@id='ap_password_check']")
# By.ID, 'ap_password_check'
# $$("#ap_password_check")

# Input Element - "Create your Amazon account" button
# $x("//input[@id='continue']")
# By.ID, 'continue'
# $$("#continue")

# Link "Conditions of use"
# $x("//a[contains(@href, 'register_notification_condition_of_use')]")
# By.By.CSS_SELECTOR, "a[href*='register_notification_condition_of_use']"
# $$("a[href*='register_notification_condition_of_use']")

# Link "Privacy Notice"
# $x("//a[contains(@href, 'register_notification_privacy_notice')]")
# By.CSS_SELECTOR, "a[href*='register_notification_privacy_notice']"
# $$("a[href*='register_notification_privacy_notice']")

# link - "Sign-in page"
# $x("//a[@class='a-link-emphasis']")
# By.CSS_SELECTOR, "a.a-link-emphasis"
# $$("a.a-link-emphasis")