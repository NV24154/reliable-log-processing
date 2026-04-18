# Task 1 — Safe File Reading (Try/Except)

from pathlib import Path

def read_lines_safe(path: str) -> list[str]:
    # TODO:
    # - try to read text (utf-8)
    # - FileNotFoundError -> print clear message and return []
    # - any other Exception -> print error and return []
    pass

def main():
    # Test 1: missing file
    missing = read_lines_safe("this_file_does_not_exist.txt")
    print("Missing file lines:", len(missing))

    # Test 2: existing file
    existing = read_lines_safe("sample_logs_exception.txt")
    print("Existing file lines:", len(existing))

if __name__ == "__main__":
    main()
