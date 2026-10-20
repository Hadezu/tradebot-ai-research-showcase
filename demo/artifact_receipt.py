"""Original educational example: verified receipts, no trading or training."""
import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory


def digest(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def confirm(directory: Path, job: str, expected_digest: str) -> dict:
    """Single-writer example; expected_digest must come from trusted evidence."""
    artifact = directory / "artifact.bin"
    if not artifact.is_file() or digest(artifact.read_bytes()) != expected_digest:
        raise ValueError("Artifact absent or inconsistent with trusted evidence")
    expected = {"job": job, "digest": expected_digest, "state": "confirmed"}
    receipt = directory / "receipt.json"
    if receipt.exists():
        if json.loads(receipt.read_text(encoding="utf-8")) != expected:
            raise ValueError("Receipt conflicts with job identity")
        return expected
    temporary = directory / "receipt.pending"
    temporary.write_text(json.dumps(expected, sort_keys=True), encoding="utf-8")
    temporary.replace(receipt)
    return expected


if __name__ == "__main__":
    with TemporaryDirectory() as temporary:
        directory = Path(temporary)
        invented = b"synthetic-example-artifact"
        (directory / "artifact.bin").write_bytes(invented)
        first = confirm(directory, "example-job", digest(invented))
        second = confirm(directory, "example-job", digest(invented))
        assert first == second
        print("Verified artifact recovered; repeated confirmation unchanged.")
