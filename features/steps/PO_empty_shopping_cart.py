from behave import when, then

@when('Amazon Shopping Cart Count has {number} items')
def verify_shopping_cart_is_empty(context, number):
    context.app.top_nav_menu.shopping_cart_counter(number)

@when('Click on Shopping Cart icon')
def click_cart_icon(context):
    context.app.top_nav_menu.click_shopping_cart()

@then('Verify that user can see {text}')
def verify_empty_cart(context, text):
    context.app.shopping_cart_page.verify_empty_cart_message(text)

