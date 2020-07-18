from behave import when, then

@when('Click on the Returns And Orders link')
def click_top_menu_item(context):
    context.app.top_nav_menu.click_on_returns_and_orders()

@then('Verify Sign In page is opened')
def verufy_signin_opened(context):
    context.app.sign_in_page.verify_email_field()