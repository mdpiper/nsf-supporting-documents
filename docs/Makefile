MD_SOURCES= \
  Piper_Bio_Sketch.md \
  Piper_Current_and_Pending.md  \
  Piper_Statement_of_Work.md \
  Piper_Budget_Justification.md  \
  Piper_Facilities_and_Equipment.md \
  Piper_Results_from_Prior.md
CSV_SOURCES=Piper_Conflict_of_Interest.csv
DOCS= \
  ${MD_SOURCES:.md=.docx} \
  ${MD_SOURCES:.md=.pdf} \
  ${CSV_SOURCES:.csv=.docx} \
  ${CSV_SOURCES:.csv=.pdf}

.SUFFIXES : .md .csv .docx .pdf

.md.docx:
	pandoc --to=docx $< -o $@

.md.pdf:
	pandoc --to=latex $< -o $@

.csv.docx:
	../scripts/coi_to_caa.py $< | pandoc --to=docx -o $@

.csv.pdf:
	../scripts/coi_to_caa.py $< | pandoc --to=latex -o $@

all: ${DOCS}
	mv Piper_Conflict_of_Interest.docx Piper_Collaborators_and_Affiliations.docx
	mv Piper_Conflict_of_Interest.pdf Piper_Collaborators_and_Affiliations.pdf

clean:
	rm -f ${DOCS} Piper_Collaborators_and_Affiliations.{docx,pdf}
