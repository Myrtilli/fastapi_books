from fastapi import HTTPException
from pydantic import BaseModel


from fastapi import FastAPI
import uvicorn

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Асинхронність в Python",
        "author": "Mathew",
    },
    {
        "id": 2,
        "title": "Backend розробка в Python",
        "author": "Artem"
    },
]

@app.get("/books", tags=["Книжки"], summary="Усі книжки")
def read_books():
    return books

@app.get("/books/{book_id}", tags=["Книжки"], summary="Конкретна книжка")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")

class NewBook(BaseModel):
    title: str
    author: str

@app.post("/books")
def create_books(new_book: NewBook):
    books.append({
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author
    })
    return {"success": True, "message": "Книжка була додана"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
