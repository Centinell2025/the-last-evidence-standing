# Publish the remaining binary exhibits — v1.5

The public repository now includes the full text investigation, forensic CSVs, 30 questions, integrity manifest, validation tools, and the Beacon of the Eagle LLC SVG seal.

The only missing items are **nine binary files**. Download and extract the binary-upload kit provided with this conversation, then upload its contents into the repository while preserving each relative path. **Do not upload the ZIP file as a replacement for the nine extracted files.**

After uploading, run:

```bash
python3 tools/verify_student.py
python3 tools/verify_witness_links.py
python3 tools/verify_network_consistency.py
python3 -m unittest discover -s tests -v
python3 tools/verify_release.py downloads/The-Last-Evidence-Standing-STUDENT.zip
```

Do not publish the confidential instructor archive, examiner writeup, grading key or author-only materials.

Publisher: **Beacon of the Eagle LLC** — Centinell Suite Defense.

The v1.5 standalone student ZIP and the nested `downloads/` ZIP have identical bytes; the student package has a root `README.md`. Nine binary uploads remain necessary for full GitHub publication.
