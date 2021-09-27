import json
import joblib

model = joblib.load('models/model.joblib')


def handler(event, context):
    print('request: {}'.format(json.dumps(event)))

    body = event.get("body")
    lambda_input = json.loads(body)
    result = model.predict([lambda_input])

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({'class': int(result[0])})
    }
