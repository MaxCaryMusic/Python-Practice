import os
import pathlib

from password_manager import write_key

def test_write_key():
    """Test that key gets written"""
    parent_dir = pathlib.Path(__file__).parent

    if os.path.exists(f"{parent_dir}/key.key"):
        os.remove(f"{parent_dir}/key.key")

    write_key()

    assert os.path.exists(f"{parent_dir}/key.key") == True