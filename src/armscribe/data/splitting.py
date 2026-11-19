"""Writer-aware dataset splitting contracts."""

from collections.abc import Iterable, Mapping, Sequence
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SplitRecord:
    """Minimal metadata required for a writer-independent split."""

    sample_id: str
    writer_id: str


class WriterIndependentSplitter:
    """Validate partition rules for splits that avoid writer leakage."""

    REQUIRED_PARTITIONS = frozenset({"train", "validation", "test"})

    def __init__(
        self,
        train_proportion: float = 0.70,
        validation_proportion: float = 0.15,
        test_proportion: float = 0.15,
    ) -> None:
        proportions = (
            train_proportion,
            validation_proportion,
            test_proportion,
        )
        if any(value <= 0 for value in proportions):
            raise ValueError("Split proportions must be greater than zero.")
        if abs(sum(proportions) - 1.0) > 1e-9:
            raise ValueError("Split proportions must add up to 1.0.")
        self.train_proportion = train_proportion
        self.validation_proportion = validation_proportion
        self.test_proportion = test_proportion

    def validate_records(self, records: Sequence[SplitRecord]) -> None:
        """Ensure a planned writer-aware split has usable metadata."""
        if not records:
            raise ValueError("At least one record is required for splitting.")
        if any(not record.writer_id.strip() for record in records):
            raise ValueError("Every split record must include a writer_id.")

    def validate_partition_writers(
        self,
        partition_writers: Mapping[str, Iterable[str]],
    ) -> None:
        """Raise when an expected partition is missing or writers overlap."""
        received_partitions = set(partition_writers)
        if received_partitions != self.REQUIRED_PARTITIONS:
            raise ValueError(
                "Partitions must be exactly: train, validation, and test."
            )

        normalized = {
            name: set(writer_ids) for name, writer_ids in partition_writers.items()
        }
        all_writers: set[str] = set()
        for name in sorted(self.REQUIRED_PARTITIONS):
            writers = normalized[name]
            if not writers:
                raise ValueError(f"The {name} partition must include a writer.")
            overlap = all_writers.intersection(writers)
            if overlap:
                joined_writers = ", ".join(sorted(overlap))
                raise ValueError(
                    f"Writer leakage detected across partitions: {joined_writers}."
                )
            all_writers.update(writers)

    def split(self, records: Sequence[SplitRecord]) -> dict[str, list[SplitRecord]]:
        """Create a future writer-independent split after data inspection."""
        self.validate_records(records)
        raise NotImplementedError(
            "Writer-aware split generation will be implemented in Phase 2."
        )
