# Automatic Structural Evaluation
This document outlines how to perform the Automatic Structural Evaluation as implemented in our paper. This evaluation method computes structural and semantic similarity between two JSON objects and combines them into an overall score, designed for assessing structured data.
If you find this evaluation method useful in your research or application, please consider citing our paper: **[Towards Enhancing Linked Data Retrieval in Conversational UIs using Large Language Models
](https://arxiv.org/abs/2409.16220)**.

## Prerequisites

To use the functions in this repository, you need to install the following dependencies:

```bash
pip install sentence-transformers torch
```

### Required Libraries:
- `sentence_transformers` for embedding text.
- `torch` for tensor operations.
- Python 3.x and above.

### Import Necessary Libraries:
```python
from sentence_transformers import SentenceTransformer, util
```

### Load the Pre-trained Model:
We recommend using the pre-trained model `paraphrase-TinyBERT-L6-v2` for encoding sentences into embeddings. Load the model as shown:

```python
model = SentenceTransformer('paraphrase-TinyBERT-L6-v2')
```

---

## Evaluation Functions

### 1. **Structural Similarity Score (StrSS)**

The `structural_similarity_score` function calculates the structural similarity between two JSON objects. This score penalizes missing keys in the generated JSON and applies a lighter penalty for additional keys.

#### Function:

```python
def structural_similarity_score(json_ref, json_gen, beta=0.1):
    """
    Calculate the Structural Similarity Score (StrSS) that weights the presence of additional keys
    less severely than the absence of reference keys.
    
    :param json_ref: Reference JSON object as a dictionary.
    :param json_gen: Generated JSON object as a dictionary.
    :param beta: Weight factor for extra keys (0 < beta <= 1).
    :return: StrSS as a float.
    """
    keys_ref = set(json_ref.keys())
    keys_gen = set(json_gen.keys())
    
    # Calculate the intersection and the extra keys in generated JSON
    intersection = keys_ref.intersection(keys_gen)
    extra_keys = keys_gen - keys_ref
    
    # union calculation
    adjusted_union = len(keys_ref) + beta * len(extra_keys)
    
    # Compute the StrSS
    return len(intersection) / adjusted_union if adjusted_union > 0 else 1
```

#### Parameters:
- `json_ref`: The reference JSON object (as a dictionary).
- `json_gen`: The generated JSON object (as a dictionary).
- `beta`: Weight factor for extra keys (0 < beta ≤ 1). The default is `0.1`.

#### Returns:
- Structural similarity score (StrSS) as a float between `0` and `1`.

### 2. **Semantic Similarity Score (SemSS)**

The `semantic_similarity_score` function calculates the semantic similarity between two JSON objects. It compares the values of the common keys using text embeddings and cosine similarity.

#### Function:

```python
def semantic_similarity_score(json_ref, json_gen):
    """
    Calculate the Semantic Similarity Score (SemSS) between two JSON objects.
    """
    # Extract the sets of keys from both JSON objects
    keys_ref = set(json_ref.keys())
    keys_gen = set(json_gen.keys())
    
    # Find the common keys in both JSON objects
    matching_keys = keys_ref.intersection(keys_gen)
    
    # Initialize a list to hold similarity scores for matching keys
    similarities = []
    
    # Iterate over each matching key to calculate similarity
    for key in matching_keys:
        # Convert the values to strings
        value_ref = str(json_ref[key])
        value_gen = str(json_gen[key])
        
        # Compute embeddings for the values using a pre-trained model
        emb_ref = model.encode(value_ref, convert_to_tensor=True)
        emb_gen = model.encode(value_gen, convert_to_tensor=True)
        
        # Calculate cosine similarity between the embeddings
        sim = util.pytorch_cos_sim(emb_ref, emb_gen)
        
        # Append the similarity score to the list (convert to a scalar value)
        similarities.append(sim.item())
    
    # Calculate the average similarity score if there are any similarities, else return 0
    return clamp(sum(similarities) / len(similarities) if similarities else 0)

def clamp(score):
    return max(0, min(score, 1))
```

#### Parameters:
- `json_ref`: The reference JSON object (as a dictionary).
- `json_gen`: The generated JSON object (as a dictionary).

#### Returns:
- Semantic similarity score (SemSS), a floating-point number between `0` and `1`.

#### Note:
- Ensure the pre-trained model is loaded before using this function:

  ```python
  model = SentenceTransformer('paraphrase-TinyBERT-L6-v2')
  ```

### 3. **Overall JSON Similarity Score**

The `overall_json_similarity_score` function computes an overall similarity by combining the structural and semantic similarity scores using a weighted average.

#### Function:

```python
def overall_json_similarity_score(json_ref, json_gen, alpha=0.5):
    """
    Calculate the overall JSON similarity score (combining structural and semantic scores).
    
    :param json_ref: Reference JSON object as a dictionary.
    :param json_gen: Generated JSON object as a dictionary.
    :param alpha: Weight factor for structural similarity (default: 0.5).
    :return: Overall similarity score as a float.
    """
    kms = structural_similarity_score(json_ref, json_gen)
    sss = semantic_similarity_score(json_ref, json_gen)
    return alpha * kms + (1 - alpha) * sss
```

#### Parameters:
- `json_ref`: The reference JSON object (as a dictionary).
- `json_gen`: The generated JSON object (as a dictionary).
- `alpha`: Weight factor for structural similarity (`0 ≤ alpha ≤ 1`). The default is `0.5`.

#### Returns:
- Overall similarity score, a floating-point number between `0` and `1`.

---

## Example Usage

### 1. **Install Dependencies**:
  ```bash
  pip install sentence-transformers torch
  ```

### 2. **Load the Model**:
  ```python
  from sentence_transformers import SentenceTransformer, util
  
  model = SentenceTransformer('paraphrase-TinyBERT-L6-v2')
  ```

### 3. **Calculate Similarity**:
  ```python
  json_ref = {
    "query": {
      "<python/Juling>": {
            "<property/HDOP>": {"value": ["Bound"]}
      }
    }
  }
  json_gen = {
    "query": {
      "<python/Juling>": {
            "<property/PDOP>": {"value": ["Not Bound"]}
      }
    }
  }

  strss = structural_similarity_score(json_ref, json_gen)
  semss = semantic_similarity_score(json_ref, json_gen)
  overall_score = overall_json_similarity_score(json_ref, json_gen)

  print(f"Structural Similarity Score: {strss}")
  print(f"Semantic Similarity Score: {semss}")
  print(f"Overall Similarity Score: {overall_score}")
  ```

---

## Conclusion

This method enables evaluation of both structural and semantic similarity for JSON objects. For further details on the methodology, please refer to our paper. If this evaluation is helpful, please consider citing our paper: **[Towards Enhancing Linked Data Retrieval in Conversational UIs using Large Language Models
](https://arxiv.org/abs/2409.16220)**.

