import os
from pathlib import Path
import tempfile

import update_allow_list


def test_remove_ips(tmp_path):
    allow = tmp_path / "allow.txt"
    remove = tmp_path / "remove.txt"
    allow.write_text("1.2.3.4\n5.6.7.8\n")
    remove.write_text("5.6.7.8\n")

    removed, remaining = update_allow_list.update_allow_list(allow, update_allow_list.read_list(remove), dry_run=False, backup=False)

    assert removed == ["5.6.7.8"]
    assert remaining == ["1.2.3.4"]
    assert allow.read_text().strip().splitlines() == ["1.2.3.4"]


def test_dry_run_no_change(tmp_path):
    allow = tmp_path / "allow2.txt"
    remove = tmp_path / "remove2.txt"
    allow.write_text("10.0.0.1\n")
    remove.write_text("203.0.113.1\n")

    removed, remaining = update_allow_list.update_allow_list(allow, update_allow_list.read_list(remove), dry_run=True, backup=False)

    assert removed == []
    assert remaining == ["10.0.0.1"]
