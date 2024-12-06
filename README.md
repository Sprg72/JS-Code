# JS-Code

You are developing a message processing system that needs to handle a stream of text messages. Each message contains multiple words separated by spaces. Your task is to implement a function that processes 
these messages according to the following rules: If a word appears for the first time, keep it as is. For any subsequent appearances of the same word in the message stream, replace it with the number 
indicating which occurrence it is (2 for second occurrence, 3 for third, etc.). Words are case-sensitive, meaning 'Hello' and 'hello' are considered different words. The order of the words in each message 
should be preserved, and the word counting persists across all messages in the stream.

EXAMPLE 1
Input:hello world hello there world
Output:hello world 2 there 2

Explanation:First 'hello' stays, second becomes '2'. First 'world' stays, second becomes '2'

EXAMPLE 2
Input:hello Hello world hello
Output:hello Hello world 3

Explanation:'hello' and 'Hello' are different words due to case sensitivity. The last 'hello' is the third occurrence of lowercase 'hello'

Requirements
1
Implement a function that takes a string message as input
2
Track word occurrences across multiple function calls
3
Preserve the original word order in the output
4
Maintain case sensitivity in word comparison
5
Replace repeated words with their occurrence number
6
Handle empty strings and single-word messages
7
Words are separated by single spaces only




To solve this problem, we can implement the following approach:

Plan:
Track Word Occurrences: Use a dictionary to track how many times each word has appeared across all message streams. The key will be the word, and the value will be the count of occurrences.
Process Each Message: For each new message:
Split the message into individual words.
For each word, check if it has appeared before:
If it’s the first time the word appears, keep it as is.
If it has appeared before, replace it with the count indicating its occurrence.
Return the Modified Message: Join the modified words back into a single string with spaces and return it.
Preserve Case Sensitivity: Ensure that the case of words is considered when counting occurrences, i.e., 'Hello' and 'hello' are treated as distinct.
Edge Cases: Handle empty strings and single-word messages.

Implementation: python Copy code


def process_message(message):
    # Dictionary to store the count of occurrences of each word
    word_count = {}
    
    # Split the message into words
    words = message.split()
    
    # List to hold the processed words
    result = []
    
    # Process each word
    for word in words:
        # Check if the word has already been encountered
        if word in word_count:
            # Increment the count of occurrences
            word_count[word] += 1
            # Append the occurrence number to the result list
            result.append(str(word_count[word]))
        else:
            # First occurrence, just append the word and initialize its count
            word_count[word] = 1
            result.append(word)
    
    # Join the processed words back into a string with spaces
    return ' '.join(result)



Explanation:
word_count: This dictionary stores the occurrence count for each word.
words: The input string is split into words using the split() method, which separates the words by spaces.
Loop through words: For each word, check if it's in the word_count dictionary:
If it's already there, increment its count and append the count as a string to the result.
If it's the first time the word is encountered, append the word to the result and initialize its count in the dictionary to 1.
Result Construction: Finally, the processed words are joined into a single string with spaces and returned.

Example 1:
Input:
process_message("hello world hello there world")

Output:
hello world 2 there 2

Explanation:
  'hello' appears first, so it stays as 'hello'.
  'world' appears first, so it stays as 'world'.
  The second 'hello' is replaced with '2', indicating the second occurrence.
  The second 'world' is replaced with '2', indicating the second occurrence.

Example 2:
Input:
process_message("hello Hello world hello")

Output:
hello Hello world 3
Explanation:
  'hello' appears for the first time, so it stays as 'hello'.
  'Hello' appears for the first time, so it stays as 'Hello'.
  'world' appears for the first time, so it stays as 'world'.
  The second 'hello' is replaced with '3', indicating the third occurrence of 'hello' (case-sensitive).

Edge Cases:
  1. Empty String:
         Input: ""
         Output: ""
         No words to process, so the output is an empty string.
  
  2. Single Word:
        Input: "hello"
        Output: "hello"
        Only one word, so no repetition and the word stays as is.

  3. Multiple Repetitions of the Same Word:
        Input: "word word word word"
        Output: "word 2 3 4"
        The first word stays as "word", the second as "2", the third as "3", and the fourth as "4".


Time Complexity:
      The time complexity of this function is O(n), where n is the number of words in the input message. This is because:
            Splitting the string takes O(n) time.
            Processing each word and updating the dictionary also takes O(n) time, as dictionary operations are on average O(1).
            Constructing the final result string also takes O(n) time.
    
     Thus, the function processes the message in linear time relative to the number of words in the input string.


