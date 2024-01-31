import csv
from argparse import ArgumentParser
from WordSugestionInterface import WordSugestionInterface
from pathlib import Path


class WordSugestion(WordSugestionInterface):
    """
    A class for word recommendation.
    ......
    Methods
    -------
    read_file(path): loads data and return a list
    """
    def read_file(self, path):
        """This method reads csv files, creates a list
        of the data and returns the result
        Args:
             path(str): absolute file path as a string
        
        Returns: 
                list: a list of data from a csv file"""
     
        # let's create an empty list to put the values in    
        data_list = []

        # We now read a csv file provided and massage the data
        with open(Path(path),'r') as csv_reader:
            data = csv.reader(csv_reader)
            for word in data:
                if word:
                    data_list.append(word[0])
        return data_list
        
    
    def get_possible_words(self, words, word_structure):
        """A method to find the possible guesses of 
        the word based on the word_structure provided.
        Args:
            word_structure(str): word format to be searched
            words(list): a list of words to be used in searching
        
        Returns:
            list: list of possible words
        """
        #find the position of the chars and store them in 
        # a variable called lookup (I could name it better)
        lookup = []
        for i, x in enumerate(word_structure):
            if ord(x) !=ord('*'): # This could be done with direct char matching
                lookup.append(i)
        
        # Create an empty list for possible words
        possible_list = []

        # Next, we loop through a list to match 
        # the word with the word_structure provided.
        for word in words:

            # Let's ignore all the words that doesn't match 
            # the size of the word_structure string provided
            if len(word) ==len(word_structure):
                flag =0
            
            # Loop through the lookup and compare the char in both
                # word_structure word and the current word. We ignore case
                # here, as we don't want to deal with them (sorry)
                for indx in lookup:
                    if word[indx].lower() == word_structure[indx].lower():
                        flag +=1
                    else:
                        continue
                possible_list.append(word) if flag ==len(lookup) else ''
            else:
                continue
        # we have the list now 
        return possible_list


def main():
    """main  method
    """
    # First, let's read in the values from the console
    parser = ArgumentParser('Word Sugestions')
    parser.add_argument('-t','--word_structure', type=str, required=True)
    parser.add_argument('-p','--path', type=str, required=True)
    args = parser.parse_args()

    # Second, we create an object of WordSuggestion
    # and call our class methods to get the job done. 
    cws = WordSugestion()
    words = cws.read_file(args.path)
    print(cws.get_possible_words(words, args.word_structure))

if __name__ =="__main__":
    main()