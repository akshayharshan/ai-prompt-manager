# AI Prompt Manager – Day 3
## Refresh Tokens + Role-Based Access Control

---

# ✅ Features Implemented

- Refresh token generation
- Refresh endpoint to obtain new access tokens
- Role field added to User model
- Admin-only route protection
- Authorization dependency pattern

---

# 🔁 Access Token vs Refresh Token

Access Token:
- Short lifetime (e.g., 15 minutes)
- Used for API authorization
- Sent in `Authorization: Bearer <token>`

Refresh Token:
- Long lifetime (e.g., 7 days)
- Used only to obtain new access tokens
- Never used directly for protected APIs

---

# 🔐 Refresh Flow

1. User logs in
2. Server returns:
   - access_token
   - refresh_token
3. Client stores tokens
4. Access token expires
5. Client calls `/auth/refresh`
6. Server verifies refresh token
7. New access token is issued

---

# 🧠 Why Use Refresh Tokens?

Security vs usability balance.

Short-lived access tokens reduce risk if stolen.

Refresh tokens prevent users from needing to log in repeatedly.

---

# 👥 Role-Based Access Control (RBAC)

RBAC restricts routes based on user roles.

Example roles:
- user
- admin

---

# 🏗 Implementation Pattern

User model:

role column added.

Authorization dependency:

require_admin() checks user role.

Protected route:

Depends(require_admin)

---

# 🧠 Authorization Flow

Request → Token validated → User fetched → Role checked → Route allowed/denied.

---

# ⚠ Security Notes

Access tokens should expire quickly.

Refresh tokens should be stored securely.

Production systems often:
- store refresh tokens in Redis or DB
- rotate refresh tokens
- invalidate stolen tokens

---

# 🎯 Backend Concepts Learned

- Stateless authentication
- JWT lifecycle
- Dependency-based authorization
- Role-based route protection
- Token refresh patterns