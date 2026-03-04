# Authentication + RBAC – Interview Q&A

---

## 1️⃣ What is the difference between authentication and authorization?

Authentication verifies who the user is.

Authorization determines what the user is allowed to do.

---

## 2️⃣ Why do access tokens expire quickly?

Short lifetimes reduce the damage if a token is stolen.

---

## 3️⃣ Why use refresh tokens?

Refresh tokens allow users to obtain new access tokens without logging in again.

---

## 4️⃣ Where should refresh tokens be stored?

Most secure approach:
HTTP-only secure cookies.

Some systems also store them in Redis or database for revocation.

---

## 5️⃣ What is RBAC?

Role-Based Access Control.

Access is determined based on the user’s role.

Example:
admin → manage users
user → normal access

---

## 6️⃣ How did you implement RBAC in FastAPI?

- Added role column in user model
- Created dependency that checks role
- Applied dependency to protected routes

---

## 7️⃣ What happens if a user role changes?

If roles are stored only in JWT:
token must be refreshed.

If roles are checked from database:
change applies immediately.

---

## 8️⃣ How can refresh tokens be invalidated?

Possible methods:
- store tokens in DB/Redis
- maintain blacklist
- rotate refresh 