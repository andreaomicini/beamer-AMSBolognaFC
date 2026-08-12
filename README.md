# beamer-AMSBolognaFC

> A simple Beamer-LaTeX style for presentations by Alma Mater Studiorum (Cesena Campus)
> with Bologna FC standard colours

## author

* Andrea Omicini

## usage

```latex
\documentclass[presentation]{beamer}\mode<presentation>{\usetheme{AMSBolognaFC}}
```

Pass the `apice` option to the document class to enable the APICe BibTeX field:

```latex
\documentclass[presentation,apice]{beamer}\mode<presentation>{\usetheme{AMSBolognaFC}}
```

A ready-to-use presentation skeleton is available in
[beamer-AMSBolognaFC-template](https://github.com/andreaomicini/beamer-AMSBolognaFC-template).

## versioning

The style version is declared in `beamerthemeAMSBolognaFC.sty` as
`\stylemajor` / `\styleminor` / `\stylepatch`, giving `Major.Minor[.Patch]`.
`\stylepatch` is optional: comment it out to release as `Major.Minor`.

Releases are tagged `Major.Minor[.Patch]-<UTC time-stamp>`, with the time-stamp
appended automatically by the CI at release time. Two commits that both forget
to bump the version therefore still produce two distinct releases instead of
clashing on the same tag.

## licence

This work is distributed under the
[LaTeX Project Public License](LICENSE), version 1.3c or later, and has the
LPPL maintenance status `maintained`.

One file is **not** covered by that licence: `apalike-AMS.bst` is a modified,
renamed derivative of Oren Patashnik's `apalike.bst` (Copyright © 1988, 2010
Oren Patashnik) and remains subject to its own terms, which permit modification
and redistribution provided the resulting file is renamed — as it is here.
