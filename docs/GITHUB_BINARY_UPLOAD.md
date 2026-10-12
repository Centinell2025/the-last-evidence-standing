# Published evidence — completed release v1.5

The nine original binary files, forensic CSVs, investigation questions, publisher image, student dossier and learner ZIP are now present in this public repository.

## Learner distribution
[Download the student ZIP](../downloads/The-Last-Evidence-Standing-STUDENT.zip) or clone the repository. Students should investigate only the synthetic case; no attacker system or external network access is required.

## Run the integrity and investigation quality checks

```bash
python3 tools/verify_student.py
python3 tools/verify_witness_links.py
python3 tools/verify_network_consistency.py
python3 -m unittest discover -s tests -v
python3 tools/verify_release.py downloads/The-Last-Evidence-Standing-STUDENT.zip
```

The student archive has SHA-256 digest `27de88fdc5a61cf57507b6f670fcd8795c85ce04a8178af2404c2b9531f35287`. Instructor solutions, worked paths, and grading answers must remain separate and confidential.

**Published by Beacon of the Eagle LLC — Centinell Suite Defense.** All technical incident data are synthetic.
