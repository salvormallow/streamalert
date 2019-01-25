import json

from stream_alert.shared.publisher import AlertPublisher, Register


@Register
class PublishWeirdly(AlertPublisher):
    def publish(self, alert, publication):
        return {
            'Alert Id': alert.alert_id,
            'Field 1': 'things',
            'Field 2': 'as',
            'record': alert.record,
        }


@Register
class CustomAwsSns(AlertPublisher):
    def publish(self, alert, publication):
        payload = json.dumps(publication, sort_keys=True, indent=2)
        return {
            'aws-sns.topic': 'This is a custom subject line!',
            'aws-sns.message': 'This is a custom body:\n\n---------------\n\n{}\n\n------------'.format(
                payload
            ),
        }


@Register
class CustomPagerDuty(AlertPublisher):
    def publish(self, alert, publication):
        return {
            'pagerduty.body': 'karjsfhawieufh',
            'is_whitelisted': True,
        }


@Register
def simple(alert, publication):
    return {}


@Register
def hydrate_random_data(alert, publication):

    publication['ipv4'] = '12.34.56.78'
    publication['macaddr'] = 'what:even:is:000:amac:444ddr'
    publication['gpg_key'] = 'AAAAA_biurghae984ty4ohljaefjawe;fjaefNOT-REALLY-A-KEY32474--'
    publication['password'] = 'aaabbbpassword12345$$$$_'
    publication['www'] = 'wwwwwwwwwww'

    return publication


@Register
def add_description(alert, publication):
    """Publisher that adds the alert.rule_description to the publication."""
    publication['description'] = alert.rule_description

    return publication


@Register
class ContextAsCustomDetails(AlertPublisher):

    def publish(self, alert, publication):
        #custom_details = 'Lorem ipsum bacon test-thing\nNewline garbage trashcan drivel\nNewline old line red line blue line\n????\n\n\n\n???'

        custom_details = '''
Does it support
natural newlines
in a heredoc?

Does it auto-interpolate
excessive\n\n\n
newline chars


Does it support
<p>Paragraph tags</p>

Break<br>Break?

<b>Bold?</b>

h1. Jira markdown title?

# Markdown title?

*Markdown bold?*

_Markdown Italics?_

<div>
  <span>HTML?</span>
</div>

<span style="color:red">Inline css?</span>
'''

        publication['@pagerduty.details'] = custom_details
        publication['@pagerduty-v2.custom_details'] = custom_details

        return publication
