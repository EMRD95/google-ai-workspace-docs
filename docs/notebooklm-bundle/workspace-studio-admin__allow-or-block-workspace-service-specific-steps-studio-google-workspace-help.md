# Allow or block Workspace service–specific steps  |  Studio  |  Google Workspace Help

**Product Area:** workspace-studio-admin
**Source:** https://knowledge.workspace.google.com/admin/studio/allow-or-block-ws-service-specific-steps

# Allow or block Workspace service–specific steps — Google Workspace Studio

**Source:** https://knowledge.workspace.google.com/admin/studio/allow-or-block-ws-service-specific-steps  
**Last updated:** 2026-06-11 UTC

## Purpose

Google Workspace administrators can control which **Workspace Studio steps and starters** users in their organization can use when creating flows. Controls can be applied:

- By **Workspace service/app** such as Gmail, Calendar, Chat, Drive
- More granularly, for specific **features or steps** within supported apps

Users must already have access to the relevant Workspace service to use its steps or starters.

> “Users must have access to a Workspace service in order to use starters and steps for that service.”

Example:

> “If Google Chat is turned off for your organization, people can't use Chat steps in their flows.”

## Supported Editions and Add-ons

### Supported Google Workspace editions

This feature is supported for:

- **Business Starter**
- **Business Standard**
- **Business Plus**
- **Enterprise Standard**
- **Enterprise Plus**
- **Education Fundamentals**
- **Education Standard**
- **Teaching and Learning add-on**
- **Education Plus**

Related link: [Compare your edition](https://knowledge.workspace.google.com/admin/getting-started/editions/compare-google-workspace-editions)

### Supported add-ons

- **AI Ultra Access**
- **Google AI Pro for Education**

Related link: [Compare add-ons](https://knowledge.workspace.google.com/admin/getting-started/editions/compare-google-ai-expansion-add-ons)

## Privacy Note

> **Note**: AI features in Workspace Studio follow the privacy principles in the [Generative AI in Google Workspace Privacy Hub](https://knowledge.workspace.google.com/admin/gemini/generative-ai-in-google-workspace-privacy-hub).

## How to Allow or Block Specific App Steps or Features

Admins can choose whether users may use Workspace Studio steps or features for specific apps, such as **Calendar** or **Gmail**.

### Admin console steps

1. In the Google Admin console, go to:  
   **Menu → Apps → Google Workspace → Workspace Studio**
2. Click **Steps & features**.
3. For the app you want to update, click **Edit**.
4. To turn the app on or off, check or uncheck the box next to the app’s name.
   - For certain apps, turning them on enables additional, more specific feature or step selections.
   - Select those by checking the box next to each option.
5. Click **Save**.

## If Users Still Can’t Access Custom Steps

If custom steps for Workspace services such as **Drive** or **Gmail** are allowed, but users still cannot access them, admins should check **Custom App Access** settings.

## Context-Aware Access Considerations

If your organization assigns **Context-Aware Access levels** to apps, you may need to exempt allowlisted apps.

### Where to check assigned access levels

Go to:

[Assign Context-Aware Access levels to apps](https://knowledge.workspace.google.com/admin/security/assign-context-aware-access-levels-to-apps)

### Apps that may need access levels unassigned

To unassign access levels, uncheck the box next to these apps:

- Drive for Workspace Studio
- Gemini for Workspace Studio
- Gmail for Workspace Studio
- Google Calendar for Workspace Studio
- Google Chat for Workspace Studio
- Google Forms to Workspace Studio
- Sheets for Workspace Studio

### Additional policy setting to verify

If this policy setting is checked:

> **Block other apps from accessing the selected apps via APIs, if access levels aren't met**

Then also check this box:

> **Exempt allowlisted apps so they can always access APIs for specific Google services, regardless of access levels**

## Related Topics

- [Troubleshoot Workspace Studio for your users](https://knowledge.workspace.google.com/admin/studio/troubleshoot-workspace-studio-for-your-users)
- [Troubleshooting and FAQ](https://support.google.com/workspace-studio/#topic=16430802)
- [Create & use custom steps in flows](https://support.google.com/a/users/answer/16433731)
- [Allow or block Gemini for Google Workspace steps](https://knowledge.workspace.google.com/admin/studio/manage-access-to-steps-and-starters-in-workspace-studio)
- [Allow or block Workspace Integrations steps](https://knowledge.workspace.google.com/admin/studio/allow-or-block-ws-integrations-steps)
- [Allow or block Google Workspace custom steps](https://knowledge.workspace.google.com/admin/studio/allow-or-block-ws-custom-steps)
- [Allow or block Send a webhook](https://knowledge.workspace.google.com/admin/studio/allow-or-block-send-a-webhook)

## Licensing

Unless otherwise noted:

- Page content is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
- Code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
- See [Google Developers Site Policies](https://developers.google.com/site-policies) for details.
