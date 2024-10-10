CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_number TEXT UNIQUE NOT NULL,
    balance REAL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL NOT NULL,
    transaction_type TEXT NOT NULL,  -- 'deposit' or 'withdraw'
    account_id INTEGER NOT NULL,
    FOREIGN KEY (account_id) REFERENCES accounts (id)
);
