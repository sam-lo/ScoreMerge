# PDF Merger

This Python script merges PDF files from a specified directory and its subdirectories. It uses the `tkinter` library to prompt the user to select a directory and the `PyPDF2` library to handle PDF operations.

## Requirements

- Python 3.x
- `tkinter` library (usually included with Python)
- `PyPDF2` library

## Installation

1. Install Python 3.x from the [official website](https://www.python.org/).
2. Install the `PyPDF2` library using pip:
    ```sh
    pip install PyPDF2
    ```

## Usage

1. Run the script:
    ```sh
    python main.py
    ```
2. A dialog will appear asking you to select the main directory containing the PDF files.
3. The script will merge all PDF files in the selected directory and its subdirectories into a single PDF file named `Merged.pdf` in the main directory.

## How It Works

1. The script prompts the user to select a directory using `tkinter.filedialog.askdirectory()`.
2. It scans the selected directory for subdirectories (sessions) and sorts them.
3. It initializes a `PdfMerger` object from the `PyPDF2` library.
4. It merges all PDF files in a subdirectory named `Percussion`.
5. For each session subdirectory, it prompts the user to input the number of pieces needed for each part and merges the specified number of pieces.
6. The merged PDF is saved as `Merged.pdf` in the main directory.

## Notes

- Ensure that the directory structure is correctly set up with subdirectories and PDF files.
- The script assumes that the `Percussion` subdirectory exists within the main directory.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
