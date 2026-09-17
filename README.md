# CompressionEngine
**Copyright © 2026 Anugrah Kaushik. All Rights Reserved.**

This repository is provided for viewing and educational reference only. No permission is granted to copy, reproduce, modify, distribute, publish, sublicense, sell or otherwise use any portion of the source code without prior written permission from the copyright owner.

## Overview

A lossless file compression and decompression program.

The program can compress files and reconstruct the original file through decompression.

## Features

* Lossless compression and decompression
* Supports arbitrary file types
* File integrity validation
* Operates at the byte level

## Project Structure

* EntropyEncoder — Compresses input files
* EntropyDecoder — Decompresses compressed files
* DataIntegrityVerifier — Verifies that the decompressed output matches the original

## Compression Results

Tested on files from the [Canterbury Corpus](https://corpus.canterbury.ac.nz/).

| File           | Compressed Size |
| -------------- | --------------: |
| `alice29.txt`  |          57.66% |
| `asyoulik.txt` |          60.56% |
| `cp.html`      |          65.84% |
| `fields.c`     |          63.01% |
| `grammar.lsp`  |          58.30% |
| `kennedy.xls`  |          44.92% |
| `lcet10.txt`   |          58.71% |
| `plrabn12.txt` |          57.19% |
| `ptt5`         |          20.76% |
| `sum`          |          67.06% |
| `xargs.1`      |          61.55% |
| `a.txt`        |          12.50% |
| `aaa.txt`      |          12.50% |
| `alphabet.txt` |          59.62% |
| `random.txt`   |          75.00% |
| `bib`          |          65.40% |
| `book1`        |          57.02% |
| `book2`        |          60.29% |
| `geo`          |          70.86% |
| `news`         |          65.34% |
| `obj1`         |          74.64% |
| `obj2`         |          78.64% |
| `paper1`       |          62.71% |
| `paper2`       |          57.93% |
| `paper3`       |          58.62% |
| `paper4`       |          59.16% |
| `paper5`       |          62.16% |
| `paper6`       |          63.04% |
| `pic`          |          20.76% |
| `progc`        |          65.42% |
| `progl`        |          59.99% |
| `progp`        |          61.19% |
| `trans`        |          69.61% |
| `bible.txt`    |          54.81% |
| `E.coli`       |          25.00% |
| `world192.txt` |          63.01% |
| `pi.txt`       |          42.49% |

> **Note:** Compressed size is expressed as a percentage of the original file size. For example, `alice29.txt` is reduced to **57.66%** of its original size.
> Compression performance depends on the characteristics of the input data. Files that are already compressed, such as JPEG or MP4 files, may not become smaller.

## Testing

The implementation was tested by compressing files, extracting them again, and validating that the extracted files match the originals.

## License

No license is granted for this repository. All rights are reserved by the copyright owner.
