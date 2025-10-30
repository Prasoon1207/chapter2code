# Chapter2Code Research Blog

A personal research blog where I annotate and implement key concepts from foundational books with code examples and explanations.

## Project Structure

- `chapters/`: Contains Jupyter notebooks for each chapter analysis
- `utils/`: Helper functions and common utilities
- `requirements.txt`: Python dependencies
- `_config.yml`: Jupyter Book configuration
- `_toc.yml`: Table of contents for the website

## Purpose

This project serves as a personal learning journey where I:
1. Read and analyze chapters from important books
2. Implement key concepts in code
3. Add detailed annotations and explanations
4. Create practical examples and demonstrations

## How to Use

Each chapter is contained in its own Jupyter notebook within the `chapters/` directory. The notebooks include:
- Key concepts from the chapter
- Code implementations
- Personal annotations and insights
- Practical examples and exercises

## Website

This project is built using Jupyter Book and automatically deployed as a website. You can:

1. View the published website at: `https://yourusername.github.io/chapter2code`
2. Build the website locally:
   ```bash
   jupyter-book build .
   ```
3. Preview locally:
   ```bash
   python -m http.server -d _build/html
   ```

## Contributing

1. Create a new branch for your changes
2. Add or modify notebooks in the `chapters/` directory
3. Update `_toc.yml` if you add new chapters
4. Push changes and create a pull request
5. The website will automatically rebuild on merge to main