# source et annexes - Markdown
SOURCES = memoire sujet resume etat_de_l_art strategie resultats conclusion annexes
# document à générer - PDF
PROJET_MEMOIRE = memoire
BIBLIO = bibliographie

#------------------------------
# a priori, ne pas modifier au delà
#------------------------------------------------------------

# config pandoc
PANDOC = pandoc
LATEX = pdflatex
ifndef BIBLIO
PANDOCOPT = --template=template.latex \
	    --listings \
	    --pdf-engine=$(LATEX) \
	    --toc \
	    -V "geometry:a4paper, margin=2cm" \
	    -V "fontsize:12pt" \
	    -V "includeheadfoot" \
	    -V "lang:fr-FR" \
			-F mermaid-filter \
		-f markdown+hard_line_breaks \
	    -s
else
PANDOCOPT = --template=template.latex \
	    --listings \
	    --pdf-engine=$(LATEX) \
	    --toc \
	    --bibliography $(BIBLIO).bib \
		--citeproc \
	    -V "geometry:a4paper, margin=2cm" \
	    -V "fontsize:12pt" \
	    -V "includeheadfoot" \
	    -V "lang:fr-FR" \
			-F ./node_modules/.bin/mermaid-filter \
		-f markdown+hard_line_breaks \
	    -s

endif
# generic rules
%.pdf: %.md
	$(PANDOC) $(PANDOCOPT) -o $@ $<

%.tex: %.md
	$(PANDOC) $(PANDOCOPT) -o $@ $<

%.rtf: %.md
	$(PANDOC) $(PANDOCOPT) -o $@ $<

# cible principale
.PHONY : all
all : $(PROJET_MEMOIRE).pdf

$(PROJET_MEMOIRE).pdf : $(addsuffix .md, $(SOURCES))
	$(PANDOC) $(PANDOCOPT) -o $@ $^

$(PROJET_MEMOIRE).tex : $(addsuffix .md, $(SOURCES))
	$(PANDOC) $(PANDOCOPT) -t latex -o $@ $^

$(PROJET_MEMOIRE).rtf : $(addsuffix .md, $(SOURCES))
	$(PANDOC) $(PANDOCOPT) -t rtf -o $@ $^

# nettoyage
.PHONY: clean
clean :
	$(RM) $(PROJET_MEMOIRE).pdf
	$(RM) $(PROJET_MEMOIRE).tex
