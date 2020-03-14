# import mock
from unittest.mock import patch
# import call command function
# to call command in source code
from django.core.management import call_command
# import operational error throws when database
# is unavailable and use error to simulate
# Database being available or not when run
# command
from django.db.utils import OperationalError
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """ Test waiting for db when db is availabe """
        # whenever this called during our test execution instead of performing
        # whatever behavior this does in django it will override it and just
        # and replace it with mock object which does two things
        # replace the return value
        # monitor how many times it was called
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """ Test Waiting For db """
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
