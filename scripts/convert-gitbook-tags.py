#!/usr/bin/env python3
"""Convert GitBook-specific template tags to standard markdown."""
import re
import glob
import os

def convert_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Convert {% embed url="URL" %} to [Video Link](URL)
    content = re.sub(r'\{%\s*embed\s+url="([^"]+)"\s*%\}', r'[Video Link](\1)', content)

    # Remove {% endembed %}
    content = re.sub(r'\{%\s*endembed\s*%\}', '', content)

    # Convert {% hint style="..." %} to blockquote
    content = re.sub(r'\{%\s*hint\s+style="info"\s*%\}', '> **Info:**', content)
    content = re.sub(r'\{%\s*hint\s+style="warning"\s*%\}', '> **Warning:**', content)
    content = re.sub(r'\{%\s*hint\s+style="danger"\s*%\}', '> **Danger:**', content)
    content = re.sub(r'\{%\s*hint\s+style="success"\s*%\}', '> **Success:**', content)

    # Remove {% endhint %}
    content = re.sub(r'\{%\s*endhint\s*%\}', '', content)

    # Convert {% file src="PATH" %} to [Download](PATH)
    content = re.sub(r'\{%\s*file\s+src="([^"]+)"\s*%\}', r'[Download File](\1)', content)

    # Remove {% endfile %}
    content = re.sub(r'\{%\s*endfile\s*%\}', '', content)

    # Catch any remaining {% ... %} tags
    content = re.sub(r'\{%\s*\w+[^%]*%\}', '', content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Converted: {filepath}")

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for filepath in glob.glob(os.path.join(root, '**/*.md'), recursive=True):
        if 'node_modules' in filepath or '_book' in filepath:
            continue
        convert_file(filepath)
    print("Done.")

if __name__ == '__main__':
    main()
