import boto3
import datetime

client = boto3.client('events')

response = client.put_events(
    Entries=[
        {
            'Time': datetime(2015, 1, 1),
            'Source': 'string',
            'Resources': [
                'string',
            ],
            'DetailType': 'string',
            'Detail': 'string',
            'EventBusName': 'string',
            'TraceHeader': 'string'
        },
    ],
    EndpointId='string'
)
