## Trie Class
## To keep collection of words
## Features:
##      add_word
##      delete_word
##      find_word
##      has_prefix
##  NOTE:  Assume word is non-case-sensitive (lower case only)..

WORD_CHOICES    =   26      # 26 alphabet letters.


## Class Node to hold each character in the Trie.
class Node:
    def __init__(self, val = None, is_end_word = False):

        self.val            =   val;                    # character 'a'-'z';
        self.next           =   [False]*WORD_CHOICES;   # An array of size 26. Each to hold next node character.
        self.is_end_word    =   is_end_word;            # True if this node is end of Trie word.


## Trie Class.

class Trie:
    def __init__ (self, words = []):
        # Initialize Trie with the words input array.

        self.head = Node( val = 'HEAD');                # Head ptr.

        for w in words:                                 # Add each word in Trie.
            self.add_word(w);

        return;

    def add_word(self, word):
        # Add each word to Trie tree.
        # Returns None.

        ptr = self.head;

        for c in word:
            c = c.lower();
            c_index = self.char_to_index(c);

            # If char c doesn't exist yet, create a new node.
            if not ptr.next[c_index]:
                ptr.next[c_index] = Node(val = c);

            # Set ptr to the next char.
            ptr = ptr.next[c_index];
        
        # Mark this node as end of word.
        ptr.is_end_word =   True;

        return;
    
    def delete_word(self, word):

        # Delete a word from Trie tree.
        # Returns True if deletion is successful. Otherwise, returns False.

        ptr     =   self.head;
        ls_word =   [self.head];

        for c in word:
            c = c.lower();
            c_index =   self.char_to_index(c);

            if ptr.next[c_index]:
                ls_word.append(ptr.next[c_index]);
            
            else:
                return False;
            
            ptr = ptr.next[c_index];
        
        if not ptr.is_end_word:         return False;

        ptr.is_end_word =   False;
    
        for i in range( len(ls_word)-1, 0, -1):

            prev, curr  =   ls_word[i-1], ls_word[i];
            
            if curr.is_end_word:        break;

            if len( set(    curr.next)) > 1:
                return True;
            
            prev.next[self.char_to_index(curr.val)] = False;
            del curr;

        return True;
    
    def find_word( self, word):
        #Returns True if word is in Trie.

        ptr = self.traverse_prefix(word);        
        return ptr.is_end_word      if ptr      else False;

    def has_prefix( self, word):
        #Returns True if Trie has prefix word.

        ptr = self.traverse_prefix(word);        
        return True            if ptr      else False;
    
    def traverse_prefix(self, word):
        # Returns the ptr in Trie where the last character of the word is.
        # If word doesn't exist, returns False.

        ptr = self.head;

        for c in word:
            c = c.lower();
            c_index = self.char_to_index(c);

            if ptr.next[c_index] != False:      ptr =   ptr.next[c_index];
            else:                               return False;
        
        return ptr;

    def char_to_index( self, char):
        # Convert char to int: 'a' = 0, 'b' = 1, ..., 'z' = 25.
        return ord(char.lower())-ord('a');

