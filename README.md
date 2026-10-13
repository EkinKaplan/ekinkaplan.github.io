# ekinkaplan.com — academic website of Ekin Kaplan

A static Astro + TypeScript + Tailwind CSS site, deployed to GitHub Pages with GitHub Actions. No database, backend or CMS.

## Local setup
```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # type-check + production build into dist/
npm run preview
```
Requires Node 20 or newer.

## Where content lives
| What | File |
|---|---|
| Name, role, affiliation, email, links, portrait, CV switch | `src/data/profile.ts` |
| Publications | `src/data/publications.ts` |
| Research themes / projects | `src/data/research.ts` |
| CV entries (appointments, education, skills, talks, teaching …) | `src/data/cv.ts` |
| Biography text | `src/pages/about.astro` (plain paragraphs) |
| Images / PDFs | `public/images/`, `public/files/` |

Components (`src/components/`) never need editing for content changes.

## Maintenance
1. **Add a publication**: copy an object in `src/data/publications.ts`, edit fields (`doi` is the bare DOI). Set `selected: true` to show it on the homepage, `themes: ['change']` to list it under a research theme. Your name is highlighted when it matches `highlightName` (`Kaplan, E.`). Optional `pdf: 'files/papers/x.pdf'`, `abstract`, `supplement`. Year/type filters appear automatically once there are six or more publications.
2. **Edit the biography**: edit the paragraphs in `src/pages/about.astro`. The homepage introduction is `intro` in `profile.ts`.
3. **Add a research project/theme**: add an object to `themes` in `src/data/research.ts` (`id`, `title`, `question`, `short`, `body`, optional `image`, `imageAlt`, `imageCredit`, `links`, `status`). Use `status: 'Planned direction'` for work not yet done.
4. **Replace the portrait**: put a square image at `public/images/portrait.jpg` (≥800 px, compressed to <200 KB, ideally also WebP) and set `portrait: 'images/portrait.jpg'`.
5. **Upload the CV**: save it as `public/files/Ekin_Kaplan_CV.pdf` and set `cvAvailable: true`. Until then the CV page shows "PDF version coming soon"; the HTML CV prints cleanly via the Print button.
6. **Change contact information**: set `email` in `profile.ts`. An empty string hides it everywhere.
7. **Update affiliation/role**: edit `role`, `tagline`, `institution`, `department`, `division` in `profile.ts`, and add the new position to `appointments` in `cv.ts`. On finishing the PhD, also update `phdStatus` and the education entry.
8. **Add social profiles**: set `links.github`, or add `{ label: 'Bluesky', url: '…' }` to `links.other`. They appear in the footer, contact page and JSON-LD `sameAs`.
9. **Change the custom domain**: see below.
10. **Deploy**: commit and push to `main`. The workflow builds and publishes; progress is under the repository's Actions tab. It can also be run manually (Actions → Deploy to GitHub Pages → Run workflow).

## GitHub Pages setup
1. Create a repository, e.g. `USERNAME.github.io` (user site, served at the root) or any name (project site, served at `/repo-name`).
2. Push this project to `main`.
3. Settings → Pages → Build and deployment → Source: **GitHub Actions**.

`.github/workflows/deploy.yml` reads the real origin and base path from `actions/configure-pages`, and passes them to Astro as `SITE` and `BASE`. Canonical URLs, the sitemap and all internal links are therefore correct for a user site, a project site or a custom domain, without editing code. All internal links go through `src/lib/url.ts`, which adds the base path.

## Custom domain (ekinkaplan.com)
1. Settings → Pages → Custom domain: enter `ekinkaplan.com` and save. Tick **Enforce HTTPS** once the certificate is issued.
2. DNS at your registrar:
   - Apex `ekinkaplan.com`: four `A` records → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` (optionally `AAAA` → `2606:50c0:8000::153`, `…8001::153`, `…8002::153`, `…8003::153`).
   - `www`: `CNAME` → `USERNAME.github.io`.
3. Verify the domain under your GitHub account settings → Pages to prevent takeovers.
4. With Actions deployments, the Settings entry is what counts and a CNAME file is not required. If you want one anyway, rename `public/CNAME.example` to `public/CNAME`.
To change domains later, repeat these steps with the new domain. The build picks up the new origin automatically.

## Images and licensing
No photographs are included. Use your own field photographs or openly licensed images (e.g. CC BY from Wikimedia Commons) and add the credit in `imageCredit`. Do not use photos that misrepresent your sites or fieldwork.

## Verified content and placeholders
The site includes only information that has been supplied and verified: the University of Vienna affiliation, supervisors, doctoral school, Research Assistant position (2022–2025), two publications, and the ORCID, Google Scholar and university links. Placeholders that hide themselves until filled in: email, GitHub, portrait, CV PDF, earlier education, further positions, conferences, teaching, fieldwork, awards. No citation metrics are shown.
