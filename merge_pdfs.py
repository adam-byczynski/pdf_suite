#Program that merges PDFs in the order of them being written down in command-line

import sys
import fitz
import os
# import getopt

all_pdfs = sys.argv[1:]


def check_validity():
   
   print(len(all_pdfs))
   try:    
      len(all_pdfs) > 1
   except:
      print('usage: merge_pdfs.py first.pdf second.pdf third.pdf etc.')
      print("ERROR: You need at least 2 pdf files to use this program.")
      sys.exit(0)       
   
   # temp_list = []  
   
   # for index in range(0,len(all_pdfs)): 
   #    try:
   #       temp_list[index] = fitz.open(all_pdfs[index])
   #       temp_list[index].close()
   #    except:
   #       print("ERROR: Parsed files must have the format of .pdf.")
   #       sys.exit(0) 
   
   return
    

def merge_pdfs(pdfs_input):
       
   merged_pdf = fitz.open()
    
   for pdf in pdfs_input:
      with fitz.open(pdf) as mfile:
         merged_pdf.insertPDF(mfile)
         
   desired_name = input("How do you want to name the merged file: ")         
   merged_pdf.save(desired_name)
   merged_pdf.close()
   print("Merged pdf has been saved!")
   return   


def main():
   
   check_validity()
   merge_pdfs(all_pdfs)

   
main()
