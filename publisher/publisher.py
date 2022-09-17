import boto3

client = boto3.client('events', region_name='us-east-1',
                      endpoint_url='http://localstack:4566',
                      aws_access_key_id='access_key',
                      aws_secret_access_key='secret_key',
                      aws_session_token='session_token')

response = client.put_events(
    Entries=[
        {
            'Source': 'publisher',
            'Resources': [
                'string',
            ],
            'DetailType': 'string',
            'Detail': 'string', # aca se define el mensaje en si (como str)
            'EventBusName': 'arn:aws:events:us-east-1:000000000000:event-bus/my-bus',
            'TraceHeader': 'string'
        },
    ]
)

print(f'----- {response}')
