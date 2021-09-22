import os
from re import sub
import subprocess
from . import config


def extractData(writeDirectory):
    """Extract contents using robocopy"""

    src_dir = config.cdDriveLetter + ":"
    contents_dir = os.path.join(writeDirectory, "objects")
    robocopy_log = os.path.join(writeDirectory, "metadata", "robocopy.log")
    robocopy_cmd = ["robocopy", src_dir, contents_dir, "/e", "/copy:DAT", "/dcopy:DAT", "/log:{}".format(robocopy_log), "/tee"]
    cmdStr = " ".join(robocopy_cmd)

    copy_result = subprocess.run(robocopy_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    if copy_result.returncode == 1:
        # robocopy returns 1 if new files were copied, so it is not an error
        status = 0
    else:
        status = copy_result.returncode

    dictOut = {}
    dictOut["cmdStr"] = cmdStr
    dictOut["status"] = status
    
    return dictOut
