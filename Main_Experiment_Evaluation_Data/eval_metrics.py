# To ensure this function works correctly, you'll need the following:

# 1. Import necessary libraries:
#    You need the `model` for encoding text into embeddings and the `util` for calculating cosine similarity.
# from sentence_transformers import SentenceTransformer, util

# 2. Instantiate the model:
#    Before calling the function, you need to load a pre-trained model suitable for encoding sentences.
# model = SentenceTransformer('paraphrase-TinyBERT-L6-v2')


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


def overall_json_similarity_score(json_ref, json_gen, alpha=0.5):
    kms = structural_similarity_score(json_ref, json_gen)
    sss = semantic_similarity_score(json_ref, json_gen)
    return alpha * kms + (1 - alpha) * sss


def clamp(score):
    return max(0, min(score, 1))
