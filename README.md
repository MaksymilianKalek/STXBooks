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
* /authors - get the list of all authors
* /categories - get the list of all categories
* /books - get the list of all books

Additionally, you can view specific book, author, category by visiting the url with an integer that represents the id of the object
* For example /books/2

With /books you can also filter and sort the results
* ?published_date=1999 will return all of the books from 1999
* ?sort=published_date will sort all of the books by their date of publishing
* ?author="Sebastian Junger"&author="P. W. Singer" will return all books written by one of these authors




