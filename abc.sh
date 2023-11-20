#!/bin/bash

# Directory containing the markdown files
DIRECTORY=/Users/dhiraj/Documents/dataq/dataq_docs/

# Loop through all markdown (.md) files in the directory
for file in "$DIRECTORY"/*.md; do
  # Check if the file is a regular file
  if [ -f "$file" ]; then
    # Use sed to replace different variations of 'DataQ' with 'Vexdata' in-place
   sed -i '' -e 's/DataQ\.io/Vexdata/g' -e 's/DataQ/Vexdata/g' -e 's/Dataq/Vexdata/g' "$file"
   echo "Processed $file"
  fi
done

echo "All files have been processed."
