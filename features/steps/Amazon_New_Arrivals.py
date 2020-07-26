from behave import when, then

@when('Hovering over New Arrivals')
def hover_over_new_arrivals(context):
    context.app.product_page.hover_over_new_arrivals()

@then('Verify the user sees the deals')
def verify_new_arrivals(context):
    context.app.product_page.verify_new_arrivals()


