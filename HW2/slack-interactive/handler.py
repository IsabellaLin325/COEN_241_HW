import json
import urllib
def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    # urlstring = urllib.unquote(req).decode('utf8').strip('payload=')
    # response = json.loads(urlstring)
    data = {
        "attachments": [
            {
                "replace_original": True,
                "response_type": "ephemeral",
                "fallback": "Required plain-text summary of the attachment.",
                "color": "#FFA500",
                "pretext": "Nice choice! Have fun with COEN 241!",
                "author_name": "Fanfang Lin",
                "author_link": "https://github.com/IsabellaLin325/COEN241",
                "author_icon": "https://avatars.githubusercontent.com/u/93758181?s=400&v=4",
                "title": "COEN 241",
                "title_link": 
"https://www.scu.edu/engineering/academic-programs/department-of-computer-engineering/graduate/course-descriptions/",
                "text": "Head over to COEN 241",
                "image_url": 
"https://www.scu.edu/media/offices/umc/scu-brand-guidelines/visual-identity-amp-photography/visual-identity-toolkit/logos-amp-seals/Mission-Dont3.png",
                "thumb_url": 
"https://www.scu.edu/engineering/academic-programs/department-of-computer-engineering/graduate/course-descriptions/",
                "footer": "Slack Apps built on OpenFaas",
                "footer_icon": "https://a.slack-edge.com/45901/marketing/img/_rebrand/meta/slack_hash_256.png",
                "ts": 123456789
            }
        ]
    }
    return json.dumps(data)
