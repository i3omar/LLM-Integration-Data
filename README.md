# LLM Integration Experiment Data Repository
Welcome to our dedicated repository, which contains all data related to our experiment. 

## Main Project
For more details about the ForestQB project, please refer to the [ForestQB main repository](https://github.com/i3omar/ForestQB).

## Automatic Structural Evaluation

For a detailed explanation of how to use and implement the Automatic Structural Evaluation methodology featured in our research, please refer to the comprehensive guide in [STRUCTURAL_EVALUATION.md](STRUCTURAL_EVALUATION.md). This document provides an in-depth description of the evaluation metrics, usage examples, and implementation steps. 

## Contents

### 1. [Dataset](./Dataset/README.md)

This `Dataset` folder contains two key files essential for our experiment:

- [**Forest_dataset.ttl**](./Dataset/Forest_dataset.ttl): This dataset, which has been uploaded to a private SPARQL endpoint, contains comprehensive data used throughout our research.

- [**dataDefinitions.ttl**](./Dataset/dataDefinitions.ttl): This is a concise file that includes data definitions relevant to our study. It encompasses the naming conventions and descriptions of the sensors used in the dataset. (This is for the RDF Embeddings step)

---
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

5. [**USECASE_3_LLMs_Experiment_Results.xlsx**](./Main_Experiment_Evaluation_Data/USECASE_3_LLMs_Experiment_Results.xlsx)
    - The full experiment result for Use Case 3.

6. [**USECASE_3_Statistical_Tests.xlsx**](./Main_Experiment_Evaluation_Data/USECASE_3_Statistical_Tests.xlsx)
    - This file contains the statistical tests conducted for Use Case 3.
---

### 3. [SPARQL_query_using_LLMs](./SPARQL_query_using_LLMs/README.md)

This folder contains the experimental data for generating SPARQL queries using Large Language Models (LLMs).

---

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

---


### Citation

If you find this repository useful in your research or projects, please consider citing our paper: **[Towards Enhancing Linked Data Retrieval in Conversational UIs using Large Language Models
](https://arxiv.org/abs/2409.16220)**.
Your support through citation helps us continue improving and sharing our work with the community. Thank you!

```bibtex
@InProceedings{10.1007/978-981-96-0573-6_18,
author="Mussa, Omar
and Rana, Omer
and Goossens, Beno{\^i}t
and Orozco-terWengel, Pablo
and Perera, Charith",
editor="Barhamgi, Mahmoud
and Wang, Hua
and Wang, Xin",
title="Towards Enhancing Linked Data Retrieval in Conversational UIs Using Large Language Models",
booktitle="Web Information Systems Engineering -- WISE 2024",
year="2025",
publisher="Springer Nature Singapore",
address="Singapore",
pages="246--261",
isbn="978-981-96-0573-6"
}
```


© 2024.

