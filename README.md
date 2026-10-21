# Retail Analytics Agentic AI (CrewAI)

A two-agent AI system built with [CrewAI](https://crewai.com) that turns a retail analytics report into an executive-ready email, automatically.

The crew reads a summary of my Tableau retail sales analysis, pulls out the key findings and verified numbers, and then writes and sends a professional email to leadership with findings, recommendations, and a caution about data limitations.

## How it works

**Agent 1: Retail Analytics Specialist**
- Reads the Analytics Context Summary PDF using a PDF search tool (retrieval with OpenAI embeddings)
- Extracts the 3 hypotheses and whether each was supported or contradicted
- Pulls the KPI snapshot: current-year vs. prior-year sales and percent change
- Identifies the top- and worst-performing categories and regions, plus the forecast direction
- Answers a set of strategic business questions

**Agent 2: Business Strategy Advisor & Communicator**
- Uses Agent 1's findings as context
- Drafts an executive email with 3 main findings (using real numbers), 3 actionable recommendations, and 1 caution about data limitations
- Is instructed to avoid generic advice and invented numbers
- Sends the email through a Gmail integration

The two tasks run sequentially, so the writer only works from verified findings produced by the analyst.

## Tech stack

- CrewAI (agents, tasks, sequential crew)
- OpenAI GPT-4o-mini
- CrewAI PDFSearchTool with OpenAI `text-embedding-3-small` embeddings
- Gmail integration for sending the final email
- Python, managed with uv

## Project structure

```
src/retailanalytics_agenticai_nt__online_section/
├── config/
│   ├── agents.yaml   # Agent roles, goals, and backstories
│   └── tasks.yaml    # Task descriptions and expected outputs
├── crew.py           # Agents, tools, and crew setup
└── main.py           # Inputs and entry point
```

## What I learned

- Breaking a business workflow into clear steps for multiple AI agents
- Writing specific roles, goals, and task instructions so agents stay accurate
- Guarding against AI hallucination by requiring agents to use only verified numbers
- Connecting AI agents to real tools (document search and email)

## Related work

This crew builds on my Tableau retail analysis project:
[Retail Store Sales Analysis & Financial Performance Dashboard](https://public.tableau.com/app/profile/nalani.taylor/viz/Book1_17779310475030/RetailAnalysisDashboard)

## Running it

1. Install [uv](https://docs.astral.sh/uv/) and Python 3.10–3.13
2. Add your `OPENAI_API_KEY` to a `.env` file (never commit this file)
3. Run `crewai install`, then `crewai run`

---
Built by Nalani Taylor · [LinkedIn](https://www.linkedin.com/in/nalani-taylor-ab582a316)
