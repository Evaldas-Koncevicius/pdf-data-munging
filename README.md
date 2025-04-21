This Python script processes PDF files containing production and inventory reports, extracting key numerical data and generating a consolidated text output. 

Here's what it does:

1. Takes PDF files as command-line arguments and processes each one sequentially.

2. Uses pdftotext library to convert PDFs to readable text

3. Uses regex patterns to identify numerical data rows (^[,\d\s]+$)

4. Captures specific headers like "Reporting Period" and "Report Date" (including revised versions)

5. Organizes extracted numbers into logical groups for reporting

6. Creates/updates a file called file.txt containing extracted data (Reporting period, Report Date, Production figures, Stock on hand figures, Calculated sales for current month (derived from production and stock values))

[Input example](https://github.com/Evaldas-Koncevicius/pdf-data-munging/blob/main/Input%20example.pdf)

[Output exampl](https://github.com/Evaldas-Koncevicius/pdf-data-munging/blob/main/Output%20example.txt)

