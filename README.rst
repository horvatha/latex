==========================================================================
Hungarian LaTeX examples and summary - Magyar LaTeX példák és összefoglaló
==========================================================================

Letöltés::

    git clone https://horvatha@github.com/horvatha/latex.git

A lefordított fájlok Linux alatt az evince (GNOME) vagy az okular (KDE)
esetleg az acroread (Adobe Reader) paranccsal nézhetőek meg. Pl::

    evince valami.pdf&

LaTeX röviden
=============

Egy rövid összefoglaló. Lefordítása és megtekintése::

    cd latex-roviden
    make
    evince latex-roviden.pdf&

Példák
======

A peldak könyvtárban találhatóak.

Lefordításuk, általában a pdflatex paranccsal történhet, van egy xelatex
kezdetű fájl, amit xelatex-hel::

    cd peldak
    pdflatex valami.tex
    xelatex xelatex_clipped_picture.tex

