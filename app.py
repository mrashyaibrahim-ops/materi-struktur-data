import sqlite3
from flask import Flask, render_template, jsonify

app = Flask(__name__)
DB = "materi.db"

def koneksi():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def siapkan_database():
    with koneksi() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS topik (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama TEXT UNIQUE NOT NULL,
                isi TEXT NOT NULL
            )
        """)
        data_awal = [
            ("stack", "Stack: tumpukan data dengan prinsip LIFO (Last In, First Out). Operasi utamanya push dan pop."),
            ("queue", "Queue: antrian data dengan prinsip FIFO (First In, First Out). Operasi utamanya enqueue dan dequeue."),
            ("linked-list", "Linked List: kumpulan node, tiap node menyimpan data dan penunjuk (pointer) ke node berikutnya."),
        ]
        conn.executemany(
            "INSERT OR IGNORE INTO topik (nama, isi) VALUES (?, ?)", data_awal
        )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/materi/<topik>")
def ambil_materi(topik):
    with koneksi() as conn:
        baris = conn.execute(
            "SELECT isi FROM topik WHERE nama = ?", (topik,)
        ).fetchone()
    isi = baris["isi"] if baris else "Materi belum tersedia."
    return jsonify({"topik": topik, "isi": isi})

siapkan_database()

if __name__ == "__main__":
    app.run(debug=True)