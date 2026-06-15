---
title: "Chrome—Generative AI features and policies - Chrome Enterprise and Education Help"
source_url: "https://support.google.com/chrome/a/answer/14443058"
product_area: "chrome-enterprise-ai"
retrieved_at: "2026-06-15T17:59:00Z"
extraction_method: "web_extract"
---

# Chrome—Generative AI Features and Policies  
**Source:** Chrome Enterprise and Education Help — <https://support.google.com/chrome/a/answer/14443058>

## Overview

Chrome provides generative AI features for ChromeOS and Chrome Browser with enterprise-oriented policy controls and data protections. Admins can manage supported AI capabilities using the **`GenAiDefaultSettings`** policy.

Chrome also supports access to other Google AI products, such as **Google Lens**, **Gemini Enterprise**, **Gemini in Chrome**, and **AI Mode**, but those are governed by their own terms and are **not covered by Chrome’s enterprise data guarantees for Chrome-built generative AI features**.

---

## Key Excerpts

> Chrome is committed to the responsible implementation and use of artificial intelligence (AI) and we are bringing the power of AI to your fingertips while offering enterprise-grade data protections.

### Enterprise Data Guarantees

When an AI feature policy is set to **Allow the feature without improving AI models**:

> **Your Customer Data will not be used to improve Google models**—Data may be sent to Google so that the AI feature works properly but that data will not be used to improve the Google model.

> **Data is not used for ads**—Google does not sell your Customer Data, nor will it be used to personalize advertisements.

### Important Scope Note

> In addition to Chrome-built features, organizations can also benefit from other Google generative AI products, such as Gemini and Gemini Enterprise, which are accessible in Chrome. These features are not covered by Chrome’s enterprise data guarantees for generative AI as they are subject to their own guarantees and/or terms of service.

---

## Chrome Generative AI Features

All listed Chrome-built AI features are supported by the **`GenAiDefaultSettings`** policy.

| Feature | ChromeOS | Chrome Browser on Win/macOS/Linux | Supported by `GenAiDefaultSettings` |
|---|---:|---:|---:|
| [Help me write](https://support.google.com/chrome/a/answer/14533935) | ✓ | ✓ | ✓ |
| [Create themes with AI](https://support.google.com/chrome/a/answer/14534723) | ✓ | ✓ | ✓ |
| [Tab organizer](https://support.google.com/chrome/a/answer/14534722) | ✓ | ✓ | ✓ |
| [DevTools AI features](https://support.google.com/chrome/a/answer/14989974) | ✓ | ✓ | ✓ |
| [Wallpaper settings](https://support.google.com/chrome/a/answer/15966259) | ✓ | ✖ | ✓ |
| Video conference background settings | ✓ | ✖ | ✓ |
| [History search settings](https://support.google.com/chrome/a/answer/15248971) | ✓ | ✓ | ✓ |
| [Tab compare](https://support.google.com/chrome/a/answer/15425104) | ✓ | ✓ | ✓ |
| Help me read | ✓ | ✖ | ✓ |
| [Enhanced autofill](https://support.google.com/chrome/a/answer/16278400) | ✓ | ✓ | ✓ |
| [AI image editing in Gallery](https://support.google.com/chrome/a/answer/16370655) | ✓ | ✖ | ✓ |
| [Inline image generation](https://support.google.com/chrome/a/answer/16278889) | ✓ | ✖ | ✓ |
| [Suggested groups](https://support.google.com/chrome/a/answer/16372481) | ✓ | ✖ | ✓ |
| [Text capture](https://support.google.com/chrome/a/answer/16370114) | ✓ | ✖ | ✓ |
| [Automated password change](https://support.google.com/chrome/a/answer/16497834) | ✓ | ✓ | ✓ |

### Platform Availability Summary

#### Available on both ChromeOS and Chrome Browser  
- Help me write  
- Create themes with AI  
- Tab organizer  
- DevTools AI features  
- History search settings  
- Tab compare  
- Enhanced autofill  
- Automated password change  

#### ChromeOS-only features  
- Wallpaper settings  
- Video conference background settings  
- Help me read  
- AI image editing in Gallery  
- Inline image generation  
- Suggested groups  
- Text capture  

---

## Enterprise Data Protections

If admins configure an AI feature policy as:

**`Allow the feature without improving AI models`**

Then:

- Customer Data may be sent to Google only so the feature can function.
- Customer Data is **not used to improve Google models**.
- Customer Data is **not sold**.
- Customer Data is **not used to personalize ads**.

---

## Admin Console Default Policy Values

| Customer Category | Default Policy State |
|---|---|
| Workspace Education | Allow feature without improving AI models. |
| Chrome Enterprise cloud managed browsers | Allow feature without improving AI models. |
| Third-party managed browsers | Allow feature and improve AI models. |
| Consumers | Allow feature and improve AI models. |

### Key Administrative Takeaway

Enterprise and education customers managed through Google’s Chrome/Workspace environments default to the more privacy-preserving setting:  
**Allow feature without improving AI models.**

Third-party managed browsers and consumer environments default to:  
**Allow feature and improve AI models.**

---

# Google Generative AI Features Available Through Chrome

These are Google AI products accessible through Chrome, but they are separate from Chrome-built AI features and governed by their own terms.

## Google Lens

**Pu

[... summary truncated for context management ...]
