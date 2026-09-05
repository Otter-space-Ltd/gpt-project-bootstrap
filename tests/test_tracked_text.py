import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
SPEC = importlib.util.spec_from_file_location(
	"tracked_text", ROOT / "scripts" / "check_tracked_text.py"
)
CHECKER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECKER)


class TrackedTextTests(unittest.TestCase):
	def setUp(self):
		self.temporary_directory = tempfile.TemporaryDirectory()
		self.root = Path(self.temporary_directory.name)
		subprocess.run(["git", "init", "--quiet", str(self.root)], check=True)

	def tearDown(self):
		self.temporary_directory.cleanup()

	def track(self, name, content):
		path = self.root / name
		path.write_bytes(content)
		subprocess.run(["git", "-C", str(self.root), "add", name], check=True)

	def test_accepts_lf_text_and_excludes_binary(self):
		self.track("good.txt", b"good\n")
		self.track("asset.bin", b"\x00binary\r\n")
		self.assertEqual(CHECKER.violations(self.root), [])

	def test_reports_crlf_and_missing_final_newline(self):
		self.track("crlf.txt", b"bad\r\n")
		self.track("unfinished.txt", b"unfinished")
		self.assertEqual(
			CHECKER.violations(self.root),
			[
				"crlf.txt: contains CR bytes; normalize to LF",
				"unfinished.txt: missing final newline",
			],
		)

	def test_bounds_tracked_file_count(self):
		original_limit = CHECKER.MAX_FILES
		self.addCleanup(setattr, CHECKER, "MAX_FILES", original_limit)
		CHECKER.MAX_FILES = 1
		self.track("one.txt", b"one\n")
		self.track("two.txt", b"two\n")
		with self.assertRaisesRegex(RuntimeError, "exceeds limit"):
			CHECKER.violations(self.root)


if __name__ == "__main__":
	unittest.main()

