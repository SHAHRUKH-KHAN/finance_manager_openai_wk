from agents import WebSearchTool, RunContextWrapper, Agent, ModelSettings, TResponseInputItem, Runner, RunConfig, trace
from pydantic import BaseModel

# Tool definitions
web_search_preview = WebSearchTool(
  search_context_size="medium",
  user_location={
    "type": "approximate"
  }
)
class NewsResearcherSchema__SummaryPointsItem(BaseModel):
  headline: str
  detail: str


class NewsResearcherSchema__Financials(BaseModel):
  revenue: float
  net_income: float
  eps: float
  guidance: str


class NewsResearcherSchema(BaseModel):
  high_risk: bool
  label: str
  company_name: str
  ticker: str
  quarter: str
  date: str
  summary_points: list[NewsResearcherSchema__SummaryPointsItem]
  financials: NewsResearcherSchema__Financials


class NewsResearcherContext:
  def __init__(self, workflow_input_as_text: str):
    self.workflow_input_as_text = workflow_input_as_text
def news_researcher_instructions(run_context: RunContextWrapper[NewsResearcherContext], _agent: Agent[NewsResearcherContext]):
  workflow_input_as_text = run_context.context.workflow_input_as_text
  return f"""You are a financial researcher. Take the {workflow_input_as_text}. Search the web for the top 3 trending stories about this company from the last 24 hours. Focus on market sentiment. 
Also, search the web for the earnings for it."""
news_researcher = Agent(
  name="News Researcher",
  instructions=news_researcher_instructions,
  model="gpt-4o",
  tools=[
    web_search_preview
  ],
  output_type=NewsResearcherSchema,
  model_settings=ModelSettings(
    temperature=1,
    top_p=1,
    max_tokens=2048,
    store=True
  )
)


risk_manager = Agent(
  name="Risk Manager",
  instructions="The news is negative. Write a short 'Risk Alert' memo. List the potential downsides and advise caution.",
  model="gpt-4.1",
  model_settings=ModelSettings(
    temperature=1,
    top_p=1,
    max_tokens=2048,
    store=True
  )
)


growth_analyst = Agent(
  name="Growth Analyst",
  instructions="The news is stable or good. Write a 'Growth Opportunity' summary highlighting the key bullish drivers.",
  model="gpt-4.1",
  model_settings=ModelSettings(
    temperature=1,
    top_p=1,
    max_tokens=2048,
    store=True
  )
)


class WorkflowInput(BaseModel):
  input_as_text: str


# Main code entrypoint
async def run_workflow(workflow_input: WorkflowInput):
  with trace("Finance Manager"):
    state = {

    }
    workflow = workflow_input.model_dump()
    conversation_history: list[TResponseInputItem] = [
      {
        "role": "user",
        "content": [
          {
            "type": "input_text",
            "text": workflow["input_as_text"]
          }
        ]
      }
    ]
    news_researcher_result_temp = await Runner.run(
      news_researcher,
      input=[
        *conversation_history
      ],
      run_config=RunConfig(trace_metadata={
        "__trace_source__": "agent-builder",
        "workflow_id": "wf_6921b49202fc8190a2c235b8066bc3650e7c64346f1098c1"
      }),
      context=NewsResearcherContext(workflow_input_as_text=workflow["input_as_text"])
    )

    conversation_history.extend([item.to_input_item() for item in news_researcher_result_temp.new_items])

    news_researcher_result = {
      "output_text": news_researcher_result_temp.final_output.json(),
      "output_parsed": news_researcher_result_temp.final_output.model_dump()
    }
    if news_researcher_result["output_parsed"]["high_risk"]:
      risk_manager_result_temp = await Runner.run(
        risk_manager,
        input=[
          *conversation_history
        ],
        run_config=RunConfig(trace_metadata={
          "__trace_source__": "agent-builder",
          "workflow_id": "wf_6921b49202fc8190a2c235b8066bc3650e7c64346f1098c1"
        })
      )

      conversation_history.extend([item.to_input_item() for item in risk_manager_result_temp.new_items])

      risk_manager_result = {
        "output_text": risk_manager_result_temp.final_output_as(str)
      }
      return risk_manager_result
    else:
      growth_analyst_result_temp = await Runner.run(
        growth_analyst,
        input=[
          *conversation_history
        ],
        run_config=RunConfig(trace_metadata={
          "__trace_source__": "agent-builder",
          "workflow_id": "wf_6921b49202fc8190a2c235b8066bc3650e7c64346f1098c1"
        })
      )

      conversation_history.extend([item.to_input_item() for item in growth_analyst_result_temp.new_items])

      growth_analyst_result = {
        "output_text": growth_analyst_result_temp.final_output_as(str)
      }
      return growth_analyst_result
