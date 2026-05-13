#!/bin/bash
# Convert GitBook-specific template tags to standard markdown
# Run this once to migrate content from GitBook to HonKit

DIR="${1:-.}"

find "$DIR" -name "*.md" -not -path "*/node_modules/*" -not -path "*/_book/*" | while read -r file; do
  # Convert {% embed url="URL" %} to [Video/Link](URL)
  sed -i '' -E 's/\{%\s*embed\s+url="([^"]+)"\s*%\}/[Video Link](\1)/g' "$file"

  # Remove {% endembed %}
  sed -i '' -E 's/\{%\s*endembed\s*%\}//g' "$file"

  # Convert {% hint style="info" %} to blockquote with bold label
  sed -i '' -E 's/\{%\s*hint\s+style="info"\s*%\}/> **Info:**/g' "$file"
  sed -i '' -E 's/\{%\s*hint\s+style="warning"\s*%\}/> **Warning:**/g' "$file"
  sed -i '' -E 's/\{%\s*hint\s+style="danger"\s*%\}/> **Danger:**/g' "$file"
  sed -i '' -E 's/\{%\s*hint\s+style="success"\s*%\}/> **Success:**/g' "$file"

  # Remove {% endhint %}
  sed -i '' -E 's/\{%\s*endhint\s*%\}//g' "$file"

  # Convert {% file src="PATH" %} to [Download](PATH)
  sed -i '' -E 's/\{%\s*file\s+src="([^"]+)"\s*%\}/[Download File](\1)/g' "$file"

  # Remove {% endfile %}
  sed -i '' -E 's/\{%\s*endfile\s*%\}//g' "$file"
done

echo "Conversion complete."
