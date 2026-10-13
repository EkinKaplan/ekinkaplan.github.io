# Ekin Kaplan — academic website

A small custom Jekyll website for https://ekinkaplan.github.io.

## Start here

This is a first review draft. No remote changes or deployment were made while preparing it.
Read `REVIEW-NOTES.md` before publishing and `UPDATE-GUIDE.md` for everyday editing.
The separately supplied `ekin-website-preview.html` is a self-contained design preview;
it is not the site's source and should not be uploaded to the repository.

## Publish with GitHub Actions

1. Put this folder's **contents**, including `.github`, `_data`, `_layouts`, and `_includes`,
   at the root of `ekinkaplan/ekinkaplan.github.io`. Do not upload the ZIP itself or nest
   the website inside another folder. Keep any unrelated repository files.
2. In the repository, open **Settings → Pages** and select **GitHub Actions** as the source.
3. Merge the reviewed files into `main`. The included workflow builds the site, checks
   internal links/assets, and deploys only if those steps succeed.
4. Open **Actions → Check and publish website** to follow progress. If needed, select
   **Run workflow** on `main` after changing the Pages source.
5. Visit https://ekinkaplan.github.io once deployment succeeds.

For a review before publication, use a branch and pull request. The workflow checks
pull requests but only deploys `main`. Public repositories have publicly visible files.

The workflow is in `.github/workflows/pages.yml`. If you already have another Pages
workflow, keep only one publishing workflow to avoid duplicate deployments.

## Local development (optional)

Requires Ruby and Bundler. This is not needed for editing files through GitHub.

```sh
bundle install
bundle exec jekyll serve
```

Open http://127.0.0.1:4000. Restart Jekyll after changing `_config.yml`.
For a production build and local-link check:

```sh
bundle exec jekyll build
python3 scripts/check_site.py _site
```

Commit the generated `Gemfile.lock` when adopting a local Bundler workflow. The
included GitHub workflow uses GitHub's maintained `jekyll-build-pages` action.

## Organisation

| File | Purpose |
| --- | --- |
| `_data/profile.yml` | Introduction, affiliation, contact links, CV and portrait paths |
| `_data/publications.yml` | Publication list and homepage selection |
| `_data/research.yml` | Research themes and descriptions |
| `_data/navigation.yml` | Main menu |
| `about.md` | Biography, education, experience |
| `index.html` | Homepage layout |
| `research.html`, `publications.html` | Page layouts |
| `_layouts/default.html` | Shared header, footer, metadata |
| `_includes/publication.html` | Shared publication formatting |
| `assets/css/style.css` | Colours, typography, spacing, responsive layout |
| `assets/images/ekin-kaplan.jpg` | Original portrait, unchanged |
| `assets/files/ekin-kaplan-cv.pdf` | Supplied August 2026 CV, unchanged |
| `_config.yml` | Website URL, title, build settings |
| `scripts/check_site.py` | Built-page checks used by GitHub |

No analytics, external fonts, JavaScript framework, database, or paid service is required.
The public site works without JavaScript.
