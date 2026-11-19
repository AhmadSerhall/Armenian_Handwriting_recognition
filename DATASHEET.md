# ArmScribe AI Dataset Datasheet

This document is a template to complete before data preparation and training.
It is intentionally not a claim that the dataset has been obtained or audited.

## Dataset identity and source

- **Primary planned source:** Mashtots Armenian handwriting dataset.
- **Version / retrieval date:** To be recorded.
- **Source URL / citation:** To be recorded.
- **License and redistribution terms:** Verify before downloading, committing,
  or publishing derived artifacts.
- **Optional source:** Volunteer-contributed samples for unseen-writer testing.

## Intended use and scope

- **Task:** classification of 39 Armenian uppercase letters.
- **Out of scope:** lowercase recognition, transliteration, and speech output.
- **Known limitations:** writer coverage, label quality, scanner/device bias,
  and class balance must be assessed after acquisition.

## Labels and class mapping

- Store the authoritative label-to-index mapping in a versioned artifact.
- Confirm that exactly 39 uppercase classes are present.
- Record Unicode characters, class indices, sample counts, and any exclusions.

## Collection and metadata

- Record available writer identifiers, collection protocol, image formats,
  resolution, and annotation process.
- Do not include personally identifying volunteer information in the repository.
- Obtain appropriate consent for volunteer contributions and record the terms.

## Preprocessing plan

- Document image mode, inversion, cropping, resize dimensions, normalization,
  and any rejected/corrupted samples.
- Keep raw inputs immutable in `data/raw/`; write derived files only to
  `data/processed/`.
- Apply data augmentation only to training samples.

## Train/validation/test separation

- Split by writer whenever writer metadata is available.
- Ensure no writer appears in more than one partition.
- Reserve volunteer writers for a clearly documented unseen-writer evaluation.
- Record seeds, split proportions, sample counts, and split manifests.

## Maintenance and review

- Revisit this datasheet after each dataset update.
- Record issues, corrections, license decisions, and reproducibility notes.
