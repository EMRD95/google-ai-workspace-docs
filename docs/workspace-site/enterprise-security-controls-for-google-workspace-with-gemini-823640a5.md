---
title: "Enterprise security controls for Google Workspace with Gemini"
source_url: "https://workspace.google.com/blog/ai-and-machine-learning/enterprise-security-controls-google-workspace-gemini?hl=en"
product_area: "workspace-site"
retrieved_at: "2026-06-15T09:03:10Z"
---

# Enterprise security controls for Google Workspace with Gemini

Source: https://workspace.google.com/blog/ai-and-machine-learning/enterprise-security-controls-google-workspace-gemini?hl=en

AI and Machine Learning

# Enterprise security controls for Google Workspace with Gemini

July 17, 2025

![https://storage.googleapis.com/gweb-cloudblog-publish/images/unnamed_3_2AuFC1M.max-1600x1600.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/unnamed_3_2AuFC1M.max-1600x1600.png)

##### Stephanie Chan

Security Product Marketing Manager

##### Adam Gavish

Senior Product Manager, Google Workspace

##### Google Workspace Newsletter

Keep up with the evolving future of work and collaboration with insights, trends, and product news.

[SIGN UP](https://workspace.google.com/?source=gafb-blog_article-body-en#newsletter)

*“Security was at the forefront of our enterprise’s most critical needs as we looked to implement a generative AI solution. During our search, we ran a platform ‘bake-off’ and found that Gemini met all our security needs. The solution inherits all our existing Workspace security settings to keep our data, prompts, and work within the tenant, giving us peace of mind to deploy generative AI across our enterprise safely.”***- JK Krug, Vice President of Digital Employee Experience, Equifax**

Generative AI has woven itself into the fabric of users’ daily lives, becoming an indispensable tool for productivity, innovation, and convenience. With its rapid adoption and growing importance, organizations are rightly concerned about potential data security and privacy risks. Evaluating generative AI’s infrastructure, data governance policies, and security controls to protect sensitive data is a must.

Google Workspace with Gemini is enterprise-ready. First, Gemini keeps customer data [confidential](https://support.google.com/a/answer/15706919) and can support compliance with different regulatory frameworks, such as HIPAA and FedRAMP High. Second, Gemini is built with a [layered defense strategy for prompt injection mitigation](https://security.googleblog.com/2025/06/mitigating-prompt-injection-attacks.html), an emerging attack vector against AI systems. And third, Workspace comes with granular user access and data security controls, helping administrators safely and securely deploy AI tools, such as the Gemini app, Gemini in Workspace apps, and NotebookLM, across their organizations with confidence. Let’s take a closer look at these controls.

### Protecting your data

Protecting sensitive data is paramount. Gemini integrates with existing data security measures in Workspace to help prevent unauthorized access and exfiltration.

- [Create and manage trust rules for Drive sharing](https://support.google.com/a/answer/10621317): Trust rules in Drive help restrict Gemini's access by controlling how data is shared between internal and external users. Since Gemini can only retrieve data the user has access to, these rules can limit what Gemini is able to retrieve.
- [Understand Gemini’s data access with Drive inventory reporting](https://support.google.com/a/answer/15141054?hl=en): Admins can utilize Drive inventory reporting to gain a holistic view of how their data is classified, who can access it, and how it’s being used.
- [Apply IRM controls to restrict Gemini’s access to sensitive data](https://support.google.com/a/answer/9656855?product_name=UnuFlow&sjid=16230191034105272886-NA&visit_id=638762643105374618-2259026318&rd=1&src=supportwidget0#irmfaq&zippy=%2Cdoes-gemini-respect-dlp-irm-policies): Data loss prevention (DLP) policies can apply information rights management (IRM) controls to sensitive files. When IRM is applied (e.g., preventing download, printing, or copying), Gemini does not retrieve those protected files to generate a response.
- [Apply client-side encryption to prevent Gemini’s access to sensitive data](https://support.google.com/a/answer/10741897): For the highest level of data protection, client-side encryption (CSE) can be used. When CSE is enabled, the protected data is indecipherable to any unauthorized third-party, including Google or any generative AI assistants, such as Gemini.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Screenshot_2025-07-11_10.21.44_AM.max-2000x2000.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/Screenshot_2025-07-11_10.21.44_AM.max-2000x2000.png)

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Screenshot_2025-07-11_10.21.44_AM.max-2000x2000.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/Screenshot_2025-07-11_10.21.44_AM.max-2000x2000.png)

Admin console UI for data loss prevention with a rule configuration to “disable download, print, and copy” in Google Drive for all collaborators.

### Understanding AI usage

Transparency and accountability are crucial for security. Workspace provides comprehensive logging and exporting capabilities for Gemini activity.

- [Review Gemini usage and data access in your organization](https://support.google.com/a/answer/14564320?hl=en&src=supportwidget0&authuser=0): Admins are able to review Gemini usage and data access across their organization to understand Gemini adoption. These reports provide the overall usage level in the Gemini app and Gemini in Workspace, as well as adoption of Gemini on a per-app basis.
- Query, investigate, and export Gemini access to files in Drive: Admins can access Gemini audit logs using the [Reports API](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/gemini-in-workspace-apps), which indicate instances when Gemini accessed a Drive file to fulfill a user query. These logs are also available in the [security investigation tool](https://support.google.com/a/answer/7575955?hl=en&sjid=16040906469908561115-NC), enabling Admins to query, investigate, and export Gemini access to Drive log data.
- [Use Google Vault to investigate conversations in the Gemini app](https://support.google.com/vault/answer/15695746): For eDiscovery purposes, administrators can leverage Vault to search and export relevant prompts and responses from the Gemini app.
- [Use the Data Export tool to export organizational data](https://support.google.com/a/answer/14339894?hl=en&ref_topic=14104519&sjid=15502736214237378009-NC): Organizations retain full control over their data in Workspace. Administrators can export their [Gemini app](https://support.google.com/a/answer/14817835?sjid=14448788510783536230-NC) and [NotebookLM](https://support.google.com/a/answer/16054396) data for archive or backup purposes using the Data Export tool. Admins are able to [manage](https://support.google.com/a/answer/15706919?hl=en&src=supportwidget0&authuser=0#zippy=%2Chow-long-are-prompts-saved) the duration for how long prompts and responses are saved in the Gemini app, enabling this content to be exported (this setting is not available for Gemini in Workspace apps, which does not save prompts or responses).

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Screenshot_2025-07-11_10.33.29_AM.max-2000x2000.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/Screenshot_2025-07-11_10.33.29_AM.max-2000x2000.png)

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Screenshot_2025-07-11_10.33.29_AM.max-2000x2000.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/Screenshot_2025-07-11_10.33.29_AM.max-2000x2000.png)

A call using the Reports API to query recent Gemini in Workspace usage activity for a given user.

### Deploying AI with flexibility

Workspace offers granular controls to manage user access, allowing administrators to define who can leverage these powerful and robust AI capabilities.

- [Manage Gemini for your organization](https://support.google.com/a/topic/15995054?hl=en&ref_topic=13853688&sjid=15502736214237378009-NC): Admins can enable or disable Gemini features across Workspace applications like Gmail, Google Drive, and Google Docs. This allows for precise access control based on users, groups, or organizational units.
- [Manage access to the Gemini app](https://support.google.com/a/answer/14571493?hl=en&ref_topic=15995054&sjid=15502736214237378009-NC): Admins have the flexibility to grant or restrict user access to the standalone Gemini app based on specific users, groups, or organizational units.
- [Turn Workspace apps in Gemini on or off](https://support.google.com/a/answer/15293691?hl=en&sjid=16230191034105272886-NA): Admins can control whether users can utilize the Workspace extension within the Gemini app, which enables the Gemini app to leverage Workspace data.
- [Turn NotebookLM on or off](https://support.google.com/a/answer/15239506): Similar to Gemini, admins can manage user access to NotebookLM and NotebookLM Plus across various users, groups, or organizational units.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Screenshot_2025-07-11_10.28.02_AM.max-2000x2000.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/Screenshot_2025-07-11_10.28.02_AM.max-2000x2000.png)

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Screenshot_2025-07-11_10.28.02_AM.max-2000x2000.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/Screenshot_2025-07-11_10.28.02_AM.max-2000x2000.png)

Admin console UI with granular settings to restrict user access of Gemini in Workspace to specific Workspace apps for users, groups, and organizational units.

### Securing access points

Beyond user-level access, organizations can implement device-specific policies to further secure Gemini usage.

- [Control access to apps based on user and device context](https://support.google.com/a/answer/9261439?hl=en&sjid=16230191034105272886-NA): Administrators can assign context-aware access (CAA) policies to limit access to the Gemini app and NotebookLM on compliant devices based on factors such as user identity, device security status, IP address, and geographical location.
- [Apply endpoint DLP policies to the Gemini app](https://support.google.com/a/answer/10104358): [Chrome Enterprise Premium](https://chromeenterprise.google/products/chrome-enterprise-premium/) enables robust data loss prevention (DLP) that extend to the Chrome browser, including the Gemini app and NotebookLM. This allows for more granular control over actions including copy and paste, printing, and uploads/downloads of sensitive data into the Chrome browser. It also offers personally identifiable information (PII) masking and screenshot protection, with all relevant activities logged for audit.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Screenshot_2025-07-11_10.29.56_AM.max-1700x1700.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/Screenshot_2025-07-11_10.29.56_AM.max-1700x1700.png)

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Screenshot_2025-07-11_10.29.56_AM.max-1700x1700.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/Screenshot_2025-07-11_10.29.56_AM.max-1700x1700.png)

Admin console UI with granular access settings for devices and OS, restricting user access levels for the Gemini app to a specific organizational unit.

*“We became the first major financial institution in Canada to empower all of our team members with Google AI in Workspace. In the pilot program, we saw that Google AI offered significant time savings and productivity gains for team members, allowing them to automate routine tasks, access information quickly, and collaborate more effectively, all while ensuring data is secure and trustworthy. Today, we’re confident this technology will help all of our team members succeed in their roles, while delivering even more exceptional experiences to our more than 820,000 clients."***- John Tarnowski, Chief Client Experience and Technology Officer, ATB Financial**

By implementing these robust security controls, organizations can confidently embrace the productivity benefits of Gemini in Workspace while helping to maintain a strong security posture and ensuring data protection.

To learn more, explore the following resources:

- White paper: [Gemini for Google Workspace privacy, security, and compliance white paper](https://workspace.google.com/learning/content/gemini-privacy-security-compliance-whitepaper)
- Help center article: [Generative AI in Google Workspace Privacy Hub](https://support.google.com/a/answer/15706919?hl=en)
- Adoption guide: [Getting the most from generative AI in your organization](https://support.google.com/a/answer/15905903?product_name=UnuFlow&hl=en&visit_id=638763526909241397-1705556830&rd=1&src=supportwidget0&hl=en)
- Customer story: [Equifax embraces secure generative AI with Gemini](https://workspace.google.com/blog/customer-stories/equifax-embraces-gemini-for-secure-innovation-across-business-units?e=48754805)
- Customer story: [Fullstory drives growth while securing data with Gemini](https://workspace.google.com/blog/customer-stories/fullstory-collaboration-culture-with-google-workspace-and-gemini?e=48754805)
- Customer story: [ATB Financial Empowers Employees with Google AI](https://www.atb.com/company/news/releases/atb-empowers-employees-with-google-ai/)

Posted in

- [AI and Machine Learning](https://workspace.google.com/blog/ai-and-machine-learning)
- [Identity and Security](https://workspace.google.com/blog/identity-and-security)

##### Related articles

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/5522d_Foundation_for_the_agentic_AI_era_Blog.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/5522d_Foundation_for_the_agentic_AI_era_Blog.max-700x700.jpg)

AI and Machine Learning

### Building a foundation for the agentic AI era

By John MacDonald • 4-minute read](https://workspace.google.com/blog/ai-and-machine-learning/building-a-foundation-for-the-agentic-ai-era)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/GWS_Image_Repository_Workspace_Drops_Blog_He.max-700x700.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/GWS_Image_Repository_Workspace_Drops_Blog_He.max-700x700.png)

Product Announcements

### May Workspace Drops: Turn raw data into tables, create new AI voiceovers, and customize your AI meeting notes

By The Google Workspace Team • 4-minute read](https://workspace.google.com/blog/product-announcements/may-workspace-drops)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/5522i_GWS_AI_small_business_advantage_Blog_h.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/5522i_GWS_AI_small_business_advantage_Blog_h.max-700x700.jpg)

AI and Machine Learning

### How AI is giving small businesses a major advantage

By Lisa Gevelber • 2-minute read](https://workspace.google.com/blog/ai-and-machine-learning/how-ai-is-giving-small-businesses-a-major-advantage)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/5522f_GWS_What_chess_can_teach_leaders_Blog_.max-700x700.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/5522f_GWS_What_chess_can_teach_leaders_Blog_.max-700x700.jpg)

AI and Machine Learning

### What chess can teach leaders about AI enablement

By Pat McCarthy • 4-minute read](https://workspace.google.com/blog/ai-and-machine-learning/what-chess-can-teach-leaders-about-ai-enablement)
