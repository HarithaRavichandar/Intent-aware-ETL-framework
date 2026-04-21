import requests
import json
from app.ai.qa import ask_question

def generate_insights(summary, intent):

    prompt = f"""
You are a senior business data analyst.

Analyze the dataset summary below and generate clear, executive-level insights.

Dataset Summary:
{json.dumps(summary, indent=2)}

Context: The data is being processed under intent = {intent}

Your response MUST include:
- Key Business Observations
- Trend Analysis
- Risks / Red Flags
- Opportunities / Recommendations
- 1-2 KPI style statements

Be concise but insightful.
"""

    return ask_question(summary, prompt)
