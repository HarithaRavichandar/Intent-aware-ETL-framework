# Intent-Aware ETL Orchestration Framework for Multi-Use-Case Data Engineering (Reporting, Machine Learning and Compliance)

An intelligent, modular data processing system that routes incoming data through different pipelines based on detected user intent. This application provides a web interface for uploading datasets and processing them according to specific business goals (reporting, ML training, compliance, or research).

## Overview

The Intent-Aware Data Pipeline is built to handle diverse data processing requirements in a unified framework. It intelligently detects the user's intent and applies the appropriate transformation, validation, and storage strategy.

**Key Capabilities:**
- **Intent Detection**: Automatically identifies and validates user intent (Reporting, ML Training, Compliance, Research)
- **Multi-Pipeline Processing**: Routes data through intent-specific pipelines
- **Intelligent Summarization**: Generates dataset summaries and insights using AI
- **Data Security**: Supports compliance-aware storage with raw data preservation
- **Interactive Q&A**: Ask questions about processed data using AI-powered chatbot
- **Comprehensive Logging**: Tracks all pipeline executions with detailed run information
- **Multiple Output Destinations**: Writes processed data to warehouse, feature store, secure storage, or research outputs

## Project Structure

```
Intent_Aware_Pipeline/
├── run.py                          # Flask application entry point
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── app/                           # Main application package
│   ├── __init__.py               # Flask app factory
│   ├── routes.py                 # API endpoints
│   │
│   ├── ai/                       # AI & Insights module
│   │   ├── insights.py           # Generate data insights
│   │   └── qa.py                 # Q&A chatbot functionality
│   │
│   ├── config/                   # Configuration files
│   │   └── intent_rules.yaml     # Intent-specific processing rules
│   │
│   ├── ingestion/                # Data loading module
│   │   └── loader.py             # Dataset loading from CSV/Excel
│   │
│   ├── intent_detector/          # Intent detection module
│   │   └── detector.py           # Intent validation and detection
│   │
│   ├── orchestrator/             # Pipeline orchestration
│   │   └── engine.py             # Main pipeline execution engine
│   │
│   ├── pipelines/                # Intent-specific pipelines
│   │   ├── compliance_pipeline.py   # Compliance data processing
│   │   ├── ml_pipeline.py           # ML training data preparation
│   │   ├── reporting_pipeline.py    # Reporting data aggregation
│   │   └── research_pipeline.py     # Research data analysis
│   │
│   ├── storage/                  # Data storage/writing module
│   │   ├── database.py           # Database operations
│   │   ├── feature_store_writer.py  # Feature store output
│   │   ├── secure_store_writer.py   # Secure/compliance storage
│   │   └── warehouse_writer.py      # Data warehouse output
│   │
│   ├── utils/                    # Utility functions
│   │   ├── cleaning.py           # Data cleaning operations
│   │   ├── fs.py                 # File system utilities
│   │   ├── logger.py             # Logging configuration
│   │   ├── privacy.py            # Privacy/PII handling
│   │   ├── schema_mapper.py      # Schema mapping utilities
│   │   ├── summarize.py          # Dataset summarization
│   │   └── validation.py         # Data validation rules
│   │
│   └── static/                   # Frontend web interface
│       ├── index.html            # Main HTML page
│       ├── script.js             # Frontend JavaScript logic
│       └── styles.css            # Frontend styling
│
├── uploads/                      # User-uploaded files directory
├── outputs/                      # Processing outputs directory
│   ├── feature_store/            # ML feature store outputs
│   ├── research/                 # Research pipeline outputs
│   ├── secure_raw/               # Compliance/secure storage outputs
│   └── warehouse/                # Data warehouse outputs
│
├── logs/                         # Application logs
└── venv/                         # Python virtual environment
```

## Features

### 1. Intent Detection
The system supports four primary intents:
- **REPORTING**: For business intelligence and reporting use cases
- **ML_TRAINING**: For machine learning model training and feature engineering
- **COMPLIANCE**: For compliance and regulatory data handling
- **RESEARCH**: For research and exploratory data analysis

### 2. Intelligent Data Routing
Each intent routes data through a specialized pipeline:
- Data validation and schema mapping
- Intent-specific transformations
- Privacy and compliance checks
- Optimized data storage

### 3. AI-Powered Features
- **Insights Generation**: Automatic extraction of key insights from data
- **Interactive Q&A**: Ask natural language questions about processed datasets
- **Data Summarization**: Comprehensive dataset statistics and summaries

### 4. Data Security & Privacy
- Secure raw data preservation for compliance
- Privacy-aware data cleaning and anonymization
- PII detection and handling
- Compliance-focused storage options

### 5. Comprehensive Logging
- Run tracking with unique run IDs
- Detailed execution logs
- Success/failure status recording
- Performance metrics

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Setup Steps

1. **Clone/Download the repository**
```bash
cd Intent_Aware_Pipeline
```

2. **Create and activate a virtual environment**
```bash
# On Windows
python -m venv venv
venv\Scripts\Activate.ps1

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Verify installation**
```bash
python run.py
```

The application should start on `http://localhost:5000`

## Usage

### Running the Application

```bash
python run.py
```

The Flask application will start in debug mode on `http://0.0.0.0:5000`

### Web Interface

1. **Navigate to**: `http://localhost:5000`
2. **Upload a file**: 
   - Select a CSV or Excel file
   - Choose an intent (Reporting, ML Training, Compliance, or Research)
   - Click "Upload"
3. **View Results**: The system processes the file and displays the summary
4. **Ask Questions**: Use the chatbot to ask questions about your data

### API Endpoints

#### Upload and Process Data
```
POST /upload
```

**Request:**
```
Content-Type: multipart/form-data

Parameters:
- file: (file) CSV or Excel file
- intent: (string) One of: reporting, ml_training, compliance, research
```

**Response:**
```json
{
  "run_id": "20250128_150230_REPORTING",
  "intent": "REPORTING",
  "status": "success",
  "row_count": 1250,
  "column_count": 15,
  "summary": {...},
  "insights": [...]
}
```

#### Ask Question (Q&A)
```
POST /ask
```

**Request:**
```json
{
  "summary": "Dataset summary from previous upload",
  "question": "What is the average transaction amount?"
}
```

**Response:**
```json
{
  "answer": "The average transaction amount is $2,450.75"
}
```

## Configuration

### Intent Rules (intent_rules.yaml)

The `app/config/intent_rules.yaml` file defines processing rules for each intent:

```yaml
REPORTING:
  # Reporting-specific rules
  data_cleaning: true
  aggregation_level: daily
  output_format: csv

ML_TRAINING:
  # ML-specific rules
  feature_engineering: true
  train_test_split: 0.8
  output_format: parquet

COMPLIANCE:
  # Compliance-specific rules
  preserve_raw: true
  pii_detection: true
  output_format: csv

RESEARCH:
  # Research-specific rules
  data_exploration: true
  statistical_analysis: true
  output_format: csv
```

## Output Locations

The system generates outputs in specialized directories:

| Intent | Output Location | Purpose |
|--------|-----------------|---------|
| REPORTING | `outputs/warehouse/` | Data warehouse for BI |
| ML_TRAINING | `outputs/feature_store/` | Feature store for ML models |
| COMPLIANCE | `outputs/secure_raw/` | Secure storage with raw data |
| RESEARCH | `outputs/research/` | Research analysis outputs |

## Data Processing Pipeline

```
1. User Upload
   ↓
2. File Storage (uploads/)
   ↓
3. Intent Detection
   ↓
4. Configuration Loading
   ↓
5. Data Ingestion (Load CSV/Excel)
   ↓
6. Data Validation & Schema Mapping
   ↓
7. Intent-Specific Pipeline Execution
   ├─ Reporting Pipeline → Warehouse Output
   ├─ ML Pipeline → Feature Store Output
   ├─ Compliance Pipeline → Secure Output
   └─ Research Pipeline → Research Output
   ↓
8. Data Summarization
   ↓
9. Insights Generation
   ↓
10. Run Logging & Completion
```

## Dependencies

- **Flask**: Web framework for API and UI
- **Pandas**: Data manipulation and analysis
- **PyYAML**: YAML configuration parsing
- **python-dotenv**: Environment variable management
- **openpyxl**: Excel file support
- **requests**: HTTP client library

See `requirements.txt` for complete list and versions.

## Logging

All pipeline executions are logged to the `logs/` directory with the following information:

- Run ID
- Intent type
- Start/end timestamps
- Input file path
- Row/column counts
- Processing status (success/failure)
- Error messages (if any)

## Error Handling

The system includes comprehensive error handling:

- **Invalid Intent**: Returns error if intent is not recognized
- **File Format**: Validates CSV/Excel file format
- **Schema Errors**: Handles missing columns or type mismatches
- **Processing Errors**: Logs and returns detailed error messages
- **Storage Errors**: Handles output directory creation and write failures

## Security & Privacy

- **PII Detection**: Identifies and handles personally identifiable information
- **Data Validation**: Validates all incoming data against schemas
- **Access Control**: Ensures compliance-specific data isolation
- **Audit Logging**: Maintains detailed logs of all data access and modifications

## Troubleshooting

### Application won't start
```bash
# Ensure virtual environment is activated
venv\Scripts\Activate.ps1

# Check Python version
python --version  # Should be 3.7+

# Reinstall dependencies
pip install -r requirements.txt
```

### Port 5000 already in use
```bash
# Change port in run.py:
app.run(host="0.0.0.0", port=5001, debug=True)
```

### File upload fails
- Ensure file is CSV or Excel format
- Check file permissions
- Verify `uploads/` directory exists

### Pipeline errors
- Check logs in `logs/` directory
- Verify intent parameter is correct (reporting, ml_training, compliance, research)
- Ensure input file matches expected schema

## Development

### Adding a New Intent Pipeline

1. Create new pipeline in `app/pipelines/` (e.g., `custom_pipeline.py`)
2. Add intent rules to `app/config/intent_rules.yaml`
3. Update `app/orchestrator/engine.py` to import and use the pipeline
4. Update `app/intent_detector/detector.py` with new intent

### Extending the AI Module

Add new AI features to `app/ai/insights.py` or create new modules in `app/ai/`

### Customizing Storage

Modify storage writers in `app/storage/` to change output formats or locations

## Performance

- **Data Loading**: Optimized for files up to 1GB
- **Processing**: Parallelized where possible
- **Storage**: Efficient write operations with indexing support
- **Logging**: Asynchronous to avoid blocking

## Future Enhancements

- [ ] Real-time data streaming support
- [ ] Advanced ML model integration
- [ ] Dashboard for pipeline monitoring
- [ ] Data quality metrics and reporting
- [ ] Support for additional data formats (JSON, Parquet)
- [ ] User authentication and authorization
- [ ] Multi-file batch processing
- [ ] Advanced data governance features

## License

[Add your license here]

## Support & Contact

For issues, questions, or suggestions:
- Check the troubleshooting section above
- Review logs in `logs/` directory
- Contact the development team

## Contributing

Contributions are welcome! Please:
1. Create a feature branch
2. Make your changes
3. Add tests for new functionality
4. Submit a pull request

---

**Last Updated**: January 2026  
**Version**: 1.0.0
