# Turn Gemini Enterprise on or off for users  |  Google Workspace Help

**Product Area:** admin-console
**Source:** https://knowledge.workspace.google.com/admin/generative-ai/gemini-enterprise/turn-gemini-enterprise-on-or-off-for-users

# Turn Gemini Enterprise on or off for users

**Source:** [Google Workspace Admin Help – Gemini Enterprise](https://knowledge.workspace.google.com/admin/generative-ai/gemini-enterprise/turn-gemini-enterprise-on-or-off-for-users)

## Overview
As an administrator, you control which users can use **Gemini Enterprise**. You can turn it on for:

- Everyone in your organization
- Specific organizational units (OUs)
- Specific access groups

Users with access can use the **Gemini Enterprise side‑panel agents**, **Gemini Enterprise assistant**, and **Gemini CLI**.

> **Important:** Gemini Enterprise is **not included** with Google Workspace subscriptions. You must purchase separate licenses.

## Get licenses
- **Business edition** – Contact a Google sales representative or Google Cloud partner.
- **All editions** – You can also sign up directly and purchase licenses.  
  → [Get subscriptions and assign licenses for Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/licenses)

---

## Turn the service on or off

Before you begin, place users’ accounts in an [organizational unit](https://knowledge.workspace.google.com/admin/users/advanced/how-the-organizational-structure-works) (department) or an [access group](https://knowledge.workspace.google.com/admin/users/advanced/customize-service-access-using-access-groups) (cross‑department access).

### Steps
1. In the **Google Admin console**, go to **Menu** → **Generative AI** → **Gemini Enterprise**.  
   *(Requires the* **Service Settings administrator** *privilege.)*
2. Click **Service status**.
3. Choose **On for everyone** or **Off for everyone**, then click **Save**.
4. (Optional) To apply the setting only to specific users, select an **organizational unit** or an **access group** at the side.  
   **Group settings override organizational units.** [Learn more](https://knowledge.workspace.google.com/admin/users/advanced/customize-service-settings-using-configuration-groups#how-groups-work)

> Changes can take **up to 24 hours** but typically happen more quickly. [Learn more](https://knowledge.workspace.google.com/admin/support/troubleshooting/how-changes-propagate-to-google-services)

---

## Share chats externally (Business edition only)
*Applies only to **Gemini Enterprise – Business edition**.*

Control whether users can share Gemini chats outside your organization.

### Steps
1. Go to **Menu** → **Generative AI** → **Gemini Enterprise** → **Business edition**.  
   *(Requires the* **Service administrator** *privilege.)*
2. Click **Sharing options**.
3. (Optional) Apply to an OU or access group.
4. Choose one:
   - **Off** – Share only with domains associated with your Google Workspace organization (primary + secondary domains). No external sharing.
   - **Share with allowlisted domains** – Share with accounts in your allowlisted domains. Click **Edit** to modify the list.  
     → [Allow sharing with only trusted domains](https://knowledge.workspace.google.com/admin/domains/allow-external-sharing-with-only-trusted-domains)
   - **On** – Share outside your organization to any domain.
5. Click **Save**.

---

## Control access to Workspace data
Gemini Enterprise – Business, Standard, and Plus editions **can independently access your organization’s Google Workspace data** (e.g., Gmail, Drive, Calendar). You decide whether each edition can read this data.

### Business edition access
1. Go to **Menu** → **Generative AI** → **Gemini Enterprise** → **Business Edition**.
2. Check or uncheck **Allow Gemini Enterprise to access Google Workspace data**.
3. (Optional) Apply to an OU or access group.
4. Click **Save**.

### Standard and Plus edition access
1. Go to **Menu** → **Generative AI** → **Gemini Enterprise** → **Standard, Plus, Frontline**.
2. Check or uncheck **Allow Gemini Enterprise to access Google Workspace data**.
3. (Optional) Apply to an OU or access group.
4. Click **Save**.

Again, **group settings override OUs**, and changes may take up to 24 hours to propagate.

---

## Legal & data ownership
- **Frontline, Standard, Plus editions:** Governed by [GCP Terms of Service](https://cloud.google.com/terms/) and Google Cloud Privacy Notice.
- **Business edition:** Governed by [Google ToS](https://policies.google.com/terms), Google Privacy Policy, and [Business Edition Additional Terms of Service](https://cloud.google.com/terms/gemini-enterprise/business).

Across all editions for Workspace customers, the following promises apply:

> - **You own your data**, not Google.  
> - Your data (prompts, outputs, and training) **isn’t used to train Google models** or models for any other customer.  
> - Google **never sells** customer data to third parties.

---

## Next steps
- [Gemini Enterprise overview (Google Cloud)](https://cloud.google.com/gemini-enterprise)

*Page last updated 2026-06-11 UTC.*
