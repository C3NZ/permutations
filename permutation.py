# Problem Set 4A
# Name: Vincenzo Marcella
# Collaborators: Me, myself, and I
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    '''

    if len(sequence) == 1:
        return [sequence]
    else:
        smaller_permutations = get_permutations(sequence[1:]) 
        permutations = []

        #Iterate through all of the permutations of the string
        for i in range(len(smaller_permutations)):
            #Iterate through the smaller permutation and insert the previous char at
            #all possible positions
            for j in range(len(smaller_permutations[i]) + 1):
                temp_list = list(smaller_permutations[i])
                temp_list.insert(j, sequence[0])
                permutations.append("".join(temp_list))

        return permutations

if __name__ == '__main__':
 
    print('\n')
    
    #Test case 1
    example_input = 'abc'
    expected_output = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print('Input:', example_input)
    print('Expected output:', sorted(expected_output))
    print('Actual Output:  ', sorted(get_permutations(example_input)))
    print('\n')

    #Test case 2
    example_input = 'def'
    expected_output = ['def', 'edf', 'efd', 'dfe', 'fde', 'fed']
    print('Input:', example_input)
    print('Expected output:', sorted(expected_output))
    print('Actual Output:  ', sorted(get_permutations(example_input)))
    print('\n')

    #Test case 3
    example_input = 'ghi'
    expected_output = ['ghi', 'hgi', 'hig', 'gih', 'igh', 'ihg']
    print('Input:', example_input)
    print('Expected output:', sorted(expected_output))
    print('Actual Output:  ', sorted(get_permutations(example_input)))
    print('\n')
    
