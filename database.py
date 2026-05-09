import sqlite3

DB_PATH = "diet.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            name        TEXT    NOT NULL,
            age         INTEGER NOT NULL,
            gender      TEXT    NOT NULL,
            weight_kg   REAL    NOT NULL,
            height_cm   REAL    NOT NULL,
            activity    TEXT    NOT NULL,
            goal        TEXT    NOT NULL,
            allergies   TEXT    DEFAULT '',
            preferences TEXT    DEFAULT '',
            created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def save_profile(data: dict) -> int:
    conn = get_connection()
    cur = conn.execute("""
        INSERT INTO users (name, age, gender, weight_kg, height_cm, activity, goal, allergies, preferences)
        VALUES (:name, :age, :gender, :weight_kg, :height_cm, :activity, :goal, :allergies, :preferences)
    """, data)
    conn.commit()
    user_id = cur.lastrowid
    conn.close()
    return user_id


def get_profile(user_id: int):
    conn = get_connection()
    row = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    return dict(row) if row else None


def get_all_profiles():
    conn = get_connection()
    rows = conn.execute("SELECT id, name, age, goal, created_at FROM users ORDER BY created_at DESC").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def delete_profile(user_id: int):
    conn = get_connection()
    conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
