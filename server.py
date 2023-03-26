import psycopg2

from typing import List
from pydantic import BaseModel

import uvicorn  
from fastapi import FastAPI, status


from fastapi.middleware.cors import CORSMiddleware


# ======= CLASS =======


class Book(BaseModel):
    id:  int = None
    volume_id : str
    title : str
    authors: str = None
    thumbnail: str = None
    state: int 
    rating: int = None

class Update_Rating_Request_Body(BaseModel):
    volume_id : str
    new_rating : int 


class Update_State_Request_Body(BaseModel):
    volume_id: str
    new_state : int
    

# ======== END POINT ======

app = FastAPI(debug=True)

app.add_middleware (
    CORSMiddleware,
    allow_origins = ("*"),
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ("*"),
)

@app.get ("/status")

async def check_status():
    return "Connected"

@app.get ("/books", response_model=List[Book], status_code=status.HTTP_200_OK)
async def get_books():
    # Connect to our database
    conn = psycopg2.connect(

        database= "postgres", user="postgres", password="mypasswordsecret", host="0.0.0.0"

    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM book ORDER BY id Desc")
    rows = cur.fetchall()

    formatted_books = []
    for row in rows:
        formatted_books.append(
            Book (
                id=row[0],
                volume_id =row[1],
                title=row[2],
                authors=row[3],
                thumbnail= row [4],
                state=row[5],
                rating=row[6],
            )

        )
    cur.close()
    conn.close()

    return formatted_books

@app.post ("/books", status_code=status.HTTP_201_CREATED)
async def new_book(book: Book):
    # Connect to our database
    conn = psycopg2.connect(
        database= "postgres", user="postgres", password="mypasswordsecret", host="0.0.0.0"
    )

    cur = conn.cursor()
    cur.execute(
        f"INSERT INTO BOOK (volume_id, title, authors, thumbnail, state) VALUES ('{book.volume_id}', '{book.title}', '{book.authors}', '{book.thumbnail}', '{book.state}',)"
    )

    cur.close()
    conn.commit()
    conn.close()
    return

@app.put("/books/update_rating", status_code=200)
async def update_rating(update_rating_body: Update_Rating_Request_Body):
      # Connect to our database
    conn = psycopg2.connect(

        database= "postgres", user="postgres", password="mypasswordsecret", host="0.0.0.0"

    )

    cur = conn.cursor()
    cur.execute(
        f"UPDATE Book Set Rating = {update_rating_body.new_rating} WHERE volume_id ='{update_rating_body.volume_id}'"
    )

    cur.close()
    conn.commit()
    conn.close()
    return

@app.put("/books/update_book_state", status_code=200)
async def update_state(update_request_body: Update_State_Request_Body):
     # Connect to our database
    conn = psycopg2.connect(

        database= "postgres", user="postgres", password="mypasswordsecret", host="0.0.0.0"

    )

    cur = conn.cursor()
    cur.execute(
        f"UPDATE Book Set State = {update_request_body.new_state} WHERE volume_id ='{update_request_body.volume_id}'"
    )

    cur.close()
    conn.commit()
    conn.close()
    return


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)