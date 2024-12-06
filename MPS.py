def process_message(message):
    word_count = {}
    
    words = message.split()
    
    
    result = []
    
    
    for word in words:
        if word in word_count:
            
            word_count[word] += 1
            
            result.append(str(word_count[word]))
        else:
            
            word_count[word] = 1
            result.append(word)
    
    
    return ' '.join(result)
