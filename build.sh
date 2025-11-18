#!/bin/bash
# Build script for chapter2code

case "$1" in
  build)
    echo "Building blog..."
    python3 scripts/build.py
    ;;
  open)
    echo "Opening blog in browser..."
    open src/index.html
    ;;
  notebook)
    echo "Launching Jupyter..."
    jupyter notebook notebooks/
    ;;
  clean)
    echo "Cleaning generated files..."
    rm -f src/posts/*.html
    echo "✓ Cleaned"
    ;;
  *)
    echo "chapter2code build commands:"
    echo ""
    echo "  ./build.sh build     - Build blog from all notebooks in notebooks/"
    echo "  ./build.sh open      - Open blog in browser"
    echo "  ./build.sh notebook  - Launch Jupyter for editing"
    echo "  ./build.sh clean     - Remove generated files"
    echo ""
    echo "The build system automatically detects all .ipynb files in notebooks/"
    ;;
esac
