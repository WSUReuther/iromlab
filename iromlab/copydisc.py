import os
import shutil
from . import config


def extractData(writeDirectory):
    """Extract contents using shutil"""

    contents_dir = os.path.join(writeDirectory, "objects")
    if os.path.exists(contents_dir):
        os.rmdir(contents_dir)

    try:
        shutil.copytree(config.cdDriveLetter + ":", contents_dir, symlinks=False, ignore=None)
        success = True
        reject = False
    except:
        success = False
        reject = True
    
    return success, reject