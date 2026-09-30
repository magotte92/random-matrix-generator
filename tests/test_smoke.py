"""Smoke checks for the map generator. Stdlib only, so CI needs no app dependencies."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = set("0123456789,@\n")


class GeneratorSmokeTest(unittest.TestCase):
    def test_sources_compile(self):
        for name in ("new_map.py", "random_map_merger.py"):
            path = ROOT / name
            compile(path.read_text(encoding="utf-8"), str(path), "exec")

    def test_script_writes_aligned_maps(self):
        script = ROOT / "new_map.py"
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [sys.executable, str(script)],
                cwd=tmp,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(
                result.returncode,
                0,
                f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}",
            )

            mapper_path = Path(tmp) / "mapper.txt"
            setter_path = Path(tmp) / "setter.txt"
            self.assertTrue(mapper_path.is_file())
            self.assertTrue(setter_path.is_file())

            mapper_text = mapper_path.read_text(encoding="utf-8")
            setter_text = setter_path.read_text(encoding="utf-8")
            mapper_lines = mapper_text.splitlines()
            setter_lines = setter_text.splitlines()

            self.assertGreater(len(mapper_lines), 0)
            self.assertEqual(len(mapper_lines), len(setter_lines))
            self.assertIn("@", mapper_text)
            self.assertTrue(set(setter_text) <= ALLOWED)

            for raw, filled in zip(mapper_lines, setter_lines):
                raw_cells = [cell for cell in raw.split(",") if cell != ""]
                filled_cells = [cell for cell in filled.split(",") if cell != ""]
                self.assertGreaterEqual(len(filled_cells), len(raw_cells))


if __name__ == "__main__":
    unittest.main()
