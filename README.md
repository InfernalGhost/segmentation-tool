# Text Segmentation Tool.

## Overview

This tool is designed to automatically segment text files into excerpts of approximately equal length. It provides fine-grained control over the minimum and maximum size of each excerpt, while preserving paragraph boundaries and avoiding paragraph splits. It also provides control over the number of excerpts to be extracted. The excerpts are extracted from different parts of the text and are evenly distributed throughout it. For example, if 10 excerpts are selected, they are sampled from positions that roughly correspond to 0%, 10%, 20%, … up to 90% of the text length.

The segmentation process is fully automated and operates over a directory of input text files.

## Usage

### Running the segmentation

To run the segmentation process, execute `script.sh`.

Running `script.sh` will:

- Process **every `.txt` file** located in the `data/` directory
- Segment each text into **a maximum of n excerpts**
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


