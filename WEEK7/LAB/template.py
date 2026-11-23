"""
RECORD CHECK  -  my version
===========================

Name  : RABIA SHAIKHANI
Lane  :  AI     
Date  :12-11-2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
def parse_line(raw_line):
    """Turn one messy raw status line into a clean dict."""
    line = raw_line.strip()
    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip().lower()

    records = {"hostname":hostname}
    for piece in rest.split(","):
        key, value = piece.split("=")
        records[key.strip().lower()] = float(value.strip())

    return records
#
def status_of(age):
    """Return not allowed and allowed based on the age."""
    
    if age <= 12 or age >= 35:
        return "not allowed"
    else:
        return "allowed"

# your function(s) go here


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.

raw_records = ["survey_2026, Rating=4,  age=23", 
               "suRvey_2026, Rating = 5, AGe=22",
               "  survey_2026,   rating=3, age=39",
               "survey_2026,   RATING=4, age=25",
               " survey_2026, rating  = 05, AGE =10"]   # replace with your code


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

for raw_record in raw_records:
    report= parse_line(raw_record) 
    status= status_of(report["age"])
    print(f"hostname: {report['hostname']}, rating: {report['rating']}, age: {report['age']}, status: {status}")


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
