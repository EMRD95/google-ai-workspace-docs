---
title: "Take actions in third-party services with flows - Workspace Studio Help"
source_url: "https://support.google.com/workspace-studio/answer/16658279?hl=en"
product_area: "workspace-studio"
retrieved_at: "2026-06-15T11:30:53Z"
extraction_method: "web_extract"
---

# Summary: Take actions in third-party services with flows

**Status:** Limited preview. Integrations allow flows in Google Workspace Studio to perform tasks in third-party services like Asana, Mailchimp, and Salesforce. Many also work with Gemini Apps.

## Important Warning
> **Important:** When you add variables to integration steps, they might contain your Google Account data, such as the contents of a message in Gmail or Chat, or event information from Calendar. The flow can then share your Google Account data with the third-party service. Make sure you trust the third-party service.

## Using Integration Steps in Flows
Integration steps are available when creating a flow with AI, using a template, or in the step selector under the third-party service name.

**Steps:**
1. Go to [studio.workspace.google.com](https://studio.workspace.google.com) and [create a flow](https://support.google.com/a/users/answer/16430397).
2. In the left panel, click the integration step.
3. If not yet connected, click **Connect** and follow prompts. You may need to install a helper app from the third‑party service. (For issues, see troubleshooting below.)
4. Set up the step.
5. (Optional) Click **Test run** to run the flow once with real actions. Select starting conditions, then **Start**. [Learn more about test runs](https://support.google.com/workspace-studio/answer/16663517).
6. Click **Turn on**.

## Connecting from Google Workspace Marketplace
Pre‑connect an integration so you won’t need to connect again when adding it to a flow.

1. Visit the [Marketplace integrations page](https://workspace.google.com/marketplace?host=workflow) (pre‑filtered for integrations).
2. Click the desired integration.
3. Click **Connect** and follow the on‑screen instructions. You may need to install a helper app.

**Disconnecting:** Return to the Marketplace listing, click **Disconnect**. If your admin set up the integration, you might not be able to disconnect.

## Managing Account Access
If you’re worried about data access, delete the integration’s connections to your account. Flows using the integration may stop working.

1. Go to [myaccount.google.com/connections](https://myaccount.google.com/connections).
2. Find and click the integration.
3. Click **Delete all connections you have with** *integration name* and confirm.

The Marketplace will still show “connected”. To reconnect, add the step again and go through the connection process.

## Troubleshooting Integration Steps
- **Paid third‑party services:** You need a subscription for that service.
- **Admin restrictions:** Your Workspace admin may limit who can connect or which integrations are allowed. Ask your admin to allow or connect it for you.
- **Helper apps:** Some integrations (e.g., Salesforce, monday) require a helper app installed by you or your admin. Check the Marketplace listing’s **Overview** section.
- **Missing permissions:** Integrations like HubSpot let you select permissions individually. If a required permission is missing (e.g., get contact data, create a contact), the step fails. Reconnect and grant all permissions. If error messages persist, your admin may be blocking some permissions—contact them for help.

*Google, Google Workspace, and related marks are trademarks of Google LLC. Other product names are trademarks of their respective companies.*
