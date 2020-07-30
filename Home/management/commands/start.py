import os
from django.core.management.commands import runserver

from logging import getLogger

from ledypi_remote.Home.views import init_firebasae

global FBC, ADDITIONAL_SETTINGS

django_logger=getLogger("django_logger")

class Command(runserver.Command):
    help = 'Displays current time'

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument('credential_path', type=str,
                            help='The path to the private key json file for Firebase')
        # Optional argument
        parser.add_argument('--databaseURL', type=str, nargs='?', default="https://ledypie.firebaseio.com/",
                            help='The Firebase database url')

        parser.add_argument('--debug', nargs='?',
                            help='If to start in debug mode')

    def handle(self, *args, **options):
        global FBC, ADDITIONAL_SETTINGS
        if os.environ.get('RUN_MAIN') != 'true':
            init_firebasae(options)
            django_logger.info("Initialized firebase")
        super(Command, self).handle(*args, **options)
