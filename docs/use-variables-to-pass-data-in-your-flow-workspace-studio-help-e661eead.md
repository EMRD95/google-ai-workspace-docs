---
title: "Use variables to pass data in your flow - Workspace Studio Help"
source_url: "https://support.google.com/workspace-studio/answer/16448468"
product_area: "workspace-studio"
retrieved_at: "2026-06-15T17:49:47Z"
extraction_method: "web_extract"
---

[Skip to main content](https://support.google.com/workspace-studio/answer/16448468#search-form)

# Use variables to pass data in your flow

Variables are dynamic placeholders that let you use information from earlier parts of your flow. This lets you create customized and flexible automations.

For example, a variable can take a new Google Form response and insert it into a Google Chat message. Or, you can use the text summarized by Gemini to create a new Google Doc.

**Important:** When you add variables to third-party integration steps or add-on steps, they might contain your Google Account data, such as the contents of a message in Gmail or Chat, or event information from Calendar. The flow can then share your Google Account data with a third-party service. Make sure you trust the third-party service.

## How to use variables in Google Workspace Studio - YouTube                   Tap to unmute                                                   [How to use variables in Google Workspace Studio](https://www.youtube.com/watch?v=t8-ibxR5j0Q) [Google Workspace Developers](https://www.youtube.com/channel/UCUcg6az6etU_gRtZVAhBXaw)    ![thumbnail-image](https://yt3.ggpht.com/yzihDq6TKct6Fp47gS9Rs-EGaqIFjpBr9cDC3VR9F3pN1qvsnJpI37jl2o-AT-IxeFxT5A4A=s68-c-k-c0x00ffffff-no-rj)    Google Workspace Developers76.4K subscribers                                                    [Watch on](https://www.youtube.com/watch?v=t8-ibxR5j0Q)

## Add a variable

1. In a flow step, click the text field where you want to add info from a previous step.
2. If the button shows, click **Variables +**.

   - Or, type **@** to find the variable dropdown menu.
3. On the dropdown menu, select the starter or output from a previous step you want to use.
   - The variable will be added as a colored chip.

**Tips:**

- Some fields only accept certain types of data, like:
  - Email addresses
  - Dates
- If no compatible variables are available from previous steps, the option to add one may not show.

## Examples on how to use variables

- **Notify someone about an email:** In a "Send a message" step in Chat, use the "\[Sender email address\]" variable from your Gmail starter in the recipient field to send them a direct message.
- **Use AI-generated text:** You can ask Gemini to summarize a doc and use the "\[Gemini summary\]" output variable to send that summary in an email.
- **Log and summarize data:** When a Google Form is submitted, you can use variables to summarize the responses with Gemini and send the summary to a Chat space.

## Related resources

- [Tips to use AI steps in flows](https://support.google.com/a/users/answer/16431105)
- [Guide to starters and steps in Workspace Studio](https://support.google.com/workspace-studio/answer/16765661)

Give feedback about this article

Choose a section to give feedback on

true

8241298360210135871

true

Search Help Center

false

true

true

true

[Google Help](https://support.google.com/)

[Help Center](https://support.google.com/workspace-studio/?hl=en) [Workspace Studio](https://studio.workspace.google.com/)

[Privacy Policy](https://www.google.com/intl/en/privacy.html) [Terms of Service](https://www.google.com/accounts/TOS)Submit feedback

false

false

## What is the issue with this selection?

What is the issue with this selection?

Inaccurate - doesn't match what I see in the product

Hard to understand - unclear or translation is wrong

Missing info - relevant but not comprehensive

Irrelevant - doesn’t match the title and / or my expectations

Minor errors - formatting issues, typos, and / or broken links

Other suggestions - ideas to improve the content

## Share additional info or suggestions

​

​

Do not share any personal info

Cancel

Submit

By continuing, you agree Google uses your answers, [account & system info](https://support.google.com/workspace-studio/answer/16448468#) to improve services, per our [Privacy](https://myaccount.google.com/privacypolicy?hl=en) & [Terms](https://policies.google.com/terms?hl=en).

false

false

false

Main menu

Google apps
