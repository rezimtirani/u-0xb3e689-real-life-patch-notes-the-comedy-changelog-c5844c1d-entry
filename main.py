"""Real-life patch note entry.

Writes one funny one-line changelog entry for a bug in real life
to /output/entry.txt, in the terse register of a real release note.
"""

import os


PATCH_NOTE = "v4.2.0: fixed a bug where walking into a room deleted the reason you went in there."


def validate_entry(text):
    """Enforce the competition gate: 1-160 chars, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= 160:
        raise ValueError("entry must be 1 to 160 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def entry_text():
    """Return the patch note with any accidental whitespace stripped."""
    return validate_entry(PATCH_NOTE.strip())


def write_entry(path):
    """Write the entry to path, creating parent folders as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(entry_text())


if __name__ == "__main__":
    write_entry("/output/entry.txt")
