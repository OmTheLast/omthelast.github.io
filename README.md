<h1 align="center">Om Patnaik’s Website</h1>

**Browse Om Patnaik’s projects, interests, and contact links through a small static portfolio.**

[Demo or published artifacts](https://ompatnaik.com)

Static HTML and CSS. No build step. Hosted with GitHub Pages and a custom domain.

By Om Patnaik · repository created June 2026.

## Install

| Platform / path | Start here |
| --- | --- |
| Browser | [Visit ompatnaik.com](https://ompatnaik.com) |
| Local preview | `python3 -m http.server 8000 --bind 127.0.0.1` |

Open http://127.0.0.1:8000 for the profile and `/projects.html` for the project list. The hosted site is the no-install preview.

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

## Why

You want one place to find project links and see what each one is about. This repository supplies the profile and project pages for ompatnaik.com. Its backups and drafts record earlier designs; they are not the current landing page.

## Find a project

Open `projects.html` to browse the portfolio, then follow the repository or demo link for setup and evidence. The landing page introduces interests and provides the current contact links.

## Notes from building it

I kept the site as static files so publishing does not need a build tool. The current landing page uses shared CSS while older layouts remain under backups and drafts. I would keep project descriptions synchronized with the repositories as they evolve.

## Commands

```bash
python3 -m http.server 8000 --bind 127.0.0.1  # preview the site
```

## Verify it yourself

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

There is no automated site test suite. In the preview, open both pages, follow project links, and check a narrow viewport and reduced-motion settings; running the server alone does not test those flows.

## Credits, license and pointers

Website and copy by Om Patnaik, using HTML, CSS, JavaScript, and GitHub Pages. No source license file is present.

[Repository history](https://github.com/OmTheLast/omthelast.github.io/commits).
