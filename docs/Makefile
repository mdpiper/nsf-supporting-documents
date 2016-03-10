SOURCES=Hutton_Bio_Sketch.md \
		 	  Hutton_Collaborators_and_Affiliations.md  \
		 	  Hutton_Current_and_Pending.md  \
		 	  Hutton_Statement_of_Work.md \
		 	  Hutton_Budget_Justification.md  \
		 	  Hutton_Facilities_and_Equipment.md
DOCS=${SOURCES:.md=.docx}
.SUFFIXES : .md .docx

.md.docx:
	pandoc --to=docx $< -o $@

all: ${DOCS}

clean:
	rm -f ${DOCS}
