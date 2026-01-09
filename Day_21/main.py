from sqlmodel import SQLModel, Field, create_engine, Session, Relationship, select

engine = create_engine("sqlite:///orm.db")

class Author(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=50)
    email: str = Field(max_length=50)

    books: list["Book"] = Relationship(back_populates="author")

class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    content: str
    author_id: int = Field(foreign_key='author.id')

    author: Author = Relationship(back_populates='books')

SQLModel.metadata.create_all(engine)

with Session(bind=engine) as session:
    author1 = Author(name="Alice", email="alice@example.com")
    author2 = Author(name="Bob", email="bob@example.com")
    Book1 = Book(title="My first book", content="Author of this book is Alice", author = author1)
    Book2 = Book(title="My second book", content="Author of this book is Alice (2nd Book)", author = author1)
    Book3 = Book(title="Bob's first book", content="Author of this book is Bob", author = author2)

    session.add_all([author1, author2, Book1, Book2, Book3])
    session.commit()

with Session(bind=engine) as session:
    statement = select(Book)
    results = session.exec(statement).all()
    print(results)

with Session(bind=engine) as session:
    statement = select(Book).where(Book.title == "My first book")
    books = session.exec(statement).all()
    for book in books:
        print(book)

with Session(bind=engine) as session:
    statement = select(Book, Author).join(Author)
    books_with_authors = session.exec(statement).all()

    for book, author in books_with_authors:
        print(f"Book: {book.title}, Author: {author.name}")

with Session(bind=engine) as session:
    book_to_update = session.exec(select(Book).where(Book.title == "My first book")).first()
    if book_to_update:
        book_to_update.title = "My Updated first book"
        session.add(book_to_update)
        session.commit()
        session.refresh(book_to_update)
        print(f"Updated book: {book_to_update.title}")

with Session(engine) as session:
    statement = select(Book).where(Book.title == "My first book")
    book_to_delete = session.exec(statement).first()

    if book_to_delete:
        session.delete(book_to_delete)
        session.commit()