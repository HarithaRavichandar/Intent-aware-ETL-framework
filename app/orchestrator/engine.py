import yaml
from app.intent_detector.detector import detect_intent
from app.ingestion.loader import load_dataset
from app.pipelines.reporting_pipeline import reporting_flow
from app.pipelines.ml_pipeline import ml_flow
from app.pipelines.compliance_pipeline import compliance_flow
from app.pipelines.research_pipeline import research_flow
from app.utils.logger import start_run, end_run, fail_run
from app.utils.summarize import summarize_dataset
from app.ai.insights import generate_insights


CONFIG = "app/config/intent_rules.yaml"


def load_rules(intent):
    with open(CONFIG) as f:
        cfg = yaml.safe_load(f)

    if intent not in cfg:
        raise ValueError(f"Unsupported intent: {intent}")

    return cfg[intent]


def run_pipeline(path, intent):

    intent = detect_intent(intent)
    rules = load_rules(intent)

    run_id, start_time = start_run(intent, path)

    try:
        # LOAD RAW DATA 
        df = load_dataset(path)

        # SUMMARIZE RAW DATA 
        raw_summary = summarize_dataset(df)

        # RUN PIPELINE 
        if intent == "REPORTING":
            processed_df, rows = reporting_flow(df, rules)

        elif intent == "ML_TRAINING":
            processed_df, rows = ml_flow(df, rules)

        elif intent == "COMPLIANCE":
            processed_df, rows = compliance_flow(df, rules)

            end_run(run_id, rows, start_time)

            return {
                "status": "success",
                "intent": intent,
                "rows": rows,
                "summary": raw_summary,
                "insights": "AI insights disabled for compliance mode."
            }

        elif intent == "RESEARCH":
            processed_df, rows = research_flow(df, rules)

        else:
            raise ValueError("Unknown intent")

        # AI INSIGHTS FROM RAW DATA 
        try:
            insights = generate_insights(raw_summary, intent)
        except Exception:
            insights = "AI insights unavailable at the moment."

        end_run(run_id, rows, start_time)

        return {
            "status": "success",
            "intent": intent,
            "rows": rows,
            "summary": raw_summary,
            "insights": insights
        }

    except Exception as e:
        fail_run(run_id, str(e))
        raise e
