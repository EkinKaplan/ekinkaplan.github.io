# First draft review notes

## Prepared

- Four pages: Home, Research, Publications, About & CV, plus a 404 page.
- Original portrait and August 2026 CV copied byte-for-byte from the supplied files.
- Small circular 200px desktop portrait on the left, with a restrained introduction and research emphasis.
- System fonts, responsive layouts, keyboard focus states, skip link, and alt text.
- Content separated from templates; one reusable publication component.
- GitHub Actions workflow: build, local-link check, then publish main only.

## Content to review before publishing

- The role is “PhD candidate in Ecology”, with education listed as ongoing. It does
  not claim a completed PhD or current paid research-assistant employment.
- Publications are transcribed from the supplied CV. Full author lists are not
  invented; journal, year, title and contribution role are shown. DOI destinations
  have not been independently checked against publisher metadata in this build.
- The report entry has no year because the supplied CV does not give one.
- The unpublished resurvey manuscript is not listed as a published paper. Add it
  with verified title and an explicit status when you want to show it.
- The public CV is your original supplied PDF; review its details before publishing.
- Google Scholar, ORCID, email, and GitHub should be checked by the owner.

## Verification limits

The drafting environment has no Ruby/Jekyll installation. A compatible Liquid
renderer was used to produce a content/layout preview and check five rendered pages,
local links, fragments, assets, headings, metadata, and image alt text. This is not
an actual Jekyll build. GitHub's included workflow performs the real build before
publishing. Browser visual QA was not available in this environment; review the
standalone preview at desktop and mobile widths before publishing.

No remote commits, repository settings changes, or live deployment have been made.
The standalone preview is a review aid, not an editable source or a deployment file.
