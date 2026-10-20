import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from artifact_receipt import confirm, digest


class ReceiptTests(unittest.TestCase):
    def setUp(self):
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.content = b"invented-input"
        self.artifact = self.directory / "artifact.bin"
        self.artifact.write_bytes(self.content)

    def run_confirmation(self, job="example-job"):
        return confirm(self.directory, job, digest(self.content))

    def test_missing_receipt_is_recovered(self):
        result = self.run_confirmation()
        self.assertEqual(result, json.loads((self.directory / "receipt.json").read_text()))
        self.assertEqual(self.content, self.artifact.read_bytes())

    def test_restart_is_repeat_safe(self):
        self.run_confirmation()
        receipt = self.directory / "receipt.json"
        before = (receipt.read_bytes(), receipt.stat().st_mtime_ns)
        self.run_confirmation()
        self.assertEqual(before, (receipt.read_bytes(), receipt.stat().st_mtime_ns))
        self.assertEqual(2, len(list(self.directory.iterdir())))

    def test_corrupt_artifact_blocks_even_with_receipt(self):
        self.run_confirmation()
        self.artifact.write_bytes(b"different")
        with self.assertRaises(ValueError):
            self.run_confirmation()

    def test_missing_artifact_blocks(self):
        self.artifact.unlink()
        with self.assertRaises(ValueError):
            self.run_confirmation()
        self.assertFalse((self.directory / "receipt.json").exists())

    def test_different_job_blocks_reuse(self):
        self.run_confirmation()
        with self.assertRaises(ValueError):
            self.run_confirmation("other-job")

    def test_damaged_receipt_blocks(self):
        (self.directory / "receipt.json").write_text("incomplete")
        with self.assertRaises(ValueError):
            self.run_confirmation()

    def test_stale_pending_receipt_is_replaced(self):
        (self.directory / "receipt.pending").write_text("incomplete")
        self.run_confirmation()
        self.assertFalse((self.directory / "receipt.pending").exists())


if __name__ == "__main__":
    unittest.main()
