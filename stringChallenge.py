def StringChallenge(strParam):
    # Store the largest number of unique characters found
    max_unique_count = 0
    
    # Iterate through the string to find matching letter pairs
    for i in range(len(strParam)):
        for j in range(i + 1, len(strParam)):
            if strParam[i] == strParam[j]:
                # Find the substring between the matching letters
                substring = strParam[i + 1:j]
                
                # Find the number of unique characters in the substring
                unique_chars = set(substring)
                
                # Update the maximum unique count
                max_unique_count = max(max_unique_count, len(unique_chars))
    
    return max_unique_count

# Keep this function call here
print(StringChallenge(input()))
