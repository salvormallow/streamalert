"""Detect StreamAlert deployment actions"""
import publishers.community.generic as generic
import publishers.community.pagerduty.pagerduty_layout as pagerduty
import publishers.custom.pagerduty as pagerduty_custom

from publishers.custom.ryxias import ContextAsCustomDetails

from publishers.community.slack import slack_layout as slack

from stream_alert.shared.rule import rule


@rule(
    logs=['ryxias:message', 'streamquery:version1'],
    outputs=[
        # 'aws-sns:ryxias',
        'slack:staging',
        # 'pagerduty:staging',
        # 'pagerduty-v2:staging',
        # 'pagerduty-incident:staging-2',
    ],
    publishers={
        'slack': [
            slack.Summary,
            slack.AttachRuleInfo,
            slack.AttachPublication,
            slack.AttachFullRecord
        ],
        # 'pagerduty-v2': [
        #     pagerduty.ShortenTitle,
        #     ContextAsCustomDetails
        # ],
        # 'pagerduty-incident': [
        #     generic.add_record,
        #     # generic.remove_streamalert_normalization,
        #     # generic.remove_fields,
        #     generic.enumerate_fields,
        #     pagerduty_layout.as_custom_details,
        #     pagerduty_layout.ShortenTitle,
        #     pagerduty_layout.incident_additional_fields
        # ],
    },
    context={
        'pagerduty-incident': {
            'assigned_user': 'derek.wang@airbnb.com',
            'incident_priority': 'P1',
            'note': 'there is no spoon'
        }
    },
)
def ryxias_alert_on_all_events(rec, context):
    """
    All events get logged for testing purposes. Use the python script to push stuff into kinesis.

    Author: Derek is a STUPID HUMAN
    Playbook: https://confluence.airbnb.biz/pages/viewpage.action?pageId=408617915
    """
    return True
