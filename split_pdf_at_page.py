#Program that splits given PDFs at the desired page, and then outputs two remaining files 

import sys
import fitz
import os

pdf_file = sys.argv[1]
split_page = int(sys.argv[2])

# def check_validity():

#    # for index in range(0,len(all_pdfs)): 
#    #    try:
#    #       temp_list[index] = fitz.open(all_pdfs[index])
#    #       temp_list[index].close()
#    #    except:
#    #       print("ERROR: Parsed files must have the format of .pdf.")
#    #       sys.exit(0) 


# #    try:    
# #       split_page is int
# #    except:
# #       print('usage: split_pdf_at_page.py given_file.pdf <page number>')
# #       print("ERROR: You need to input one pdf file and splitting page to use this program.")
# #       sys.exit(0)    
   
# #    return


def split_pdf(pdf_to_split,split_page):
       
   split_pdf = fitz.open(pdf_to_split)    
   first_part = fitz.open()
   second_part = fitz.open()
   
   first_part.insert_pdf(split_pdf, to_page = split_page-1)
   second_part.insert_pdf(split_pdf, from_page = split_page)
   split_pdf.close()
         
   first_name = input("How do you want to name the first file(name.pdf): ")         
   first_part.save(first_name)
   first_part.close()
   
   second_name = input("How do you want to name the second file(name.pdf): ")
   second_part.save(second_name)
   second_part.close()
   
   print("PDF has been split and both parts were saved!")
   return   


def main():
       
   print("Program that splits given PDFs at the desired page(including), and then outputs two remaining files.")
   # check_validity()
   split_pdf(pdf_file,split_page)

   
main()
