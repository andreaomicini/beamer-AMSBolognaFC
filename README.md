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

## structure

| file | what it is |
|---|---|
| `beamerthemeAMSBolognaFC.sty` | the theme: the `apice` option, the beamer templates and colour assignments, the commands below, and the workarounds a deck would otherwise have to carry itself |
| `beamercolorthemebolognafc.sty` | the palette alone — `bolognafcblue`, `bolognafcred`, `bolognafcsilver`, `bolognafcwhite` — loaded by the theme |
| `almacesena-background.pdf` | the Alma Mater Cesena background image |
| `apalike-AMS.bst` | the bibliography style, a renamed derivative of `apalike.bst` (see the licence note below) |

Every release attaches a `style.zip` holding all four plus the `LICENSE`, so
the archive is enough to typeset with on its own.

Beyond the beamer furniture, the theme defines:

| command | for |
|---|---|
| `\speaker` `\sspeaker` | marking the actual speaker among the authors, in the long and short forms. Safe in `\author`: the name still reaches the PDF `/Author` field, only the colouring is dropped |
| `\ccite` `\cccite` | superscript citations, in two weights |
| `\uurl` `\uuurl` | URLs, in two sizes |
| `\ddoi` `\dddoi` | DOIs, linked, in two sizes |
| `\apicepar` | the APICe marker; defined either way, but expands to nothing unless the `apice` option is given |
| `\aalert` | a quieter alternative to `\alert` |

The theme also declares a small-caps substitution for the sans font and
neutralises `\speaker`, `\sspeaker`, `\translate` and `\\` inside hyperref's
PDF strings, so decks build without the font-shape and PDF-string warnings that
otherwise appear.

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
