#!/usr/bin/env python3
"""
Convert Jupyter notebooks to HTML for web viewing
"""
import os
import subprocess
from pathlib import Path

def convert_notebooks():
    """Convert all notebooks in the notebooks/ directory to HTML"""
    notebooks_dir = Path(__file__).parent.parent / "notebooks"
    output_dir = Path(__file__).parent.parent / "src" / "posts"
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all .ipynb files
    notebook_files = list(notebooks_dir.glob("*.ipynb"))
    
    if not notebook_files:
        print("No notebooks found in notebooks/ directory")
        return
    
    print(f"Converting {len(notebook_files)} notebook(s)...")
    
    for notebook in notebook_files:
        print(f"Converting {notebook.name}...")
        output_file = output_dir / f"{notebook.stem}.html"
        
        # Use nbconvert to convert to HTML
        cmd = [
            "jupyter", "nbconvert",
            "--to", "html",
            "--output", str(output_file.absolute()),
            str(notebook.absolute())
        ]
        
        try:
            subprocess.run(cmd, check=True, capture_output=True)
            print(f"  ✓ Created {output_file.name}")
        except subprocess.CalledProcessError as e:
            print(f"  ✗ Error converting {notebook.name}")
            print(f"    {e.stderr.decode()}")
    
    print("\nDone! Posts created in src/posts/")

if __name__ == "__main__":
    convert_notebooks()
