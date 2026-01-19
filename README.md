# Text Segmentation Tool.

## Overview

The goal of this project is to automatically segment text files into a fixed number of excerpts while allowing fine-grained control over the minimum and maximum size of each excerpt. If the size constraints prevent the extraction of the intended number of excerpts, the script will extract fewer excerpts accordingly.

The segmentation process is fully automated and operates over a directory of input text files.

## Usage

### Running the segmentation

To run the segmentation process, execute `script.sh`.

Running `script.sh` will:

- Process **every `.txt` file** located in the `data/` directory
- Segment each text into **a maximum of 10 excerpts**
- Create a **dedicated directory for each processed text**, containing the corresponding excerpts

## Output Structure

For each processed `.txt` file:

- A new directory is created
- This directory contains **all excerpts extracted from the original text**
- The name of the directory corresponds to the original text file, making it easy to trace each set of excerpts back to its source text

## Configuration

Segmentation parameters can be customized in `segment_text.py`.

In the section labeled **"set parameters"**, it is possible to modify:

- The **minimum size** of each excerpt
- The **maximum size** of each excerpt
- The **intended number of excerpts** to be extracted per text

The variable names in this section are designed to be self-explanatory, making configuration straightforward.

After updating the parameters, simply re-run `script.sh` for the changes to take effect.

## Requirements

- Python 3
- A Unix-like environment (for running `script.sh`)


