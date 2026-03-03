# AI Prompt Manager – Day 2
## 🔐 JWT Authentication (Access Token)

---

# ✅ What Was Implemented

- Login endpoint using OAuth2PasswordRequestForm
- JWT access token creation
- exp claim added to token
- OAuth2PasswordBearer integration
- Protected route using Depends(get_current_user)
- Swagger Authorize integration

---

# 🧠 JWT Structure

JWT = Header.Payload.Signature

Header:
- Algorithm (HS256)

Payload:
- sub (user_id)
- exp (expiration time)

Signature:
- Signed using SECRET_KEY

JWT is stateless.
Server does NOT store session.

---

# 🔑 Login Flow

1. Client sends form data (username, password)
2. Server verifies password (Argon2)
3. Server creates JWT with user_id
4. JWT returned to client
5. Client stores token (usually frontend)
6. Client sends token in Authorization header

Authorization header format:
Authorization: Bearer <token>

---

# 🧠 OAuth2PasswordRequestForm

- Extracts form data
- Requires python-multipart
- Uses username field (mapped to email)

---

# 🔐 Protected Route Flow

1. Request hits protected endpoint
2. oauth2_scheme extracts token
3. jwt.decode validates:
   - Signature
   - Expiration
4. Extract user_id from payload
5. Fetch user from DB
6. Allow access

If token invalid → 401

---

# ⚡ Token Expiration

exp claim ensures:
- Token auto-expires
- Reduces security risk
- Forces re-login

If expired:
JWTError raised → 401 Unauthorized

---

# 🎯 Backend Concepts Learned

- Stateless authentication
- Token-based auth vs session-based auth
- Dependency injection in FastAPI
- OAuth2 flow integration
- Form vs JSON request bodies

---

# 🚀 Current Authentication Capability

✔ Secure login  
✔ Stateless auth  
✔ Protected endpoints  
✔ Expiring tokens  

Authentication layer is complete (basic version).