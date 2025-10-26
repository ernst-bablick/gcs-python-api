import config
import unittest

import ocs.ocs_bridge as ocs

class OcsVersionTest(unittest.TestCase):
    def setUp(self):
        self.logger = config.logger
        self.sge_version = config.sge_version

    def test_version(self):
        version = ocs.Version.get_version()
        version_as_hex_string = hex(version)

        self.logger.info(f"Internal version number: {version_as_hex_string}")
        # we expect a 32bit value: length is 0x followed by 8 digits => 10
        self.assertEqual(10, len(version_as_hex_string))

    def test_version_string(self):
        version = ocs.Version.get_version_string()

        self.logger.info(f"Version from inst_sge: {self.sge_version}")
        self.logger.info(f"Version from ocs.Version: {version}")

        self.assertEqual(self.sge_version, version)


    def test_version_major_minor_patch_suffix(self):
        major, minor, patch, suffix  = ocs.Version.get_version_token()

        self.logger.info(f"Major: {major} Minor: {minor} Patch: {patch} Suffix: {suffix}")

        composed_version = f"{major}.{minor}.{patch}{suffix}"
        self.assertEqual(self.sge_version, composed_version)

    def test_short_product_name(self):
        product_name = ocs.Version.get_short_product_name()
        self.logger.info(f"Short product name: {product_name}")
        self.assertEqual("GCS", product_name)

    def test_long_product_name(self):
        product_name = ocs.Version.get_long_product_name()
        self.logger.info(f"Long product name: {product_name}")
        self.assertEqual("Gridware Cluster Scheduler", product_name)


if __name__ == '__main__':
    unittest.main()
