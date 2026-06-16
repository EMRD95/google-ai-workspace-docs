---
title: "Combined source: chat"
product_area: "chat"
source_count: 18
generated_at: "2026-06-16T08:47:02Z"
source_type: "coverage_merged_official_extracts"
---

# Combined source: chat

This file merges 18 official extracted source document(s) from coverage area `chat` for NotebookLM import limits.
No synthetic documentation is added; each section preserves the source URL and extracted Markdown body.

## Source index

1. Build a Google Chat app with a Gemini Enterprise AI agent Stay organized with collections Save and categorize content based on your preferences. — https://developers.google.com/workspace/add-ons/chat/quickstart-ge-agent?hl=en
2. Chat apps built by Google - Google Chat Help — https://support.google.com/chat/answer/9649420
3. Collaborate with Gemini in Google Chat - Computer - Google Chat Help — https://support.google.com/chat/answer/15345722?hl=en
4. Collaborate with Gemini in Google Chat (Workspace Experiments) - Computer - Google Chat Help — https://support.google.com/chat/answer/15395284
5. Get started with Ask Gemini in Google Chat - Computer - Google Chat Help — https://support.google.com/chat/answer/17036303?hl=en
6. Get started with Google Workspace with Gemini - Business / Enterprise - Google Chat Help — https://support.google.com/chat/answer/13952129
7. Improve your Chat messages with Refine - Google Chat Help — https://support.google.com/chat/answer/16512046
8. Learn about spaces - Google Chat Help — https://support.google.com/chat/answer/7659784
9. Manage space settings - Computer - Google Chat Help — https://support.google.com/chat/answer/13340792
10. Meet app for Google Chat Turndown - Google Chat Help — https://support.google.com/chat/answer/7655908
11. Summarize chats in Google Chat - Computer - Google Chat Help — https://support.google.com/chat/answer/12918975
12. Use an AI Overview in Google Chat - Google Chat Help — https://support.google.com/chat/answer/16944767
13. Use apps in Google Chat - Computer - Google Chat Help — https://support.google.com/chat/answer/7655820
14. Use the Bulk Member Manager app in Google Chat - Computer - Google Chat Help — https://support.google.com/chat/answer/14016224
15. Use the Jenkins app in Google Chat - Computer - Google Chat Help — https://support.google.com/chat/answer/9632691
16. Use the Jira app in Google Chat - Computer - Google Chat Help — https://support.google.com/chat/answer/9575067
17. Use the PagerDuty app in Google Chat - Computer - Google Chat Help — https://support.google.com/chat/answer/12156602
18. Use the Zapier app in Google Chat - Computer - Google Chat Help — https://support.google.com/chat/answer/9470843

---

## Source 1: Build a Google Chat app with a Gemini Enterprise AI agent Stay organized with collections Save and categorize content based on your preferences.

- Source URL: https://developers.google.com/workspace/add-ons/chat/quickstart-ge-agent?hl=en
- Original file: `docs/build-a-google-chat-app-with-a-gemini-enterprise-ai-agent-stay-organized-with-co-37a1f379.md`
- Product area: `chat`

# Build a Google Chat app with a Gemini Enterprise AI agent Stay organized with collections Save and categorize content based on your preferences.

Source: https://developers.google.com/workspace/add-ons/chat/quickstart-ge-agent?hl=en

- [Home](https://developers.google.com/)
- [Google Workspace](https://developers.google.com/workspace)
- [Add-ons](https://developers.google.com/workspace/add-ons/overview)

Send feedback

# Build a Google Chat app with a Gemini Enterprise AI agent Stay organized with collections Save and categorize content based on your preferences.

This page explains how to build a Google Workspace add-on that works in
Google Chat and interfaces with a
[Gemini Enterprise](//docs.cloud.google.com/gemini/enterprise/docs/get-started)
AI agent.

**Note:** In Google Chat, add-ons appear to users as
Google Chat apps. You can also build your Chat app using
*Google Chat API interaction events*. To learn more, see the
[Extend Google Chat overview](/workspace/add-ons/chat).

AI agents autonomously perceive their environment, reason, and execute complex,
multi-step actions to achieve a defined goal. In this tutorial, you use
[the Idea Generation agent](//docs.cloud.google.com/gemini/enterprise/docs/idea-generation)
provided by default by Google that helps with innovation and problem-solving for
enterprise users.

![Idea Generation agent as Chat app.](/static/workspace/add-ons/images/quickstart-ge-agent.png)

The following diagram shows the architecture and messaging pattern:

![Architecture of a Chat app implemented with a Gemini Enterprise AI agent.](/static/workspace/add-ons/images/design-patterns/ge-agent.svg)

In the preceding diagram, a user interacting with a
Chat app implemented with a Gemini Enterprise AI agent
has the following flow of information:

1. A user sends a message to a Chat app, either in a
   direct message or in a Chat space.
2. The Chat app logic that's implemented either in
   Apps Script or as a web server with HTTP endpoints receives
   and processes the message.
3. The Gemini Enterprise AI agent receives and processes the interaction.
4. Optionally, the Chat app or AI agent can integrate
   with Google Workspace services, such as Calendar or
   Sheets, or other Google services, such as Google Maps
   or YouTube.
5. The Chat app asynchronously sends responses
   using the Google Chat API to communicate the AI agent progress.
6. The responses are delivered to the user.

## Objectives

- Set up your environment.
- Deploy the Chat app.
- Configure the Chat app.
- Test the Chat app.

## Prerequisites

- A Business or Enterprise
  [Google Workspace](https://support.google.com/a/answer/6043576) account with access to
  [Google Chat](https://workspace.google.com/products/chat/).
- A Google Cloud project with billing enabled. To check that an existing project has billing enabled,
  see [Verify the
  billing status of your projects](https://cloud.google.com/billing/docs/how-to/verify-billing-enabled). To create a project and set up billing, see
  [Create a Google Cloud project](/workspace/guides/create-project).
- A [Gemini Enterprise app](//docs.cloud.google.com/gemini/enterprise/docs/create-app)
  set up with Google Identity as identity provider.

## Set up your environment

### Turn on the Chat API

Before using Google APIs, you need to turn them on in a Google Cloud project.
You can turn on one or more APIs in a single Google Cloud project.

In the Google Cloud console, enable the Google Chat API.

[Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=chat.googleapis.com)

### Configure the OAuth consent screen

All apps using OAuth 2.0 require a consent screen configuration. Configuring
your app's OAuth consent screen defines what is displayed to users and app
reviewers, and registers your app so you can publish it later.

1. In the Google API Console, go to Menu menu
   > **Google Auth platform**
   > **Branding**.

   [Go to Branding](https://console.developers.google.com/auth/branding)
2. If you have already configured the Google Auth platform, you can configure the following OAuth Consent Screen settings in [Branding](https://console.developers.google.com/auth/branding), [Audience](https://console.developers.google.com/auth/audience), and [Data Access](https://console.developers.google.com/auth/scopes). If you see a message that says **Google Auth platform not configured yet**, click **Get Started**:

1. Under **App Information**, in **App name**, enter a name for the app.
2. In **User support email**, choose a support email address where users can contact you if they have questions about their consent.
3. Click **Next**.
4. Under **Audience**, select **Internal**.
5. Click **Next**.
6. Under **Contact Information**, enter an **Email address** where you can be notified about any changes to your project.
7. Click **Next**.
8. Under **Finish**, review the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy) and if you agree, select **I agree to the Google API Services: User Data Policy**.
9. Click **Continue**.
10. Click **Create**.

3. For now, you can skip adding scopes.
   In the future, when you create an app for use outside of your
   Google Workspace organization, you must change the **User type** to **External**. Then
   add the authorization scopes that your app requires. To learn more, see the full
   [Configure OAuth consent](/workspace/guides/configure-oauth-consent) guide.

### Create a service account in Google Cloud console

Create a new service account with the role `Discovery Engine User` by following
these steps:

### Google API Console

1. In the Google API Console, go to Menu menu
   > **IAM & Admin**
   > **Service Accounts**.

   [Go to Service Accounts](https://console.developers.google.com/iam-admin/serviceaccounts)
2. Click **Create service account**.
3. Fill in the service account details, then click **Create and continue**.
   Note: By default, Google creates a unique service account ID. If you would like to
   change the ID, modify the ID in the service account ID field.
4. Optional: Assign roles to your service account to grant access to your Google Cloud project's resources. For more details, refer to [Granting, changing, and revoking access to resources](https://cloud.google.com/iam/docs/granting-changing-revoking-access).
5. Click **Continue**.
6. Optional: Enter users or groups that can manage and perform actions with this service account. For more details, refer to [Managing service account impersonation](https://cloud.google.com/iam/docs/impersonating-service-accounts).
7. Click **Done**. Make a note of the email address for the service account.

### gcloud CLI

1. Create the service account:

   ```
   gcloud iam service-accounts create SERVICE_ACCOUNT_NAME \
     --display-name="SERVICE_ACCOUNT_NAME"
   ```
2. Optional: Assign roles to your service account to grant access to your Google Cloud project's resources. For more details, refer to [Granting, changing, and revoking access to resources](https://cloud.google.com/iam/docs/granting-changing-revoking-access).

The service account appears on the service account page.

### Create a private key

**Warning:**  This example uses an exported
service account key for simplicity's sake. Exporting a private key is not
recommended in production because it shouldn't be stored in an insecure
location, such as source control.

To learn more about secure service
account implementations and best practices, see
[Choose
when to use service accounts](https://cloud.google.com/iam/docs/best-practices-for-using-and-managing-service-accounts#choose-when-to-use).

To create and download a private key for the service account, follow these
steps:

1. In the Google Cloud console, go to Menu menu
   > **IAM & Admin**
   > **Service Accounts**.

   [Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)
2. Select your service account.
3. Click **Keys** > **Add key** > **Create new key**.
4. Select **JSON**, then click **Create**.

   Your new public/private key pair is generated and downloaded to your
   machine as a new file. Save the downloaded JSON file as `credentials.json` in your
   working directory. This file is the only copy of this key. For information about how to store
   your key securely, see
   [Managing service account keys](https://cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).
5. Click **Close**.

For more information about service accounts, see
[service accounts in the Google Cloud IAM documentation](https://cloud.google.com/iam/docs/service-accounts).

## Create and configure the Chat app project

1. In the Google API Console, go to Menu menu
   > **IAM & Admin**
   > **Settings**.

   [Go to IAM & Admin Settings](https://console.developers.google.com/iam-admin/settings)
2. Note the **Project number** and **Project ID** fields.
3. Go to Gemini Enterprise:

   [Open Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/apps)
4. Note the **Location** and **ID** of the application.
5. Click the following button to open the **GE AI Agent Quickstart**
   Apps Script project.

   [Open the project](https://script.google.com/d/1YeDvZtq5c5TU2DXFVCNGjA6RCVkUn5x0ip5QVksmSwgsy7gwpI7izPLt/edit?usp=sharing)
6. Click info\_outline **Overview** > ![The icon for making a copy](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/file_copy/default/24px.svg) **Make a copy**.
7. In your Apps Script project,
   click ![The icon for project settings](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/settings/default/24px.svg) **Project Settings**
   > **Edit script properties** > **Add script property**
   to add the following script properties:

   1. `REASONING_ENGINE_RESOURCE_NAME` with the Gemini Enterprise app resource
      composed with the information noted in previous steps.

      ```
      projects/PROJECT_ID/locations/APP_LOCATION/collections/default_collection/engines/APP_ID
      ```
   2. `SERVICE_ACCOUNT_KEY` with the JSON key from the service account
      downloaded in previous steps such as `{ ... }`.
8. Click **Save script properties**
9. In your Apps Script project,
   click ![The icon for project settings](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/settings/default/24px.svg) **Project Settings**.
10. Under **Google Cloud Platform (GCP) Project**, click **Change project**.
11. In **GCP project number**, paste the Google Cloud project number noted in
    previous steps.
12. Click **Set project**. The Cloud project and
    Apps Script project are now connected.

## Create a test deployment

You need a deployment ID for this Apps Script project, so that
you can use it in the next step.

To get the head deployment ID, do the following:

1. In the Chat app Apps Script project,
   click **Deploy**
   > **Test deployments**.
2. Under **Head deployment ID**, click ![The icon for making a copy](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/file_copy/default/24px.svg)
   **Copy**.
3. Click **Done**.

## Configure the Chat app

Using your Apps Script deployment, follow these steps to deploy the Google Chat app for testing:

1. In the [API Console](https://console.developers.google.com/), search for `Google Chat API`,
   and click **Google Chat API**.
2. Click **Manage**.
3. Click **Configuration** and set up the Chat app:

   1. In the **App name** field, enter `GE Quickstart`.
   2. In the **Avatar URL** field, enter
      `https://developers.google.com/workspace/add-ons/images/quickstart-app-avatar.png`.
   3. In the **Description** field, enter `GE Quickstart`.
   4. Under **Functionality**, select **Join spaces and group conversations**.
   5. Under Connection settings, select **Apps Script project**.
   6. In the **Deployment ID** field, paste the Head deployment ID that you
      previously copied.
   7. Under Visibility, select **Specific people and groups in your
      domain**, and enter your email.
4. Click **Save**.

The Chat app is ready to respond to messages.

## Test the Chat app

To test your Chat app, open a direct message space with
the Chat app and send a message:

1. Open Google Chat using the Google Workspace account that you
   provided when you added yourself as a trusted tester.

   [Go to Google Chat](https://chat.google.com)
2. Click add **New chat**.
3. In the **Add 1 or more people** field, type the name of your
   Chat app.
4. Select your Chat app from the results. A direct
   message opens.

   **Note:** If you don't see your Chat app in the list of
   results, ensure that you've included your Google Workspace account in the
   **Visibility** settings of the [**Chat API Configuration**](/workspace/chat/configure-chat-api)
   page in the Google API Console.
5. In the new direct message with the app, type `I need to find ideas!` and press`enter`.

   The Chat app replies with **Default Idea Generation** agent response.

To add trusted testers and learn more about testing interactive features, see
[Test interactive features for
Google Chat apps](/workspace/chat/test-interactive-features).

## Troubleshoot

When a Google Chat app or
[card](/workspace/chat/create-messages#create) returns an error, the
Chat interface surfaces a message saying "Something went wrong."
or "Unable to process your request." Sometimes the Chat UI
doesn't display any error message, but the Chat app or
card produces an unexpected result; for example, a card message might not
appear.

Although an error message might not display in the Chat UI,
descriptive error messages and log data are available to help you fix errors
when error logging for Chat apps is turned on. For help viewing,
debugging, and fixing errors, see
[Troubleshoot and fix Google Chat errors](/workspace/chat/troubleshoot).

## Clean up

To avoid incurring charges to your Google Cloud account for the
resources used in this tutorial, we recommend that you delete the
Cloud project.

**Caution:** Deleting a project has the following effects:

- **Everything in the project is deleted.** If you used an existing project for this tutorial, when you delete it, you also delete any other work you've done in the project.
- **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as a URL on appspot.com, delete the selected resources inside the project instead of deleting the whole project.

If you plan to explore multiple tutorials and quickstarts, reusing projects can help you avoid exceeding project quota limits.

1. In the Google API Console, go to the **Manage resources** page. Click
   **Menu** menu
   > **IAM & Admin**
   > **Manage Resources**.

   [Go to Resource Manager](https://console.developers.google.com/cloud-resource-manager)
2. In the project list, select the project you want to delete and then click
   **Delete** delete.
3. In the dialog, type the project ID and then click **Shut down** to delete
   the project.

## Related topics

- [Build Gemini Enterprise agents that are tightly integrated with Workspace data stores, APIs, and Chat apps](//codelabs.developers.google.com/ge-gws-agents)
- [Build Vertex AI agents that are tightly integrated with Workspace data stores, APIs, and Chat apps](//codelabs.developers.google.com/vertexai-gws-agents)
- [Build a Google Chat app with an ADK AI agent](/workspace/add-ons/chat/quickstart-adk-agent)
- [Build a Google Chat app with an ADK AI agent exposed by A2A](/workspace/add-ons/chat/quickstart-a2a-agent)
- [Build a Google Chat app with an ADK AI agent exposed by A2UI](/workspace/add-ons/chat/quickstart-a2ui-agent)
- [Fact-check statements with an ADK AI agent and Gemini model](/apps-script/samples/custom-functions/fact-check)
- [Plan travels with an AI agent accessible across Google Workspace](/workspace/add-ons/samples/travel-concierge)
- [Integrate fundamental AI concepts in Chat apps](//codelabs.developers.google.com/chat-apps-ai-concepts)
- [Answer questions based on Chat conversations with a Gemini AI Chat app](/workspace/add-ons/samples/tutorial-ai-knowledge-assistant)
- [Respond to incidents with Google Chat, Vertex AI, Apps Script, and user authentication](/workspace/add-ons/samples/tutorial-incident-response-user-auth)
- [Manage projects with Google Chat, Vertex AI, and Firestore](/workspace/add-ons/samples/tutorial-project-management)

Send feedback

---

## Source 2: Chat apps built by Google - Google Chat Help

- Source URL: https://support.google.com/chat/answer/9649420
- Original file: `docs/chat-apps-built-by-google-google-chat-help-38aae835.md`
- Product area: `chat`

[Skip to main content](https://support.google.com/chat/answer/9649420#search-form)

# Chat apps built by Google

These Chat apps are available for personal, work, and school accounts.

If you use Chat with a work or school account, your administrator may need to give you permission to install or use Chat apps. [Who is my administrator?](https://support.google.com/a/answer/6208960)

For information about an app, click the app’s name.

| App name | Category | Description |
| --- | --- | --- |
| [Asana](https://support.google.com/hangoutschat/answer/9632129) | Tracking | Get notifications about Asana projects. |
| [Bulk Member Manager](https://support.google.com/chat/answer/14016224) | Google | Manage space membership in bulk. |
| [Feeds](https://support.google.com/chat/answer/16774650) | Communication | Get updates from RSS Feeds. |
| [Giphy](https://support.google.com/hangoutschat/answer/9632290) | Social & fun | Post GIFs in spaces and conversations. |
| [GitHub](https://support.google.com/hangoutschat/answer/9632291) | Developer | Get updates about GitHub projects. |
| [Google Cloud Build](https://support.google.com/chat/answer/9914994) | Developer | Get updates from Google Cloud Build. |
| [Google Drive](https://support.google.com/hangoutschat/answer/7660707) | Google | Get updates about activity in Drive. |
| [Jenkins](https://support.google.com/hangoutschat/answer/9632691) | Developer | Get updates about Jenkins builds or trigger jobs. |
| [Jira](https://support.google.com/chat/answer/9575067) | Developer | Get updates from Jira Cloud. |
| [PagerDuty](https://support.google.com/chat/answer/12156602) | Tracking | Get notifications about PagerDuty incidents. |
| [Poll](https://support.google.com/chat/answer/15667559) | Google | Gather team input quickly and make decisions with Google Chat's Poll app. |
| [Salesforce](https://support.google.com/hangoutschat/answer/9632289) | Tracking | Search for info in Salesforce. |
| [Workday](https://support.google.com/chat/answer/13790449) | Human Resources | Complete Workday quick actions. |
| [Zapier](https://support.google.com/hangoutschat/answer/9470843) | Automation | Get updates about Zap actions. |
| [Zendesk](https://support.google.com/hangoutschat/answer/9632209) | Support | Get updates when issues occur in Zendesk. |

_Google, Google Workspace, and related marks and logos are trademarks of Google LLC. All other company and product names are trademarks of the companies with which they are associated._

**Tip:** For other apps, [check out our Marketplace](https://support.google.com/marketplace/answer/6067029).

Give feedback about this article

Choose a section to give feedback on

## Need more help?

### Try these next steps:

[Post to the help community  Get answers from community members](https://support.google.com/chat/community?hl=en&help_center_link=CIz6zAQSGUNoYXQgYXBwcyBidWlsdCBieSBHb29nbGU)

true

12679049797548708393

true

Search Help Center

false

true

true

true

[Google Help](https://support.google.com/)

[Help Center](https://support.google.com/chat/?hl=en) [Community](https://support.google.com/chat/community?hl=en&help_center_link=CIz6zAQSGUNoYXQgYXBwcyBidWlsdCBieSBHb29nbGU) [Google Chat](https://chat.google.com/)

[Privacy Policy](https://www.google.com/intl/en/privacy.html) [Terms of Service](https://www.google.com/accounts/TOS)Submit feedback

true

true

1026838

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

By continuing, you agree Google uses your answers, [account & system info](https://support.google.com/chat/answer/9649420#) to improve services, per our [Privacy](https://myaccount.google.com/privacypolicy?hl=en) & [Terms](https://policies.google.com/terms?hl=en).

false

false

false

Search

Clear search

Close search

Main menu

Google apps

---

## Source 3: Collaborate with Gemini in Google Chat - Computer - Google Chat Help

- Source URL: https://support.google.com/chat/answer/15345722?hl=en
- Original file: `docs/collaborate-with-gemini-in-google-chat-computer-google-chat-help-0bffb825.md`
- Product area: `chat`

# Collaborate with Gemini in Google Chat — Summary

**Source:** Google Chat Help — “Collaborate with Gemini in Google Chat”  
**Applies to:** Computer / Google Chat

## Overview

Gemini in Google Chat helps users collaborate across Chat conversations by allowing them to:

- **Find information from any conversation in Chat**
- **Generate summaries** of specific topics discussed in a space or file
- **Summarize unread messages**
- **List action items**
- **Answer questions** about previous conversations

---

## Feature Availability

Gemini in Chat is only available under certain conditions:

- Requires an **eligible Google Workspace subscription**
- Availability depends on supported languages for **Google Workspace with Gemini**
- **Alpha users** may not have access to the side panel in Google Chat
- Users with access to **Ask Gemini in Google Chat** can access Gemini collaboration tools through Ask Gemini

---

## Getting Started with Gemini in Chat

To use Gemini in Chat on a computer:

1. Go to [chat.google.com](https://chat.google.com/)
   - Or open the **Chat standalone app**
   - Or open **Chat in Gmail**
2. At the top right, click **Ask Gemini**
3. Use either:
   - A suggested prompt
   - Your own prompt in the prompt box

### Use a Suggested Prompt

1. Select a suggestion from the list
   - Select **More suggestions** to see additional options
2. Replace the example text in the prompt box with your own information
3. Press **Enter**

### Enter Your Own Prompt

1. Type a prompt in the prompt box at the bottom
2. Press **Enter**

---

## Important Tips

Gemini conversation history in Chat may be lost when:

- You refresh your browser
- You close and reopen Chat
- Your computer goes offline

To remove conversation history:

> Click **More options** → **Clear history**

---

## Gemini in Chat Controls and Actions

| Action | Purpose |
|---|---|
| **Ask Gemini** | Open Gemini |
| **More options** | Clear recent Gemini history or ask for more suggestions |
| **Expand** | Make Gemini larger |
| **Collapse** | Return Gemini to its original size |
| **Close** | Close Gemini |
| **Clear history** | Remove all generated text and images |
| **More suggestions** | Find more Gemini suggestions |
| **More image suggestions** | Find more image suggestions from Gemini |
| **Insert** | Insert generated text into your Chat |
| **Copy** | Copy a suggestion |
| **Retry with Google Search** | Search Google for more information about your question or request |
| **View more** | Show more of Gemini’s response |
| **View less** | Minimize Gemini’s response |
| **Good suggestion** | Give positive feedback on a Gemini response |
| **Bad suggestion** | Report an issue with a Gemini response |

---

## Things You Can Ask Gemini in Chat

Gemini can help with questions, summaries, files, and action items across conversations.

---

## 1. Answer Questions About Conversations

Gemini can search through your chat history to answer questions about conversations.

You can ask specific questions and may receive citations.

### Example Prompts

> “What did [leader name] announce to the team yesterday?”

> “What’s the decision on the project discussed in this conversation?"

---

## 2. Summarize a Conversation

Gemini can search through chat history and summarize conversations, unread messages, or specific topics.

### Example Prompts

> "Summarize my unread messages."

> "What are the key takeaways in this conversation?”

After receiving an initial summary, you can ask for more detail:

> "Give me a detailed summary of [topic] discussed in this space."

---

## 3. Summarize a File

Gemini can summarize files shared in a Chat conversation if certain requirements are met.

### File Summary Requirements

Gemini can summarize a file if:

- The message is **not blocked**
- The file is shared as a **Drive link** in Google Chat
- Download restrictions are **off** for the file

### Supported File Types

Gemini can summarize:

- Google Docs
- Google Sheets
- Google Slides
- `.pdf`
- `.csv`
- `.txt`
- Zip files
- Microsoft Office formats, including:
  - `.docx` — Word
  - `.xlsx` — Excel
  - `.pptx` — PowerPoint

### How to Summarize a File

1. On your computer, open [Google Chat](https://chat.google.com/) or [Gmail](https://gmail.google.com/)
   - In Gmail, click **Chat** on the left
2. Select a direct message or space that contains a file
3. Under the file, click **Summarize this file**

---

## 4. List Action Items

Gemini can identify action items from any conversation.

### Example Prompts

> "What are the action items in this conversation?”

> “Are there any action items for me?"

> “Summarize [person's] action items”

---

## Giving Feedback on Gemini Output

Google states that Workspace with Gemini is continuously improving and may not always support every request.

### Important Feedback Warning

> Because feedback may be human readable, please do not submit data that contains personal, confidential, or sensitive information.

If Gemini g

[... summary truncated for context management ...]

---

## Source 4: Collaborate with Gemini in Google Chat (Workspace Experiments) - Computer - Google Chat Help

- Source URL: https://support.google.com/chat/answer/15395284
- Original file: `docs/collaborate-with-gemini-in-google-chat-workspace-experiments-computer-google-chat-he-5dc77b33.md`
- Product area: `chat`

# Collaborate with Gemini in Google Chat — Markdown Summary

**Source:** Google Chat Help — “Collaborate with Gemini in Google Chat (Workspace Experiments)”  
**URL:** https://support.google.com/chat/answer/15395284  
**Platform covered:** Computer

---

## Overview

Gemini in Google Chat lets users collaborate with AI from within an open space or conversation. It can help users:

- **Summarize** a space or conversation.
- **Generate action items** from a space or conversation.
- **Answer specific questions** about a space or conversation.

---

## Feature Availability

Gemini in Chat is available through Google’s early access testing program:

> **“This feature is available as part of our early access testing program”**

Availability notes:

- Part of **Google Workspace Experiments**.
- Also available in **Gemini Business** and **Gemini Enterprise Alpha**.
- To turn off Workspace Experiments features, users must **exit the Workspace Experiments program**.

---

## Get Started with Gemini in Chat

### Open Gemini in Chat

1. On your computer, go to [chat.google.com](https://chat.google.com/).
   - You can also use:
     - The **Chat standalone app**
     - **Chat in Gmail**
2. At the top right, click **Ask Gemini**.
3. In the side panel:
   - Select a suggested prompt, or
   - Write your own prompt.

---

## Example Prompts

### Ask Gemini to find information from past chats

Original examples:

> `When are we launching [feature name]?`

> `What did [colleague] announce to the team yesterday?`

### Ask Gemini to summarize multiple conversations

Original examples:

> `Summarize my conversations with [colleague] from this week.`

> `Summarize my unread messages.`

---

## Using Suggested Prompts

To use a suggested prompt:

1. Select from the list of suggestions.
   - To see more, select **More suggestions**.
2. At the bottom, in the prompt box, replace the example text with the information you want.
3. Press **Enter**.

---

## Entering Your Own Prompt

To write your own prompt:

1. At the bottom of the side panel, enter a prompt in the prompt box.
2. Press **Enter**.

---

## Conversation History Tips

Gemini in Chat conversation history may be lost when:

- You refresh your browser.
- You close and reopen Chat.
- Your computer goes offline.

To remove your Gemini conversation history:

1. Click **More options**.
2. Select **Clear history**.

---

## Gemini in Chat Controls and Actions

| Action | Purpose |
|---|---|
| **Ask Gemini** | Open Gemini. |
| **More options** | Clear recent Gemini history and ask for more suggestions. |
| **Expand** | Make Gemini larger. |
| **Collapse** | Return Gemini to its original size. |
| **Close** | Close Gemini. |
| **Clear history** | Remove generated text and images that haven’t been inserted into the document yet. |
| **More suggestions** | Find more suggestions from Gemini. |
| **More image suggestions** | Find more image suggestions from Gemini. |
| **Insert** | Insert generated text into your Chat. |
| **Copy** | Copy a suggestion. |
| **Retry with Google Search** | Search Google for more information about your question or request. |
| **View more** | Show more of Gemini’s response. |
| **View less** | Minimize Gemini’s response. |
| **Good suggestion** | Give positive feedback about a Gemini response. |
| **Bad suggestion** | Report an issue with a Gemini response. |

---

# Things You Can Ask Gemini in Chat

Gemini can help with an open conversation or space by:

- Summarizing the conversation.
- Listing action items.
- Answering specific questions.
- Summarizing supported files shared in Chat.

---

## Summarize a Conversation

Gemini can summarize a conversation that is currently open in Chat.

Suggested prompts include:

> `"Summarize this conversation."`

> `"What are the key takeaways in this conversation?”`

After receiving an initial summary, you can request more detail:

> `"Give me a detailed summary of [topic] discussed in this space."`

**Important:** The relevant conversation should be open while using Gemini in Chat.

---

## Summarize a File in a Chat Conversation

Gemini can summarize a file shared within a conversation if certain conditions are met.

### Requirements

A file can be summarized if:

- The message is **not blocked**.
- The file is shared as a **Drive link** in Google Chat.
- Download restrictions are **off** for the file.

### Supported File Types

Gemini can summarize these files shared as Drive links:

- Google Docs
- Google Sheets
- Google Slides
- `.pdf`
- `.csv`
- `.txt`
- Zip files
- Microsoft Office formats, including:
  - `.docx` — Word
  - `.xlsx` — Excel
  - `.pptx` — PowerPoint

### Steps to Summarize a File

1. On your computer, open:
   - [Google Chat](https://chat.google.com/), or
   - [Gmail](https://gmail.google.com/)
2. If using Gmail:
   - On the left, click **Chat**.
3. Select a direct message or space containing a file.
4. Under the file, click **Summarize this file**.

---

## List Action Items

Gemini can identi

[... summary truncated for context management ...]

---

## Source 5: Get started with Ask Gemini in Google Chat - Computer - Google Chat Help

- Source URL: https://support.google.com/chat/answer/17036303?hl=en
- Original file: `docs/get-started-with-ask-gemini-in-google-chat-computer-google-chat-help-c3b294c2.md`
- Product area: `chat`

# Get started with Ask Gemini in Google Chat — Summary

**Source:** https://support.google.com/chat/answer/17036303?hl=en  
**Platform covered:** Computer / Google Chat / Gmail Chat

---

## Overview

**Ask Gemini in Google Chat** is an AI-powered assistant designed to help users manage work, find information, summarize updates, draft communications, generate images, and manage calendar events from within Google Chat.

It can help you:

- Find quick answers from scattered information across **Google Workspace data**
- Summarize updates on key topics across **Chat spaces**
- Identify **daily priorities**
- Search the web or Workspace content such as **Gmail, Google Drive, and Google Calendar**
- Draft emails or chat messages
- Generate images
- Catch up on unread messages and updates
- Schedule, reschedule, delete, or find calendar events

---

## Feature Availability

> **Feature availability**
>
> - Ask Gemini features are rolling out gradually as part of the Gemini Alpha; only some Gemini Alpha users will have access to Ask Gemini.
> - You may not have access to some or all of the Ask Gemini features.
>
> - Your administrator controls access to the Gemini Alpha. If you can’t find these features, your administrator may not have Alpha features enabled for your organization.

**Important requirement:**

> **Important:** To use these features, you must enroll in Workspace Smart Features.

---

## How to Find Ask Gemini in Google Chat

1. On your computer, open:
   - [Google Chat](https://chat.google.com/), or
   - [Gmail](https://mail.google.com/)
     - In Gmail, click **Chat** on the left.

2. Find **Ask Gemini**.

### Locations and Shortcuts

| Where to find Ask Gemini in Chat | Steps |
|---|---|
| **Shortcuts or Conversation list** | On the left, under **“Shortcuts,”** click **Ask Gemini**. |
| **Keyboard shortcut** | **ChromeOS and Windows:** `Ctrl + g`<br>**macOS:** `Command + g` |

---

## Use Ask Gemini to Answer Specific Questions

Ask Gemini can search across your Workspace or the web and provide a unified response. It keeps context across conversations, so you may not need to repeat details every time.

### Steps

1. Open **Ask Gemini** in Google Chat.
2. Type a prompt in the message field.
3. Click **Send**.

### Example Prompts

> “Find me the deck about [Project Name] that [Person’s Name] shared with me last week.”

> “Give me the latest update on [Example Topic].”

> “What did [Person's Name] ask me last week about [Example Topic] and when am I meeting them next?”

**Tip:** Ask Gemini includes **citations** to show the source of its information.

---

## Use Ask Gemini to Prepare for Your Day

You can ask Gemini for current action items based on the most recent available information.

### Steps

1. Open **Ask Gemini** in Google Chat.
2. Enter a prompt.
3. Click **Send**.

### Example Prompt

> “What are my action items?”

---

## Use Ask Gemini to Draft Communications

Ask Gemini can draft or refine emails and chat messages.

### Steps

1. Open **Ask Gemini** in Google Chat.
2. Enter a prompt.
3. Click **Send**.

### Example Prompts

> “Draft an email to [Person’s Name] summarizing our progress on [Topic Name].”

> “Refine the following chat message I am sending to [Person’s Name]: [Paste your draft here]. Make sure it’s professional and concise.”

---

## Use Ask Gemini to Generate Images

You can create images directly from Chat using Ask Gemini. Prompts can specify style, setting, subject, or purpose.

### Steps

1. Open **Ask Gemini** in Google Chat.
2. Enter an image-generation prompt.
3. Click **Send**.

### Example Prompts

> “Generate an image of a futuristic workspace in an ultra-realistic style.”

> “Create an image showing the team welcoming our new sales lead.”

> “Create a colorful icon for [Project Name].”

---

## Use Ask Gemini for Catch-Up Summaries

Ask Gemini can summarize missed updates, unread messages, emails, and activity in spaces.

### Steps

1. Open **Ask Gemini** in Google Chat.
2. Enter a catch-up prompt.
3. Click **Send**.

### Example Prompts

> “What did I miss on [date or topic]?”

> “Summarize some of the latest updates in [Space Name].”

> “Catch me up on unread messages.”

---

## Use Ask Gemini to Schedule, Manage, or Find Events

Ask Gemini can help with calendar-related tasks, including:

- Scheduling events
- Rescheduling existing events
- Deleting events
- Finding open time slots
- Checking calendar availability

### Steps

1. Open **Ask Gemini** in Google Chat.
2. Enter a calendar-related prompt.
3. Click **Send**.

### Example Prompts

> “Create a 30 minute meeting with [Person’s Name] this week.”

> “Schedule 1 hour of focus time for me this week.”

> “Reschedule meeting with [Person’s Name] to next week.”

---

## Give Feedback About Ask Gemini

Google notes that Gemini may not always support a request or provide accurate/safe suggestions.

> Google Workspace with Gemini is constantly learning and may not be able to support your request.

If a suggest

[... summary truncated for context management ...]

---

## Source 6: Get started with Google Workspace with Gemini - Business / Enterprise - Google Chat Help

- Source URL: https://support.google.com/chat/answer/13952129
- Original file: `docs/get-started-with-google-workspace-with-gemini-business-enterprise-google-chat-he-49763417.md`
- Product area: `chat`

# Get started with Google Workspace with Gemini — Summary

**Source:** Google Chat Help — “Get started with Google Workspace with Gemini”  
**URL:** https://support.google.com/chat/answer/13952129

## Overview

Google Workspace with Gemini adds AI-assisted features across Workspace apps, including drafting emails, revising documents, summarizing conversations/files, generating images/audio/video, analyzing spreadsheets, taking meeting notes, and more.

The article covers:

- Requirements to use Google Workspace with Gemini
- Gemini features by Workspace app
- Feature availability by Workspace edition: **Business, Enterprise, Frontline**
- Feature availability by personal **Google AI plans**
- Gemini Apps and NotebookLM
- Data protection, admin controls, and usage tips

---

## Key Requirements

To use Google Workspace with Gemini, you must:

- Be **18 or over**
- Have an eligible Google Account:
  - **Work or school account:** requires an eligible Google Workspace plan
  - **Personal Google Account:** requires one of:
    - Google AI Plus
    - Google AI Pro
    - Google AI Ultra

### Language Availability

Some AI features may not be available in every language. If a feature is unavailable, users can switch their Google Account to a supported language.

### Free Gemini in Gmail Features for Personal Accounts in the US

If you have a **personal Google Account**, these Gemini in Gmail features are available **at no charge in the US**:

- Help me write
- AI Overviews for email threads
- Suggested Replies

---

## Important Excerpts

> With Google Workspace with Gemini, you can use AI-assisted features to draft emails, revise documents, and more.

> To use Google Workspace with Gemini features, you need to have an eligible Google Workspace edition for your work account. Availability of Gemini features varies depending on your Google Workspace edition.

> For Google AI plans, usage limits apply.

> When you use Gemini in Gmail, Chat, Docs, Drive, Sheets, Slides, Meet, and Vids, your data is under your control.

> Your interactions with Gemini in Google Workspace apps stay within your organization. Prompts and content you generate with these features is stored alongside your Workspace content and is never shared outside your organization.

> None of your content is used for model training outside of your domain without permission.

---

# Gemini Features by Google Workspace App

## Gmail

| Feature | What it does |
|---|---|
| **AI Inbox** | Reviews top priorities and topics from your inbox |
| **AI Overview for Gmail search** | Generates concise summaries or answers from emails above search results when using natural-language questions |
| **AI Overview for email threads** | Summarizes long email conversations with key points and replies |
| **Help me schedule** | Proposes meeting times in an email |
| **Help me write** | Drafts new emails or refines existing text from a prompt |
| **Proofread** | Suggests improvements for conciseness, tone, and style beyond spelling/grammar |
| **Suggested replies** | Provides detailed, context-aware reply suggestions |
| **Summarize and draft emails** | Lets Gemini summarize, draft, and suggest responses to emails |

## Google Calendar

| Feature | What it does |
|---|---|
| **Help me schedule** | Analyzes participant availability and suggests meeting times that work for everyone |

## Google Chat

| Feature | What it does |
|---|---|
| **Answer questions** | Ask Gemini about chat history and action items |
| **Automatic Translation** | Automatically translates incoming chat messages into your preferred language |
| **Summarize conversations** | Summarizes unread messages in spaces or conversations |

## Google Docs

| Feature | What it does |
|---|---|
| **Audio generation** | Generates audio content from document text |
| **Create personalized documents** | Builds customized formatted documents such as blog posts or campaign briefs |
| **Generate an image** | Creates custom inline or cover images from text descriptions |
| **Help me write** | Drafts and refines documents |
| **Summarize a document** | Produces high-level summaries via the `@` menu or side panel |
| **Write and edit** | Writes, refines, or edits text from a prompt in the bottom bar |

## Google Drive

| Feature | What it does |
|---|---|
| **AI Overviews** | Provides high-level summaries and insights for files/folders in Drive |
| **Ask Gemini in Drive** | Finds files, generates insights, and summarizes documents across Drive |
| **Audio overviews for PDFs** | Generates audio summaries of PDFs |
| **Catch me up** | Gives an overview of recent file activities and updates |
| **File organization** | Helps organize files and folders more effectively |

## Google Forms

| Feature | What it does |
|---|---|
| **Generate questions** | Creates form questions from existing content or a topic |
| **Help me create a form** | Builds surveys/questionnaires from a prompt |
| **Summarize responses** | Analyzes open-text r

[... summary truncated for context management ...]

---

## Source 7: Improve your Chat messages with Refine - Google Chat Help

- Source URL: https://support.google.com/chat/answer/16512046
- Original file: `docs/improve-your-chat-messages-with-refine-google-chat-help-418bdcd3.md`
- Product area: `chat`

[Skip to main content](https://support.google.com/chat/answer/16512046#search-form)

# Improve your Chat messages with Refine

To improve the clarity and tone of your message before you send it, use Refine to edit your message in Google Chat.

**Important:** This feature requires an eligible Google Workspace or Google AI plan. [Learn about Gemini features and plans](https://support.google.com/docs/answer/13952129).

You can use Refine in the following languages:

- English
- French
- German
- Italian
- Japanese
- Korean
- Portuguese
- Spanish

If your draft text isn’t in these languages, you receive an error message.

## Refine your message

1. On your computer, open [Google Chat](https://chat.google.com/) or [Gmail](https://mail.google.com/).


   - **In Gmail:** On the left, click **Chat**.
2. Enter a message in Chat.
3. To refine your message:
   - Click Formatting options ![](https://storage.googleapis.com/support-kms-prod/fukkWXYGVSLm6EY3Ddsh6vsxbdmNNKAA0i5X).
   - Activate the Refine hint text:
     - **Mac:** Press **Option + H**.
     - **Windows:** Press **Alt + H**.
   - Highlight the text you want to refine.
4. Click Refine ![](https://storage.googleapis.com/support-kms-prod/hmj7qlpK26lHFvYgUMfB8qf9ge6ost3RQ54Y).

   - Above the Compose area, a refined version of your message displays.
5. To replace your original text with the refined version, click **Replace**.

**Tips:**

- To dismiss the Refine hint text and prevent it from appearing again throughout the current compose session, press **Esc**. The Refine hint text appears again after a page refresh.
- To manage the Refine hint text suggestion, in the Chat settings, under "Message & Media," turn **Smart Compose** on or off.

## Turn Refine on or off

1. On your computer, open [Gmail](https://mail.google.com/).
2. At the top right, click Settings ![](https://lh3.googleusercontent.com/GMF3aAfNCij0aDjnx4S9qlZSB8vSb4UDdxlzPPqHAFukiP3k4Q8RGBq6Nr2jGFMPpD4=h36)![and then](https://lh3.googleusercontent.com/3_l97rr0GvhSP2XV5OoCkV2ZDTIisAOczrSdzNCBxhIKWrjXjHucxNwocghoUa39gw=h36)**See all settings**.
3. Under the "General" tab, in the "Google Workspace smart features" section, click **Manage Workspace smart features settings**.
4. Turn on **Smart features in Google Workspace**.
5. At the bottom, click **Save**.

## Learn about Gemini feature suggestions

- Gemini feature suggestions don’t represent Google’s views, and should not be attributed to Google.
- Don’t rely on Gemini features as medical, legal, financial, or other professional advice.
- Gemini features may suggest inaccurate or inappropriate information. Your feedback makes Gemini more helpful and safe.
- Enterprise end users can submit feedback about their experience using this feature. End users are informed before they submit feedback that the feedback data shouldn’t contain personal, sensitive, or confidential information.

[Learn how to use Google Workspace with Gemini & double-checking responses](https://support.google.com/a/users/answer/16304582).

## Related resources

- [Send a direct message](https://support.google.com/chat/answer/7652736)
- [Reply to a message in Google Chat](https://support.google.com/chat/answer/7654374)
- [Use Smart Compose in Google Chat](https://support.google.com/chat/answer/13568047)

Give feedback about this article

Choose a section to give feedback on

## Need more help?

### Try these next steps:

[Post to the help community  Get answers from community members](https://support.google.com/chat/community?hl=en&help_center_link=CK7o7wcSJkltcHJvdmUgeW91ciBDaGF0IG1lc3NhZ2VzIHdpdGggUmVmaW5l)

true

Search

Clear search

Close search

Main menu

Google apps

18294428233622428209

true

Search Help Center

false

true

true

true

[Google Help](https://support.google.com/)

[Help Center](https://support.google.com/chat/?hl=en) [Community](https://support.google.com/chat/community?hl=en&help_center_link=CK7o7wcSJkltcHJvdmUgeW91ciBDaGF0IG1lc3NhZ2VzIHdpdGggUmVmaW5l) [Google Chat](https://chat.google.com/)

[Privacy Policy](https://www.google.com/intl/en/privacy.html) [Terms of Service](https://www.google.com/accounts/TOS)Submit feedback

true

true

1026838

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

By continuing, you agree Google uses your answers, [account & system info](https://support.google.com/chat/answer/16512046#) to improve services, per our [Privacy](https://myaccount.google.com/privacypolicy?hl=en) & [Terms](https://policies.google.com/terms?hl=en).

false

false

false

---

## Source 8: Learn about spaces - Google Chat Help

- Source URL: https://support.google.com/chat/answer/7659784
- Original file: `docs/learn-about-spaces-google-chat-help-0d7280fe.md`
- Product area: `chat`

# Learn about Spaces — Google Chat Help Summary

**Source:** https://support.google.com/chat/answer/7659784  
**Topic:** What Google Chat spaces are, how they differ from direct messages, and how access/roles work.

---

## Key Excerpts

> To communicate with a group of people or an organization about a topic, project, or shared interest, create a space in Google Chat.

> **Important:** If you use Chat with your personal Google Account, you can only create spaces for collaboration.

> After you create a space for announcements, you can’t change the type of space.

> In addition to the main conversation in the space, you can reply to any message and create a separate thread.

> In work or school accounts, you can make the space private or discoverable to everyone or a target audience in your organization.

---

## What Google Chat Spaces Are

Google Chat **spaces** are shared areas for group communication around a **topic, project, team, organization, or shared interest**.

Examples include:
- Discussing timelines for a marketing campaign
- Coordinating project or team updates
- Sharing announcements
- Connecting around interests like travel or cooking

With spaces, you can:

- Focus conversations around a shared topic or project
- Make organizational announcements
- Create threads for detailed discussions
- Share files
- Assign tasks to members
- Add apps to create workflows inside the space

---

## Types of Spaces

Google Chat supports two main types of spaces:

1. **Collaboration spaces**
2. **Announcement spaces**

### Collaboration Spaces

**Availability:**
- Personal Google Accounts
- Work accounts
- School accounts

**Use for:**
- Project updates
- Team discussions
- Shared interests
- Open collaboration among members

**Capabilities:**
- Everyone in the space can:
  - Post messages
  - React to messages
  - Reply to messages
- Members can message the entire space in the main conversation
- Members can reply directly to messages and create threads

**Important limitation:**

> If you use Chat with your personal Google Account, you can only create spaces for collaboration.

---

### Announcement Spaces

**Availability:**
- Work or school accounts only

**Use for:**
- Sharing important news
- Posting team or organization updates

**Space owner/manager capabilities:**
- Post announcements in the main conversation window
- Respond to member comments on announcements
- Turn off replies

**Space member capabilities:**
- React to announcements
- Reply directly to announcements

**Important restriction:**

> After you create a space for announcements, you can’t change the type of space.

---

## Threads in Spaces

Spaces include a **main conversation**, but members can also reply to individual messages to create separate **threads**.

Threads are useful for:
- Tracking focused discussions
- Keeping the main conversation uncluttered
- Organizing detailed conversations by topic

In a thread, you can:

- Send and reply to messages
- Follow or unfollow the thread
- Change notification settings for new messages in the thread

Related help article: [Use threads in a space](https://support.google.com/chat/answer/12176589)

---

## Space Access Settings

For **work or school accounts**, spaces can be configured as either:

- **Private**
- **Discoverable** to everyone or to a target audience in the organization

---

### Private Spaces

Private spaces are best for:
- Teams
- Projects
- Specific groups
- Discussions limited to certain people

Key behavior:
- You must be invited or added by an existing member to join
- If you are not a member or invited, you cannot browse for the space in Chat

---

### Discoverable Spaces

Discoverable spaces are best for:
- Topics not limited to specific people or teams
- Broad organizational discussions
- Open-interest spaces

Key behavior:
- Users can browse, preview, and join the space
- If someone has a link to the space, they can join through that link

---

## Spaces vs. Direct Messages

Google Chat supports both **spaces** and **direct messages**, but they serve different purposes.

### Core Difference

- **Spaces:** Central places where people can share files, assign tasks, and stay connected.
- **Direct messages:** Chats with a person or group, often for quick discussions.

Example use case for direct messages:
- A quick discussion after a meeting

---

## Comparison: Spaces vs. Direct Messages

| Feature | Spaces | Direct Messages |
|---|---|---|
| **Message history** | Admin determines whether history is on by default and whether users can change it. | Personal accounts can turn history on/off. Workspace account history depends on organization settings. |
| **Name** | In Google Workspace, the **“Who can modify space board and details”** permission controls who can edit the name and description. If created by a personal account, any space member can change the name. | Member names are listed. |
| **Description** | In Google Workspace, the **“Who can modify space board and d

[... summary truncated for context management ...]

---

## Source 9: Manage space settings - Computer - Google Chat Help

- Source URL: https://support.google.com/chat/answer/13340792
- Original file: `docs/manage-space-settings-computer-google-chat-help-16a9a04e.md`
- Product area: `chat`

# Manage Space Settings — Google Chat Help (Computer)

**Source:** https://support.google.com/chat/answer/13340792  
**Topic:** How Google Chat space owners/managers can manage access, roles, permissions, and membership settings.

---

## Key Excerpts

> **As of September 29, 2025, existing space managers became owners, and a new manager role is available.**

As a **space owner or manager**, you can:

- Control who can join a space.
- Control who can manage members and groups.
- Change whether the space is accessible to anyone in your organization or only to people you invite.
- Control permissions for space members.
- Control whether non-members can request to join a space.

**Important:**

- To manage space settings, you need a **Google Workspace account**.
- When you create a space, you can invite people outside of your organization into a space. However, they won’t have access to some features, such as updating space details or adding people.

---

## Role Capabilities

| Capability | Owner | Manager | Member |
|---|---:|---:|---:|
| Delete a space | ✅ |  |  |
| Approve requests to join | ✅ | ✅ *If the user can manage members* |  |
| Change another owner's role | ✅ |  |  |
| Make another space member an owner | ✅ |  |  |
| Make another space member a manager | ✅ | ✅ |  |
| Change the space access setting | ✅ | ✅ |  |
| Configure emailability | ✅ | ✅ |  |
| Delete any message in the space | ✅ | ✅ |  |
| Control whether users can request to join a space | ✅ | ✅ |  |

### Role Summary

- **Owners** have full administrative control, including deleting the space, changing owner roles, and promoting members to owners or managers.
- **Managers** can handle many operational controls, such as access settings, emailability, message deletion, join requests, and promoting members to managers.
- **Members** do not have the listed administrative capabilities.

---

## Update Space Access Settings

Space **owners or managers** can make a Google Chat space either:

- Accessible to anyone in the organization, or
- Limited to invited people only.

### Steps on Computer

1. Open [Google Chat](https://chat.google.com/) or [Gmail](https://mail.google.com/mail/u/0/#chat/home).
   - **In Gmail:** On the left, click **Chat**.
2. On the left, select the space you want to update.
3. At the top, next to the space name, click the **Down arrow** → **Space settings**.
4. Under the **Access** section, next to the current access audience, click the **Down arrow**.
5. In the dropdown menu, choose an audience option:
   - To make a restricted space discoverable, select the audience for your entire domain.
   - To make a discoverable space private, select **Private**.
6. Under **Who can manage members and groups**, select one of:
   - **All members**
   - **Managers and owners**
   - **Owners**

### Tips

- **Discoverable spaces** are searchable and browsable.
- You can share a link to a discoverable space.
- If people outside your organization are already allowed to join the space, you **can’t** make the space discoverable to others.

---

## Update Permissions for a Space

Space permissions define which roles can perform certain actions.

### Steps on Computer

1. Open [Google Chat](https://chat.google.com/) or [Gmail](https://mail.google.com/mail/u/0/#chat/home).
   - **In Gmail:** On the left, click **Chat**.
2. On the left, select the space you want to update.
3. At the top, next to the space name, click the **Down arrow** → **Space settings**.
4. Under **Permissions**, select whether each permission applies to:
   - **All members**
   - **Managers and owners**
   - **Owners only**
5. Click **Save**.

### Permissions You Can Configure

You can decide who can:

- **Modify space details**
- **Turn history on or off**
- **Use @all**
- **Manage apps**
- **Manage webhooks**

---

## Requirements and Limitations

- A **Google Workspace account** is required to manage space settings.
- External users can be invited to spaces, but they may not have access to all features.
  - Examples of unavailable features for external users include:
    - Updating space details
    - Adding people
- Spaces that allow external members cannot be made discoverable to others in the organization.

---

## Additional Help

Google suggests posting to the help community for more support:

- [Google Chat Help Community](https://support.google.com/chat/community?hl=en&help_center_link=CPigrgYSIE1hbmFnZSBzcGFjZSBzZXR0aW5ncyAtIENvbXB1dGVy)

---

## Source 10: Meet app for Google Chat Turndown - Google Chat Help

- Source URL: https://support.google.com/chat/answer/7655908
- Original file: `docs/meet-app-for-google-chat-turndown-google-chat-help-99ece205.md`
- Product area: `chat`

[Skip to main content](https://support.google.com/chat/answer/7655908#search-form)

# Meet app for Google Chat Turndown

The Meet app for Google Chat shut down in summer 2024. To modify or reschedule meetings or to look up your schedule, go to Calendar on [calendar.google.com](https://calendar.google.com/) or use the Google Calendar [Android](https://play.google.com/store/apps/details?id=com.google.android.calendar) or [iOS](https://apps.apple.com/us/app/google-calendar-get-organized/id909319292) app.

Give feedback about this article

Choose a section to give feedback on

## Need more help?

### Try these next steps:

[Post to the help community  Get answers from community members](https://support.google.com/chat/community?hl=en&help_center_link=COSj0wMSIU1lZXQgYXBwIGZvciBHb29nbGUgQ2hhdCBUdXJuZG93bg)

true

13789806477800556845

true

Search Help Center

false

true

true

true

[Google Help](https://support.google.com/)

[Help Center](https://support.google.com/chat/?hl=en) [Community](https://support.google.com/chat/community?hl=en&help_center_link=COSj0wMSIU1lZXQgYXBwIGZvciBHb29nbGUgQ2hhdCBUdXJuZG93bg) [Google Chat](https://chat.google.com/)

[Privacy Policy](https://www.google.com/intl/en/privacy.html) [Terms of Service](https://www.google.com/accounts/TOS)Submit feedback

true

true

1026838

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

By continuing, you agree Google uses your answers, [account & system info](https://support.google.com/chat/answer/7655908#) to improve services, per our [Privacy](https://myaccount.google.com/privacypolicy?hl=en) & [Terms](https://policies.google.com/terms?hl=en).

false

false

false

Search

Clear search

Close search

Main menu

Google apps

---

## Source 11: Summarize chats in Google Chat - Computer - Google Chat Help

- Source URL: https://support.google.com/chat/answer/12918975
- Original file: `docs/summarize-chats-in-google-chat-computer-google-chat-help-68d703e3.md`
- Product area: `chat`

# Summarize chats in Google Chat

## Overview
- Google Workspace users benefit from **automatic conversation summaries** in spaces with many read and unread messages (available by default).
- Some users can also use **Gemini** to manually request summaries for read and unread conversations in the Home view.

---

## Use Gemini summaries for read & unread conversations

### Important Requirements & Limitations
- **Eligible Google Workspace subscription** required.  
  [Learn about Gemini features and plans](https://support.google.com/docs/answer/13952129).
- Available only in **select supported languages**.  
  [See supported languages for summaries in home](https://support.google.com/meet/answer/14925782#zippy=%2Csummaries-in-home).
- Summaries are **not available** for:
  - Messages with apps
  - Conversations where history is turned off
- **Tip:** Enable conversation and space summaries in Home by [turning on smart features in Gmail](https://support.google.com/mail/answer/10079371).

### How to Summarize in Home

#### Summarize a specific read & unread conversation
1. On your computer, open [Google Chat](http://chat.google.com/) or Chat in [Gmail](http://gmail.google.com/).
2. Hover over the conversation in Home.
3. Click **Summarize**.

#### Summarize unread messages inside a conversation
1. Open [Google Chat](https://chat.google.com/) or [Gmail](https://gmail.google.com/).  
   - *In Gmail:* On the left, click the Chat icon.
2. Choose a conversation with unread messages.
3. Click **Summarize unread**.
   - A summary of recent unread messages appears under “Recent discussions”.
4. Click **Close summary** to dismiss.

---

## Give feedback about Gemini conversation summaries
> **Important:** Google Workspace with Gemini may not always support your request. Feedback may be **human-readable** – do **not** submit personal, confidential, or sensitive information.

1. At the bottom of the generated output, click **Good suggestion** 👍 or **Bad suggestion** 👎.
2. In the pop‑up:
   - Choose which data to share (you can uncheck unwanted items).
   - If you selected bad suggestion, click **Next** to select the issue and add comments.
3. Click **Submit**.

For general feedback: Go to **Help** &gt; **Send feedback to Google**.  
[Learn more about sending feedback in Chat](https://support.google.com/chat/answer/13985546).

To report a legal issue, [create a request](https://support.google.com/legal/answer/3110420).

---

## Learn about Gemini feature suggestions
- Gemini suggestions **do not represent Google’s views** and should not be attributed to Google.
- **Do not rely on Gemini** for medical, legal, financial, or other professional advice.
- Gemini features may suggest **inaccurate or inappropriate information**. Your feedback helps make it better.
- Enterprise end users must ensure feedback data contains **no personal, sensitive, or confidential information** before submitting.

---

## Need more help?
- [Post to the help community](https://support.google.com/chat/community?hl=en&help_center_link=CL_BlAYSKVN1bW1hcml6ZSBjaGF0cyBpbiBHb29nbGUgQ2hhdCAtIENvbXB1dGVy) – Get answers from community members.

---

## Source 12: Use an AI Overview in Google Chat - Google Chat Help

- Source URL: https://support.google.com/chat/answer/16944767
- Original file: `docs/use-an-ai-overview-in-google-chat-google-chat-help-fed08585.md`
- Product area: `chat`

# Use an AI Overview in Google Chat — Summary

**Source:** Google Chat Help — <https://support.google.com/chat/answer/16944767>

## Feature Availability

- AI Overview in Google Chat is **rolling out gradually** as part of the **Gemini Alpha**.
- Only **some Gemini Alpha users** have access.
- Users may not have access to some or all related features.
- Access is controlled by the organization’s administrator.
  - If the feature is missing, the admin may not have enabled **Alpha features** for the organization.

> **Feature availability**
>
> - This feature is rolling out gradually as part of the Gemini Alpha. Only some Gemini Alpha users will have access to this feature.
> - You may not have access to some or all of these features.
> - Your administrator controls access to the Gemini Alpha.

## What AI Overview in Google Chat Does

AI Overview helps users quickly find information from Google Chat conversations by asking questions or entering keywords in the Chat search bar.

It can help:

- Locate specific information or messages across the user’s full Workspace profile.
- Understand past discussions or outcomes mentioned in chats.
- Find attachments without extensive manual searching.

## Search Google Chat Conversations with AI Overview

### Important Limitations

> **Important:**
>
> - If you use search operators, like `is:unread` or `from:`, you won’t get an AI Overview.
> - Search within any conversation or space doesn’t provide an AI Overview.

Key points:

- AI Overview appears only when searching from the main Chat search bar.
- It does **not** appear when:
  - Using search operators such as `is:unread` or `from:`
  - Searching within a specific conversation or space

### How to Get an AI Overview

1. On a computer, open:
   - [Google Chat](https://chat.google.com/), or
   - [Gmail](https://mail.google.com/)
     - In Gmail, click **Chat** on the left.
2. In the search bar, enter keywords or a natural-language query.

Examples:

> - "What was the deadline for project X?"
> - "Find messages from Alice about the Q3 review."
> - "Show me attachments from the design sprint space."

3. Click **Search** or press **Enter**.
4. Review the **AI Overview** at the top of the search results.

**Tip:** Provide as much detail as possible in the search description to get the best AI Overview.

## Expand or Collapse an AI Overview

When an AI Overview summary appears:

- Click **Show more** to expand and view the full summary.
- Click **Collapse** to hide the expanded overview.

## Give Feedback About an AI Overview

Google notes that Workspace with Gemini is continually learning and may not always support a request accurately.

If an AI Overview is inaccurate or feels unsafe, users can submit feedback to help improve AI-assisted Workspace features and Google’s broader AI efforts.

### Privacy Warning for Feedback

> Because feedback may be human readable, do not submit data that contains personal, confidential, or sensitive information.

### Feedback Steps

1. At the top right of the generated output, select:
   - **Good summary**, or
   - **Bad summary**
2. In the pop-up window, choose what data to share with the feedback.
   - Users can uncheck data they do not want to share.
   - If selecting **Bad summary**, click **Next** to choose the issue and add more feedback.
3. Select **Submit**.

### General Feedback

To provide general feedback about the feature:

- Select **Help**
- Then select **Send feedback to Google**

Google also links to instructions for sending feedback in Google Chat.

### Legal Issues

To report a legal issue, users should create a request through Google’s legal support process.

## Gemini Feature Suggestions: Important Disclaimers

Google provides several cautions about Gemini-powered suggestions:

> - Gemini feature suggestions don’t represent Google’s views, and should not be attributed to Google.
> - Don’t rely on Gemini features as medical, legal, financial or other professional advice.
> - Gemini features may suggest inaccurate or inappropriate information. Your feedback makes Gemini more helpful and safe.
> - Enterprise end users can submit feedback about their experience using this feature. End users are informed before they submit feedback that the feedback data shouldn’t contain personal, sensitive, or confidential information.

Key takeaway:

- Gemini outputs may be inaccurate or inappropriate.
- Users should not treat them as professional advice.
- Feedback may be reviewed, so users should avoid including sensitive information.

## Related Resources

- [Use Gemini conversation summaries for unread messages](https://support.google.com/chat/answer/16358670)
- [Summarize chats in Google Chat](https://support.google.com/chat/answer/12918975)

## Article Feedback Options

The page includes an article feedback form asking:

> **What is the issue with this selection?**

Available options include:

- **Inaccurate** — doesn’t match what the user sees in the product
- **Hard to understand

[... summary truncated for context management ...]

---

## Source 13: Use apps in Google Chat - Computer - Google Chat Help

- Source URL: https://support.google.com/chat/answer/7655820
- Original file: `docs/use-apps-in-google-chat-computer-google-chat-help-81d44226.md`
- Product area: `chat`

# Use Apps in Google Chat — Summary

**Source:** Google Chat Help — “Use apps in Google Chat”  
**Platform covered:** Computer  
**URL:** https://support.google.com/chat/answer/7655820

---

## Overview

Apps in Google Chat are special accounts you can message to connect Chat with other services. They can help you:

- Look up information
- Schedule meetings
- Complete tasks

Google Chat apps may be built and maintained by Google or by third-party software vendors.

---

## Key Excerpts

> Apps are special accounts you can message that connect you to services in Chat

Apps can help you:

- Look up information.
- Schedule a meeting.
- Do tasks.

When you interact with an app in Chat, the app can see your:

- Email address
- Avatar
- Basic information, such as your name

> The app can see other’s basic information in a chat, but it can't see their email address or avatar unless they interact directly with the app.

**Important:**

- On your work or school accounts, your admin can install apps for you. Afterwards, the apps can send you direct messages. You can't uninstall the apps but you can turn off notifications for conversations with the app.
- If you're an external member of a Google Chat space created by a work or school account, you can't add, remove, or interact with any apps.

App commands use:

```text
/
```

> The app commands you use in a conversation are private. The app's responses appear in the conversation.

---

## How Apps Work in Google Chat

When you interact with a Chat app, it may access certain user details.

### Information an App Can See About You

An app can see your:

- Email address
- Avatar
- Basic profile information, such as your name

### Information an App Can See About Others

In a chat, the app can see other users’ basic information, but it **cannot** see their:

- Email address
- Avatar

unless those users interact directly with the app.

### Google vs. Third-Party Apps

Google creates and maintains some apps, including:

- Google Drive app
- Poll app

Other apps are created and maintained by third-party vendors.

If you use a third-party app, Google recommends reviewing the vendor’s:

- Terms of Service
- Privacy policy

to understand how your data is used.

---

## Work or School Account Limitations

If you use a work or school Google account:

- Your organization controls which apps are available.
- Your administrator can install apps for you.
- Admin-installed apps can send you direct messages.
- You cannot uninstall admin-installed apps.
- You can turn off notifications for conversations with those apps.

If you are an **external member** of a Google Chat space created by a work or school account:

- You cannot add apps.
- You cannot remove apps.
- You cannot interact with apps.

---

## Find & Install a Chat App

**Important:** If you have a work or school account, your organization controls which apps are available to you.

### Steps

1. On your computer, open:
   - [Google Chat](https://chat.google.com/), or
   - [Gmail](https://mail.google.com/)
2. Choose one of the following:
   - Click **New chat** → **Find apps**
   - In the Chat sidebar, click **Get Add-ons**
3. Search or browse for an app.
4. Select an app.
5. Choose an installation option:
   - Click **Install** to create a dedicated 1:1 direct message with the app and use its features individually.
   - Click **Add to Space** to add the app to a space so all space members can use it.

### Tips

- You can also find and install apps in the Google Workspace Marketplace.
- If an app needs to perform tasks on your behalf, it will ask for permission to access your Google Account.
  - To grant access, click **Allow** in the permission prompt.
- You can remove third-party app access from your Google Account settings.
- To uninstall an app from a direct message:
  1. Open the app conversation.
  2. Click the app name at the top.
  3. Click **Uninstall**.
- For work or school accounts, you cannot uninstall apps installed by your administrator.

---

## Add Apps to a Conversation or Space

Installed apps can be used in conversations and spaces.

When you add an app to a space, you grant it permission to:

- Fetch basic information about the space
- Create messages in the space

### Steps

1. Open [Google Chat](https://chat.google.com/) or [Gmail](https://mail.google.com/) on your computer.
2. Select a conversation or space.
3. At the top, click the space name or conversation participants.
4. Click **Apps & integration** → **Add apps**.
5. Enter the app name.
6. Select one or more apps.
7. Click **Add**.

### Important Access Notes

- Adding an app to a space gives it access to messages that trigger the app.
- It does **not** automatically allow the app to read every message in the space.
- Apps that need full message context can only access it with explicit permission.

### Additional Notes

When you add an app to a space:

- The app is installed in your **Apps** section.
- The app becomes available in every other space 

[... summary truncated for context management ...]

---

## Source 14: Use the Bulk Member Manager app in Google Chat - Computer - Google Chat Help

- Source URL: https://support.google.com/chat/answer/14016224
- Original file: `docs/use-the-bulk-member-manager-app-in-google-chat-computer-google-chat-help-dfd63d09.md`
- Product area: `chat`

[Skip to main content](https://support.google.com/chat/answer/14016224#search-form)

# Use the Bulk Member Manager app in Google Chat

To add or remove multiple members in bulk to a space, use the Bulk Member Manager app for Google Chat. With the app, you can:

- Copy and paste email addresses.
- Add a comma-separated values (.csv) file (computer only).

## Before you begin

- To use the Bulk Member Manager app, you must be a space owner, manager, or member who has permission to manage members.
- You need permission to install apps from your Google Workspace administrator.
- Add the app to Chat. [Learn how to find apps and add them to Chat](https://support.google.com/chat/answer/7655820).

ComputerAndroidiPhone & iPad

More

More

## Set up the Bulk Member Manager app in Chat

1. On your computer, open [Chat](http://chat.google.com/).
2. Search for the space.
3. Next to the reply area, click Action ![](https://storage.googleapis.com/support-kms-prod/wcXvPr1ZLKpNbQTlfDMXivfrzFGLB2FyjUGa).
4. In the search bar, enter “Bulk Member Manager.”
5. Click the app ![and then](https://lh3.googleusercontent.com/3_l97rr0GvhSP2XV5OoCkV2ZDTIisAOczrSdzNCBxhIKWrjXjHucxNwocghoUa39gw=h36)**Add to space**.
6. To update memberships, you can use either:

Email addresses

1. In the reply area, enter a slash command.
   - To add members, enter `/addDialog`.
   - To remove members, enter `/removeDialog`.
2. On your keyboard, press **Enter**.
3. In the window, copy and paste the list of email addresses.
   - Use commas to separate email addresses in the list.
4. Click **Send request**.

A .csv file

1. In the reply area, enter a slash command.
   - To add members, enter `/addCsv`.
   - To remove members, enter `/removeCSV`.
2. To add the .csv file, click Upload file ![](https://storage.googleapis.com/support-kms-prod/OycVXHRAE83YB9OV50AEgLrxBjMsfk5OrDxA).
3. On your keyboard, press **Enter**.

[Add app to space](https://workspace.google.com/marketplace/app/bulk_member_manager/927553207499)

**Tip:** You can also add the app from the:

- “Apps & integrations” page in Chat. [Learn how to find apps and add them in Chat](https://support.google.com/chat/answer/7655820).
- Side panel in Gmail and Chat. [Learn how to use Google products side by side](https://support.google.com/drive/answer/106237).

## Related resources

- [Use apps in Google Chat](https://support.google.com/chat/answer/7655820)
- [Chat apps available from Google](https://support.google.com/chat/answer/9649420)

Give feedback about this article

Choose a section to give feedback on

## Need more help?

### Try these next steps:

[Post to the help community  Get answers from community members](https://support.google.com/chat/community?hl=en&help_center_link=COC91wYSOVVzZSB0aGUgQnVsayBNZW1iZXIgTWFuYWdlciBhcHAgaW4gR29vZ2xlIENoYXQgLSBDb21wdXRlcg)

true

Search

Clear search

Close search

Main menu

Google apps

7464981024472161818

true

Search Help Center

false

true

true

true

[Google Help](https://support.google.com/)

[Help Center](https://support.google.com/chat/?hl=en) [Community](https://support.google.com/chat/community?hl=en&help_center_link=COC91wYSOVVzZSB0aGUgQnVsayBNZW1iZXIgTWFuYWdlciBhcHAgaW4gR29vZ2xlIENoYXQgLSBDb21wdXRlcg) [Google Chat](https://chat.google.com/)

[Privacy Policy](https://www.google.com/intl/en/privacy.html) [Terms of Service](https://www.google.com/accounts/TOS)Submit feedback

true

true

1026838

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

By continuing, you agree Google uses your answers, [account & system info](https://support.google.com/chat/answer/14016224#) to improve services, per our [Privacy](https://myaccount.google.com/privacypolicy?hl=en) & [Terms](https://policies.google.com/terms?hl=en).

false

false

false

---

## Source 15: Use the Jenkins app in Google Chat - Computer - Google Chat Help

- Source URL: https://support.google.com/chat/answer/9632691
- Original file: `docs/use-the-jenkins-app-in-google-chat-computer-google-chat-help-d4cf45fe.md`
- Product area: `chat`

# Use the Jenkins App in Google Chat — Summary

**Source:** Google Chat Help  
**Purpose:** Use the Jenkins app in Google Chat to receive Jenkins build notifications and trigger Jenkins builds from Chat.

---

## Overview

The Jenkins app for Google Chat lets teams receive notifications about Jenkins builds directly in Chat spaces or direct messages. After installing a Jenkins plugin and configuring tokens generated by the Chat app, Jenkins can send build and pipeline notifications to Chat.

---

## Before You Begin

To use the Jenkins app in Google Chat:

- You need permission from your **Google Workspace administrator** to install apps.
- Add the Jenkins app to Google Chat.
  - Google provides separate instructions for finding and adding apps to Chat.

---

## Step 1: Install the Chat Plugin on the Jenkins Server

**Requirement:** You must be signed in as a **Jenkins administrator**.

### Steps

1. Download the Chat Notifier Plugin file:  
   `google-hangouts-chat-notifier.hpi`
2. In Jenkins, go to:
   - **Manage Jenkins**
   - **Manage Plugins**
3. Open the **Advanced** tab.
4. Under **Upload Plugin**, select the plugin file.
5. Click **Upload**.

After this plugin is installed, people in your organization can install and set up the Jenkins app.

---

## Step 2: Set Up the Jenkins App in Google Chat

Jenkins needs a token generated by the Chat app to send build notifications.

### Key Facts

- Each Google Chat space where the Jenkins app is added gets its own token.
- The app sends notifications to every space where it is a member.

### Steps

1. Open [Google Chat](https://chat.google.com/).
2. Open a direct message with the Jenkins app or go to a space where it is installed.
3. Copy the token shown by the app.
4. Optional: Display the token again:
   - In a direct message, enter:

     **`token`**

   - In a space, enter:

     **`/jenkins_token`**

5. Optional: Regenerate the token by clicking **Regenerate Token**.

---

## Step 3: Set Up Jenkins Build Notifications

To configure notifications for a specific Jenkins build:

1. Open **Jenkins**.
2. Go to the build you want to add Chat notifications for.
3. Under **Build**, next to **Add build step**, click the down arrow.
4. Choose the notifications you want to receive.
5. Under **Post-build Actions**, next to **Add post-build actions**, click the down arrow.
6. Select **Notify Hangouts Chat**.
7. Choose an option and paste the token copied from Chat:
   - **Chat:** Choose a global configuration that was previously set up.
   - **Chat Token:** Override the global configuration for a specific Chat space.
8. Check the boxes for the items you want to receive notifications about in Chat.
9. Click **Save**.

### Build Notification Actions

From a build event notification in Chat, you can click:

- **Open Build:** Opens Jenkins to modify the build configuration.
- **View Details:** Shows information about the notification.

---

## Step 4: Get Notifications for a Jenkins Pipeline

To send notifications from a Jenkins pipeline:

1. Open **Jenkins**.
2. Open the pipeline you want to add Chat notifications for.
3. Add the following to your pipeline script:

```text
hangoutsNotify message: "This message is from a pipeline!",token: {your_jenkins_token},threadByJob: false
```

### Important Tip

Replace:

```text
{your_jenkins_token}
```

with the token requested from the Chat app.

You can set:

```text
threadByJob
```

to either:

```text
true
```

or:

```text
false
```

4. Click **Save**.

---

## Using the Jenkins App in Google Chat Spaces

When using the Jenkins app in spaces:

- You must **@mention the app** in each message sent to the app.
- You must also @mention the app in replies to messages from the app.
- The @mention confirms the message is intended for the Jenkins app and not for other people in the space.

You can also type:

```text
/jenkins_
```

and select the desired command from the dropdown menu.

---

## Triggering Jenkins Builds from Google Chat

You can trigger Jenkins jobs directly from Chat.

### Steps

1. In a space where Jenkins is installed, or in a direct message with Jenkins, enter:

```text
/jenkins_triggerJob
```

2. In the dialog that opens, fill in the required fields:
   - **Jenkins URL**
   - **Job Name**
   - **UserName**
   - **ApiToken**

3. Click **Submit**.

### Optional Settings

You can also choose whether to:

- Store your token  
  - Google notes that it **will never be shown**.
- Pass optional parameters to your build request.

---

## Key Commands and Snippets

### Show token in direct message

```text
token
```

### Show token in a space

```text
/jenkins_token
```

### Trigger a Jenkins job

```text
/jenkins_triggerJob
```

### Pipeline notification snippet

```text
hangoutsNotify message: "This message is from a pipeline!",token: {your_jenkins_token},threadByJob: false
```

---

## Trademark Notice

> _Google, Google Workspace, and related marks and logos are trademarks of Google LLC. All other company and product

[... summary truncated for context management ...]

---

## Source 16: Use the Jira app in Google Chat - Computer - Google Chat Help

- Source URL: https://support.google.com/chat/answer/9575067
- Original file: `docs/use-the-jira-app-in-google-chat-computer-google-chat-help-e796071a.md`
- Product area: `chat`

# Use the Jira App in Google Chat — Summary

**Source:** Google Chat Help — “Use the Jira app in Google Chat”  
**Purpose:** Use the Jira app in Google Chat to receive messages about updates to Jira Software projects. The app sends Jira updates into Google Chat direct messages or spaces.

---

## Before You Begin

To use the Jira app in Google Chat:

- You need permission from your **Google Workspace administrator** to install apps.
- Add the Jira app to Google Chat.
  - Google’s related help: *Learn how to find apps and add them to Chat*
- Install the **Chat Jira plugin** from the **Atlassian Marketplace**.
  - Your Jira admin may need to approve the plugin.

---

## Set Up the Jira App in Google Chat

1. Open [Google Chat](https://chat.google.com/).
2. Open either:
   - A **direct message** with the Jira app, or
   - A **space** where the Jira app has been added.
3. After installation, you’ll receive:
   - A welcome message
   - A card prompting you to connect to Jira
4. Click **Connect**.

### Direct Message Setup

If you connect Jira in a direct message, you can receive personal notifications for issues that you:

- Report
- Watch
- Are assigned to
- Are mentioned in

These notifications can apply across **one or more Jira sites**.

### After Connecting

- If Jira was already set up, the app uses the site from the previous connection.
- After connecting Jira:
  - **In a direct message:** Select projects for personal notifications.
  - **In a space:** Select projects to quickly subscribe to issue updates.
- After successful connection, you receive:
  - A confirmation message
  - A list of connected Jira sites or projects

To edit filters or settings, click **Edit notification settings**.

### Configure Project Notifications

1. Enter project names to receive notifications.
2. Optional: Use multi-select search to enter projects.
3. Click **Save**.
4. Optional: Click **Edit notification settings** to update notifications later.

> **Tip:** You need to set up notifications in each space where you add the app. The app sends notifications to all spaces where it's a member.

---

## Update Jira App Notification Settings

You can manage personal-notification settings from the Jira app’s direct message in Chat.

---

## Manage Personal Filters

Use personal filters to choose which issue updates you receive.

### Steps

1. On your computer, open a direct message with the Jira app.
2. Open the settings dialog:
   - Select **Edit notification settings**, if prompted, or
   - Type:

```text
/jira_settings
```

Then press **Enter**.

3. Select or deselect updates for issues:
   - You’re watching
   - You’ve reported
   - You’re the assignee on
   - You’re mentioned in
4. Optional: Manage connected Jira sites from this page.
5. Click **Save**.

---

## Filter Notifications by Project

### Single Connected Jira Site

If you have only one Jira site connected, you can filter personal notifications to specific projects.

#### Steps

1. Open a direct message with the Jira app.
2. Open settings:
   - Click **Edit notification settings**, or
   - Type:

```text
/jira_settings
```

Then press **Enter**.

3. Under **“Send updates from only these projects,”** select the projects to filter for.
4. Click **Save**.

> **Tip:** The default interface provides **“All Projects.”**

---

### Multiple Connected Jira Sites

If you have multiple Jira sites connected, you can filter personal notifications by project for each site.

#### Steps

1. Open a direct message with the Jira app.
2. Open settings:
   - Select **Edit notification settings**, or
   - Type:

```text
/jira_settings
```

Then press **Enter**.

3. Under **“Send updates from only these projects,”** select specific projects for a site.
4. Optional: Repeat for other connected Jira sites.
5. Click **Save**.

> **Tip:** Each Jira site provides an option like **“sitename: All Projects.”**

---

## Jira App Commands in Google Chat

> **Important:** To get available commands, enter:

```text
/
```

You can use these slash commands in a direct message or space with the Jira app in Chat:

| Command | Purpose |
|---|---|
| `/jira_connect` | Connects the Jira app to your Jira site. |
| `/jira_create` | Creates a new issue. |
| `/jira_view [issue_id]` | Provides information for the specified Jira issue. |
| `/jira_disconnect` | Disconnects the Jira app or the current space from your Jira site. |
| `/jira_help` | Displays the help message. |
| `/jira_feedback` | Sends feedback about the Jira app. |
| `/jira_subscriptions` | Shows settings to manage subscriptions for Jira projects with specific filters. |
| `/jira_setting` | Shows settings for personal notifications and space subscriptions. |

You can also use the **Create issue** and **Settings** buttons for quick access to related actions.

---

## Change App Settings

1. Open [Google Chat](https://chat.google.com/).
2. Open a direct message with the Jira app or go to a space with the app.
3. Type:

```text
/jira_settings
```

4. Pres

[... summary truncated for context management ...]

---

## Source 17: Use the PagerDuty app in Google Chat - Computer - Google Chat Help

- Source URL: https://support.google.com/chat/answer/12156602
- Original file: `docs/use-the-pagerduty-app-in-google-chat-computer-google-chat-help-1b4d77dc.md`
- Product area: `chat`

[Skip to main content](https://support.google.com/chat/answer/12156602#search-form)

# Use the PagerDuty app in Google Chat

Use the PagerDuty app in Google Chat to get notifications about PagerDuty incidents and acknowledge, resolve, and record new incidents.

## Before you begin

- You need permission from your Google Workspace administrator to install apps.
- You need to add the app to Chat. [Learn how to find apps and add them to Chat](https://support.google.com/hangoutschat/answer/7655820#addbots).
- You need a PagerDuty account with Admin or Account Owner permissions in order to first set up the integration.

ComputerAndroidiPhone & iPad

More

More

## Set up the PagerDuty app in Chat

1. Open [Chat](https://chat.google.com/).
2. Select an option:

- Open a direct message with the app.
- Go to a space with the app.

03. To sign in to your PagerDuty account and subdomain, click **Authorize**. To set up the app, you must sign in to a PagerDuty account with Admin or Account Owner permissions in the subdomain.
04. Complete the sign-in on the PagerDuty website.
05. Allow the PagerDuty Chat app to access some PagerDuty permissions.
06. If prompted, select the correct PagerDuty account to use.
07. Once the connection is successful, configure your notification settings by entering “/pd\_settings”.
08. Click **Create New Settings**.
09. Select the PagerDuty source you want to receive notifications from.
10. Check the boxes for the items you want to get notifications about in Chat.
11. Click **Save**.
12. (Optional) To add another project, enter “/pd\_settings” again. Then, at the bottom of the dialogue, click the **Authorize** button.

You must set up notifications in each space where you add the app. The app sends notifications to all spaces where it's a member.

## Change app settings

Only PagerDuty Admins or Account Owners can change the settings.

1. Open [Chat](https://chat.google.com/).
2. Select an option:
   - Open a direct message with the app.
   - Go to a Space with the app.
3. Enter settings.
   - In the Space, enter “/pd\_settings”. The current settings for the app appear.
   - If you’re in a direct message with the app, you can view all your active PagerDuty connections.
   - If you’re in a Space, you can view all the PagerDuty connections that are active in that Space.
4. To edit or delete any visible connection, click **Edit** or **Delete**.
5. In order to make new PagerDuty connections, click **Authorize**.

Removing the app from a space deletes the app settings.

## Use the app in spaces

To use the app in spaces, you can use various commands by entering “/”. To see the full list of commands, enter “/pd\_help”.

Give feedback about this article

Choose a section to give feedback on

## Need more help?

### Try these next steps:

[Post to the help community  Get answers from community members](https://support.google.com/chat/community?hl=en&help_center_link=CLr95QUSL1VzZSB0aGUgUGFnZXJEdXR5IGFwcCBpbiBHb29nbGUgQ2hhdCAtIENvbXB1dGVy)

true

3494862939682980562

true

Search Help Center

false

true

true

true

[Google Help](https://support.google.com/)

[Help Center](https://support.google.com/chat/?hl=en) [Community](https://support.google.com/chat/community?hl=en&help_center_link=CLr95QUSL1VzZSB0aGUgUGFnZXJEdXR5IGFwcCBpbiBHb29nbGUgQ2hhdCAtIENvbXB1dGVy) [Google Chat](https://chat.google.com/)

[Privacy Policy](https://www.google.com/intl/en/privacy.html) [Terms of Service](https://www.google.com/accounts/TOS)Submit feedback

true

true

1026838

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

By continuing, you agree Google uses your answers, [account & system info](https://support.google.com/chat/answer/12156602#) to improve services, per our [Privacy](https://myaccount.google.com/privacypolicy?hl=en) & [Terms](https://policies.google.com/terms?hl=en).

false

false

false

Search

Clear search

Close search

Main menu

Google apps

---

## Source 18: Use the Zapier app in Google Chat - Computer - Google Chat Help

- Source URL: https://support.google.com/chat/answer/9470843
- Original file: `docs/use-the-zapier-app-in-google-chat-computer-google-chat-help-00a4dd6c.md`
- Product area: `chat`

[Skip to main content](https://support.google.com/chat/answer/9470843#search-form)

# Use the Zapier app in Google Chat

Use the Zapier app in Chat to get notifications about Zap actions. The app sends messages from the Zap to Chat.

## Before you begin

- You need permission to install apps from your Google Workspace administrator.
- Add the app to Chat. [Learn how to find apps and add them to Chat](https://support.google.com/chat/answer/7655820).

ComputerAndroidiPhone & iPad

More

More

## Set up the Zapier app in Chat

Set up Chat to get messages from a Zap.

1. Open [Google Chat](https://chat.google.com/).
2. Open a direct message with the app or go to a space with the app.
3. Enter the command **allowzaps**.

   - In spaces, enter **@Zapier allowzaps** or **/Zapier allowzaps**.
   - The app shows a card to allow Zaps.
4. Click **Click To Allow Zaps**.
5. Sign in to you work or school account.
   - A message confirms that Zaps can send messages to this chat for you.

## Stop Zaps in Chat

1. Open [Google Chat](https://chat.google.com/).
2. Open a direct message with the app or go to a space with the app.
3. Enter the command **stopzaps**.

   - In spaces, enter **@Zapier stopzaps** or **/Zapier stopzaps**.
   - The app shows a card to stop Zaps.
4. Click **Click To Stop Zaps**.

   - A message confirms that Zaps can no longer send messages to this chat for you.

## Connect a Zap to Google Chat

To integrate with Chat, you need to set up a Zap action. Here's a summary of the steps in Zapier. For detailed instructions, visit the [Zapier website](https://zapier.com/app-directory/google-hangouts-chat/integrations).

1. Open [Zapier](https://zapier.com/app/zaps).
2. Create a Zap or open an existing Zap.
3. Add an action step to the Zap:
1. Choose the Google Chat app.
2. Save the Create Message action.
3. Connect your Google Account. This is the work or school account you use for Chat.
4. Set up a template for the messages. You can choose Chat spaces where you added the app and allow zaps.

The Zap can now contact the Zapier app and send messages to Chat.

Give feedback about this article

Choose a section to give feedback on

## Need more help?

### Try these next steps:

[Post to the help community  Get answers from community members](https://support.google.com/chat/community?hl=en&help_center_link=CPuGwgQSLFVzZSB0aGUgWmFwaWVyIGFwcCBpbiBHb29nbGUgQ2hhdCAtIENvbXB1dGVy)

true

Search

Clear search

Close search

Main menu

Google apps

1723110569979239796

true

Search Help Center

false

true

true

true

[Google Help](https://support.google.com/)

[Help Center](https://support.google.com/chat/?hl=en) [Community](https://support.google.com/chat/community?hl=en&help_center_link=CPuGwgQSLFVzZSB0aGUgWmFwaWVyIGFwcCBpbiBHb29nbGUgQ2hhdCAtIENvbXB1dGVy) [Google Chat](https://chat.google.com/)

[Privacy Policy](https://www.google.com/intl/en/privacy.html) [Terms of Service](https://www.google.com/accounts/TOS)Submit feedback

true

true

1026838

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

By continuing, you agree Google uses your answers, [account & system info](https://support.google.com/chat/answer/9470843#) to improve services, per our [Privacy](https://myaccount.google.com/privacypolicy?hl=en) & [Terms](https://policies.google.com/terms?hl=en).

false

false

false

---
