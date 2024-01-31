'''
* **********************************Instructions********************************
* This is an abstract for the word suggestion program 
* 1. This program would have an input pattern with ch and wildcard (*)
* 2. The program should return all words from the provided file that match the input pattern. 
*    
*  Example Input: b**k
*  Output: Results: ['back', 'bank', 'book', 'buck', 'bulk']
*   
*  Example Input: **l
*  Output: Results: ['all', 'aol', 'cal', 'col', 'del', 'dsl', 'gel', 'gpl', 'ill', 'jul', 'lil', 'lol', 'mel', 
                    'mil', 'nfl', 'nhl', 'nil', 'oil', 'pal', 'rel', 'sol', 'sql', 'ssl', 'tel', 'til', 'url', 'val', 'vol', 'wal', 'xml']
* 
'''


class WordSugestionInterface:
    def read_file(self, path):
        '''This methos will read the 
        file.
        Args:
            path: file location'''
        pass

    # Return results from here.
    def get_possible_words(self, words, word_structure):
        """This methos would generate all possible words
        based on the word_structure provided.
        Args:
            words: words
            word_structure: word template"""
        pass