# Tests

Offline unit tests for repository validation, contribution scope, certification, and credits.

- [test_policy.py](test_policy.py): tests URL/date validation, PR contribution scope, stack policies, preserved entries, and tier/Markdown sync
- [test_certification.py](test_certification.py): tests PR certification checks
- [test_credits.py](test_credits.py): tests `CREDITS.md` generation and diff checks

Run all tests from the repository root:

```sh
python3 -m unittest discover -s tests -v
```
