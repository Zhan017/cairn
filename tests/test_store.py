"""Tests for the seed key/value store.

These are the invariants Phase 1's on-disk engine must also satisfy, so the
suite carries forward as the interface implementation changes underneath it.
"""

import pytest

from cairn.store import InMemoryStore


def test_get_missing_key_returns_none() -> None:
    store = InMemoryStore()
    assert store.get(b"absent") is None


@pytest.mark.parametrize(
    "key, value",
    [
        (b"a", b"1"),
        (b"key", b"value"),
        (b"", b"empty-key-is-allowed"),
        (b"unicode", "café".encode()),
        (b"\x00\x01\x02", b"\xff\xfe"),
    ],
)
def test_put_then_get_roundtrip(key: bytes, value: bytes) -> None:
    store = InMemoryStore()
    store.put(key, value)
    assert store.get(key) == value


def test_put_overwrites_existing_value() -> None:
    store = InMemoryStore()
    store.put(b"k", b"old")
    store.put(b"k", b"new")
    assert store.get(b"k") == b"new"


def test_delete_removes_key_and_reports_prior_presence() -> None:
    store = InMemoryStore()
    store.put(b"k", b"v")
    assert store.delete(b"k") is True
    assert store.get(b"k") is None
    assert store.delete(b"k") is False


def test_len_counts_distinct_keys() -> None:
    store = InMemoryStore()
    store.put(b"a", b"1")
    store.put(b"b", b"2")
    store.put(b"a", b"3")  # overwrite, not a new key
    assert len(store) == 2
