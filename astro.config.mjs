import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import tailwindcss from '@tailwindcss/vite';

// SITE: full origin of the deployed site (no trailing slash).
// BASE: sub-path. "/" for a user site (USERNAME.github.io) or custom domain,
//       "/repo-name" for a project site (USERNAME.github.io/repo-name).
// Both are set automatically in the GitHub Actions workflow; the defaults
// below are used for local development and custom-domain builds.
const site = process.env.SITE || 'https://ekinkaplan.com';
const base = process.env.BASE || '/';

export default defineConfig({
  site,
  base,
  output: 'static',
  trailingSlash: 'ignore',
  integrations: [sitemap()],
  vite: { plugins: [tailwindcss()] },
});
