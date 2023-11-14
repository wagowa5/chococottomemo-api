import json
import requests

def lambda_handler(event, context):
    pagename = event['queryStringParameters']['pagename']

    response = requests.get(f"https://scrapbox.io/api/pages/chocottomemo-public/{pagename}")
    data = {}
    if response.status_code == 200:
        data_content = response.json()
        texts = [line['text'] for line in data_content['lines']]

        for text in texts:
            print(text)
        information = str('\n'.join(texts)).replace('\n\n','').replace('/icons/hr.icon','')

        is_not_found = False
    else:
        is_not_found = True
        information = ""
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'isNotFound': is_not_found,
            'information': information
        })
    }
