# Authentication – Interview Q&A (Level 1)

---

## 1️⃣ Why should we hash passwords?

Passwords must be hashed to prevent exposure if the database is compromised. Hashing is one-way, meaning original passwords cannot be retrieved from stored hashes.

---

## 2️⃣ What is the difference between hashing and encryption?

Hashing:
- One-way
- Cannot be reversed
- Used for passwords

Encryption:
- Two-way
- Can be decrypted with key
- Used for secure data transmission

---

## 3️⃣ Why use Argon2 instead of bcrypt?

Argon2:
- Memory-hard
- Resistant to GPU attacks
- No 72-byte limitation
- Winner of Password Hashing Competition

bcrypt:
- Older
- 72-byte input limit
- Still secure but less modern

---

## 4️⃣ What is salting?

Salting:
- Random value added before hashing
- Prevents rainbow table attacks
- Argon2 automatically handles salting

---

## 5️⃣ Why not store plain passwords?

If DB leaks:
- Plain passwords expose users immediately
- Users often reuse passwords
- Leads to severe security breach

---

## 6️⃣ What is separation of concerns?

Routes handle HTTP.
Services handle business logic.
Models define database structure.
Schemas validate input/output.

This improves maintainability and testing.

---

## 7️⃣ Why use async database sessions?

FastAPI runs on ASGI.
Async prevents blocking while waiting for DB operations.
Improves scalability under concurrency.

---

## 8️⃣ Why check if user exists before creating?

To:
- Enforce uniqueness
- Prevent duplicate users
- Maintain data integrity

---

## 9️⃣ What happens if two users register simultaneously?

Database unique constraint ensures:
- Only one succeeds
- Other fails
Application-level check is not enough.
DB-level constraint is required.

---

## 🔟 What should be validated in registration?

- Email format
- Password minimum length
- Password maximum length
- Unique email