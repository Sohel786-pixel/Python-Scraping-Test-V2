# Your code here

# First Part
# task 1
# define function
def most_recurrent_two_sequence(keywords):
    if not keywords:
        return None
    
    # Initialize a dictionary to store the frequency of each two-character sequence
    two_sequence_freq = {}
    
    # Iterate through each keyword in the list
    for keyword in keywords:
        # Iterate through each character in the keyword
        for i in range(len(keyword)-1):
            # Get the two-character sequence
            two_sequence = keyword[i:i+2]
                
            # Increment the frequency of the sequence in the dictionary
            two_sequence_freq[two_sequence] = two_sequence_freq.get(two_sequence, 0) + 1
    
    # Find the two-character sequence with the maximum frequency
    max_freq = max(two_sequence_freq.values())
    most_recurrent_two_sequences = [seq for seq, freq in two_sequence_freq.items() if freq == max_freq]
    
    return most_recurrent_two_sequences

# Apply function to given list
keywords = ['milk', 'chocolate', 'c+', 'python', 'cat', 'dog']
result = most_recurrent_two_sequence(keywords)
print(result)







#task 2

def parse_nutritional_info(text):
  """
  Parses the given input string to a dictionary containing nutritional information.

  Args:
    text: The input string containing nutritional information.

  Returns:
    A dictionary containing parsed data, or None if parsing fails.
  """
  data = {}
  lines = text.splitlines() # Split into individual lines
  for line in lines:
    if ":" in line:
      # Split based on the first colon, remove excess whitespace
      key, value = line.strip().split(":", 1)
      key = key.strip()
      value = value.strip()
      data[key] = value
  return data if data else None

# Example usage
text = """
Additifs nutritionnels : Vitamine C-D3 : 160 UI, Fer (3b103) : 4mg, Iode (3b202) : 0,28 mg, Cuivre (3b405, 3b406) : 2,2 mg,Manganèse (3b502, 3b503, 3b504) : 1,1 mg, Zinc (3b603,3b605, 3b606) : 11 mg –Clinoptilolited’origine sédimentaire : 2 g. Protéine : 11,0 % - Teneur en matières grasses : 4,5 % - Cendres brutes : 1,7 % - Cellulose brute : 0,5 % - Humidité : 80,0 %.
"""

parsed_data = parse_nutritional_info(text)

if parsed_data:
  print(parsed_data)
else:
  print("Error parsing data.")








# Task 3
#Create function for Grandma list

def is_grandma_list(lst):
    # Base case: if the list is empty, return False
    if not lst:
        return False
    
    # Check if the list contains any non-list elements
    non_list_elements = [elem for elem in lst if not isinstance(elem, list)]
    if non_list_elements:
        # If there are non-list elements, check if the product of adjacent elements is 2
        for i in range(len(non_list_elements) - 1):
            if non_list_elements[i] * non_list_elements[i+1] == 2:
                return True
        return False
    
    # If the list contains only nested lists, recursively check each nested list
    for sublist in lst:
        if is_grandma_list(sublist):
            return True
    
    return False

# Apply function to given list
grandma_list1 = [1, 2, [[4, 5], [4, 7]], 5, 4, [[95], [2]]]
grandma_list2 = [5, 9, 4, [[8, 7]], 4, 7, 1, [[5]]]

print(is_grandma_list(grandma_list1))
print(is_grandma_list(grandma_list2))




