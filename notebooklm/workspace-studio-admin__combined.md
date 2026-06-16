---
title: "Combined source: workspace-studio-admin"
product_area: "workspace-studio-admin"
source_count: 5
generated_at: "2026-06-16T08:47:02Z"
source_type: "coverage_merged_official_extracts"
---

# Combined source: workspace-studio-admin

This file merges 5 official extracted source document(s) from coverage area `workspace-studio-admin` for NotebookLM import limits.
No synthetic documentation is added; each section preserves the source URL and extracted Markdown body.

## Source index

1. Allow or block Gemini for Google Workspace steps  |  Studio  |  Google Workspace Help — https://knowledge.workspace.google.com/admin/studio/allow-or-block-gemini-for-ws-steps
2. Allow or block Workspace service–specific steps  |  Studio  |  Google Workspace Help — https://knowledge.workspace.google.com/admin/studio/allow-or-block-ws-service-specific-steps
3. Get started: Workspace Studio set up guide for admins  |  Google Workspace Help — https://knowledge.workspace.google.com/admin/studio/get-started-workspace-studio-set-up-guide-for-admins
4. Set up activity alerts for Workspace Studio  |  Google Workspace Help — https://knowledge.workspace.google.com/admin/studio/set-up-activity-alerts-for-workspace-studio
5. Stop a Workspace Studio flow as an admin  |  Google Workspace Help — https://knowledge.workspace.google.com/admin/studio/stop-a-workspace-studio-flow-as-an-admin

---

## Source 1: Allow or block Gemini for Google Workspace steps  |  Studio  |  Google Workspace Help

- Source URL: https://knowledge.workspace.google.com/admin/studio/allow-or-block-gemini-for-ws-steps
- Original file: `docs/allow-or-block-gemini-for-google-workspace-steps-studio-google-workspace-help-a631417f.md`
- Product area: `workspace-studio-admin`

# Allow or Block Gemini for Google Workspace Steps — Summary

**Source:** Google Workspace Help  
**URL:** https://knowledge.workspace.google.com/admin/studio/allow-or-block-gemini-for-ws-steps  
**Last updated:** 2026-06-11 UTC

---

## Purpose

Google Workspace administrators can control whether **Gemini for Google Workspace** is enabled for **Google Workspace Studio**.

When enabled, Gemini lets users:

- Create custom AI steps from a prompt
- Use those AI steps in Workspace Studio flows

If admins only want to block specific AI-powered steps, Google recommends using the separate setting:

- [Allow or block Workspace service–specific steps](https://knowledge.workspace.google.com/admin/studio/allow-or-block-ws-service-specific-steps)

---

## Supported Editions

> _Supported editions for this feature: Enterprise Standard and Enterprise Plus; Teaching and Learning add-on and Education Plus; Google AI Pro for Education, and AI Ultra Access. [Compare your edition](https://knowledge.workspace.google.com/admin/getting-started/editions/compare-google-workspace-editions)_

Supported editions include:

- **Enterprise Standard**
- **Enterprise Plus**
- **Teaching and Learning add-on**
- **Education Plus**
- **Google AI Pro for Education**
- **AI Ultra Access**

---

## Age Restriction

> _Users designated as under 18 can't use AI features in Workspace Studio._

Users marked as **under 18** are not allowed to use AI features in Workspace Studio.

---

## Privacy Note

> **Note:** AI features in Workspace Studio follow the privacy principles in the  
> [Generative AI in Google Workspace Privacy Hub](https://knowledge.workspace.google.com/admin/generative-ai/generative-ai-in-google-workspace-privacy-hub).

---

## Required Admin Privilege

To change this setting, an admin must have the:

- [Gemini Settings administrator privilege](https://knowledge.workspace.google.com/admin/users/administrator-privilege-definitions#gemini)

---

## How to Allow or Block Gemini for Workspace Studio

### Steps in the Google Admin Console

1. In the Google Admin console, go to:

   **Menu → Generative AI → Gemini for Workspace**

   Direct link:

   [Go to Gemini for Workspace](https://admin.google.com/ac/managedsettings/793154499678)

2. Click the **Feature access panel**.

3. Optional: To apply the setting only to certain users, select one of the following from the side panel:

   - An **organizational unit**, often used for departments
   - A configuration **group**, for advanced configuration

   > Group settings override organizational units. [Learn more](https://knowledge.workspace.google.com/admin/users/advanced/customize-service-settings-using-configuration-groups#how-groups-work)

4. Next to **Workspace Studio**, click **Edit**.

5. Select either:

   - **On**
   - **Off**

6. Click **Save**.

   Alternatively, for an organizational unit, you might click **Override**.

---

## Restoring Inherited Settings

To later restore the inherited value:

- Click **Inherit** for an organizational unit
- Click **Unset** for a group

---

## What Happens When Gemini Is Turned Off for Workspace Studio

When Gemini for Google Workspace is turned off for Workspace Studio, users cannot:

- Create flows from a prompt
- Use AI steps

Important operational impact:

> Any active flows that have AI steps in them stop working.

---

## Related Topics

- [Troubleshoot Workspace Studio for your users](https://knowledge.workspace.google.com/admin/studio/troubleshoot-workspace-studio-for-your-users)
- [Troubleshooting and FAQ](https://support.google.com/workspace-studio/#topic=16430802)
- [Create & use custom steps in flows](https://support.google.com/a/users/answer/16433731)
- [Allow or block Workspace service–specific steps](https://knowledge.workspace.google.com/admin/studio/allow-or-block-ws-service-specific-steps)
- [Allow or block Workspace Integrations steps](https://knowledge.workspace.google.com/admin/studio/allow-or-block-ws-integrations-steps)
- [Allow or block Google Workspace custom steps](https://knowledge.workspace.google.com/admin/studio/allow-or-block-ws-custom-steps)
- [Allow or block Send a webhook](https://knowledge.workspace.google.com/admin/studio/allow-or-block-send-a-webhook)

---

## Licensing

Unless otherwise noted:

- Page content is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/)
- Code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0)
- See [Google Developers Site Policies](https://developers.google.com/site-policies) for details
- Java is a registered trademark of Oracle and/or its affiliates.

---

## Source 2: Allow or block Workspace service–specific steps  |  Studio  |  Google Workspace Help

- Source URL: https://knowledge.workspace.google.com/admin/studio/allow-or-block-ws-service-specific-steps
- Original file: `docs/allow-or-block-workspace-service-specific-steps-studio-google-workspace-help-d89aec76.md`
- Product area: `workspace-studio-admin`

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

---

## Source 3: Get started: Workspace Studio set up guide for admins  |  Google Workspace Help

- Source URL: https://knowledge.workspace.google.com/admin/studio/get-started-workspace-studio-set-up-guide-for-admins
- Original file: `docs/get-started-workspace-studio-set-up-guide-for-admins-google-workspace-help-adf45c07.md`
- Product area: `workspace-studio-admin`

# Get started: Workspace Studio set up guide for admins — Summary

**Source:** https://knowledge.workspace.google.com/admin/studio/get-started-workspace-studio-set-up-guide-for-admins  
**Last updated:** 2026-06-11 UTC  
**Audience:** Google Workspace administrators

---

## Overview

Google Workspace Studio lets users create **“flows”** to automate routine work across Google Workspace apps such as **Gmail, Drive, and Chat**, as well as third-party services.

Users with access to **Gemini** can build flows by describing what they want the automation to do.

> Google Workspace Studio allows users to create "flows" that automate routine work tasks across Google Workspace apps, including Gmail, Drive, and Chat, and third-party services.

Flows can act on behalf of users, including:

- Drafting emails
- Creating and updating files
- Creating tasks
- Performing other automated actions across connected services

Because flows can modify data and send communications, poorly configured flows may create risk.

> Poorly configured flows could unintentionally edit or delete data, or send excessive notifications.

Admins can manage risks using:

- Access policies
- Feature controls
- Sharing settings
- Alerts
- Audit and investigation tools
- Emergency stop procedures

---

# Step 1. Set up Workspace Studio for your organization

Before enabling users, Google recommends configuring access and guardrails so flows behave as expected and data remains secure.

---

## 1. Manage access to Studio

### Admin setting location

**Admin console → Menu → Apps → Google Workspace → Workspace Studio**

### Required action

Check that **Service status** is set to **ON** for the correct:

- Organizational units
- Groups

### Recommendation

Create a **child organizational unit** with Workspace Studio access turned **off**.

This gives admins a fast emergency control: move a user into that OU to stop all flows they own.

> **Recommendation**: Create a child organizational unit that has access to Studio turned off. This lets you quickly move a user to it to stop a flow they own.

### Related help

- [Turn Google Workspace Studio on or off for your organization](https://knowledge.workspace.google.com/admin/users/access/turn-google-workspace-studio-on-or-off-for-your-organization)

---

## 2. Manage access to Studio features

Admins can control whether users can:

- Use **Gemini** to create flows
- Use **AI-powered steps** in flows
- Use steps for other Google Workspace services
- Use integrations or custom steps

### Recommendations

- Allow users with **Gemini for Google Workspace** access to use Gemini features in Studio.
- Allow users to use steps for Workspace services they already have access to.
- Only block service-specific steps if there is a clear risk of abuse.
- Use the **Google Workspace Marketplace allowlist** to control:
  - Integrations
  - Published custom steps

### Related help

- [Manage access to steps and starters in Workspace Studio](https://knowledge.workspace.google.com/admin/studio/manage-access-to-steps-and-starters-in-workspace-studio)

---

## 3. Manage who can share flows

Allowing flow sharing can improve productivity by letting trusted users distribute reusable flow templates.

### How sharing works

When someone shares a flow:

- The recipient receives a **copy** of the flow.
- The copy includes the owner’s setup, such as:
  - Text entered into the flow
  - Email addresses
  - Links to Drive files
- The recipient does **not** get access to private data they could not already access.

> When a user shares a flow, the recipient clicks a link to get a _copy_ of the flow. The copy includes the owner's setup, such as text they entered, email addresses, and links to files in Drive. The recipient does not get access to the owner's private data, like emails or Drive files, only the content that they can already access.

### Admin setting location

**Admin console → Apps → Google Workspace → Workspace Studio → Sharing settings**

### Recommendation

Allow sharing for **trusted organizational units and groups** so they can distribute standardized flow templates.

### Related help

- [Allow people to share flows in Workspace Studio](https://knowledge.workspace.google.com/admin/studio/allow-people-to-share-flows-in-workspace-studio)

---

## 4. Set up alerts

Admins can create activity rules to be notified about specific Workspace Studio activity.

---

### Recommended alert: High-frequency flow activity

Purpose: Detect flows that may be looping or running excessively.

**Condition:**

- Create a rule for **Rule log events**
- Event: **Start run**

**Threshold:**

- Alert if count exceeds **100** in **1 hour**

**Action:**

- Send an email to all admins

---

### Recommended alert: AI usage

Purpose: Monitor generative AI use in automations.

**Condition:**

- Create a rule where **Step name** contains **"Ask Gemini"**
- Optionally include other AI-powered steps

For the full list of available steps, see:

- [Guide t

[... summary truncated for context management ...]

---

## Source 4: Set up activity alerts for Workspace Studio  |  Google Workspace Help

- Source URL: https://knowledge.workspace.google.com/admin/studio/set-up-activity-alerts-for-workspace-studio
- Original file: `docs/set-up-activity-alerts-for-workspace-studio-google-workspace-help-ff969952.md`
- Product area: `workspace-studio-admin`

# Set up activity alerts for Workspace Studio — Summary

**Source:** Google Workspace Help  
**URL:** https://knowledge.workspace.google.com/admin/studio/set-up-activity-alerts-for-workspace-studio  
**Last updated:** 2026-06-11 UTC

---

## Overview

Administrators can create activity alerts for **Google Workspace Studio flow activity** in the **Workspace Alert Center**. Alerts can notify admins by **email** or in the **Admin Console**.

These alerts are useful for monitoring situations such as:

- Flows running unusually often
- Potential loops or misconfigurations
- Excessive quota consumption
- Heavy usage of AI-powered steps such as **Ask Gemini**

> “As an administrator, you can get alerts about Google Workspace Studio flow activity, such as when flows run a lot or use a lot of AI steps.”

Alerts are configured through **Rules** in the Google Admin console.

---

## Prerequisites

To create these activity rules:

- Go to the Google Admin console.
- Navigate to **Menu → Rules**.
- You need the **View Trust Rules administrator privilege**.
- The data source **Workspace Studio log events** must be available.
  - If it does not appear, verify that:
    - Your Google Workspace edition supports it.
    - You have privileges to view Workspace Studio event logs.

Direct link:

> [Go to Rules](https://admin.google.com/ac/ax)

---

# Example 1: Alert for High Flow Activity

## Purpose

Create an activity rule to notify administrators when Workspace Studio flows run an unusually high number of times in a short period.

This helps identify:

- Potential loops
- Misconfigurations
- Quota consumption issues

## Alert Trigger

This example sends a notification when the **Start run** event occurs more than **100 times in one hour**.

> “This example shows how to create an activity rule that sends a notification when the ‘Start run’ event occurs more than 100 times in one hour.”

---

## Steps

1. In the Google Admin console, go to:

   **Menu → Rules**

   Direct link:

   > [Go to Rules](https://admin.google.com/ac/ax)

2. At the top of the rules table, click:

   **Create rule → Activity**

3. Enter a **Rule name**, for example:

   > `High Workspace Studio flow activity`

4. Optionally enter a **Description**, for example:

   > `Alert when flows run more than 100 times in an hour.`

5. Click **Continue**.

6. Click **Data source** and select:

   > `Workspace Studio log events`

7. Add a condition:

   - **Attribute:** `Event`
   - **Operator:** `Is`
   - **Value:** `Start run`

8. Click **Continue**.

9. In **Action and notification**, select:

   > **If the event frequency meets a specific threshold**

10. Configure the frequency threshold:

    - **Count:** `100`
    - **Time period:** `1 Hour`

    Meaning:

    > “more than 100 times in 1 hour”

11. Select where to send notifications and choose a severity level.

12. Click **Continue**.

13. Verify the settings:

    - **Source:** Workspace Studio log events
    - **Conditions:** Event Is Start run
    - **Threshold:** If the event happens more than 100 times in 1 hour
    - **Alerts:** On, if notifications in the Alert center were selected
    - **Emails:** On, if email notifications were selected
    - **Rule status:** Active

14. Click **Create Rule**.

---

# Example 2: Alert When Flows Use Gemini a Lot

## Purpose

Create an activity rule to notify administrators when Workspace Studio flows use the **Ask Gemini** step frequently.

This helps track usage of the AI-powered **Ask Gemini** step.

> “You can set up an activity rule to notify administrators when Workspace Studio flows use the **Ask Gemini** step.”

---

## Alert Trigger

This example sends a notification when **Ask Gemini** steps are used more than **1000 times in 24 hours**.

> “This example shows how to create an activity rule that sends a notification when these AI-powered steps are used more than 1000 times in 24 hours.”

---

## Steps

1. In the Google Admin console, go to:

   **Menu → Rules**

   Direct link:

   > [Go to Rules](https://admin.google.com/ac/ax)

2. At the top of the rules table, click:

   **Create rule → Activity**

3. Enter a **Rule name**, for example:

   > `Workspace Studio - Ask Gemini Alert`

4. Optionally enter a **Description**, for example:

   > `Alert when flows use Ask Gemini more than 1000 times in 24 hours.`

5. Click **Continue**.

6. Click **Data source** and select:

   > `Workspace Studio log events`

7. Add the first condition:

   - **Attribute:** `Event`
   - **Operator:** `Is`
   - **Value:** `Start step`

8. Click **Add condition** and add a second condition:

   - **Attribute:** `Step name`
   - **Operator:** `Contains`
   - **Value:** `Ask Gemini`

9. Click **Continue**.

10. Select where to send notifications and choose a severity level.

11. Click **Continue**.

12. Verify the settings:

    - **Source:** Workspace Studio log events
    - **Conditions:** Event Is **Start step** AND Step Name Contains **Ask Gemini**
    - **Threshold:** If the

[... summary truncated for context management ...]

---

## Source 5: Stop a Workspace Studio flow as an admin  |  Google Workspace Help

- Source URL: https://knowledge.workspace.google.com/admin/studio/stop-a-workspace-studio-flow-as-an-admin
- Original file: `docs/stop-a-workspace-studio-flow-as-an-admin-google-workspace-help-3d78d2df.md`
- Product area: `workspace-studio-admin`

# Stop a Workspace Studio Flow as an Admin — Summary

**Source:** Google Workspace Help  
**URL:** https://knowledge.workspace.google.com/admin/studio/stop-a-workspace-studio-flow-as-an-admin  
**Last updated:** 2026-06-11 UTC

---

## Purpose

Google Workspace Studio lets users create **flows** that automate work across Google Workspace and allowed third-party services. While flows can improve productivity, they may sometimes behave in **unexpected or unwanted ways**.

Admins can stop problematic flows by:

1. Identifying which flow is causing the issue.
2. Contacting Google Workspace Support to stop that specific flow.
3. If urgent, temporarily disabling **all Workspace Studio flows** for the flow owner.

---

## Key Excerpts

> With Google Workspace Studio, people in your organization can create flows to automate work across Workspace and third-party services they're allowed to connect to.

> These flows can make people more productive by automating routine tasks, but they can sometimes work in unexpected or unwanted ways.

> To stop a flow, first you figure out which flow is causing the problem, then send a request to Support to stop it.

> **Important:** These steps turn off all the user's flows. Make sure that they don't have any business critical flows before you continue.

---

## How Unwanted Flow Activity Is Usually Discovered

Admins typically detect problematic Studio flow activity through:

- **User reports**
- **Workspace event logs**

Examples of suspicious or unwanted activity include:

### High Frequency Activity

Examples:

- More Gmail messages sent than normal
- More Google Chat messages sent than normal
- More file changes than expected
- More files created than would be possible for a human user

**Tip:** Chat messages sent by Studio flows include a **chip next to the sender’s name** showing they were sent by a Studio flow.

### Regularly Scheduled Unwanted Activity

Examples:

- Activity repeating approximately every hour
- Activity occurring at all times of day

**Note:** Flows have built-in staggering, so repeated activity may not happen at exactly the same interval each time.

---

## Step 1: Find Which Flow Is Causing the Problem

Use **Workspace Studio log events** in either:

- **Audit and investigation tool**
- **Security investigation tool**

Reference: [Workspace Studio log events](https://knowledge.workspace.google.com/admin/reports/workspace-studio-log-events)

### Recommended Attribute Filters

Use these filters when searching Studio logs:

#### Actor

Set the **Actor** filter to the affected user’s email address.

#### Event

If you know when the problem occurred:

- Filter by **Step complete**
- Look for a step that finished around the same time as the unwanted activity

You may also filter by **Step app** if you know where the activity occurred, such as:

- Gmail
- Google Chat
- Another Workspace app

### Record the Flow ID

Once you identify the flow in the results list, note the:

- **Flow ID**

This is required when contacting Google Workspace Support.

---

## Step 2: Stop a User’s Flow

### Preferred Method: Contact Google Workspace Support

Contact Google Workspace Support and provide the **Flow ID** for the flow you want stopped.

Support will stop the specific flow for you.

Reference: [Contact Google Workspace support](https://knowledge.workspace.google.com/admin/support/contact-google-workspace-support)

---

## Urgent Option: Stop All Flows Owned by the User

If the flow must be stopped immediately and you cannot wait for Support, you can stop **all** flows owned by that user.

> **Important:** These steps turn off all the user's flows. Make sure that they don't have any business critical flows before you continue.

### Steps

1. **Add an organizational unit**
   - Set the user’s current organizational unit as the parent.
   - Reference: [Add an organizational unit](https://knowledge.workspace.google.com/admin/users/advanced/add-an-organizational-unit)

2. **Move the user to the new organizational unit**
   - Reference: [Move the user to an organizational unit](https://knowledge.workspace.google.com/admin/users/advanced/move-users-to-an-organizational-unit)

3. In the **Google Admin console**, go to:

   ```text
   Menu > Apps > Google Workspace > Workspace Studio
   ```

   Direct link: [Go to Workspace Studio](https://admin.google.com/ac/managedsettings/243976345647)

   **Required privilege:**  
   [Service Settings administrator privilege](https://knowledge.workspace.google.com/admin/users/administrator-privilege-definitions#service_settings)

4. Click **Service status**.

5. On the left, select the new organizational unit.

6. Change **Service status** to **Off**.

7. Click **Override**.

8. After Support stops the problematic flow:
   - Move the user back to their original organizational unit.
   - The user can use Workspace Studio again.
   - The stopped flow remains off until the user manually turns it back on.

---

## Important Notes and Cautions

-

[... summary truncated for context management ...]

---
