import unittest
import gcs_bridge as gcs

class MyTestCase(unittest.TestCase):
    def test_basic(self):
        expected_value = 1234

        job_descr = gcs.get_JB_Type()
        job_id_nm = gcs.get_field()

        elem=gcs.lCreateElem(job_descr)

        gcs.lSetUlong(elem, job_id_nm, expected_value)
        value = gcs.lGetUlong(elem, job_id_nm)

        stdout = gcs.get_stdout()
        gcs.lWriteElemTo(elem, stdout)

        self.assertEqual(expected_value, value)


if __name__ == '__main__':
    unittest.main()
