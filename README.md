# chapter2code

research notes on advanced ml topics, annotated in jupyter notebooks

## structure

```
chapter2code/
├── notebooks/              # jupyter notebooks (source)
│   └── forward_diffusion.ipynb
├── src/                    # website source files
│   ├── index.html         # main blog page
│   ├── posts/             # individual blog posts
│   │   └── forward_diffusion.html
│   └── styles/            # css stylesheets
│       ├── style.css      # index page styles
│       └── post-style.css # blog post styles
├── scripts/               # build and conversion scripts
│   ├── convert_notebooks.py
│   └── generate_blog_posts.py
├── requirements.txt
├── .gitignore
└── README.md
```

## notebooks

- **forward_diffusion.ipynb** - forward diffusion process in diffusion models

## adding new notebooks

1. Create a new notebook in `notebooks/` directory
2. Add your content with markdown and code cells
3. Run `./build.sh build` to generate the blog post
4. The notebook will automatically appear on the blog!

The build system automatically:
- Discovers all `.ipynb` files in `notebooks/`
- Generates individual blog posts in `src/posts/`
- Updates `src/index.html` with all available notebooks

## setup

```bash
# clone the repository
git clone https://github.com/yourusername/chapter2code.git
cd chapter2code

# install dependencies
pip install jupyter numpy matplotlib pillow
```

## workflow

```bash
# build blog from notebooks
./build.sh build

# open blog in browser
./build.sh open

# launch jupyter to edit notebooks
./build.sh notebook

# clean generated files
./build.sh clean
```

or use python scripts directly:

```bash
# build all posts
python3 scripts/build.py

# generate single post (advanced)
python3 scripts/generate_blog_posts.py
```

## contributing

feel free to open issues or submit prs with new chapter notebooks.

## license

mit
