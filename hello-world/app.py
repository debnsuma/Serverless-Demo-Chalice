def handler(event, context):
    name = event["name"] # This means we expect event to be a dictionary with "name" as one of the key
    msg = f"Thanks for joining this webinar {name}"

    return msg


