# make sure the dataset is in the same directory as your python file, or put the absolute path to the dataset
file = open('file_path_to_dataset/hyperskill-dataset-82227383.txt', 'r')

# split each string in file into a list of strings based on the line breaks 
words = file.read().splitlines()

# the word we want to look for is "summer"
word = "summer"

# initiate counter variable
counter = 0

for line in words:
    if line == word:
        counter += 1

print(counter)

file.close()