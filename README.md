# CV and Cover Letter for EA Senior Product Manager Application

## Overview
This folder contains the customized CV and cover letter for Abdelrahmane Ferchichi's application to the Senior Product Manager role at EA's Creative Innovation team.

## Files
- `application/senior_pm.html`: HTML version of the CV
- `application/senior_pm.pdf`: PDF version of the CV
- `application/cover_letter.html`: HTML version of the cover letter
- `application/cover_letter.pdf`: PDF version of the cover letter
- `generate_pdf.py`: Python script to generate PDFs from HTML using Playwright

## Context for AI Assistant
When this folder is open, the AI should be aware of the following:

### Recent Edits and Customizations
- **CV Updates**: Experience sections rewritten for distinct wording, bold keywords (e.g., OKRs, UX/UI, AIoT), added Hobbies section, compact sidebar, smaller chips, modern font (Poppins).
- **Cover Letter Updates**: Content refined, justified text, centered layout, modern font, removed repetitions, generalized company mentions.
- **PDF Generation**: All changes regenerated to PDF using `python generate_pdf.py <html_file> <pdf_file>`.

### Key Features
- Responsive design with print media queries for PDF export.
- ATS-friendly keywords in hidden div.
- Professional styling inspired by tech/gaming industry.

### Instructions for AI
- If user requests edits to CV or cover letter, use `replace_string_in_file` on the HTML files, then run PDF generation.
- Maintain bold formatting for keywords in experience sections.
- Ensure PDFs are up-to-date after changes.
- Use modern, clean fonts and layouts suitable for creative/tech roles.

### Todo
- [x] Customize CV for EA application
- [x] Create matching cover letter
- [x] Generate final PDFs

If further customizations are needed, proceed with edits and PDF regeneration.