# Chat — Google AI Documentation (4 docs)

Combined for easy NotebookLM import. Each section is a separate help article.

---

## 1. Build a Google Chat app with a Gemini Enterprise AI agent Stay organized with collections Save and categorize content based on your preferences.

**Source:** https://developers.google.com/workspace/add-ons/chat/quickstart-ge-agent?hl=en

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

## 2. Collaborate with Gemini in Google Chat - Computer - Google Chat Help

**Source:** https://support.google.com/chat/answer/15345722?hl=en

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

## 3. Get started with Ask Gemini in Google Chat - Computer - Google Chat Help

**Source:** https://support.google.com/chat/answer/17036303?hl=en

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

## 4. Summarize chats in Google Chat - Computer - Google Chat Help

**Source:** https://support.google.com/chat/answer/12918975

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

