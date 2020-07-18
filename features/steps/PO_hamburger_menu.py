from behave import when, then

@when('Click on hamburger menu')
def click_ham_menu(context):
    context.app.top_nav_menu.click_h_m()

@when('Click on Amazon Music menu item')
def click_amazon_music(context):
    context.app.ham_menu_page.click_amazon_music()

@then('{number} menu items are present')
def verify_ammount_of_items(context, number):
    context.app.ham_menu_page.verify_menu_items(number)

