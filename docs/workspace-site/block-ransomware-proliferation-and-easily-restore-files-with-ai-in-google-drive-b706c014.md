---
title: "Block ransomware proliferation and easily restore files with AI in Google Drive"
source_url: "https://workspace.google.com/blog/product-announcements/ai-ransomware-detection-in-google-drive?hl=en"
product_area: "workspace-site"
retrieved_at: "2026-06-15T09:03:10Z"
---

# Block ransomware proliferation and easily restore files with AI in Google Drive

Source: https://workspace.google.com/blog/product-announcements/ai-ransomware-detection-in-google-drive?hl=en

Product Announcements

# Block ransomware proliferation and easily restore files with AI in Google Drive

September 30, 2025

![https://storage.googleapis.com/gweb-cloudblog-publish/images/GWS_Blog_header_Digital_sovereignty_no_tit.max-2500x2500_0Fho7Ki.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/GWS_Blog_header_Digital_sovereignty_no_tit.max-2500x2500_0Fho7Ki.png)

##### Luke Camery

Director of Product Management, Google Workspace

##### Kristina Behr

Vice President, Product Management, Google Workspace

##### Google Workspace Newsletter

Keep up with the evolving future of work and collaboration with insights, trends, and product news.

[SIGN UP](https://workspace.google.com/?source=gafb-blog_article-body-en#newsletter)

Ransomware remains one of the most damaging cyber threats facing organizations today. These attacks can lead to substantial financial losses, operational downtime, and data compromise, impacting organizations of all sizes and industries, including healthcare, retail, education, manufacturing, and government. In fact, intrusions related to ransomware represented [21%](https://cloud.google.com/security/resources/m-trends) of all the intrusions observed by Mandiant last year, with an average ransomware or extortion incident cost exceeding [$5M](https://www.ibm.com/reports/data-breach).

While native Workspace documents (e.g., Google Docs, Sheets) are not impacted by ransomware and ChromeOS has [never](https://chromeos.google/#security) had a ransomware attack, ransomware is a persistent threat for other file formats (e.g., PDF, Microsoft Office) and desktop operating systems (e.g., Microsoft Windows). **That’s why we're enhancing Google Drive for desktop with AI-powered ransomware detection to automatically stop file syncing and allow users to easily restore files with a few clicks.**

![https://storage.googleapis.com/gweb-cloudblog-publish/images/unnamed_17_X2xzaKr.max-1600x1600.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/unnamed_17_X2xzaKr.max-1600x1600.png)

![https://storage.googleapis.com/gweb-cloudblog-publish/images/unnamed_17_X2xzaKr.max-1600x1600.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/unnamed_17_X2xzaKr.max-1600x1600.png)

Users see this notification in Drive for desktop when ransomware has been detected on their device, automatically pausing file syncing to the cloud.

### The traditional approach to fighting ransomware falls short

To date, ransomware has largely been treated as an antivirus (AV) issue: Seek out potentially malicious code before it’s activated and quarantine it. This is an important and necessary defense, but with the continued success of ransomware attacks over the last few years, it’s clear this approach is insufficient. Ransomware is no longer just an IT issue and has become increasingly disruptive for core business operations, such as manufacturing lines, retail operations, or hospital services. We believe that it’s paramount to find a better way to fight ransomware.

What we’re announcing today is an entirely new layer of defense. While AV solutions continue their work to stop ransomware from getting in, we’ve built the protections to stop it from being effective once it is, inevitably, through the door. Our AI-powered detection in [Drive for desktop](https://support.google.com/drive/answer/10838124) identifies the core signature of a ransomware attack — an attempt to encrypt or corrupt files en masse — and rapidly intervenes to put a protective bubble around a user’s files by stopping file syncing to the cloud before the ransomware can spread. This helps to stop ransomware from doing what it must to be most effective: corrupt important files and make them unusable.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/maxresdefault_11.max-1300x1300.jpg](https://storage.googleapis.com/gweb-cloudblog-publish/images/maxresdefault_11.max-1300x1300.jpg)

Detecting a ransomware attack, stopping file upload to the cloud, and allowing a user to easily restore multiple files.

In addition, the built-in virus detection in Drive, as well as in Gmail and Chrome, helps to prevent ransomware from spreading to other devices with the aim of taking over an entire network. As a result, these defenses can help organizations in industries such as healthcare, retail, education, manufacturing, and government from being disrupted by the types of ransomware attacks that have been so destructive up to this point.

### How it works

[Drive for desktop](https://support.google.com/drive/answer/10838124), available on Windows and macOS, is used to efficiently and securely sync user files and documents to the cloud. It can be also used as a critical line of defense against malware and ransomware attacks. With that in mind, we’ve built a specialized AI model, trained on millions of real-world ransomware samples, to look for signals that a file has been maliciously modified. The detection engine adapts to novel ransomware by continuously analyzing file changes and incorporating new threat intelligence from VirusTotal. When Drive detects unusual activity that suggests a ransomware attack, it automatically pauses syncing of affected files, helping to prevent widespread data corruption across an organization’s Drive and the disruption of work.

Users then receive an alert on their desktop and via email, guiding them to restore their files. Unlike traditional solutions that require complex re-imaging or costly third-party tools, the intuitive web interface in Drive allows users to easily restore multiple files to a previous, healthy state with just a few clicks. This rapid recovery capability helps to minimize user interruption and data loss, even when using traditional software such as Microsoft Windows and Office.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Rewind_UI_in_Drive.max-2200x2200.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/Rewind_UI_in_Drive.max-2200x2200.png)

![https://storage.googleapis.com/gweb-cloudblog-publish/images/Rewind_UI_in_Drive.max-2200x2200.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/Rewind_UI_in_Drive.max-2200x2200.png)

Users can easily restore multiple files to a previous, healthy state with Google Drive.

For IT teams, administrators maintain the visibility and control they need by receiving alerts in the Admin console for detected ransomware activity. Administrators can leverage the [security center](https://support.google.com/a/answer/7492003?hl=en) to review the audit log with detailed information. This new capability is on by default for all customers, but administrators have the controls to disable detection and restoration capabilities for end users, if needed. As a reminder, Google [does not](https://cloud.google.com/privacy) use customer data, including prompts and generated outputs, for advertising purposes or to train or fine-tune any of its generative AI models without customer permission or instruction.

![https://storage.googleapis.com/gweb-cloudblog-publish/images/unnamed_19_ZXhuUv5.max-1600x1600.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/unnamed_19_ZXhuUv5.max-1600x1600.png)

![https://storage.googleapis.com/gweb-cloudblog-publish/images/unnamed_19_ZXhuUv5.max-1600x1600.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/unnamed_19_ZXhuUv5.max-1600x1600.png)

An alert in the Admin console showing a notification for detected ransomware.

“By seamlessly integrating AI-powered ransomware detection and restore capabilities into Drive, Google is helping organizations with an innovative way to avoid an increasingly common and increasingly dangerous threat while also giving end users the ability to continue working. This is great not only for Google Workspace users but individuals and companies who may use other office productivity suites as well” – **Bob O'Donnell**, **President and Chief Analyst**, **TECHnalysis Research**

### Next steps

Starting today, this capability is rolling out in an open beta and is one of the many enterprise-grade security controls in Drive that provide robust protection of sensitive data and business continuity for organizations of all sizes. Ransomware detection, alerting, and file restoration capabilities are included in most Workspace commercial plans at no additional cost. Consumer users also benefit from the file restoration capability at no additional cost. [Learn more](https://support.google.com/drive/answer/16482799) about these new capabilities and [download Drive for desktop](https://support.google.com/a/users/answer/13022292) today.

Posted in

- [Product Announcements](https://workspace.google.com/blog/product-announcements)
- [Identity and Security](https://workspace.google.com/blog/identity-and-security)

##### Related articles

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/GWS_Image_Repository_Workspace_Drops_Blog_He.max-700x700.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/GWS_Image_Repository_Workspace_Drops_Blog_He.max-700x700.png)

Product Announcements

### May Workspace Drops: Turn raw data into tables, create new AI voiceovers, and customize your AI meeting notes

By The Google Workspace Team • 4-minute read](https://workspace.google.com/blog/product-announcements/may-workspace-drops)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/26765_Blog_2_Recap_Hero_2436x1200-1x.max-700x700.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/26765_Blog_2_Recap_Hero_2436x1200-1x.max-700x700.png)

Product Announcements

### 10 more announcements from Google Workspace at Cloud Next ‘26

By Yulie Kwon Kim • 5-minute read](https://workspace.google.com/blog/product-announcements/10-more-announcements-workspace-at-next-2026)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/26765_Blog_1_Workspace_Intelligence_Hero_243.max-700x700.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/26765_Blog_1_Workspace_Intelligence_Hero_243.max-700x700.png)

Product Announcements

### Introducing Workspace Intelligence

By Yulie Kwon Kim • 5-minute read](https://workspace.google.com/blog/product-announcements/introducing-workspace-intelligence)

[![https://storage.googleapis.com/gweb-cloudblog-publish/images/Workspace_drops_hero_image.max-1300x1300_1.max-700x700.png](https://storage.googleapis.com/gweb-cloudblog-publish/images/Workspace_drops_hero_image.max-1300x1300_1.max-700x700.png)

Product Announcements

### Workspace Drop: New easy ways to create and share videos with AI in Google Vids

By The Google Workspace Team • 3-minute read](https://workspace.google.com/blog/product-announcements/workspace-drops-create-and-share-videos-with-ai-in-google-vids)
