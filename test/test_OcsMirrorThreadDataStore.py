import time

import config
import unittest

import ocs.ocs_bridge as ocs

class OcsMirrorClientDataStoreTest(unittest.TestCase):
    def setUp(self):
        self.logger = config.logger
        self.sge_version = config.sge_version

    def test_start_stop(self):
        mirror_thread = ocs.MirrorClientDataStore()

        # Start the OcsMirrorClientDataStore thread
        mirror_thread.start()

        # let the thread run for 10 seconds
        time.sleep(10)

        # Stop the OcsMirrorClientDataStore thread
        mirror_thread.stop()
        mirror_thread.join()

if __name__ == '__main__':
    unittest.main()
