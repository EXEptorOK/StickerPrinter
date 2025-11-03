import win32print
import win32api
import win32ui
import win32con

import fitz

from vars import width_p, height_p


def printPdf(pdf_path, printer_name, amount):
    try:
        if printer_name == "def":
            printer_name = win32print.GetDefaultPrinter()

        hprinter = win32print.OpenPrinter(printer_name)

        for i in range(amount):
            dc = win32ui.CreateDC()
            dc.CreatePrinterDC(hprinter)

            dc.SetMapMode(win32con.MM_ISOTROPIC)
            dc.SetWindowOrg((0,0))
            dc.SetWindowExt((width_p, height_p))
            dc.SetViewportOrg((0,0))
            dc.SetViewportExt((width_p, height_p))

            dc.startPage()
            dc.endPage()
        
        dc.EndDoc()
        win32print.ClosePrinter(hprinter)

    except Exception as e:
        print(f"Ошибка печати: {e}")
