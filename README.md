# Om Patnaik’s portfolio

A static technical portfolio built around inspectable systems and research evidence.

[Website](https://ompatnaik.com/) · [Projects](https://ompatnaik.com/projects.html) · [GitHub](https://github.com/OmTheLast)

## Pages

| URL | Purpose |
| --- | --- |
| `/` | Introduction and three featured projects |
| `/projects.html` | Featured research, other built projects, earlier learning |
| `/jee/` | LlamaJEE.js case study and experiment limits |
| `/llamajee/` | Existing browser solver; preserved compiled application |
| `/tokenizers/` | Tokenizer study methods, controls, results, and limitations |
| `/hinglish/` | mBERT/MuRIL results, transfer failures, and error analysis |
| `/projects/drishya/` | Mechanics lab project notes |
| `/projects/contextfair/` | Conversation planner project notes |
| `/projects/lumen/` | Local desktop agent project notes |
| `/projects/football-rule-cite/` | Retrieval project and static sample preview |
| `/projects/twistlab/` | Cube simulator project notes |
| `/projects/news-classifier/` | Earlier API project and local setup link |

Drishya, ContextFair, TwistLab, and Football Rule Cite are separately deployed project sites. Their routes are not directories to copy into this repository. Lumen is a desktop application with its own project website. The tokenizer and Hinglish studies have published artifacts, not hosted inference apps.

## Preview and verify

No framework, package installation, or build step is required.

```sh
python3 -m http.server 4173 --bind 127.0.0.1
python3 scripts/check_site.py
python3 scripts/check_site.py --external
```

Open `http://127.0.0.1:4173/`. The checker covers internal routes and anchors, document structure, image text and dimensions, metadata, copied-figure hashes, and the custom domain. The optional external check requires curl and network access. It checks HTTP responses, not application correctness.

Check keyboard navigation, the three case studies, and phone/tablet/desktop widths in a browser. The solver’s model download is optional for portfolio QA; loading the interface is not proof of model inference. The October 2026 audit and validation scope are recorded in [docs/portfolio-audit.md](docs/portfolio-audit.md).

## Evidence and assets

Case-study citations link to inspected repository commits. Original charts are copied without alteration; [assets/research/sources.json](assets/research/sources.json) records source URLs and SHA-256 hashes. Tables expose the key numbers without requiring readers to inspect small chart labels. Public claims distinguish development results, computational validation, and runtime checks.

The shared stylesheet retains the existing dark palette, Inter/IBM Plex Mono typography, and restrained lime accent. Portfolio pages use semantic HTML without JavaScript. Google Fonts remain an external dependency with system-font fallbacks. Figures load lazily with explicit dimensions.

## Deployment

GitHub Pages currently publishes `main` from the repository root. Merge the portfolio branch to publish through that existing setup. Keep `CNAME` as `ompatnaik.com` and preserve the compiled `/llamajee/` application and its pinned deployment metadata. No DNS, framework, or hosting migration is required.

Merge dependent profile/project README changes after the site deploys so new case-study backlinks resolve. The old Football Rule Cite preview path was replaced with `/Football-Rule-Cite/`; the former Railway news API returned HTTP 404 and is not advertised as live.

Backups and drafts remain as design history. `robots.txt` asks crawlers not to index those directories; it does not restrict access.
