# Chemicals Project 

## Chemical Mixer

### chemical-mixer dependiencies:
python3, flask, pubchempy, wolframalpha

### How to use chemical-mixer:
Open the "chemical-mixer" folder and install dependencies.
Run 

> main.py

Then open up 127.0.0.1:5000 in the browser. 
Input a PubChem CID to search. When each each search bar
has a PubChem CID, the "Mix" button can be selected. There
is a short wait as the the server makes an api call to 
wolframalpha. Sometimes this has a chance to give an error 
even if the chemicals can successfully be mixed. The 
solution is to select "Mix" again.

## Chemical Visualiszer

### How to use chemical-visualizer
Open the "chemical-visualizer" folder, then open "index.html" 
in your browser. This is just a demo of two hydrogen atoms.

## JSON Scraper

### JSON Scraper dependencies:
python3, pubchempy, flask

### How to use JSON Scraper
Open the "json-scraper" folder. Add PubChem CIDs to "list_of_cids" 
in "scrape.py." There are some already there to test out the 
functionality. Run 

> ./scrape.py

This should create a file, 
"test.json" that has the information of the chemicals stored in 
a JSON file.

## Multi PDF Parser

### Dependencies:
python, pdfminer

Requires a specific version of pdfminer to be installed.

> sudo pip install --upgrade --ignore-installed slate==0.3 pdfminer==20110515

### How to use:
Open the "multi-pdf-parser" folder. Create two folders, 'pdfs' and 'txt'. 
Place PDFs you need to be converted into the folder 'pdfs'. After running
> ./output.py

you should see the converted txt files in 'txt.'

