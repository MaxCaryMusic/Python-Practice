import os
import sys

from lib.crypto_utils import init_key
from lib.crypto_utils import check_db
from lib.hash_utils import create_master_password
from lib.hash_utils import check_master_password
from lib.hash_utils import init_master_password

# Structure of project needs to be fixed to make this nicer
sys.path.append('.')

def test_init_key():
    """Test that key gets written"""

    if os.path.exists("./key.key"):
        os.remove("./key.key")

    init_key()

    assert os.path.exists("./key.key") == True