from behave import when, then

@when('Hover over Add To Cart button')
def hover_add_to_cart(context):
    context.app.product_page.hover_add_to_cart()

@then('Verify size selection tooltip is shown')
def verify_size_tooltip(context):
    context.app.product_page.verify_size_tooltip()