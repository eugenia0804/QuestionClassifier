# CCL-LLM Question Classifier

## Code Structure
```plaintext
.
├── Dataset
│   ├── BioUnitDataCoding                # Codebook Original Data File 
│   └── Questionset-TaxonomyMath         # Questions Needed to be processed
├── Results
│   └── iteration-1
│       ├── final.json                    # Combined final result
│       ├── prompts.txt                   # Prompts for each call
│       ├── raw_results.txt               # Direct LLM output for each call
│       └── results.json                  # Structured results for each call
├── llm.py                                # Python script file for language model
├── main.py                               # Entry point/main file for the project
├── prompts.py                            # Code related to generating prompts for the language model
├── analysis.py                           # Code for analyzing project results
├── support.py                            # Supporting functions/utilities
├── LICENSE                               # License information for the project
└── README.md                             # README file with project information
```

## Iterations:
- **iteration#1:** \
    model used: GPT3.5(text-davinci-003)\
    prompt composition: practice, subpractice, question, instruction\
    results: result.csv (filtered result), raw_result.txt (raw result), prompt.txt\
    packages: os, pandas, csv, openai
    
- **iteration#2:** \
    model used: GPT3.5(text-davinci-003) & PaLM-2(text-bison-001)\
    prompt composition: practice, subpractice, question, instruction\
    results: result.json (composite result), raw_result.json (raw result), prompt.txt\
    packages: os, pandas, json, langchain.llms

