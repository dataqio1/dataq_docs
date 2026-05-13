#!/usr/bin/env python3
"""Convert Loom {% video %} tags to HTML iframes since the video plugin only supports YouTube/Vimeo."""
import re
import glob
import os

def convert_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Convert Loom {% video %}...{% endvideo %} to HTML iframe
    def replace_loom(match):
        url = match.group(1)
        return f'<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;"><iframe src="{url}" style="position:absolute;top:0;left:0;width:100%;height:100%;border:none;" allowfullscreen></iframe></div>'

    content = re.sub(
        r'\{%\s*video\s*%\}(https://www\.loom\.com/embed/[^{]+)\{%\s*endvideo\s*%\}',
        replace_loom, content
    )

    # Convert non-video URLs wrapped in video tags to plain links
    def replace_non_video(match):
        url = match.group(1).strip()
        if 'youtube' not in url and 'vimeo' not in url and 'loom' not in url:
            return f'[Reference Link]({url})'
        return match.group(0)

    content = re.sub(r'\{%\s*video\s*%\}([^{]+)\{%\s*endvideo\s*%\}', replace_non_video, content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Fixed: {filepath}")

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for filepath in glob.glob(os.path.join(root, '**/*.md'), recursive=True):
        if 'node_modules' in filepath or '_book' in filepath:
            continue
        convert_file(filepath)
    print("Done.")

if __name__ == '__main__':
    main()
