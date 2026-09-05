#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path


MAX_FILES = 5_000
MAX_BYTES = 1_000_000


def violations(root):
	output = subprocess.check_output(["git", "-C", str(root), "ls-files", "-z"])
	paths = [path for path in output.split(b"\0") if path]
	if len(paths) > MAX_FILES:
		raise RuntimeError(f"tracked file count {len(paths)} exceeds limit {MAX_FILES}")

	problems = []
	for raw_path in paths:
		relative = Path(raw_path.decode("utf-8", "surrogateescape"))
		data = (root / relative).read_bytes()
		if len(data) > MAX_BYTES or b"\0" in data:
			continue
		if b"\r" in data:
			problems.append(f"{relative.as_posix()}: contains CR bytes; normalize to LF")
		if data and not data.endswith(b"\n"):
			problems.append(f"{relative.as_posix()}: missing final newline")
	return problems


def main():
	root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
	try:
		problems = violations(root)
	except RuntimeError as error:
		print(error, file=sys.stderr)
		return 2
	if problems:
		print("Tracked text validation failed:", file=sys.stderr)
		for problem in problems:
			print(f"- {problem}", file=sys.stderr)
		return 1
	print("Tracked text validation passed.")
	return 0


if __name__ == "__main__":
	raise SystemExit(main())

