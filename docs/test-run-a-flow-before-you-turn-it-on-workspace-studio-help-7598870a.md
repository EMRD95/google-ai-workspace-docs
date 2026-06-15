---
title: "Test run a flow before you turn it on - Workspace Studio Help"
source_url: "https://support.google.com/workspace-studio/answer/16663517"
product_area: "workspace-studio"
retrieved_at: "2026-06-15T17:48:10Z"
extraction_method: "web_extract"
---

[Skip to main content](https://support.google.com/workspace-studio/answer/16663517#search-form)

# Test run a flow before you turn it on

Before you turn on a flow to run automatically, you can run it once using real data to check the results. This helps you see if it does what you want. You can also use a test run to run a flow manually if you don’t want it to run automatically.

**Important:** A test run does real actions. For example, it sends messages, sets up calendar events, and changes docs. If you’re worried about bothering other people or changing important files, see the tips on this page for how to do safer test runs.

## Do a test run

![](https://storage.googleapis.com/support-kms-prod/4BMw4ze7sYv0aoC6pJUaNVGDdmDUWd1gje7A)

1. Go to [https://studio.workspace.google.com](https://studio.workspace.google.com/) and [create a flow](https://support.google.com/a/users/answer/16430397).
2. (Optional) Change your flow a little so it doesn't affect other people or real files. For tips, on this page see [Tips for a safer test run](https://support.google.com/workspace-studio/answer/16663517#safer).
3. When you’re ready, click **Test run**.
4. If your flow starts with **On a schedule**, click **Start**.
5. If your flow starts in other ways, it needs existing data to use.
1. Sometimes, a default value is automatically filled in for you. For example, with **When I get an email**, it finds the last matching email you got. If that works, click **Start**. If you want to start from something else, remove what’s there, click the box, and select the one you want. Then click **Start**.
2. Sometimes, you need to select the data yourself. For example, with **When I’m mentioned in spaces** set to all spaces, you select a space, then a matching message is found automatically. Then click **Start**.

## Review test run results

![](https://storage.googleapis.com/support-kms-prod/4BMw4ze7sYv0aoC6pJUaNVGDdmDUWd1gje7A)

You can see the test run results as it goes. Some results, like a response from Gemini, are shown right there. Others, like a message in Chat, have a linked chip that you can click to see it in Chat.

You might see the following error cases:

- **Red “Test complete”:** The test run went as far as it could, but couldn’t finish because something’s wrong with the flow’s setup. Check for issues like missing required fields, incomplete conditional statements, and unconnected integrations, then try again.
- **Yellow “Test couldn’t complete”:** The test went as far as it could, but couldn’t finish because of an issue with the data it’s trying to use. For example, a security risk was blocked while running a Gemini step. Your flow might be set up correctly, but the test couldn’t run all the way through. Try using different starting data, like a different email to summarize, and try again.

## Tips for a safer test run

![](https://storage.googleapis.com/support-kms-prod/4BMw4ze7sYv0aoC6pJUaNVGDdmDUWd1gje7A)

You might not want your test run to affect other people or real files. Here are some ways to set up your flow to make that less likely. After it works in the safer setup, you can add people or real files before you turn it on.

- Have emails and chat messages sent only to you, instead of using a variable that could include other people.
- Use test documents, like a copy of the document or sheet you want your flow to update.
- Create a test meeting where you’re the only guest.

Give feedback about this article

Choose a section to give feedback on

true

Main menu

Google apps

11246236653943354327

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

By continuing, you agree Google uses your answers, [account & system info](https://support.google.com/workspace-studio/answer/16663517#) to improve services, per our [Privacy](https://myaccount.google.com/privacypolicy?hl=en) & [Terms](https://policies.google.com/terms?hl=en).

false

false

false
