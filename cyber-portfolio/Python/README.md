# update_allow_list.py

Small utility to update an allow-list file by removing IP addresses present in a remove-list.

Usage examples:

Dry run (no changes):
```
python update_allow_list.py --allow-file allow_list.txt --remove-file remove_list.txt --dry-run
```

Perform the change (creates a timestamped backup by default):
```
python update_allow_list.py --allow-file allow_list.txt --remove-file remove_list.txt
```

Skip backup:
```
python update_allow_list.py --allow-file allow_list.txt --remove-file remove_list.txt --no-backup
```

The script ignores blank lines and lines starting with `#` in both files.
