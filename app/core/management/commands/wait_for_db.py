"""
this is a management command
it's a helper command that will allow django to wait
for database to be available before continuing
and runing other command
use this in docker compose file when starting django app
"""
# import time to make app sleep for a few seconds
import time
# import the connection module that test connection is available
from django.db import connections
from django.db.utils import OperationalError
# import base command the class to build custom command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ Django Command to pause execution until database is available """

    # handle Function ran whenever we run this management command
    def handle(self, *args, **options):
        # deplay msg in screen
        self.stdout.write('Waiting for database.....')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, Waiting 1 second..')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
