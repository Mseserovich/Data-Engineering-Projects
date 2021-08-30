import unittest
from unittest.mock import patch

from sib_api_v3_sdk.api.transactional_emails_api import TransactionalEmailsApi
from send_inspiration.send_inspiration import TransactionalEmailsApi, send_email
from send_inspiration.send_inspiration import send_email
from sib_api_v3_sdk.rest import ApiException

class Api_Test(unittest.TestCase):
    @patch.object(TransactionalEmailsApi, 'send_transac_email', side_effect=ApiException)
    def test_sender(self, mocker):
        with self.assertRaises(ApiException):
            send_email()
            mocker.send_transac_email.call_count = 2
            mocker.send_transac_email.asser_called_once()
            mocker.send_transac_email.assert_called_once_with()

if __name__ == "__main__":
    unittest.main()
