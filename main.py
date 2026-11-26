"""The 3AM Commit Message bounty entry.

Competition: The 3AM Commit Message
Slug: u-kiencx-the-3am-commit-message-10bc7b35
"""

from pathlib import Path

ENTRY: str = (
    "revert 8 microservices and a raft cluster; realized I hardcoded "
    "'return False' in the mock I wrote to fix the mock I wrote at midnight"
)


def validate_entry(text: str = ENTRY) -> None:
    """Assert entry conforms strictly to competition gate rules."""
    assert isinstance(text, str), "Entry must be a string"
    assert 1 <= len(text) <= 139, (
        f"Entry length ({len(text)}) must be between 1 and 139 characters"
    )
    assert "\n" not in text, "Entry must not contain newline characters"
    assert "\r" not in text, "Entry must not contain carriage return characters"
    assert not text.isspace(), "Entry must not be only whitespace"
    assert text == text.strip(), "Entry must not contain leading or trailing whitespace"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as e:
        raise AssertionError("Entry must be valid UTF-8") from e


def write_entry(dest: Path = Path("/output/entry.txt")) -> Path:
    """Validate entry, create parent dirs, write entry with newline, and verify."""
    validate_entry(ENTRY)
    dest.parent.mkdir(parents=True, exist_ok=True)
    expected_content = f"{ENTRY}\n"
    dest.write_text(expected_content, encoding="utf-8")

    # Read back and assert exact match
    actual_content = dest.read_text(encoding="utf-8")
    assert actual_content == expected_content, (
        "Written file content does not match ENTRY with trailing newline"
    )
    return dest


def main() -> None:
    """Main entry point."""
    write_entry()


if __name__ == "__main__":
    main()
