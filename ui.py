import tkinter

def clear_window():
    for objects in main_window.winfo_children():
        objects.destroy()

def merge_PDFs_window():
    
    clear_window()
    label = tkinter.Label(main_window, text = "Welcome to the PDF_Suite").pack()

    page = tkinter.Label(main_window, text = "Page of split:").place(x = 30,y = 50)
    enter_page_nr = tkinter.Entry(main_window).place(x = 110,  y = 50)
    name = tkinter.Label(main_window, text = "Select PDF file:").place(x = 30,y = 80)
    select_pdf_file = tkinter.Entry(main_window).place(x = 110,  y = 80)
    
    main_window.mainloop() #responsible for window popping up


def split_page_window():
    
    clear_window()
    label = tkinter.Label(main_window, text = "Welcome to the PDF_Suite").pack()
    
    page = tkinter.Label(main_window, text = "Page of split:").place(x = 30,y = 50)
    enter_page_nr = tkinter.Entry(main_window).place(x = 110,  y = 50)
    name = tkinter.Label(main_window, text = "Select PDF file:").place(x = 30,y = 80)
    select_pdf_file = tkinter.Entry(main_window).place(x = 110,  y = 80)
    
    main_window.mainloop() #responsible for window popping up

# def back_to_main_menu():
    

def initial_setup():
    
    main_window.title("PDF_Suite")
    
    main_window.geometry("800x600")
    main_window.mainloop() #responsible for window popping up
    
#main program body    
    
main_window = tkinter.Tk() #program window

label = tkinter.Label(main_window, text = "Welcome to the PDF_Suite").pack()

#scripts buttons
select_merge_scrpt_bt = tkinter.Button(text = "Merge PDFs Script", command = merge_PDFs_window).place(x = 400,y = 50)
select_split_at_page_scrpt_bt = tkinter.Button(text = "Split At Page Script").place(x = 400,y = 80)
another_bt = tkinter.Button(text = "anoder").place(x = 400,y = 110)   
    
initial_setup() #do usuniecia bo bedzie odpalane w innym skrypcie
