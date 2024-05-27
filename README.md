# Best practices

## Data naming conventions

- No spaces (use “-”, “_”, or casing to convey breaks)
- Folder name starting with “YYMMDD_” for alphabetically-sortable chronology (e.g., “240506_PDMS-loading-DMA-workup”)
- Encode data in file name to decode in script (sample type, weight, iteration, etc., e.g., PDMS_3-45cm_3.csv)
- For complex projects (maybe >100 lines), keep the workflow modular with functions, cells, or scripts exposing each component as a separate step, e.g.:
  - Step 1: consolidate multiple files into a single one
  - Step 2: apply corrections, normalization, smoothing, etc.
  - Step 3: extract statistics and show plots
  - Step 4: export resulting data to another fileset

## Hotkeys

- F2 (rename symbol)
- Ctrl + F5 (run script in the active window)
- Ctrl + ~ (toggle between console and workspace)
- Ctrl + K, S (save all in workspace)
- Ctrl + K, P (copy path of active file)
- Ctrl + K, R (reveal active file in file explorer)
- Ctrl + K, Z (zen mode)
- Ctrl + tab (next window)
- Ctrl + +/- (zoom in/out)
- Ctrl + left/right arrow (move cursor across a symbol)
- Ctrl + shift + left/right arrow (highlight across symbols)
- Ctrl + X (cut, but even for an entire line)
- Ctrl + U (undo last cursor operation)
- Alt + up/down arrow (move a line up/down)
- Alt + left click (multi-line edit)
- Shift + left click (highlight between cursor and click position)

## Quality of Life

- Hovering over library modules for the hint panel (descriptions/arguments)
- Multi-windows snap to parts of page and detach from window
- Right click → copy relative path
- Preview readme
- Highlighting + brackets (“(“, “{“, or “[“) completes bracket around the item
- Moving windows (e.g., readme preview → second monitor)
- Common files on the root directory (e.g., “SharedModules.py” and colorDict.txt”) can be helpful, but they should be copied into project folders before sharing them

## Extensions

- Intellisense from language extensions and copilot
- Live Share (YT Video)
- Themes (Atom One Dark)
- “Better Comments”
- CSVs: “CSV to Table”, “Rainbow CSV”

## Emulating Spyder Functionality

Create modular “cells” to run independent of other script components using “#%%”
This should open the “Jupyter variables” and “Interactive” windows automatically

## Terminal

Commands:
- ls (list contents)
- cd (change directory)
- mkdir (make directory)

Hotkeys:
- Up arrow (cycle previous commands)
- Tab (cycle auto-complete)

## General Windows Hotkeys

### Ctrl + 

- c (copy)
- x (cut)
- v (paste)
- z (undo)
- a (select all)
- f (find/search)
- t (new tab)
- Tab (next browser tab)
- r (refresh)
- k (hyperlink)
  
### Windows + 

- Shift + s (snip region + copy to clipboard)
- v (clipboard history)
  
### Alt +

- Tab (cycle open applications)
- F4 (close window), Space (system menu for application)
- F (file menu for applications)
- Left/Right Arrow (backwards/forward history)
- D (highlight address bar)

### Function keys

- F2 (rename)
- F5 (refresh)
- F11 (full screen)

### Middle mouse click

- Link (open in new tab), tab (close tab)

## 
And always remember The Zen of Python