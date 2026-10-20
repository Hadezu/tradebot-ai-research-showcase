# Synthetic receipt demonstration

This original, standalone example illustrates a reliability principle used in the private project: a verified artifact can have its missing receipt reconstructed, while unproven content must be rejected.

It is **not extracted TradeBot code**, a trading simulator, a model trainer or a substitute for the private crash-recovery tests. All input is invented. It has no network dependencies and writes only to a temporary directory when run directly.

From the repository root:

```sh
python -B demo/artifact_receipt.py
python -B -m unittest discover -s demo -p "test_*.py" -v
```

The caller supplies an expected digest from a previously trusted step. A hash alone does not establish trust. The example uses one local writer; concurrent writers, hostile filesystem modifications and storage-level crash durability are outside its scope. Atomic replacement here does not claim protection from every hardware failure.
