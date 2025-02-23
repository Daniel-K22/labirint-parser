# Labirint Parser
A simple parser for the Labirint.ru website that collects book data (title, author, price) and saves it to a CSV file.

## Features
- Parsing books from Labirint.ru with a customizable number of items.
- Bypassing blocks using random User-Agent and delays.
- Displaying data in a table and saving it to a CSV file.

## Installation
### 1. Clone the repository:  
```bash
 git clone https://github.com/Daniel-K22/labirint-parser.git 
```
### 2. Install dependencies:
```bash
pip install -r requirementes.txt
```
### 3.Run the parser:
```bash
python parser.py
```

## Usage
1. Launch the script.
2. Choose the site (1 for Labirint.ru or enter your own URL).
3. Specify how many books to parse.
4. Get a table and the books_data.csv file with results.

## Technologies
- Python
- Requests, BeautifulSoup4, Tabulate

## Author
Daniel-K22 - developer with experience in parsing and automation.