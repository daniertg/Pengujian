def levenshtein_distance(s1, s2):
    """
    Calculate Levenshtein distance between two strings manually
    without external dependencies
    """
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    # Create matrix
    previous_row = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            # Cost of insertions, deletions and substitutions
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    
    return previous_row[-1]

def calculate_similarity_percentage(str1, str2):
    """Calculate similarity percentage using Levenshtein distance"""
    if not str1 or not str2:
        return 0.0
    
    # Normalize strings
    str1_norm = ' '.join(str1.strip().split())
    str2_norm = ' '.join(str2.strip().split())
    
    if str1_norm == str2_norm:
        return 100.0
    
    # Calculate distance
    distance = levenshtein_distance(str1_norm, str2_norm)
    max_len = max(len(str1_norm), len(str2_norm))
    
    if max_len == 0:
        return 100.0
    
    # Convert to similarity percentage
    similarity = ((max_len - distance) / max_len) * 100
    return round(similarity, 2)
