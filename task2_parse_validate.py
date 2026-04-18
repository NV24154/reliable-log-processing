# Task 2 — Safe Parsing + Validation (Try/Except)

ALLOWED_LEVELS = {"INFO", "WARN", "ERROR"}

def parse_and_validate_line(line: str):
    """Return (timestamp, LEVEL, service, message) OR None."""
    try:
        # TODO: implement the rules from assignment
        # 1) strip line
        # 2) if empty -> None
        # 3) split by '|' and strip each field
        # 4) if len != 4 -> None
        # 5) reject empty fields
        # 6) normalize level to uppercase
        # 7) reject if level not allowed
        # 8) return tuple
        pass
    except Exception:
        return None

def main():
    tests = [
        "2026-02-05 08:11:20 | warn | api | Slow response",
        "BAD LINE WITHOUT SEPARATORS",
        "2026-02-05 08:11:22 | ERROR | db | DB timeout",
        "2026-02-05 08:11:23 | DEBUG | api | debug msg",
        "2026-02-05 08:11:24 | ERROR |  | missing service",
        "   ",
    ]

    for t in tests:
        print(t, "->", parse_and_validate_line(t))

if __name__ == "__main__":
    main()
