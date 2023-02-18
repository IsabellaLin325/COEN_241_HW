import json
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    data = {
        "text": "Serverless Message",
        "attachments": [{
            "title": "Welcome to COEN 241",
            "fields": [{
                "title": "Follower",
                "value": "10000",
                "short": True
            }],
            "author_name": "Fangfang Lin",
            "author_icon": "",
            "image_url": "https://avatars.githubusercontent.com/u/93758181?s=400&v=4"
        },
        {
            "title": "Details about COEN 241",
            "text": "It's a course about cloud computing"
        },
        {
            "fallback": "Would you recommend COEN 241 to your friends?",
            "title": "Would you recommend COEN 241 to your friends?",
            "callback_id": "response123",
            "color": "#FF0000",
            "attachment_type": "default",
            "actions": [
                {
                    "name": "recommend",
                    "text": "Of Course!",
                    "type": "button",
                    "value": "recommend"
                },
                {
                    "name": "definitely",
                    "text": "Most Definitely!",
                    "type": "button",
                    "value": "definitely"
                }
            ]
        }]
    }
    return json.dumps(data)
