#!/usr/bin/env bash

INPUT_DIR="data"

for file in "$INPUT_DIR"/*.txt; do
    # Skip if no .txt files exist
    [[ -e "$file" ]] || continue

    echo "Processing: $file"
    python3 segment_text.py -f=$file
done

