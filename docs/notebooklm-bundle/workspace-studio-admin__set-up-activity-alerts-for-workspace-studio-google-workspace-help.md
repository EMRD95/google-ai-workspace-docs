# Set up activity alerts for Workspace Studio  |  Google Workspace Help

**Product Area:** workspace-studio-admin
**Source:** https://knowledge.workspace.google.com/admin/studio/set-up-activity-alerts-for-workspace-studio

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
