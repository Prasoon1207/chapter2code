#!/usr/bin/env python3
"""
Convert Jupyter notebooks to integrated blog posts with embedded code
"""
import json
from pathlib import Path

def escape_html(text):
    """Escape HTML special characters"""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&#39;'))

def convert_markdown_to_html(md_text):
    """Simple markdown to HTML conversion for basic formatting"""
    lines = md_text.split('\n')
    html_lines = []
    in_list = False
    
    for line in lines:
        # Headers
        if line.startswith('# '):
            html_lines.append(f'<h1>{line[2:]}</h1>')
        elif line.startswith('## '):
            html_lines.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('### '):
            html_lines.append(f'<h3>{line[4:]}</h3>')
        # Bold
        elif '**' in line:
            line = line.replace('**', '<strong>', 1).replace('**', '</strong>', 1)
            html_lines.append(f'<p>{line}</p>')
        # Lists
        elif line.startswith('- '):
            if not in_list:
                html_lines.append('<ul>')
                in_list = True
            html_lines.append(f'<li>{line[2:]}</li>')
        else:
            if in_list and not line.startswith('- '):
                html_lines.append('</ul>')
                in_list = False
            if line.strip():
                html_lines.append(f'<p>{line}</p>')
    
    if in_list:
        html_lines.append('</ul>')
    
    return '\n'.join(html_lines)

def notebook_to_blog_post(notebook_path, output_path, title, meta):
    """Convert a Jupyter notebook to an integrated blog post"""
    
    with open(notebook_path, 'r') as f:
        notebook = json.load(f)
    
    # Start HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} · chapter2code</title>
    <link rel="stylesheet" href="../styles/post-style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/default.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/languages/python.min.js"></script>
    <script>hljs.highlightAll();</script>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
    <div class="container">
        <nav class="top-nav">
            <a href="../index.html">chapter2code</a>
            <span class="sep">/</span>
            <span class="current">{title.lower()}</span>
        </nav>

        <article>
            <header class="post-header">
                <h1>{title}</h1>
                <div class="meta">{meta}</div>
            </header>

"""
    
    # Process cells
    skip_first_title = True
    for cell in notebook['cells']:
        cell_type = cell['cell_type']
        source = ''.join(cell['source'])
        
        if cell_type == 'markdown':
            # Skip the first h1 title since we already have it in header
            if skip_first_title and source.strip().startswith('# '):
                skip_first_title = False
                continue
            
            # Convert markdown to HTML (basic)
            html += f"            {convert_markdown_to_html(source)}\n\n"
            
        elif cell_type == 'code':
            # Add code block
            escaped_code = escape_html(source)
            html += f"""            <div class="code-block">
                <pre><code class="language-python">{escaped_code}</code></pre>
"""
            
            # Add output if present
            if 'outputs' in cell and cell['outputs']:
                output_text = []
                for output in cell['outputs']:
                    if 'text' in output:
                        output_text.extend(output['text'])
                    elif 'data' in output and 'text/plain' in output['data']:
                        output_text.extend(output['data']['text/plain'])
                
                if output_text:
                    output_str = ''.join(output_text).strip()
                    escaped_output = escape_html(output_str)
                    html += f"""                <div class="output">
                    <div class="output-label">output:</div>
                    <pre>{escaped_output}</pre>
                </div>
"""
            
            html += "            </div>\n\n"
    
    # End HTML
    html += """            <div class="post-footer">
                <a href="../index.html">← back to posts</a>
            </div>
        </article>
    </div>
</body>
</html>
"""
    
    # Write output
    with open(output_path, 'w') as f:
        f.write(html)
    
    print(f"✓ Created {output_path.name}")

if __name__ == "__main__":
    notebooks_dir = Path(__file__).parent.parent / "notebooks"
    output_dir = Path(__file__).parent.parent / "src" / "posts"
    
    # Example: Convert forward_diffusion notebook
    notebook_to_blog_post(
        notebooks_dir / "forward_diffusion.ipynb",
        output_dir / "forward_diffusion.html",
        "Forward Diffusion Process",
        "chapter 2 · diffusion models · november 2025"
    )
    
    print("\nDone! Check src/posts/forward_diffusion.html")
