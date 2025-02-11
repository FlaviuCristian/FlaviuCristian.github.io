import sqlite3

# Conectare la baza de date (se va crea dacă nu există)
conn = sqlite3.connect("chatbot.db")
cursor = conn.cursor()

# Creare tabel pentru mesaje și răspunsuri
cursor.execute("""
CREATE TABLE IF NOT EXISTS responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_message TEXT UNIQUE,
    bot_response TEXT
)
""")

# Adăugăm răspunsuri prestabilite
responses = [
    ("Salut", "Bună! Cum te pot ajuta?"),
    ("Cum te numești?", "Sunt un chatbot inteligent!"),
    ("Ce faci?", "Sunt aici să răspund la întrebările tale."),
    ("Mulțumesc", "Cu plăcere!"),
]

cursor.executemany("INSERT OR IGNORE INTO responses (user_message, bot_response) VALUES (?, ?)", responses)

# Salvăm și închidem conexiunea
conn.commit()
conn.close()

print("Baza de date a fost creată și populată!")
