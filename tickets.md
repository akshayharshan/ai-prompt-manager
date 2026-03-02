# Project Tickets Segregated by Day

## 🟢 DAY 1 – JWT Core Authentication
- apm-101-setup-passlib-bcrypt-password-hashing-type-security
- apm-102-create-user-registration-endpoint-register-type-feature
- apm-103-implement-login-endpoint-with-jwt-access-token-login-type-feature
- apm-104-add-jwt-token-creation-utility-hs256-exp-claim-type-feature
- apm-105-implement-protected-route-middleware-depends-based-auth-type-feature
- apm-106-add-me-endpoint-for-authenticated-user-type-feature

## 🟢 DAY 2 – Refresh Tokens + RBAC
- apm-201-add-refresh-token-model-and-storage-logic-type-feature
- apm-202-implement-refresh-token-endpoint-refresh-type-feature
- apm-203-add-role-column-to-user-model-admin-user-type-feature
- apm-204-implement-role-based-access-dependency-type-security
- apm-205-create-admin-only-protected-endpoint-type-feature

## 🟡 DAY 3 – Redis + Basic Caching
- apm-301-add-redis-service-to-docker-compose-type-infra
- apm-302-setup-redis-client-connection-in-fastapi-type-infra
- apm-303-implement-cache-aside-pattern-for-get-prompts-type-feature
- apm-304-add-ttl-configuration-for-cached-prompts-60s-type-enhancement

## 🟡 DAY 4 – Cache Invalidation
- apm-401-invalidate-cache-on-prompt-update-type-enhancement
- apm-402-invalidate-cache-on-prompt-delete-type-enhancement
- apm-403-clear-relevant-cache-keys-on-prompt-create-type-enhancement
- apm-404-implement-cache-key-naming-strategy-type-enhancement

## 🔴 DAY 5 – Rate Limiting
- apm-501-implement-redis-based-fixed-window-rate-limiting-type-security
- apm-502-apply-rate-limiting-to-login-endpoint-type-security
- apm-503-apply-rate-limiting-to-ai-generation-endpoint-type-security
- apm-504-return-http-429-for-rate-limit-exceeded-type-security

## 🟣 DAY 6 – Logging & Observability
- apm-601-setup-structured-logging-configuration-type-infra
- apm-602-implement-request-logging-middleware-type-enhancement
- apm-603-log-response-time-for-each-request-type-enhancement
- apm-604-create-separate-error-log-file-type-infra

## 🔵 DAY 7 – Testing
- apm-701-setup-pytest-fastapi-testclient-type-testing
- apm-702-write-registration-endpoint-tests-type-testing
- apm-703-write-login-success-failure-tests-type-testing
- apm-704-test-protected-route-access-type-testing
- apm-705-test-rate-limiting-logic-type-testing
- apm-706-implement-dependency-override-for-test-db-type-testing

## 🐳 DAY 8 – Docker Production Setup
- apm-801-optimize-dockerfile-for-production-type-infra
- apm-802-add-redis-to-multi-container-network-type-infra
- apm-803-configure-environment-variables-via-env-type-security
- apm-804-configure-gunicorn-with-uvicorn-workers-type-infra

## 🔐 DAY 9 – Security Hardening
- apm-901-implement-strict-cors-configuration-type-security
- apm-902-add-secure-http-headers-middleware-type-security
- apm-903-remove-debug-logs-from-production-type-security
- apm-904-validate-request-schemas-strictly-pydantic-enforcement-type-security
- apm-905-hide-internal-error-details-from-client-responses-type-security

## 🚀 DAY 10 – Final Review & Resilience
- apm-1001-review-jwt-access-refresh-flow-type-documentation
- apm-1002-review-redis-cache-logic-failure-strategy-type-documentation
- apm-1003-implement-redis-failure-fallback-handling-type-enhancement
- apm-1004-add-token-revocation-strategy-blacklist-concept-type-security
- apm-1005-prepare-system-architecture-readme-type-documentation
- apm-1006-prepare-interview-explanation-notes-type-documentation