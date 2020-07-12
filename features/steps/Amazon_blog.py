from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then

BLOG_LINK = (By.XPATH, "//a[contains(text(), 'blog.aboutamazon.com')]")
BLOG_HEADER = (By.CSS_SELECTOR, "h1.ArticlePage-headline")
BLOG_ICON = (By.CSS_SELECTOR, "div.ArticlePage-navigation a img[alt*='Day One Blog Image (White)']")
HAM_MENU = (By.CSS_SELECTOR, "button.ArticlePage-header-menuToggle")
POP_UP_MENU = (By.CSS_SELECTOR, "div.ArticlePage-navigation")
CLOSE_BUTTON = (By.CSS_SELECTOR, "button.ArticlePage-header-menuClose")

@when("Store original windows")
def store_windows(context):
    context.original_window = context.driver.current_window_handle
    context.original_windows = context.driver.window_handles
    print("context.original_window", context.original_window)
    print("original_windows", context.original_windows)


@when("Click on blog link 'See daily updates at blog.aboutamazon.com'")
def blog_link_click(context):
    context.driver.wait.until(EC.element_to_be_clickable(BLOG_LINK)).click()
    context.driver.wait.until(EC.new_window_is_opened)


@when("Switch to the newly opened window")
def switch_windows(context):
    current_windows = context.driver.window_handles

    size = len(current_windows)
    print(size)
    print(current_windows)
    for x in range(size):
        context.driver.switch_to.window(current_windows[x])
        print(context.driver.title)

    for old_window in context.original_windows:
        current_windows.remove(old_window)
    print('after remove',current_windows)
    context.driver.switch_to_window(current_windows[0])


@then("Verify that Amazon Blog window is opened")
def verify_blog_opened(context):
    text = context.driver.wait.until(EC.visibility_of_element_located(BLOG_HEADER)).text
    assert 'blog' in text, f'Expected to open Amazon Blog page, but get {text}'
    context.driver.find_element(*BLOG_ICON)


@then("User can open and close Blog menu")
def blog_menu(context):
    context.driver.find_element(*HAM_MENU).click()
    context.driver.find_element(*POP_UP_MENU)       #Popup menu is open
    context.driver.find_element(*CLOSE_BUTTON).click()
    context.driver.wait.until(EC.invisibility_of_element_located(POP_UP_MENU))


@then("User can close new window and switch back to original")
def go_back(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)



