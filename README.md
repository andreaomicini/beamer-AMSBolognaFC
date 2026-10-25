# beamer-AMSBolognaFC

![AMSBolognaFC Beamer style logo](logo/amsbolognafc-style-full.svg)

> A simple Beamer-LaTeX style for presentations by Alma Mater Studiorum —
> Università di Bologna, in the colours of Bologna FC

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

**No option, no watermark.** Pass `bologna` for a deck of the Alma Mater, which
watermarks the slides with the Ateneo seal, or `cesena` for one of the Campus di
Cesena, which uses the Campus seal instead:

```latex
\documentclass[presentation,bologna]{beamer}\mode<presentation>{\usetheme{AMSBolognaFC}}
\documentclass[presentation,cesena]{beamer}\mode<presentation>{\usetheme{AMSBolognaFC}}
```

The seals are institutional marks, so a deck has to claim one out loud: leaving
the option out is what anyone not belonging — or no longer, or not yet
belonging — to the Alma Mater Studiorum — Università di Bologna should do, and
the style is theirs to use with no logo on the slides at all. **Up to 1.7 the
Cesena seal was always there**: a deck that wants it back adds `cesena`.

A ready-to-use presentation skeleton is available in
[beamer-AMSBolognaFC-template](https://github.com/andreaomicini/beamer-AMSBolognaFC-template).

## relation to beamer-AMSUniBo

[beamer-AMSUniBo](https://github.com/andreaomicini/beamer-AMSUniBo) began as this
style with a different palette, and went on to gain features of its own. Since
1.8 this style has them too — everything but the colours and the faces, which
stay Bologna FC's and Computer Modern's:

* the `bologna` and `cesena` options, with no seal by default;
* the two seals as AMSUniBo carries them — grey, at 18%, the same 538 bp disc at
  the same anchor — so that `almacesena-background.pdf` is now visibly there
  rather than at the 10% it used to have;
* `\ccite` and `\cccite` take `\cite`'s optional note;
* `\speaker` and `\sspeaker` are bold, and `\sspeaker` inherits its surface's
  colour;
* DOIs resolve through `https://doi.org`;
* the APICe marker reads `APICe`, without parentheses or italic;
* the bibliography ranks an entry: the key is a quiet pointer, the title bold.

Since 1.10 `apalike-AMS.bst` is AMSUniBo 1.7.3's, and with it come a `talk`
entry type for APICe's Talks, APICe's theses, and a `subtitle` printed after the
title past a colon; the theme gains the talk and thesis markers `\apicetalkpar`
and `\apicethesispar`. The
[AMSUniBo README](https://github.com/andreaomicini/beamer-AMSUniBo#subtitles)
describes all three.

## structure

<!-- markdownlint-disable MD013 -->
| file | what it is |
| --- | --- |
| `beamerthemeAMSBolognaFC.sty` | the theme: the `apice` and `bologna`/`cesena` options, the beamer templates and colour assignments, the commands below, and the workarounds a deck would otherwise have to carry itself |
| `beamercolorthemebolognafc.sty` | the palette alone — `bolognafcblue`, `bolognafcred`, `bolognafcsilver`, `bolognafcwhite` — loaded by the theme |
| `almabologna-background.pdf` | the background under the `bologna` option: the Ateneo seal in grey, as a watermark cropped at the lower-right corner |
| `almacesena-background.pdf` | the same, with the Campus di Cesena seal, for the `cesena` option |
| `apalike-AMS.bst` | the bibliography style, a renamed derivative of `apalike.bst`, with titles emboldened (see [the references frame](#the-references-frame) and the licence note below) |

<!-- markdownlint-enable MD013 -->

Every release attaches a `style.zip` holding all five plus the `LICENSE`, so
the archive is enough to typeset with on its own.

Beyond the beamer furniture, the theme defines:

<!-- markdownlint-disable MD013 -->
| command | for |
| --- | --- |
| `\speaker` `\sspeaker` | marking the actual speaker among the authors, in the long and short forms, both in bold. Safe in `\author`: the name still reaches the PDF `/Author` field, only the markup is dropped |
| `\ccite` `\cccite` | superscript citations, in two weights; both take `\cite`'s optional note, as in `\ccite[p.~42]{key}` |
| `\uurl` `\uuurl` | URLs, in two sizes; since 1.7.5 no character in the address needs escaping |
| `\ddoi` `\dddoi` | DOIs, linked, in two sizes; since 1.7.5 no character in the DOI needs escaping |
| `\apicepubpar` | the APICe marker; defined either way, but expands to nothing unless the `apice` option is given |
| `\apice` `\aapice` | an APICe object — publication, talk, course, event — by its kind and its page name, printed as its short address and linked; since 1.9 |
| `\apicesite` `\aapicesite` | an APICe alias host, such as `andreaomicini.apice.unibo.it`; since 1.9 |
| `\apicepage` `\aapicepage` | any other APICe page, by its space and page path; since 1.9 |
| `\aalert` | a quieter alternative to `\alert` |

<!-- markdownlint-enable MD013 -->

The three APICe commands are AMSUniBo's, from its 1.7 — see
[its README](https://github.com/andreaomicini/beamer-AMSUniBo#apice-addresses)
for the kinds, the aliases and the optional text.

Since 1.7.5 the four address commands **string their argument before using
it**, so `\ddoi{10.1007/978-3-032-22940-3_12}` and
`\ddoi{10.1007/978-3-032-22940-3\_12}` give the same link and the same text.
Stringing turns every token into an ordinary character, so an `_` no longer asks
for maths mode; every backslash is then dropped, which is what makes the two
spellings equivalent, and what a DOI never needs to keep. It matters most in the
bibliography, where nobody gets to escape anything: `apalike-AMS.bst` copies the
`doi` and `url` fields into the `.bbl` verbatim, and a Springer LNCS chapter DOI
ends in `_<chapter>`. The work is done when the command runs, not by reading the
argument verbatim as `\url` does, and that is forced by beamer: a frame body is
tokenised when the frame is read, before anything in it runs, so a catcode trick
would make every frame citing a DOI `fragile`.

The theme also declares a small-caps substitution for the sans font and
neutralises `\speaker`, `\sspeaker`, `\ccite`, `\cccite`, `\uurl`, `\uuurl`,
`\ddoi`, `\dddoi`, `\translate` and `\\` inside hyperref's PDF strings, so decks
build without the font-shape and PDF-string warnings that otherwise appear. A
citation says nothing in a bookmark, so `\ccite` and `\cccite` go entirely, note
and all; their replacement is expandable, since an unexpandable one would have
hyperref drop the name alone and leave `[p.~42]{key}` behind as literal text.
The four address
commands are neutralised there because a PDF string is expanded before the
stringing above can run: a URL keeps its address, a DOI becomes `DOI:<doi>`, and
a bare `_` is still dropped with *Token not allowed in a PDF string* — as it is
in plain text — so `\_` remains the spelling that survives in a `\title` or a
`\section`.

**`\speaker` and `\sspeaker` are bold**, since 1.8. Colour alone did not single
the speaker out well, and `\sspeaker` made things worse: light italic on the
footline, it read *quieter* than the co-authors beside it. It now has no colour
of its own and inherits its surface's, so it works on the footline and on a
light surface alike.

## the references frame

An entry's citation key and its title used to read as the same kind of thing:
beamer parents `bibliography item` on `item`, which this style sets to red for
bullets, so the key came out red beside a red title. Since 1.8 the key is a
muted blue-grey — a pointer, not a bullet — and `apalike-AMS.bst` emboldens the
title, through an `embolden` function applied where an article or a book title is
formatted. Doing it in the `.bst` rather than the theme is deliberate: beamer
parents the author, location and note fonts on the title's, so bolding the
title there would bold the whole entry.

No block of an entry ends in a full stop, since the next one starts on a new line
anyway. The APICe marker carries its own trailing gap, outside the link, so that
the DOI or URL after it no longer runs into it: the `.bst` puts two spaces there,
but BibTeX wraps the `.bbl` line at exactly that point and they collapse into one.

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
