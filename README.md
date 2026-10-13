
# Assignment: Shopping List Manager

This project practices Python lists, list operations, membership checks, loops, and generating reports.

## Project Files

- `list_warmup.py` — Practices creating lists, accessing items by index, adding and removing items, and checking membership.
- `shopping_list.py` — Provides an interactive menu to add, remove, and view shopping list items.
- `list_report.py` — Generates a report showing all items, unique items, and duplicate entries.

## Why Check `in` Before Calling `.remove()`?

Checking whether an item exists in a list before calling `.remove()` makes the program safer and more reliable. If the item does not exist, `.remove()` raises a `ValueError`, which can stop the program unexpectedly. Using `in` first allows us to remove an item only when it exists and display a helpful message when it does not.

