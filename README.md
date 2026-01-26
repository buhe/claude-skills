## Prerequisites

- nano-banana-pro skill need `google-genai`

  ```bash
  pip install google-genai
  export GEMINI_API_KEY=AI_YOUR_KEY
  ```
- blog-deploy skill need `vercel` cli
  ```bash
  yarn global add vercel@latest

  vercel login --github

  vercel switch
  vercel project ls

  ```
- A working shell (macOS, Linux, or Windows WSL) with network access.

## nano-banana-pro

Use the `nano-banana-pro` model to generate images.

## magic-note

Magic Note is an intelligent note-taking and query system with built-in relationship visualization. Capture your thoughts with a simple syntax
and Let the system automatically extract and organize metadata.

### Quick Syntax
save/content ［#tag］ ［$feeling］ ［@person］ ［&todo］

### Features
- Tags （#tag）- Categorize notes （uses existing - Feelings （$feel）- Track your emotional state
- Mentions（@who）- Reference people or things - Todos（&）- Mark actionable items tags）

### Examples
save Need to review Apple's earnings today #stock $excited
record Meeting with @john about project planning &

### Query & Visualize 2
- review notes from past X days - Notes with feelings/mentions
- ｛tag｝ notes from past X months - Filter by tag with relationship graph
- ｛feel｝ notes - Filter by emotion unstal DB4S

taessystem automaticacey tdenttfues Telattonsnups petween notes and generates AseL network Vtsuatzattons Snowung now your Ldeas connect ove time.