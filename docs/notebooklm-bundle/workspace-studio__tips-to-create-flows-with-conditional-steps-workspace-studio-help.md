# Tips to create flows with conditional steps - Workspace Studio Help

**Product Area:** workspace-studio
**Source:** https://support.google.com/workspace-studio/answer/16431010?hl=en

# Tips to Create Flows with Conditional Steps — Google Workspace Studio

**Source:** [Workspace Studio Help](https://support.google.com/workspace-studio/answer/16431010?hl=en)  
**Topic:** Using conditional logic in Google Workspace Studio flows so certain steps run only when specified conditions are met.

---

## Key Excerpts

> “In Google Workspace Studio, you can have certain steps in your flows happen only if certain conditions are met.”

> “Conditional steps set off certain steps into substeps that the flow does only in certain scenarios.”

Workspace Studio supports **2 steps** for checking conditions:

- **Decide** – uses Gemini to evaluate if conditions you describe are true or false
- **Check if** – compares values

Important limitations:

> “You can’t use variables from a substeps in steps in the main flow.”

> “An flow can’t have nested conditional steps. But a flow can have more than one conditional step, they just run in order.”

Gemini availability note:

> “The Decide step is only available if you have access to Gemini. If you don’t have Gemini, use Check if instead.”

---

## Overview: How Conditional Steps Work

Conditional steps let a flow run certain **substeps** only in specific situations.

You can add conditional logic in two ways:

- **Describe conditions when creating a flow with AI**
- **Manually add conditional steps** to an existing or new flow

After adding a conditional step, you add the actions that should happen inside its **substeps**. You can also add regular steps after the conditional section; those top-level steps run for all flow runs.

---

## Conditional Flow Limitations

### 1. Substep variables cannot be used in the main flow

Variables created inside conditional substeps are not available to later top-level steps.

Example:

- A conditional substep uses **Ask Gemini** to draft a reply.
- The main flow cannot later add that draft to a tracking document.

### 2. No nested conditional steps

A flow cannot place one conditional step inside another conditional section.

However:

- A flow **can have multiple conditional steps**
- They run sequentially, in order

---

# AI-Powered Conditions with **Decide**

## What “Decide” Does

**Decide** uses Gemini to evaluate natural-language conditions and return a true/false result.

How it works:

- You tell Gemini what conditions to check.
- Gemini determines whether the conditions are **true** or **false**.
- A **Decide** step is automatically paired with a **Check if** step.
- The paired **Check if** step is prefilled to check whether the **Decide** result is **true**.
- You can change the paired **Check if** step so substeps run when the result is **false** instead.
- The flow runs the substeps only if the paired **Check if** condition matches.
- Any other main-flow steps after the condition still run afterward.

---

## Set Up a **Decide** Step

1. Go to [https://studio.workspace.google.com](https://studio.workspace.google.com/) and create a flow.
2. If building manually, or if Gemini did not add it automatically, add a **Decide** step.
   - A **Check if** step is automatically added with it.
3. In the **Decide** step, describe the conditions Gemini should evaluate.

### Tips for describing Decide conditions

- **Start from a common use case**
  - Click one of the suggested options below the field, such as **Is urgent**, to begin the condition description.
- **Add variables**
  - Use variables from previous steps to give Gemini context.
  - Example: Add the email message body variable so Gemini can check whether it has a negative tone.

---

## Run Substeps When Decide Is False

To make the substeps run only when the **Decide** condition is **not met**:

1. Click the paired **Check if** step.
2. Change the matching condition from **is true** to **is false**.

---

## Add Conditional Actions

Below the **Check if** step:

- Add or edit the steps you want the flow to run when the condition matches.
- You **cannot** add another **Check if** step inside these substeps.

Optional:

- Add more top-level steps after the conditional section if they should run for all flow executions.
- Remember: those top-level steps **cannot use variables from the substeps**.

---

## Tip: Handle the Opposite Condition

> “To have the flow do steps for the opposite condition, add another Check if step with the matching set to the opposite of the first.”

Example:

- First conditional branch: run substeps when the decision is **true**
- Second conditional branch: run different substeps when the decision is **false**

---

## Test and Turn On a Decide-Based Flow

Optional testing:

1. Click **Test run**.
2. Select the starting conditions.
3. Click **Start**.

Important:

> “A test run runs your flow once, taking real actions so you can see the outcome.”

When ready:

- Click **Turn on**.

---

# Condition Matching with **Check if**

## What “Check if” Does

**Check if** compares values from the flow against specified conditions.

How it works:

- You 

[... summary truncated for context management ...]
