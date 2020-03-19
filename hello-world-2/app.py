from chalice import Chalice

app = Chalice(app_name='hello-world-2')

@app.lambda_function()
def hello_world(event, context):
    msg = f"hello from {event['name']}"

    return msg

