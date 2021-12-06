from app import app, db, routes
from app.models import Author, Book, Borrowed

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "Author": Author,
       "Book": Book,
       "Borrowed": Borrowed
   }