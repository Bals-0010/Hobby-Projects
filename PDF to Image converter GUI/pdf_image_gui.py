
class Pdf_to_Image_GUI:
    def __init__(self, window):
        self.window = window
        self.window.title("PDF to Image Converter")
        self.window.geometry("350x200")
        self.window.resizable()
        self.introlabel=Label(window,text="""Select the pdf document
( Only supported type: .pdf )\n""")
        self.introlabel.grid()
        self.browse_button = Button(window, text="Select your pdf file", command=self.browse_func)
        self.browse_button.grid()
        self.save_file = Button(window, text=" Save as image file ", command=self.save)
        self.save_file.grid()
        self.exit_button = Button(window, text="Exit the application", command=self.exit_func)
        self.exit_button.grid()
        
    
    def browse_func(self):
        self.filename = filedialog.askopenfilename(title="Select a file to upload", initialdir="/",\
            filetypes=( ('PDF Files', '*.pdf'),('All files', '*') ))
        
        if self.filename[-3:] == "pdf":
            messagebox.showinfo("Upload Success !","File Path:\n" + self.filename)
        else:
            messagebox.showerror("Invalid file","You must select a PDF file !")
        
     
    def save(self):
        location_to_save_files = filedialog.askdirectory()
        images = convert_from_path(self.filename, fmt= 'jpeg', poppler_path = "C:/Program Files/poppler-0.68.0/bin")
        
        try:
            if self.filename != "" or None:    
                for i, image in enumerate(images):
                    fname = location_to_save_files + "/image"+ str(i+1) +".png"
                    image.save(fname, "PNG")
                messagebox.showinfo("Save", "PDF converted into jpg file(s) in\n" + location_to_save_files)
            else:
                messagebox.showwarning("Warning","No file uploaded !")
        except AttributeError:
                messagebox.showwarning("Warning","No file uploaded !")
    
    def exit_func(self):
        self.window.destroy()
    
    
def main():
    window=Tk()
    Pdf_to_Image_GUI(window)
    window.mainloop()


if __name__=="__main__":
    from pdf2image import convert_from_path
    from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError)
    from tkinter import *
    from tkinter import filedialog, messagebox
    main()