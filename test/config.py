import logging
import os
from pathlib import Path


def get_version_from_inst_sge():
    """
    Get the version of OCS/GCS from the inst_sge file
    :return: Version of OCS/GCS
    """
    file_path = Path(sge_root + "/inst_sge")
    with open(file_path, 'r') as file:
        for line in file:
            if 'SGE_VERSION' in line:
                return line.split('=')[1].strip().strip('"')
    return None


# OCS/GCS specific values
sge_root = os.getenv('SGE_ROOT')
sge_version = get_version_from_inst_sge()

# Default logger for the test suite
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("test_logger")
