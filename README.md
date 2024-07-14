# LLM Experiment Datastore
Welcome to our dedicated repository, which contains all data related to our experiment. For the duration of the peer-review process, this repository will remain private and managed under strict anonymity. Access is strictly limited to authorized reviewers. We anticipate making this repository public to facilitate broader access and collaboration once the peer-review process has been successfully completed.

## Contents

### 1. [Dataset](./Dataset/README.md)

This `Dataset` folder contains two key files essential for our experiment:

- [**Forest_dataset.ttl**](./Dataset/Forest_dataset.ttl): This dataset, which has been uploaded to a private SPARQL endpoint, contains comprehensive data used throughout our research.

- [**dataDefinitions.ttl**](./Dataset/dataDefinitions.ttl): This is a concise file that includes data definitions relevant to our study. It encompasses the naming conventions and descriptions of the sensors used in the dataset. (This is for the RDF Embeddings step)

### 2. [Main_Experiment_Evaluation_Data](./Main_Experiment_Evaluation_Data/README.md)

This folder contains the evaluation data for our main experiment. It provides results, analyses, and key metrics that demonstrate the effectiveness of our experimental approach. Included in this folder are the Python codes for calculating the Structural Similarity Score (StrSS), the Semantic Similarity Score (SemSS), and the Overall JSON Similarity Score (OJSS) used in the study. Below is a detailed description of the contents of this folder:

1. [**USECASE_1_Evaluation_Metrics.xlsx**](./Main_Experiment_Evaluation_Data/USECASE_1_Evaluation_Metrics.xlsx)
    - Contains the evaluation metrics results for Use Case 1.
    
2. [**USECASE_1_LLMs_Experiment_Results.xlsx**](./Main_Experiment_Evaluation_Data/USECASE_1_LLMs_Experiment_Results.xlsx)
    - The full experiment result for Use Case 1.
    
3. [**USECASE_2_LLMs_Experiment_Results.xlsx**](./Main_Experiment_Evaluation_Data/USECASE_2_LLMs_Experiment_Results.xlsx)
    - The full experiment result for Use Case 2.
    
4. [**eval_metrics.py**](./Main_Experiment_Evaluation_Data/eval_metrics.py)
    - The Python functions for calculating the Structural Similarity Score (StrSS), the Semantic Similarity Score (SemSS), and the Overall JSON Similarity Score (OJSS).

### 3. [SPARQL_query_using_LLMs](./SPARQL_query_using_LLMs/README.md)

This folder contains the experimental data for generating SPARQL queries using Large Language Models (LLMs).



### 4. [Prompt_Test](./Prompt_Test/README.md)

The `Prompt_Test` folder contains query list and test results that involve the two different prompts used in our study (In section 4.3 Prompts templates). 

Below is a detailed description of the contents of this folder:

1. [**Prompt_Test_Results.xlsx**](./Prompt_Test_Results.xlsx)
    - Contains the results from both prompt testing experiments.

2. [**gpt35_turbo-0125_prompt1_test_response.xlsx**](./gpt35_turbo-0125_prompt1_test_response.xlsx)
    - The test responses for the GPT-3.5 Turbo-0125 model using Prompt 1.

3. [**gpt35_turbo-0125_prompt2_test_response.xlsx**](./gpt35_turbo-0125_prompt2_test_response.xlsx)
    - The test responses for the GPT-3.5 Turbo-0125 model using Prompt 2.

4. [**query_list.txt**](./query_list.txt)
    - A text file listing the queries used in the prompt testing experiments.
