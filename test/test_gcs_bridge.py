import unittest
import ocs_bridge as ocs

class MyTestCase(unittest.TestCase):
    def test_basic(self):
        expected_value = 1234

        job_descr = ocs.get_JB_Type()
        job_id_nm = ocs.get_field()

        elem=ocs.lCreateElem(job_descr)

        ocs.lSetUlong(elem, job_id_nm, expected_value)
        value = ocs.lGetUlong(elem, job_id_nm)

        stdout = ocs.get_stdout()
        ocs.lWriteElemTo(elem, stdout)

        self.assertEqual(expected_value, value)


if __name__ == '__main__':
    unittest.main()
