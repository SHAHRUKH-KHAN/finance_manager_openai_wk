Financial Manager — Agentic Workflow (OpenAI Agents)

This repository contains a fully working Agentic Workflow built using the OpenAI Agents platform.

It demonstrates how multiple autonomous agents can collaborate to perform financial research, market sentiment analysis, and risk evaluation for any public company—powered by real-time web search.

The workflow automatically:

Searches the web for the latest trending news about a company.

Extracts financial data and evaluates sentiment.

Routes the output to one of two agents:

Risk Manager → when the news is negative.

Growth Analyst → when the news is positive or stable.

Returns a clean, human-readable memo summarizing the final investment outlook.

🚀 Features

Web-powered financial researcher agent: Accesses real-time data.

Conditional logic routing: Intelligently switches between risk vs. growth analysis.

Three-agent collaborative workflow: Demonstrates multi-agent orchestration.

Structured Pydantic output schemas: Ensures reliable data parsing.

Reusable async run_workflow() entrypoint: Easy to integrate into larger apps.

Perfect for demos, education, or extending into full financial AI tools.

🧠 How It Works

The workflow uses three agents coordinated by conditional logic.

graph TD
    Start[User Input: 'Analyze Company X'] --> Researcher(📰 News Researcher)
    Researcher --> Decision{High Risk Flagged?}
    Decision -- Yes --> Risk(⚠️ Risk Manager)
    Decision -- No --> Growth(📈 Growth Analyst)
    Risk --> Output[Final Investment Memo]
    Growth --> Output


The Agents

📰 News Researcher

Searches the web for the top trending news & latest earnings for the given company.

Outputs: Structured JSON including market sentiment, summary bullet points, financial metrics (Revenue, EPS, etc.), and a high_risk boolean flag.

⚠️ Risk Manager

Trigger: Activated if high_risk=True.

Action: Generates a Risk Alert Memo summarizing potential downsides, market volatility, and bearish signals.

📈 Growth Analyst

Trigger: Activated if the company appears stable or positive.

Action: Writes a Growth Opportunity Summary highlighting upside potential and bullish indicators.

📂 Repository Structure

/ (root)
│── main.py        # Complete agentic workflow (entrypoint)
│── README.md      # Documentation
│── requirements.txt (optional)


Future expansions could include example_requests/, utils/, and deployment/ folders.

📦 Requirements

Python 3.10+

OpenAI Agents SDK

Pydantic 2.x

To install dependencies (once you generate your requirements file):

pip install -r requirements.txt


▶️ Running the Workflow

You can import the workflow entrypoint into your application or run it directly.

from main import run_workflow, WorkflowInput
import asyncio

async def test():
    # Example: Analyze a specific stock
    input_data = WorkflowInput(input_as_text="Analyze Tesla stock")
    
    print(f"Starting analysis for: {input_data.input_as_text}...")
    result = await run_workflow(input_data)
    
    print("\n--- Final Analysis Result ---")
    print(result)

if __name__ == "__main__":
    asyncio.run(test())


⭐ Why This Exists

This project demonstrates how Agentic Workflows aren’t some abstract buzzword — they’re simply the digital equivalent of a coordinated team:

A Researcher who gathers facts.

A Risk Expert who evaluates threats.

A Growth Analyst who identifies opportunities.

This workflow shows how easy it is to automate such multi-step analysis with OpenAI’s Agent Builder, moving beyond simple chatbots to complex, logical task execution.

🤝 Contributing

Feel free to fork this repo, open issues, or submit PRs. If you build new agents (valuation agents, portfolio advisors, risk calculators), you can plug them right into the logic flow in main.py.
