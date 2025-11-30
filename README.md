# seekpy
CLI utility to search for keywords across codebase

## Installation
`
git clone https://github.com/Ujjwal-Singh-20/SEEKPY.git
cd SEEKPY
python main.py --help
`

## Arguments in CLI

- `-p`, `-path` (required): Specify the full path of the directory or file to search.
- `-k`, `-keyword` (required): Define the keyword to search for within the specified directory or file.
- `-ext`, `-extension` (optional): Provide one or more file extensions to include in the search. Multiple extensions can be space-separated.

## Example usage

- Search in a directory   
`
python main.py -p "C:\Users\KIIT\Desktop\UJJU\PROJECT\82" -k DigitalHealthIdPage
`

-Search in a single file   
`
python main.py -p "C:\Users\KIIT\Desktop\UJJU\PROJECT\82\frontend\HealthPage.jsx" -k DigitalHealthIdPage
`

- Restrict search to specific extensions  
`
python main.py -p "C:\Users\KIIT\Desktop\UJJU\PROJECT\82" -ext .py .js .tsx .jsx -k DigitalHealthIdPage
`

## Example output
`
Keyword found in file pages App.jsx - line 9: // import DigitalHealthIdPage from "./pages/DigitalHealthIdPage";
`   
`
Keyword found in file pages App.jsx - line 35: import DigitalHealthIdPage from "./pages/DigitalHealthIdPage";
`

## Skipped file types
The tool automatically ignores binary/non-text formats such as:
`
[".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".ico", ".tiff", ".mp3", ".wav", ".mp4", ".avi", ".mov", ".mkv", ".zip", ".tar", ".gz", ".rar", ".7z", ".exe", ".dll", ".so", ".bin", ".class", ".o", ".ttf", ".otf", ".woff", ".woff2", ".pdf", ".docx", ".xlsx", ".pptx"]
`

