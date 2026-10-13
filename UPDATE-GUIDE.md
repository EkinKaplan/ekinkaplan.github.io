# How to update your website

## A normal edit on GitHub

1. Open your repository: https://github.com/ekinkaplan/ekinkaplan.github.io.
2. Open the file from the table below and select the pencil (Edit) button.
3. Make your change. Keep indentation in `.yml` files; use spaces, not tabs.
4. Select **Commit changes** and write a short description, such as “Add new paper”.
5. For a small change, commit to `main` to publish. For a larger change, create a new
   branch and pull request, review the changes/checks, then merge into `main`.
6. Check the Actions tab. The new version becomes live after a successful deployment.

| I want to… | Edit |
| --- | --- |
| Change my role, affiliation, email or introduction | `_data/profile.yml` |
| Add a publication or change a DOI | `_data/publications.yml` |
| Choose homepage papers | Set `featured: true` for up to three publications |
| Change research descriptions | `_data/research.yml` |
| Edit my biography or education | `about.md` |
| Replace my CV | `assets/files/ekin-kaplan-cv.pdf` and the `cv_label` in profile.yml |
| Replace my photo | `assets/images/ekin-kaplan.jpg` |
| Change colours or typography | Variables at the top of `assets/css/style.css` |

## Add a publication

Copy an existing entry and add the new one at the top of `_data/publications.yml`.
The homepage displays the first three entries marked `featured: true`.

```yaml
- title: "Your exact paper title"
  year: 2027
  journal: Your journal name
  role: First author
  doi: https://doi.org/YOUR-REAL-DOI
  featured: true
  type: journal
```

Do not publish the example DOI: replace it with the paper's real DOI, or omit `doi`
if one does not yet exist. Use `type: report` or `type: thesis` for other outputs.
To offer an authorised PDF, upload it to `assets/files/` and add:

```yaml
  pdf: /assets/files/your-paper.pdf
```

Keep titles in double quotes if they contain a colon. If they also contain double
quotes, use single quotes around the title (and double any single quote inside it).
Keep unpublished manuscripts clearly labelled; do not list a submission as published.

## Change affiliation

In `_data/profile.yml`, change `role` and `affiliation`. This updates the home and
About introductions. The education history in `about.md` is separate: update that
when you complete your PhD. Update the downloadable CV as appropriate too.

## Replace your CV or photograph

Upload the replacement into the same folder using exactly the same filename.
For the CV, also change `cv_label` in `_data/profile.yml` to its new date.
The original supplied CV is included unchanged. Read it before making it public and
remove any details you do not want on your website.

The portrait is displayed at 200 × 200 pixels in a circular frame on desktop, smaller on mobile. The
source image stays unchanged. Adjust `.portrait` in the stylesheet for its framing.

## Add a new page

Create `teaching.md` in the repository root:

```markdown
---
layout: default
title: Teaching
permalink: /teaching/
---

# Teaching

Your text here.
```

To show it in the menu, add to `_data/navigation.yml`:

```yaml
- title: Teaching
  url: /teaching/
```

## Recover from a mistake

If the build fails, open the failed run in **Actions** and inspect its first failed
step. Often a quotation mark or indentation in a YAML file needs correcting. A
failed build will not replace the last successful live deployment.

For a text mistake, open that file's History, view the previous version, and copy the
correct content into a new edit. Save it as a new commit. For a merged pull request,
GitHub may offer a Revert button. Avoid force-pushing or deleting the repository.

For help, share the changed file and the error message; there is no need to share
passwords, tokens, or secrets.
