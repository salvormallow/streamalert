"""
Copyright 2017-present, Airbnb Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from publishers.community.pagerduty.pagerduty_layout import AttachImage
from stream_alert.shared.publisher import Register


@Register
def v2_additional_fields(alert, publication):

    publication['@pagerduty-v2.severity'] = 'warning'
    publication['@pagerduty-v2.links'] = [
        {
            'href': 'https://streamalert.io',
            'text': 'Visit us on StreamAlert.io!',
            'badkey': 'asdf',
        }
    ]
    publication['@pagerduty-v2.images'] = [
        {
            'src': 'https://i.ytimg.com/vi/rTztN4OYSOk/maxresdefault.jpg',
            'alt': "You're freaking me out!",
            'href': 'https://github.com/airbnb/streamalert',
            'uzzdafa': 'dddss',
        }
    ]

    return publication


@Register
def v1_additional_fields(alert, publication):

    publication['@pagerduty.client_url'] = 'https://streamalert.io/en/stable/'
    publication['@pagerduty.contexts'] = [
        {
            'type': 'link',
            'href': 'https://streamalert.io/en/stable/architecture.html',
        },
        {
            'type': 'image',
            'src': 'https://streamalert.io/en/stable/_images/sa-complete-arch.png',
        }
    ]

    return publication


@Register
def incident_additional_fields(alert, publication):

    publication['@pagerduty-incident.incident_title'] = 'This is an Incident Title'
    publication['@pagerduty-incident.incident_body'] = 'This is an Incident body *&W$R)*WEYGF)*&HQER#*)QH#R)*&H#RO*H&RF)Q&GFH)*'
    publication['@pagerduty-incident.note'] = 'This is an Incident Note ========'
    publication['@pagerduty-incident.urgency'] = 'low'

    # - @ pagerduty - incident.incident_title
    # - @ pagerduty - incident.incident_body
    # - @ pagerduty - incident.note
    # - @ pagerduty - incident.urgency
    return publication


@Register
class AttachMeme(AttachImage):
    IMAGE_URL = 'https://i.ytimg.com/vi/rTztN4OYSOk/maxresdefault.jpg'
    IMAGE_CLICK_URL = 'https://github.com/airbnb/streamalert'
    IMAGE_ALT_TEXT = "You're freaking me out!"
