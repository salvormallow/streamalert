#! /usr/bin/env python
"""Script to sort conf/logs.json schema file"""

import boto3
import logging
import datetime
import json
import socket
import sys
import time

logging.basicConfig()

# Change this to the name of your kinesis stream
KINESIS_STREAM = 'ryxias20190211_prod_stream_alert_kinesis'


class DummyKinesisEventSender(object):
    """
    Sends a dummy event to the provided Kinesis stream
    """

    def __init__(self):
        self._logger = logging.getLogger()
        self._logger.setLevel('INFO')

    def send_dummy_kinesis_event(self):
        self._logger.info('Sending test record to kinesis stream: {}'.format(KINESIS_STREAM))
        client = boto3.client('kinesis')
        response = client.put_records(
            Records=[
                {
                    'Data': json.dumps(self.data()),
                    'PartitionKey': 'partitionKeyFoo'
                },
            ],
            StreamName=KINESIS_STREAM
        )
        self._logger.debug(response)

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            self._logger.info('Success.')
        else:
            self._logger.info('ERROR!')

        self._logger.info('Done.')

    @staticmethod
    def data():
        # This is the record structure of
        SCRUBBED_RECORD = {
            "actor_ip": "1.80.44.222",
            "repo_id": 9001,
            "from": "pull_requests#merge",
            "created_at": 1552323464711,
            "org_id": "2",
            "actor": "pizza-toilet",
            "repo": "csirt/streamalert",
            "note": "",
            "actor_id": "9999",
            "org": "airbnb",
            "action": "protected_branch.policy_override",
            "user_id": "",
            "streamalert:envelope_keys": {
                "ident": "github_audit",
                "fluent_aggregator": "i-1234567890987",
                "pid": 0,
                "host": "git-musta-ch-primary",
                "fluent_tag": "rsyslog.local7.info",
                "fluent_event_time": "2019-03-11 09:57:44 +0000"
            },
            "data": {
                "reasons": [
                    {
                        "message": "Required status check \"buildkite/streamalert\" is expected.",
                        "code": "required_status_checks"
                    }
                ],
                "@timestamp": 1552323464711,
                "failures_json": "[{\"buildkite/streamalert\":\"expected\"}]",
                "request_category": "other",
                "actor_session": 12345,
                "overridden_codes": [
                    "required_status_checks"
                ],
                "before": "80870adebe89ad70ebf8a0ed870a9e87db09ae8d7b0a9ef8",
                "server_id": "0987a0ebd-a098eb7dae-79-eabd8a-e77087b7a0ebd",
                "areas_of_responsibility": [
                    "code_collab",
                    "pull_requests"
                ],
                "branch": "refs/heads/master",
                "policy": "adeab53fb5a3fb53fb5da53b5a35bda3b3d",
                "method": "POST",
                "dbconn": "github@127.0.0.1/github_enterprise",
                "after": "087409487aebdefbedbefb7a89ebfe7bd7ebfbe7f98e7bf0",
                "client_id": "0909309090908309.11233413513",
                "_document_id": "aj89we0fna4908ra43hor-O7w",
                "actor_location": {
                    "location": {
                        "lat": 0,
                        "lon": 0
                    }
                },
                "controller_action": "merge",
                "newsies_dbconn": "github@127.0.0.1/github_enterprise",
                "url": "https://git.musta.ch/csirt/streamalert/pull/999999/merge",
                "referrer": "https://git.musta.ch/csirt/streamalert/pull/999999",
                "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
                "request_id": "deadbeef-deadbeef-deadbeef-deadbeef-deadbeef"
            },
            "user": ""
        }
        return {
            'ryxias': 'e',
            'message': 'hello world!',
            'event_data': SCRUBBED_RECORD
        }

    @staticmethod
    def data_old():
        """Determines what data to send to the kinesis stream

        Feel free to override this data method with whatever"""
        return {
            # dont forget to update the schema if you change toplevel keys
            'ryxias': '',
            'message': 'Manually executed send_dummy_event_staging.py',
            'event_data': {
                'machine_name': socket.gethostname(),
                'timestamp': time.mktime(datetime.datetime.now().timetuple()),
                'cmd': {
                    'cmd': sys.argv[0],
                    'args': sys.argv,
                },
                'extra_data': {
                    'streamalert:normalization': {
                        'lorem': '''
Lorem ipsum dolor sit amet, albucius volutpat accusamus usu ne, suavitate adversarium at pri.
Mollis abhorreant deterruisset at sed, qui et choro audiam detracto. Legere cetero signiferumque
mel et, an nemore inimicus percipitur vis. At eam docendi reformidans, an duo clita mollis.

Pri ubique intellegat id. An sed aliquip eligendi deseruisse, vis ne modus verear qualisque.
Mel atqui animal vocibus ea, ea usu quis mucius. Mazim nominati definiebas vim eu. Inani regione
no pro, ut vis sale everti iisque, eam id labore eruditi voluptua.

Eum in dico accumsan erroribus, sea partem fabellas ne. Ea tota oratio fastidii mea, nonumy
laoreet euripidis et eam, mea prompta iracundia ei. Vim viris nihil maiestatis ei. Nec an zril
disputationi, constituam consectetuer quo ex, justo nusquam vel ne. Qui novum possit feugait cu.

Id ignota pertinacia eum, lobortis appellantur ei ius. Nam no viderer tacimates. Mea cu reque
explicari, no qui eirmod feugait. Ad oratio soluta sed, vis in latine iudicabit, ius ipsum quodsi
insolens no. Oratio primis consulatu an quo.

Blandit invidunt te qui, sit ea labores nostrum concludaturque, ius sint ignota mollis ne.
Et atqui vivendum mei. Ei mel insolens efficiantur, cu fabellas constituto vim. At purto
salutandi sit.
''',
                        'alignment': 'chaotic evil',
                        'reputation': '-1',
                        'class': 'paladin',
                        'race': 'gnork',
                        'weapon': 'daggerfish',
                    },
                    'streamalert:not_normalization': {
                        'you': 'sense a soul in search for answers',
                        'there': 'is no cow level',
                        'greed': 'is good',
                        'it': 'is a good day to die',
                        'or': 'is it?',
                    }
                },
            }
        }


if __name__ == "__main__":
    sorter = DummyKinesisEventSender()
    sorter.send_dummy_kinesis_event()
