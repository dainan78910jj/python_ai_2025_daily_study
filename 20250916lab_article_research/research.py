import os
from datetime import datetime
from pathlib import Path
from typing import Optional


def save_summary(summary_text: str, summaries_dir: Optional[str] = None, prefix: str = "summary") -> str:
    """
    Save the provided summary text into a timestamped file under a summaries directory.

    Args:
        summary_text: The content of the summary to be saved.
        summaries_dir: Directory where summary files will be stored. If None, uses "summaries" in project root.
        prefix: Filename prefix to help categorize summaries (default: "summary").

    Returns:
        The absolute path to the written summary file.
    """
    base_dir = summaries_dir or "summaries"
    base_path = Path(base_dir)
    base_path.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_prefix = "".join(c for c in prefix if c.isalnum()
                          or c in ("-", "_")).strip("-") or "summary"
    filename = f"{safe_prefix}_{timestamp}.txt"
    file_path = base_path / filename

    # Ensure we do not accidentally overwrite (shouldn't happen with timestamp, but double-guard)
    counter = 1
    while file_path.exists():
        filename = f"{safe_prefix}_{timestamp}_{counter}.txt"
        file_path = base_path / filename
        counter += 1

    file_path.write_text(summary_text, encoding="utf-8")
    return str(file_path.resolve())
