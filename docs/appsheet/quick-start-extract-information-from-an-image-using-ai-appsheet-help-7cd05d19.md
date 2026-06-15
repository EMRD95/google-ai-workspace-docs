---
title: "Quick start: Extract information from an image using AI - AppSheet Help"
source_url: "https://support.google.com/appsheet/answer/15985259"
product_area: "appsheet"
retrieved_at: "2026-06-15T12:26:01Z"
extraction_method: "web_extract"
---

# Quick Start: Extract Information from an Image Using AI – AppSheet Help

**Scenario**: A car dealership owner wants to automatically populate inventory fields (make, model, color, year, description) by uploading a photo. The built automation uses an AI task to extract data and save it to an AppSheet database.

> See also the [Car identification with Gemini sample app](https://www.appsheet.com//template/showdef?appId=CarIdentificationwithGemini-2078346&quickStart=False) for a more comprehensive scenario.

---

## High‑Level Process

1. Create an AppSheet database with the required columns.
2. Generate an app from that database.
3. Build a bot with an **Extract** AI task to pull info from the uploaded image.
4. Simplify the input form so users only see the photo upload field.
5. Test the automation by uploading a car photo in the app preview.

---

## Step‑by‑Step Details

### 1. Create an AppSheet Database

- **Database name**: `Car inventory`
- **Table name**: `Car inventory` (rename from `Table 1`)
- **Delete all dummy rows** before adding real data.

**Columns to edit/add**:

| Original/New Column | Final Name | Type / Config                                                                 |
|---------------------|------------|-------------------------------------------------------------------------------|
| `Title`             | `Make`    | Text (rename only)                                                           |
| `Assignee`          | `Model`   | Type **Name** (or Text)                                                      |
| `Status`            | `Color`   | Enum (dropdown) with options:<br>White, Green, Yellow, Orange, Red, Blue, Silver, Black, **Other** (catch‑all)<br>Assign a color swatch to each. |
| `Date`              | `Year`    | **Number** (no thousands separator)                                          |
| (new)               | `Description` | Text                                                                       |
| (new)               | `Car photo` | Attachments → Image                                                        |

*Careful database design is fundamental – the data structure determines the app’s behavior.*

### 2. Create an App From the Database

- In the database editor, click **Apps > New AppSheet app**.
- Rename the app to `Car inventory`.
- Open the **Data** pane: the table is linked to your AppSheet database.
- Edit the `Year` column: turn **off** “Show thousands separator” (year values don’t need formatting).

### 3. Build the Automation (Bot)

**Bot creation**:

- Go to **Automation** (left nav). Click `+` → Create a new bot.
- Rename the bot to `Update car inventory`.

**Event**:

- Click **Configure event**.
- *Event name*: `Update car inventory`
- **Condition** (to ensure an image is present):

  ```
  ISNOTBLANK([Car photo])
  ```

  *This expression prevents the bot from running unless a photo has been uploaded.*

**Step – AI extraction**:

- Click **+ Add a step** (in the bot flow).
- *Step name*: `Extract from photo`
- Configuration in the right pane:
  - **Task type**: AI task
  - **AI task**: `Extract` (extracts info from photo, PDF, or text)
  - **Input column**: `Car photo`
  - **Output**:
    - **Save to table** (enabled)
    - Map extracted data to columns: **Make**, **Model**, **Color**, **Year**, **Description** (add each in order).

**Additional instructions** (copy this text exactly):

> If not sure of Make, Model, or Year, make best guess  
> If not sure of Color, set to "Other"  
> For Description, add 2 to 3 sentences

- **Save** the app.

### 4. Customize the Input Form

- Go to **App > Views**.
- Select the system‑generated `Car inventory_Form` view.
- Set **Column order** to **Manual**.
- Remove all columns **except `Car photo`** from the column order list.
- The live preview shows a form with only the photo upload field.

### 5. Test the Automation in the App Preview

- In the app preview, click the `Car photo` field and upload a car image (from your device or internet).
- Click **Save** – AppSheet syncs and triggers the bot.
- After sync, navigate to **Car inventory** list, open the new item. The Make, Model, Color, Year, and Description fields are auto‑populated by the AI.

---

## Next Steps

- Extend the automation to **categorize the car by body style** → see [Quick start: Categorize information using AI](https://support.google.com/appsheet/answer/16338286).
- Explore more Gemini‑powered [quick starts](https://support.google.com/appsheet/answer/16045284#quick-start).
- Learn about other AppSheet features via [quick starts](https://support.google.com/appsheet/answer/13474783).

---

**Key phrases & code snippet preserved verbatim**:

- `ISNOTBLANK([Car photo])` – condition for bot event
- Additional instructions text:
  ```
  If not sure of Make, Model, or Year, make best guess
  If not sure of Color, set to "Other"
  For Description, add 2 to 3 sentences
  ```
