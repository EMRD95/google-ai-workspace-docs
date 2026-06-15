---
title: "Class ChatResponse  |  Apps Script  |  Google for Developers"
source_url: "https://developers.google.com/apps-script/reference/card-service/chat-response"
product_area: "apps-script-ai"
retrieved_at: "2026-06-15T18:20:14Z"
extraction_method: "web_extract"
---

[Skip to main content](https://developers.google.com/apps-script/reference/card-service/chat-response#main-content)

[![Google Workspace](https://www.gstatic.com/images/branding/productlogos/googleg_gradient/v1/16px.svg)](https://developers.google.com/workspace)

- [GoogleWorkspace](https://developers.google.com/workspace)

`/`

- English
- Deutsch
- Español
- Español – América Latina
- Français
- Indonesia
- Italiano
- Polski
- Português – Brasil
- Tiếng Việt
- Türkçe
- Русский
- עברית
- العربيّة
- فارسی
- हिंदी
- বাংলা
- ภาษาไทย
- 中文 – 简体
- 中文 – 繁體
- 日本語
- 한국어

Sign in

- [Apps Script](https://developers.google.com/apps-script)

- [Home](https://developers.google.com/)
- [Google Workspace](https://developers.google.com/workspace)
- [Apps Script](https://developers.google.com/apps-script)
- [Reference](https://developers.google.com/apps-script/reference)



 Send feedback



# Class ChatResponse    Stay organized with collections      Save and categorize content based on your preferences.

![Spark icon](https://developers.google.com/_static/images/icons/spark.svg)

## Page Summary

outlined\_flag

- ChatResponse is the response object for a card message in Google Chat, available only for Google Chat apps.

- You can create a ChatResponse using `CardService.newChatResponseBuilder()`, adding text and cards using `setText()` and `addCardsV2()`.

- The `printJson()` method is available for debugging and prints the JSON representation of the ChatResponse object.


ChatResponse

The response object for a card message in Google Chat.

Only available for Google Chat apps. Not available for Google Workspace add-ons.

```
// Creates a card message in Chat.
const cardHeader = CardService.newCardHeader()
                       .setTitle('Card Header Title')
                       .setSubtitle('Card Header Subtitle');

const card = CardService.newCardBuilder().setHeader(cardHeader).build();

const chatResponse =
    CardService.newChatResponseBuilder()
        .setText('Example text')
        .addCardsV2(
            CardService.newCardWithId().setCardId('card_id').setCard(card))
        .build();

console.log(chatResponse.printJson());
```

### Methods

| Method | Return type | Brief description |
| --- | --- | --- |
| `printJson()` | `String` | Prints the JSON representation of this object. |

## Detailed documentation

### `printJson()`

Prints the JSON representation of this object. This is for debugging only.

#### Return

`String`



 Send feedback



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-13 UTC.


Need to tell us more?






\[\[\["Easy to understand","easyToUnderstand","thumb-up"\],\["Solved my problem","solvedMyProblem","thumb-up"\],\["Other","otherUp","thumb-up"\]\],\[\["Missing the information I need","missingTheInformationINeed","thumb-down"\],\["Too complicated / too many steps","tooComplicatedTooManySteps","thumb-down"\],\["Out of date","outOfDate","thumb-down"\],\["Samples / code issue","samplesCodeIssue","thumb-down"\],\["Other","otherDown","thumb-down"\]\],\["Last updated 2026-04-13 UTC."\],\[\],\["The \`ChatResponse\` object, exclusive to Google Chat apps, facilitates the creation of card messages. It is not for Google Workspace add-ons. You can build card messages using methods like \`newCardHeader()\` and \`newCardBuilder()\`. \`newChatResponseBuilder()\` builds the ChatResponse by adding text and cards. \`printJson()\` outputs the JSON representation of the constructed \`ChatResponse\` object, for debugging purposes.\\n"\]\]
