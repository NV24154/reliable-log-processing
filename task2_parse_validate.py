# Task 2 — Safe Parsing + Validation (Try/Except)

ALLOWED_LEVELS = {"INFO", "WARN", "ERROR"}

def parse_and_validate_line(line: str):
    """Return (timestamp, LEVEL, service, message) OR None."""
    try:
        s = line.strip()
        if s == "":
            return None

        parts = [p.strip() for p in s.split("|")]
        if len(parts) != 4:
            return None

        ts, level, svc, msg = parts
        if ts == "" or level == "" or svc == "" or msg == "":
            return None

        level_norm = level.upper()
        if level_norm not in ALLOWED_LEVELS:
            return None

        return (ts, level_norm, svc, msg)
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

