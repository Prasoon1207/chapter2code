#!/usr/bin/env python3
"""
Generate index.html dynamically from available notebooks
"""
import json
from pathlib import Path

def get_notebook_metadata(notebook_path):
    """Extract metadata from a notebook"""
    with open(notebook_path, 'r') as f:
        notebook = json.load(f)
    
    # Get title from first markdown cell with # header
    title = notebook_path.stem.replace('_', ' ').title()
    description = ""
    
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown':
            source = ''.join(cell['source'])
            lines = source.strip().split('\n')
            
            # Look for title
            for line in lines:
                if line.startswith('# '):
                    title = line[2:].strip()
                    break
            
            # Look for description (first paragraph after title)
            in_desc = False
            desc_lines = []
            for line in lines:
                if line.startswith('**Chapter') or line.startswith('Chapter'):
                    in_desc = True
                    continue
                if in_desc and line.strip() and not line.startswith('#'):
                    desc_lines.append(line.strip())
                    if len(desc_lines) >= 2:
                        break
            
            if desc_lines:
                description = ' '.join(desc_lines)
            break
    
    return {
        'title': title,
        'description': description,
        'filename': notebook_path.stem,
        'tags': []  # Could be extracted from notebook metadata
    }

def generate_index_html(notebooks_info):
    """Generate index.html from notebook metadata"""
    
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>chapter2code</title>
    <link rel="stylesheet" href="styles/style.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>chapter2code</h1>
            <p class="tagline">research notes on ml topics</p>
        </header>

        <nav>
            <a href="#about">about</a>
            <a href="#notebooks">notebooks</a>
            <a href="https://github.com/Prasoon1207/chapter2code" target="_blank">github</a>
        </nav>

        <section id="about">
            <h2>about</h2>
            <p>
                The purpose of this blog is to document my learning journey through some scientific topics I find interesting. Here, I share research notes, code implementations, and insights gained from studying various concepts in depth.
            </p>
        </section>

        <section id="notebooks">
            <h2>notebooks</h2>
            
"""
    
    # Generate notebook entries
    for nb in notebooks_info:
        # Create a simple description if none found
        desc = nb['description'] if nb['description'] else f"Exploring {nb['title'].lower()}."
        
        html += f"""            <article class="notebook-entry">
                <h3>
                    <a href="posts/{nb['filename']}.html">{nb['title'].lower()}</a>
                </h3>
                <div class="meta">november 2025</div>
                <p>
                    {desc}
                </p>
            </article>

"""
    
    html += """        </section>

        <footer>
            <p>© 2025</p>
        </footer>
    </div>
</body>
</html>
"""
    
    return html

def build_index():
    """Build index.html from available notebooks"""
    base_dir = Path(__file__).parent.parent
    notebooks_dir = base_dir / "notebooks"
    output_path = base_dir / "src" / "index.html"
    
    # Find all notebooks
    notebooks = sorted(notebooks_dir.glob("*.ipynb"))
    
    # Filter out checkpoint files
    notebooks = [nb for nb in notebooks if '.ipynb_checkpoints' not in str(nb)]
    
    if not notebooks:
        print("⚠ No notebooks found in notebooks/ directory")
        return
    
    print(f"Found {len(notebooks)} notebook(s):")
    
    # Extract metadata from each notebook
    notebooks_info = []
    for notebook in notebooks:
        print(f"  - {notebook.name}")
        try:
            metadata = get_notebook_metadata(notebook)
            notebooks_info.append(metadata)
        except Exception as e:
            print(f"    ⚠ Error reading metadata: {e}")
    
    # Generate index.html
    html = generate_index_html(notebooks_info)
    
    with open(output_path, 'w') as f:
        f.write(html)
    
    print(f"\n✓ Generated src/index.html with {len(notebooks_info)} notebook(s)")

if __name__ == "__main__":
    build_index()
