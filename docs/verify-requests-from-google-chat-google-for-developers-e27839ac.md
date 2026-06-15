---
title: "Verify requests from Google Chat  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/verify-requests-from-chat"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:14:37Z"
extraction_method: "web_extract"
---

# Verify Requests from Google Chat — Markdown Summary

**Source:** https://developers.google.com/workspace/chat/verify-requests-from-chat  
**Last updated:** 2026-04-20 UTC

---

## Core Purpose

For Google Chat apps built with **HTTP endpoints**, you must verify that incoming HTTPS requests actually originate from **Google Chat**.

Google Chat includes a **bearer token** in the `Authorization` header of every HTTPS request sent to your app endpoint.

```http
POST
Host: yourappurl.com
Authorization: Bearer AbCdEf123456
Content-Type: application/json
User-Agent: Google-Dynamite
```

The bearer token is a **cryptographic token produced by Google**. Its type and `audience` value depend on the **Authentication Audience** setting configured for the Chat app.

---

## Key Facts

- Google Chat sends a bearer token in the `Authorization` header of HTTPS requests.
- The token verifies that the request originated from Google Chat.
- If verification fails, your service should return:

```http
401 Unauthorized
```

- For **Cloud Run functions / Cloud Run**, Google Cloud IAM can handle token verification automatically.
- For apps with their own HTTP server, verify the bearer token using:
  - A Google API client library
  - Or direct validation of the ID token / JWT
- The token format depends on the Chat app’s **Authentication Audience**:
  - **HTTP endpoint URL** → Google-signed **OIDC ID token**
  - **Project Number** → self-signed **JWT**

---

## Google Chat Service Account

Requests from Chat are associated with this service account:

```text
chat@system.gserviceaccount.com
```

This value is used as the expected issuer/email when verifying tokens.

---

## Recommended Google API Client Libraries

For self-managed HTTP servers, Google recommends using open source Google API client libraries:

- **Java:** https://github.com/google/google-api-java-client
- **Python:** https://github.com/google/google-api-python-client
- **Node.js:** https://github.com/google/google-api-nodejs-client
- **.NET:** https://github.com/google/google-api-dotnet-client

---

# Authentication with Cloud Run Functions

If your Chat app is implemented using **Cloud Run functions**, Cloud IAM handles token verification automatically.

## Required Chat App Configuration

In the Chat app connection settings:

- Set **Authentication Audience** to:

```text
HTTP endpoint URL
```

- Ensure the configured HTTP endpoint URL matches the Cloud Run function endpoint URL.

## Required IAM Configuration

Authorize the Google Chat service account as an invoker:

```text
chat@system.gserviceaccount.com
```

---

## Grant Invoker Permission Using Google Cloud Console

After deploying your function or service:

1. Open the Cloud Run page in Google Cloud Console.
2. In the Cloud Run services list, select the checkbox next to the receiving function.
   - Do **not** click the function itself.
3. Click **Permissions**.
4. Click **Add principal**.
5. In **New principals**, enter:

```text
chat@system.gserviceaccount.com
```

6. Select the role:

```text
Cloud Run > Cloud Run Invoker
```

7. Click **Save**.

---

## Grant Invoker Permission Using `gcloud`

Use:

```bash
gcloud functions add-invoker-policy-binding RECEIVING_FUNCTION \
  --member='serviceAccount:chat@system.gserviceaccount.com'
```

Replace:

```text
RECEIVING_FUNCTION
```

with the name of your Chat app’s function.

---

# Authentication with an ID Token

Use this method when the Chat app’s **Authentication Audience** is set to:

```text
HTTP endpoint URL
```

## Token Characteristics

When using an HTTP endpoint URL as the audience:

- The bearer token is a Google-signed OpenID Connect **ID token**.
- The `email` field is:

```text
chat@system.gserviceaccount.com
```

- The token audience is the endpoint URL configured for the Chat app.

Example:

If the configured endpoint is:

```text
https://example.com/app/
```

then the ID token audience is:

```text
https://example.com/app/
```

## Recommendation

This is the **recommended authentication method** if your HTTP endpoint is not hosted on a service that supports IAM-based authentication, such as Cloud Run.

Benefits:

- Your service only needs to know its endpoint URL.
- It does **not** need to know the Google Cloud project number.

---

## ID Token Verification Examples

### Java

Source: `java/basic-app/src/main/java/com/google/chat/app/basic/App.java`

```java
String CHAT_ISSUER = "chat@system.gserviceaccount.com";
JsonFactory factory = JacksonFactory.getDefaultInstance();

GoogleIdTokenVerifier verifier =
    new GoogleIdTokenVerifier.Builder(new ApacheHttpTransport(), factory)
        .setAudience(Collections.singletonList(AUDIENCE))
        .build();

GoogleIdToken idToken = GoogleIdToken.parse(factory, bearer);
return idToken != null
    && verifier.verify(idToken)
    && idToken.getPayload().getEmailVerified()
    && idToken.getPayload().getEmail().equals(CHAT_ISSUER);
```

### Python

Source: `python/basic-app/main.py`

```python
# Bearer T

[... summary truncated for context management ...]
