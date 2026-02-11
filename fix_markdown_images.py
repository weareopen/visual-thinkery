import json
from pathlib import Path
from collections import defaultdict

# Load data
with open('captions.json') as f:
    captions = json.load(f)

with open('categories_map.json') as f:
    categories_map = json.load(f)

# Create caption lookup
caption_lookup = {item['suggested_filename']: item['caption'] for item in captions}

# Group by category
categories = defaultdict(list)
for filename, category in categories_map.items():
    categories[category].append(filename)

# Output path
output_path = Path('visual-thinkery-gallery-fixed')

# Category display names
category_names = {
    'project-management': 'Project Management',
    'user-research': 'User Research',
    'open-badges': 'Open Badges & Recognition',
    'open-education': 'Open Education',
    'cooperative': 'Co-operative Principles',
    'learning-design': 'Learning Design',
    'community': 'Community Building',
    'facilitation': 'Facilitation',
    'general': 'General'
}

# Generate category pages with Markdown image syntax
for category, filenames in categories.items():
    cat_path = output_path / category
    
    display_name = category_names.get(category, category.replace('-', ' ').title())
    
    cat_md = f"# {display_name}\n\n"
    cat_md += f"[← Back to main gallery](../)\n\n"
    
    sorted_files = sorted(filenames)
    
    # Use simple list format instead of tables
    for filename in sorted_files:
        caption = caption_lookup.get(filename, "Visual thinkery illustration")
        title = Path(filename).stem.replace('-', ' ').title()
        
        # Markdown image syntax
        cat_md += f"### {title}\n\n"
        cat_md += f"![{caption}]({filename})\n\n"
        cat_md += f"_{caption}_\n\n"
        cat_md += "---\n\n"
    
    cat_md += f"**{len(sorted_files)} images** in this collection\n\n"
    cat_md += "All images © Bryan Mathers, available under [CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/)\n"
    
    (cat_path / "README.md").write_text(cat_md)
    print(f"✓ Fixed {category}/README.md")

print("\n✓ All converted to Markdown image syntax!")
