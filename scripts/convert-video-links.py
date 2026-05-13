#!/usr/bin/env python3
"""Convert [Video Link](URL) markdown links to {% video %}URL{% endvideo %} for HonKit video plugin."""
import re
import glob
import os

def convert_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Convert [Video Link](URL) to {% video %}URL{% endvideo %}
    # For Loom share links, convert to embed format
    def replace_video(match):
        url = match.group(1)
        # Convert Loom share URLs to embed URLs
        loom_match = re.match(r'https://www\.loom\.com/share/([^?]+)', url)
        if loom_match:
            video_id = loom_match.group(1)
            return f'{{% video %}}https://www.loom.com/embed/{video_id}{{% endvideo %}}'
        # Convert YouTube watch URLs to embed URLs
        yt_match = re.match(r'https://www\.youtube\.com/watch\?v=([^&]+)', url)
        if yt_match:
            video_id = yt_match.group(1)
            return f'{{% video %}}https://www.youtube.com/embed/{video_id}{{% endvideo %}}'
        # Convert youtu.be short URLs
        ytshort_match = re.match(r'https://youtu\.be/([^?]+)', url)
        if ytshort_match:
            video_id = ytshort_match.group(1)
            return f'{{% video %}}https://www.youtube.com/embed/{video_id}{{% endvideo %}}'
        # Convert Vimeo URLs to embed URLs
        vimeo_match = re.match(r'https://vimeo\.com/(\d+)(?:/([a-f0-9]+))?', url)
        if vimeo_match:
            video_id = vimeo_match.group(1)
            hash_part = vimeo_match.group(2)
            if hash_part:
                return f'{{% video %}}https://player.vimeo.com/video/{video_id}?h={hash_part}{{% endvideo %}}'
            return f'{{% video %}}https://player.vimeo.com/video/{video_id}{{% endvideo %}}'
        # Vimeo player progressive redirect (direct mp4) - use iframe approach
        if 'player.vimeo.com/progressive_redirect' in url:
            return f'<video controls width="100%"><source src="{url}" type="video/mp4"></video>'
        # Default: wrap in video tags
        return f'{{% video %}}{url}{{% endvideo %}}'

    content = re.sub(r'\[Video Link\]\(([^)]+)\)', replace_video, content)

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
