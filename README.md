# STXBooks

STXBooks is a simple REST API based on Django Rest Framework that allows you to browse through google's book volumes from <https://www.googleapis.com/books/v1/volumes>

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install STXBooks.

```bash
pip install -r requirements.txt
```

## Usage

You can visit this working API at <http://makskalek.pythonanywhere.com>

### Available paths are
* /db - send a POST request that will populate the database with books from <https://www.googleapis.com/books/v1/volumes> with body {'q', 'war'} (as specified in this task's documentation)
* /books/4 - view a specific book, where the number is an integer that is the id of the book
* /books - get the list of all books

With /books you can also filter and sort the results
* ?published_date=1999 will return all of the books from 1999
* ?sort=published_date will sort all of the books by their date of publishing
* ?author="Sebastian Junger"&author="P. W. Singer" will return all of the books written by one of these authors




