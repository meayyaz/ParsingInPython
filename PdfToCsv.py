#!/usr/bin/python3 

import PyPDF2 
import csv


pdfFileObj = open('/Users/ayyaz/Downloads/TaxpayersDirectory2018.pdf', 'rb') 
  
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 

with open('/Users/ayyaz/Downloads/TaxpayersDirectory2018.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Sr.", "Taxpayer Name", "Registration No","Tax Paid"])
    for pageNum in range(1000, 35445, 100):
        pageObj = pdfReader.getPage(2000+pageNum) 
        data = pageObj.extractText()
        rows = data.split('\n')

        count=0
        data_row = list()
        for r in rows:
            if r.strip() == '':
                continue
            if(count%4==0):
                if(len(data_row)!=0 and data_row[0]!='Sr.' ): writer.writerow(data_row)
                data_row.clear()
            data_row.append(r.strip())
            count += 1