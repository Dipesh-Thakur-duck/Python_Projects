#!/home/dipesh-thakur/Documents/python_projects/venv/bin/python
# exMCB.pyw - Saves and loads pieces of text ot the clipboard
# Usage:
# exMCB.pyw save <keyword> - Saves clipboard to keyword.
# exMCB.pyw <keyword> - Loads keyword to clipboard.
# exMCB.pyw list - Loads all keywords to clipboard.
# exMCB.pyw delete - clears all the values
# exMCB.pyw delete <keyword> - deletes the keyword


import shelve, pyperclip, sys

mcbShelf = shelve.open('exMCB')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]
        print('Keyword deleted!')
    else:
        print(f"Keyword '{sys.argv[2]}' not found.")
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
        print('File cleared!')
    elif sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()
