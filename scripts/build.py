#!/usr/bin/env python3
"""
Build the chapter2code blog
"""
import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))

from generate_blog_posts import notebook_to_blog_post
from generate_index import build_index

def build():
    """Build all blog posts from notebooks"""
    base_dir = Path(__file__).parent.parent
    notebooks_dir = base_dir / "notebooks"
    output_dir = base_dir / "src" / "posts"
    
    # Ensure output directory exists
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("Building chapter2code blog...\n")
    
    # Find all notebooks automatically
    notebooks = sorted(notebooks_dir.glob("*.ipynb"))
    notebooks = [nb for nb in notebooks if '.ipynb_checkpoints' not in str(nb)]
    
    if not notebooks:
        print("⚠ No notebooks found in notebooks/ directory")
        return
    
    print(f"Found {len(notebooks)} notebook(s) to build:\n")
    
    # Convert each notebook
    for notebook_path in notebooks:
        print(f"Building {notebook_path.name}...")
        output_path = output_dir / notebook_path.with_suffix('.html').name
        
        # Extract title from notebook name
        title = notebook_path.stem.replace('_', ' ').title()
        meta = "november 2025"
        
        try:
            notebook_to_blog_post(
                notebook_path,
                output_path,
                title,
                meta
            )
        except Exception as e:
            print(f"  ✗ Error building {notebook_path.name}: {e}")
    
    # Generate index.html
    print("\nGenerating index...")
    build_index()
    
    print(f"\n✓ Build complete! Open src/index.html to view the blog.")

if __name__ == "__main__":
    build()
