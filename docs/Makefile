MD_SOURCES= \
  Hutton_Bio_Sketch.md \
  Hutton_Current_and_Pending.md  \
  Hutton_Statement_of_Work.md \
  Hutton_Budget_Justification.md  \
  Hutton_Facilities_and_Equipment.md \
	Hutton_Results_from_Prior.md
CSV_SOURCES=Hutton_Conflict_of_Interest.csv
DOCS=${MD_SOURCES:.md=.docx} ${CSV_SOURCES:.csv=.docx}

.SUFFIXES : .md .csv .docx

.md.docx:
	pandoc --to=docx $< -o $@

.csv.docx:
	../scripts/coi_to_caa.py $< | pandoc --to=docx -o $@

all: ${DOCS}
	mv Hutton_Conflict_of_Interest.docx Hutton_Collaborators_and_Affiliations.docx

clean:
	rm -f ${DOCS} Hutton_Collaborators_and_Affiliations.docx
