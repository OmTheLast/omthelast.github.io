# Portfolio audit and implementation record

25 October 2026. Scope: portfolio presentation and documentation links. No model training, benchmark reruns, framework migration, DNS changes, or production merge.

## Before implementation

The site had two current static pages, one shared CSS file, a profile image, archived designs, a CNAME file, and a separately compiled LlamaJEE application. The homepage led with the numbered ML learning series. The projects page placed those early projects first and included an empty “Next project” row. The three requested case studies did not exist. The old Football Rule Cite repository and preview names were stale.

GitHub Pages was built from `main`, repository root, with custom domain `ompatnaik.com`. The live portfolio, solver, Drishya, ContextFair, TwistLab, and Lumen project site were reachable. Football Rule Cite’s old `/DECISIONCITATION/` preview returned 404; its configured `/Football-Rule-Cite/` route returned 200. The documented Railway News Classifier API returned 404.

Implementation plan: retain static hosting and the visual identity; feature three source-backed studies; organize all projects into research, built systems, and earlier learning; add concise notes for built applications; prepare README backlinks on separate branches; verify routes, evidence, layout, and preserved application files.

## Changes

- Homepage: introduction, three featured studies, direct GitHub and full-project links.
- Projects: Featured Research & Systems; Other Built Projects; Earlier Experiments & Learning. No empty placeholder.
- New primary routes: `/jee/`, `/tokenizers/`, `/hinglish/`.
- Six concise project-note routes under `/projects/`: `drishya`, `contextfair`, `lumen`, `football-rule-cite`, `twistlab`, `news-classifier`.
- Shared CSS: existing colors and font families, responsive cards, readable case-study layout, accessible tables, keyboard focus, visible skip link. Removed pointer-tracking JavaScript from portfolio pages.
- Titles, descriptions, canonical URLs, Open Graph/Twitter metadata, favicon, sitemap, robots file.
- Three original charts with source commit links and SHA-256 provenance. No fabricated screenshots or metrics.
- Site README and a repeatable structural/link/asset checker.

`CNAME`, `/llamajee/`, archived designs, and existing application deployments are preserved. All six files named by the solver’s deployment hash manifest match their recorded SHA-256 values.

## Evidence review

Case-study sources were inspected from repository commits, and citations preserve those revisions. The copied chart manifest records exact source paths.

- LlamaJEE: every table value was checked against `history.csv`. Strict answers, coordinator procedure ratings, and capped responses remain separate. No adapter promotion is claimed. Conversion parity is presented separately from model quality; image mistakes and hardware limits remain visible.
- Tokenizers: 100 originals plus 40 JSON variants; eight configurations; 1,120 saved encodings. Ratios and language strata were checked against the two October 19 reports. The page distinguishes same-input comparisons, controlled JSON formatting, shared tokenizer components, Python decoding, and cross-runtime encoding. It does not claim a study app or full-prompt benchmarks.
- Hinglish: all six Macro F1 means and sample standard deviations were checked against the saved summary CSV. Matched multi-seed, earlier seed-42 transfer, and threshold diagnostics remain separate. Split variation, evaluation reuse, collapsed mixtures, and error-analysis limitations are explicit.
- Built projects: descriptions and lessons follow their current READMEs. Football Rule Cite is labelled a static sample; Lumen is a desktop application. ContextFair is distinct from the research study. The unavailable API is not advertised as a live demo.

## Verification completed

- Structural checker: 11 portfolio pages, 187 local references, no missing local files or fragment targets; one main landmark and H1 per page; descriptions, canonicals, social metadata, image alternatives, and dimensions present.
- All 46 unique external destinations returned HTTP 200 after redirects. Connection prefetch hints are not page links and are excluded.
- Browser layout checks: all 11 pages at 320, 768, and 1280 CSS pixels; no document-level horizontal overflow. Desktop and phone screenshots inspected; table wrappers can scroll independently.
- Keyboard: skip link appears on focus and Enter moves focus to `main`. Navigation and case-study-to-solver links work.
- Source chart hashes and all six solver deployment hashes pass.
- LlamaJEE: live interface inspected; preserved local application tested for example insertion and 9B/0.8B selection. Multi-gigabyte model inference was not rerun. Earlier execution evidence is linked and labelled as saved evidence.
- ContextFair: public exact Qwen measurement reproduced the documented three-kept estimate versus one-kept measured-content plan for the default example.
- Drishya: prediction selection unlocks motion; simulation advances and reports conservation residuals.
- TwistLab: default four-move sequence completes with four moves in history.
- Football Rule Cite: corrected public preview produces the sample penalty explanation and Law 12/14 citations.
- Lumen: installation hub loads and identifies the local agent as offline. Native desktop operation was not tested or installed.

These are portfolio and application smoke checks, not a full accessibility audit, device certification, scientific replication, or model-quality evaluation. Font files still depend on Google Fonts, with system fallbacks.

## Deployment order

1. Review and merge the portfolio branch to `main`; the existing Pages deployment publishes it.
2. Verify the new public case-study routes after deployment.
3. Merge the dependent profile and project README branches so backlinks point to deployed pages.

No manual DNS, custom-domain, build-tool, or hosting configuration is required. New public case-study URLs will not resolve until the portfolio change is deployed. Do not merge README backlinks first. The obsolete API cannot be restored by a portfolio edit.
