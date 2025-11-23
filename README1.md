Financial Manager — Agentic Workflow (OpenAI Agents)

This repository contains a fully working Agentic Workflow built using the OpenAI Agents platform.
It demonstrates how multiple autonomous agents can collaborate to perform financial research, market sentiment analysis, and risk evaluation for any public company—powered by real-time web search.

The workflow automatically:

-- Searches the web for the latest trending news about a company
-- Extracts financial data and evaluates sentiment
-- Routes the output to one of two agents:
-- -- Risk Manager → when the news is negative
-- -- Growth Analyst → when the news is positive or stable
Returns a clean, human-readable memo summarising the final investment outlook.

It’s a simple example, but it shows how powerful agentic workflows can become when chained logically—almost like having your own mini research team on demand.

- Features
-- Web-powered financial researcher agent
-- Conditional logic routing (risk vs growth)
-- Three-agent collaborative workflow
-- Structured Pydantic output schemas
-- Reusable async run_workflow() entrypoint
-- Perfect for demos, education, or extending into full financial AI tools

- How It Works
The workflow uses three agents:

📰 News Researcher
Searches the web for the top trending news & latest earnings for the given company.
Outputs structured JSON, including:
-- Market sentiment
-- Summary bullet points
-- Financial metrics (Revenue, EPS, etc.)
-- High-risk boolean flag

⚠️ Risk Manager
If the researcher flags high_risk=True, this agent generates a Risk Alert Memo summarising the potential downsides.

📈 Growth Analyst
If the company appears stable or positive, this agent writes a Growth Opportunity Summary.
Routing between these agents happens automatically based on the sentiment extracted from real-time data.

If the company appears stable or positive, this agent writes a Growth Opportunity Summary.

Routing between these agents happens automatically based on the sentiment extracted from real-time data.
