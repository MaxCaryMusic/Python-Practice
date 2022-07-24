import os
import sys

# Structure of project needs to be fixed to make this nicer
sys.path.append('.')
from password_manager import write_key

def test_write_key():
    """Test that key gets written"""

    if os.path.exists("./key.key"):
        os.remove("./key.key")

    write_key()

    assert os.path.exists("./key.key") == True