"""Tests for writer-independent splitting safeguards."""

import pytest

from armscribe.data.splitting import WriterIndependentSplitter


def test_writer_partitions_must_not_share_a_writer() -> None:
    """A writer in two partitions is rejected to prevent data leakage."""
    splitter = WriterIndependentSplitter()

    with pytest.raises(ValueError, match="Writer leakage"):
        splitter.validate_partition_writers(
            {
                "train": {"writer-a", "writer-b"},
                "validation": {"writer-c"},
                "test": {"writer-a"},
            }
        )


def test_writer_partitions_accept_disjoint_writers() -> None:
    """Disjoint writer sets satisfy the Phase 1 split contract."""
    splitter = WriterIndependentSplitter()

    splitter.validate_partition_writers(
        {
            "train": {"writer-a", "writer-b"},
            "validation": {"writer-c"},
            "test": {"writer-d"},
        }
    )
