## Trie_main.py

## Main function to test Trie implementation.

from Trie import Trie, Node;

def main():

    words  =   [    'shocking', 'jeans', 'groan', 'employ', 'milky', 'supply', 'silk', 'lean', 'brawny',
                    'peace', 'destruction', 'notice','apple', 'app', 'apps', 'self', 'loops', 'error', 'dynamic'
                ];
                
    trie = Trie(words);

    words_2 = ['sunny', 'abc', 'zorro'] + words + ['eve', 'zebra'];
    
    trie.delete_word('shocking');
    trie.delete_word('apps');


    excluded_words  =   [];

    for w in words_2:
        if not trie.find_word(w):
            excluded_words.append(w);

    print(excluded_words);

    false_deletion = [];

    for w in words_2:
        if not trie.delete_word(w):
            false_deletion.append(w);
    
    print(false_deletion);

    assert excluded_words == false_deletion, 'FAIL/CORRUPT DELETION in TRIE.'
    
    return 0;


if __name__ == '__main__':
    main();