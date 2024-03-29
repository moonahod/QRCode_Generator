import tkinter
import json
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import qrcode

root = Tk()

# window appearance
root['bg'] = 'blue'
root.title('Open QR Code Generator')
root.wm_attributes('-alpha', 0.8)
root.geometry('525x700')

# root.resizable(width=False, height=False)

# Functions
def dataget():
    code_data = dataField.get()
    data_check = f"Data you want to input is: {str(code_data)}"
    if not code_data:
        messagebox.showerror(title='Error', message='There is no data for QR code!')
    else:
        messagebox.showinfo(title='Check', message=data_check)


def generation_stuff():
    file_name = (filenameField.get())
    if not file_name:
        messagebox.showerror(title='Error', message='Necessarily add file name!')

    elif not dataField.get():
        messagebox.showerror(title='Error', message='There is no data for QR code!')

    elif not versionField.get():
        messagebox.showwarning(title='Warning', message='Necessarily add version for your QR code!')

    elif str(ecField.get()) == 'L':
        messagebox.showinfo(title='Check', message=f'You choose version: {int(versionField.get())}, '
                                                   f'error correction level: {str(ecField.get())} '
                                                   f'and file name: {str(file_name)}')
        filename = (filenameField.get())
        qr = qrcode.QRCode(
            version=versionField.get(),
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=5
        )
        qr.add_data(dataField.get())
        qr.make(fit=True)
        code = qr.make_image()
        code.save(filename+'.png')

        image = ImageTk.PhotoImage(Image.open(filename+'.png'))
        image_label = Label(target_frame, image=image)
        image_label.image = image
        image_label.pack()

    elif str(ecField.get()) == 'M':
        messagebox.showinfo(title='Check', message=f'You choose version {int(versionField.get())}, '
                                                   f'error correction level: {str(ecField.get())} '
                                                   f'and file name: {str(file_name)}')
        filename = (filenameField.get())
        qr = qrcode.QRCode(
            version=versionField.get(),
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=5
        )
        qr.add_data(dataField.get())
        qr.make(fit=True)
        code = qr.make_image()
        code.save(filename+'.png')

        image = ImageTk.PhotoImage(Image.open(filename+'.png'))
        image_label = Label(target_frame, image=image)
        image_label.image = image
        image_label.pack()

    elif str(ecField.get()) == 'Q':
        messagebox.showinfo(title='Check', message=f'You choose version {int(versionField.get())}, '
                                                   f'error correction level: {str(ecField.get())} '
                                                   f'and file name: {str(file_name)}')
        filename = (filenameField.get())
        qr = qrcode.QRCode(
            version=versionField.get(),
            error_correction=qrcode.constants.ERROR_CORRECT_Q,
            box_size=10,
            border=5
        )
        qr.add_data(dataField.get())
        qr.make(fit=True)
        code = qr.make_image()
        code.save(filename+'.png')

        image = ImageTk.PhotoImage(Image.open(filename+'.png'))
        image_label = Label(target_frame, image=image)
        image_label.image = image
        image_label.pack()

    elif str(ecField.get()) == 'H':
        messagebox.showinfo(title='Check', message=f'You choose version: {int(versionField.get())}, '
                                                   f'error correction level: {str(ecField.get())} '
                                                   f'and file name: {str(file_name)}')
        filename = (filenameField.get())
        qr = qrcode.QRCode(
            version=versionField.get(),
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=5
        )
        qr.add_data(dataField.get())
        qr.make(fit=True)
        code = qr.make_image()
        code.save(filename+'.png')

        image = ImageTk.PhotoImage(Image.open(filename+'.png'))
        image_label = Label(target_frame, image=image)
        image_label.image = image
        image_label.pack()

    else:
        messagebox.showwarning(title='Warning', message='Necessarily add error correction level for QR code!')


# General frames
outer_frame = Frame(root, height=700, width=525, bg='blue')
outer_frame.pack(fill=BOTH, expand=1)

target_frame = Frame(root, bg='blue')
target_frame.pack()

# Canvas
canvas1 = Canvas(outer_frame, height=850, width=510, bg='blue')
canvas1.pack_configure(side=LEFT, fill=BOTH, expand=1)

# Scrollbar
scrollbar = tkinter.Scrollbar(outer_frame, orient=VERTICAL, command=canvas1.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure canvas
canvas1.configure(yscrollcommand=scrollbar.set)
canvas1.bind(
    '<Configure>', lambda e: canvas1.configure(scrollregion=canvas1.bbox('up'))
)

# Frames
frame_welcoming = Frame(target_frame, bg='blue')
frame_welcoming.pack()

frame_data_input = Frame(target_frame, bg='blue')
frame_data_input.pack()

frame_title_version_input = Frame(target_frame, bg='blue')
frame_title_version_input.pack()

frame_version_input = Frame(target_frame, bg='blue')
frame_version_input.pack()

frame_title_EC_input = Frame(target_frame, bg='blue')
frame_title_EC_input.pack()

frame_Entry_EC = Frame(target_frame, bg='blue')
frame_Entry_EC.pack()

frame_name_alert = Frame(target_frame, bg='blue')
frame_name_alert.pack()

frame_generate_btn = Frame(target_frame, bg='blue')
frame_generate_btn.pack()

# Entry fields
dataField = Entry(frame_data_input, bg='light grey')
dataField.pack()

filenameField = Entry(frame_generate_btn, bg='light grey')
filenameField.pack()

versionField = Entry(frame_version_input, bg='light grey')
versionField.pack()

ecField = Entry(frame_Entry_EC, bg='light grey')
ecField.pack()

# Welcoming
title_main = Label(frame_welcoming, height=3, width=50, text='Welcome to open QR code generator!', bg='orange')
title_main.pack()

# Titles
title_welcoming = Label(frame_welcoming, height=2, width=50, text='Lets get started with making your own QR code!',
                        bg='white')
title_welcoming.pack()

title_input_data = Label(frame_welcoming, text='In the following field place data you want to put into your QR code ↓',
                         bg='white')
title_input_data.pack()

title_input_version = Label(frame_title_version_input, text='Choose version for your QR code (1..40) ↓', bg='white')
title_input_version.pack()

title_EC_input = Label(frame_title_EC_input, text='Now choose error correction level'
                                                  ' for your QR code (L, M, Q or H) ↓', bg='white')
title_EC_input.pack()

title_file_name = Label(frame_name_alert, text='Now create the file name for your QR code', bg='white')
title_file_name.pack()

# Buttons
btn_data = Button(frame_data_input, height=1, width=7, text='Check data', bg='white', command=dataget)
btn_data.pack()

btn_gencode = Button(frame_generate_btn, height=1, width=10, text='Generate', bg='white', command=generation_stuff)
btn_gencode.pack()

canvas1.create_window((0, 0), window=target_frame, anchor="nw")
root.mainloop()
