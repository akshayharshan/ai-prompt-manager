# JWT Authentication – Interview Q&A

---

## 1️⃣ What is JWT?

JWT (JSON Web Token) is a compact, URL-safe token used for stateless authentication.

It consists of:
Header.Payload.Signature

---

## 2️⃣ Why is JWT stateless?

Because the server does not store session data.
All required information is inside the token payload.

---

## 3️⃣ What is inside JWT payload?

Common claims:
- sub (subject / user_id)
- exp (expiration)
- iat (issued at)
- role (optional)

---

## 4️⃣ Why use expiration (exp)?

To:
- Reduce token misuse risk
- Limit lifetime of compromised tokens
- Improve security

---

## 5️⃣ What happens if token expires?

jwt.decode raises exception.
Server returns 401 Unauthorized.

---

## 6️⃣ Difference between JWT and session-based auth?

Session-based:
- Server stores session
- Requires server memory
- Harder to scale

JWT:
- Stateless
- Scales easily
- Token stored client-side

---

## 7️⃣ Where is JWT stored?

Usually:
- Browser memory
- HTTP-only cookie
- Secure storage

Should not store in localStorage for sensitive apps (XSS risk).

---

## 8️⃣ What is OAuth2PasswordBearer?

FastAPI helper that:
- Extracts Bearer token from Authorization header
- Integrates with Swagger UI

---

## 9️⃣ What algorithm are we using?

HS256:
- Symmetric key signing
- Same key for sign and verify

---

## 🔟 How would you invalidate JWT?

Options:
- Short expiration
- Token blacklist (Redis)
- Refresh token rotation