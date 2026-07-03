"""The key/value store interface and its Phase 0 seed implementation.

`InMemoryStore` is the walking skeleton: correct, tested, and just enough to
build CI and a clean interface around. Phase 1 replaces it with a Bitcask-style
engine (append-only log + in-memory hash index + segment compaction) with a real
crash-recovery story — keeping this same get/put/delete interface stable.
"""

from __future__ import annotations


class InMemoryStore:
    """A minimal in-memory key/value store over ``bytes`` keys and values."""

    def __init__(self) -> None:
        self._data: dict[bytes, bytes] = {}

    def put(self, key: bytes, value: bytes) -> None:
        """Store ``value`` under ``key``, overwriting any existing value."""
        self._data[key] = value

    def get(self, key: bytes) -> bytes | None:
        """Return the value for ``key``, or ``None`` if absent."""
        return self._data.get(key)

    def delete(self, key: bytes) -> bool:
        """Remove ``key``. Return ``True`` if it was present, ``False`` otherwise."""
        existed = key in self._data
        self._data.pop(key, None)
        return existed

    def __len__(self) -> int:
        return len(self._data)
