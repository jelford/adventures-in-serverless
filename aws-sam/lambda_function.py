import json
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info(f'Received request: {json.dumps(event)}')
    logger.info(f'Event: {event}')

    e = event or {}
    qsp = e.get('queryStringParameters') or {}
    name = qsp.get('name') or 'you'

    return {
            'body': json.dumps({'hello': name}),
            'statusCode': 200,
            'headers': {},
            }
