#testing managment commands 



from unittest.mock import patch

from Psycopg2 import OperationalError as Psycopg2Error
from django.core.management import call_command
from django.db.utils import OperationalError 
from django.test import SimpleTestCase 



@patch('core.managment.commands.wait_for_db.Command.check')
class CommandTest(SimpleTestCase):
    

    def test_wait_for_db_ready(self ,patched_ckeck):
        patched_ckeck.return_value = True 

        call_command('wait_for_db')

        patched_ckeck.assert_called_once_with(database=['default'])

        
        