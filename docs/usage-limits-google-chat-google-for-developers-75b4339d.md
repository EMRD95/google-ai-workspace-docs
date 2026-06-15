---
title: "Usage limits  |  Google Chat  |  Google for Developers"
source_url: "https://developers.google.com/workspace/chat/limits"
product_area: "chat-developers"
retrieved_at: "2026-06-15T18:22:09Z"
extraction_method: "web_extract"
---

# Google Chat API Usage Limits — Summary

**Source:** Google for Developers — Google Chat API Usage Limits  
**Last updated:** **2026-05-01 UTC**

## Overview

Google Chat API enforces quotas and limits to ensure **fair usage** and protect **Google Workspace performance**.

> Because the Google Chat API is a shared service, we apply quotas and limitations to make sure that it's used fairly by all users and to protect the overall performance of Google Workspace.

If a quota is exceeded, the API returns:

```http
429: Too many requests
```

Google notes that additional backend rate-limit checks can also produce the same error.

**Recommended response:** use a **truncated exponential backoff** algorithm and retry later.

> As long as you stay within the per-minute quotas listed in the following tables, there's no limit to the number of requests you can make per day.

Multiple quota types can apply to a Chat API method:

- **Per-project quotas** — apply to a Google Cloud project / single Chat app.
- **Per-space quotas** — apply within a given Chat space and are shared by all Chat apps acting in that space.
- **Per-user quotas** — apply across all Chat apps calling API methods on behalf of a user using user authentication.

---

## Per-Project Quotas

Per-project quotas limit query rates for a **Google Cloud project**, typically applying to a single Chat app calling the listed Chat API methods.

These limits are also visible in the Google Cloud Console on the **Quotas** page.

| Per-project quota | Chat API methods | Limit |
|---|---|---:|
| **Message writes per minute** | `spaces.messages.create`<br>`spaces.messages.patch`<br>`spaces.messages.delete` | **3000 / 60 sec** |
| **Message reads per minute** | `spaces.messages.get`<br>`spaces.messages.list` | **3000 / 60 sec** |
| **Membership writes per minute** | `spaces.members.create`<br>`spaces.members.delete` | **300 / 60 sec** |
| **Membership reads per minute** | `spaces.members.get`<br>`spaces.members.list` | **3000 / 60 sec** |
| **Space writes per minute** | `spaces.setup`<br>`spaces.create`<br>`spaces.patch`<br>`spaces.delete` | **60 / 60 sec** |
| **Space reads per minute** | `spaces.get`<br>`spaces.list`<br>`spaces.findDirectMessage` | **3000 / 60 sec** |
| **Attachment writes per minute** | `media.upload` | **600 / 60 sec** |
| **Attachment reads per minute** | `spaces.messages.attachments.get`<br>`media.download` | **3000 / 60 sec** |
| **Reaction writes per minute** | `spaces.messages.reactions.create`<br>`spaces.messages.reactions.delete` | **600 / 60 sec** |
| **Reaction reads per minute** | `spaces.messages.reactions.list` | **3000 / 60 sec** |
| **CustomEmoji writes per minute** | `customEmojis.create`<br>`customEmojis.delete` | **600 / 60 sec** |
| **CustomEmoji reads per minute** | `customEmojis.get`<br>`customEmojis.list` | **3000 / 60 sec** |
| **Section writes per minute** | `users.sections.create`<br>`users.sections.delete`<br>`users.sections.patch`<br>`users.sections.position`<br>`users.sections.items.move` | **600 / 60 sec** |
| **Section reads per minute** | `users.sections.list`<br>`users.sections.items.list` | **3000 / 60 sec** |

---

## Per-Space Quotas

Per-space quotas limit query rates **inside a specific Chat space**.

These quotas are **shared among all Chat apps** acting in that space.

| Per-space quota | Chat API methods | Limit |
|---|---|---:|
| **Reads per second** | `media.download`<br>`spaces.get`<br>`spaces.members.get`<br>`spaces.members.list`<br>`spaces.messages.get`<br>`spaces.messages.list`<br>`spaces.messages.attachments.get`<br>`spaces.messages.reactions.list` | **15 / sec** |
| **Writes per second** | `media.upload`<br>`spaces.delete`<br>`spaces.patch`<br>`spaces.messages.create`<br>`spaces.messages.delete`<br>`spaces.messages.patch`<br>`spaces.messages.reactions.delete` | **1 / sec** |
| **Create Reaction writes per second** | `spaces.messages.reactions.create` | **5 / sec** |
| **Message writes per second while importing data to Google Chat** | `spaces.messages.create` | **10 / sec** |

**Important note:** additional limits apply to **incoming webhooks** for `spaces.messages.create`.

---

## Per-User Quotas

Per-user quotas limit query rates for a **Google Chat user**.

They apply to all Chat apps that call Chat API methods **on behalf of a user** using **user authentication**.

| Per-user quota | Chat API methods | Limit |
|---|---|---:|
| **CustomEmoji writes per second** | `customEmojis.create`<br>`customEmojis.delete` | **1 / sec** |
| **CustomEmoji reads per second** | `customEmojis.get`<br>`customEmojis.list` | **15 / sec** |
| **Section writes per second** | `users.sections.create`<br>`users.sections.delete`<br>`users.sections.patch`<br>`users.sections.position`<br>`users.sections.items.move` | **1 / sec** |
| **Section reads per second** | `users.sections.list`<br>`users.sections.items.list` | **15 / sec** |

---

## Additional Usage Limits

High traffic directed at the same Chat space can trigger **ad

[... summary truncated for context management ...]
