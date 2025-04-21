import re
import pdftotext
import sys

with open ("file.txt", "w") as f:
    f.write("")

numbers = re.compile(r"^[,\d\s]+$")

for arg in sys.argv[1:]:

    infile = open(sys.argv[sys.argv.index(arg)], "rb")
    pdf = pdftotext.PDF(infile)
    lines = "".join(pdf).split("\n")
    numbers_in_file = []
    numbers_for_list = []
    reporting_period = None
    report_date = None
    

    for line in lines:
        if line.startswith("Reporting Period") or line.startswith("REVISED Reporting Period"):
            reporting_period = line

        elif line.startswith("Report Date") or line.startswith("REVISED Report Date"):
            report_date = line
        
        elif numbers.match(line):
            numbers_for_list.append(line)

        else:
            if len(numbers_for_list) != 0:
                numbers_in_file.append(numbers_for_list)
            numbers_for_list = []

    sales = int(numbers_in_file[0][0].replace(",", "")) - int(numbers_in_file[-2][0].replace(",", ""))

    with open ("file.txt", "a") as f:
        f.write(f"""
            {reporting_period}
            {report_date}

            Production Current Month - {numbers_in_file[0][0]}
            Production Prior Year Current Month - {numbers_in_file[1][0]}
            Production Current Year Cumulative to Date - {numbers_in_file[2][0]}
            Production Prior Year Cumulative to Date - {numbers_in_file[3][0]}

            Stock On Hand End-Of-Month Current Month - {numbers_in_file[-2][0]}
            Stock On Hand End-Of-Month Prior Year Current Month - {numbers_in_file[-1][0]}

            Current Month Sales - {sales:,}


            """)
        




