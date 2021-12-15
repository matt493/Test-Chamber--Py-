def getDirName():
    import tkinter
    from tkinter import filedialog

    root = tkinter.Tk()
    root.withdraw()

    path = ''
    while path == '':
        print('SELECT BASE DIRETORY!')
        path = filedialog.askdirectory()

    return str.replace(path, '/','//')

print("DIR: ", getDirName())