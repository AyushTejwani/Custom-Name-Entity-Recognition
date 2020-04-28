import csv
 
with open("ner_dataset.csv",'r') as csvin, open("output.tsv", 'w', newline='') as tsvout:
    csvin = csv.reader(csvin)
    tsvout = csv.writer(tsvout, delimiter='\t')
 
    for row in csvin:
        tsvout.writerow(row)