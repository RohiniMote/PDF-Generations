from django.shortcuts import render
from fpdf import FPDF
from django.http import FileResponse
#from PyPDF2 import PdfFileWriter, PdfFileReader
# Create your views here.

def PdfView(request):
    context={}
    template_name="app1/pdf.html"

    return render(request,template_name,context)

def ReportView(request):
    
    sales = [
        {"Roll No": "1", "Name": "Rohini","Marks":'88'},
        {"Roll No": "2", "Name": "Rana","Marks":"77"},
        {"Roll No": "3", "Name": "Arjun","Marks":"65"},
        {"Roll No": "4", "Name": "Nikhil","Marks":"78"},
        {"Roll No": "5", "Name": "Roshni","Marks":"80"},
        {"Roll No": "6", "Name": "Komal","Marks":"75"},
    ]
    
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('courier', 'B', 16)
    pdf.cell(40, 10, 'This is what you have sold this month so far:',0,1)
    pdf.cell(30, 10, '',0,1)
    pdf.set_font('courier', '', 12)
    pdf.cell(150, 8, f"{'Roll No'.ljust(20)} {'Name'.rjust(20)} {'Marks'.rjust(20)}", 0, 1)
    pdf.line(10, 30, 200, 30)
    pdf.line(10, 38, 200, 38)
    for line in sales:
        pdf.cell(150, 8, f"{line['Roll No'].ljust(20)} {line['Name'].rjust(20)} {line['Marks'].rjust(20)}", 0, 1)

    pdf.output('report.pdf', 'F')
    return FileResponse(open('report.pdf', 'rb'), as_attachment=True, content_type='application/pdf')


''' 
# create a PdfFileWriter object
out = PdfFileWriter()
  
# Open our PDF file with the PdfFileReader
file = PdfFileReader("report.pdf")
  
# Get number of pages in original file
num = file.numPages
  
# Iterate through every page of the original 
# file and add it to our new file.
for idx in range(num):
    
    # Get the page at index idx
    page = file.getPage(idx)
      
    # Add it to the output file
    out.addPage(page)
  
  
# Create a variable password and store 
# our password in it.
password = "pass"
  
# Encrypt the new file with the entered password
out.encrypt(password)
  
# Open a new file "myfile_encrypted.pdf"
with open("report_encrypted.pdf", "wb") as f:
    
    # Write our encrypted PDF to this file
    out.write(f)

from PyPDF2 import PdfFileWriter, PdfFileReader
  
# Create a PdfFileWriter object
out = PdfFileWriter()
  
# Open encrypted PDF file with the PdfFileReader
file = PdfFileReader("report_encrypted.pdf")
  
# Store correct password in a variable password.
password = "pass"
  
# Check if the opened file is actually Encrypted
if file.isEncrypted:
  
    # If encrypted, decrypt it with the password
    file.decrypt(password)
  
    # Now, the file has been unlocked.
    # Iterate through every page of the file
    # and add it to our new file.
    for idx in range(file.numPages):
        
        # Get the page at index idx
        page = file.getPage(idx)
          
        # Add it to the output file
        out.addPage(page)
      
    # Open a new file "myfile_decrypted.pdf"
    with open("report_decrypted.pdf", "wb") as f:
        
        # Write our decrypted PDF to this file
        out.write(f)
  
    # Print success message when Done
    print("File decrypted Successfully.")
else:
    
    # If file is not encrypted, print the 
    # message
    print("File already decrypted.")
'''