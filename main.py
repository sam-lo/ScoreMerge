from tkinter.filedialog import askdirectory
import PyPDF2 as pdf
import os

mainFolder = askdirectory()  # askdirectory()
Merged = mainFolder + "/Merged.pdf"
sessions = sorted([f.path for f in os.scandir(mainFolder) if f.is_dir()])  # List of session folders
merger = pdf.PdfMerger()

percussion = mainFolder + "/Percussion"
percussionParts = sorted([f.path for f in os.scandir(percussion)])
for part in percussionParts:
    file = open(part, "rb")
    merger.append(pdf.PdfReader(file))

for session in sessions:  # Each session folder
    print(f'Current session: {session.split("/")[-1]}')
    parts = sorted([f.path for f in os.scandir(session)])  # List of Parts in folder
    for part in parts:  # Each part
        fileName = part.split("-")[-1].split(".")[0]
        piece = input(f'Pieces needed for {fileName}: ')
        if piece != "":
            file = open(part, "rb")
            for i in range(int(piece)):
                merger.append(pdf.PdfReader(file))

merger.write(Merged)
merger.close()
