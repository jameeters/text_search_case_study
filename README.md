### How to Run the Program
1. Running the interactive version
    1. `cd` to the `text_search_case_study` directory.
    2. Execute `python3 driver.py`
    3. The program will continue asking you to search until terminated.
2. Running unit tests
    1. In `text_search_case_study` execute `python3 -m unittest`
3. Running stress tests
    1. In the same directory execute `python3 stress_testing.py`
    2. The stress testing takes some time.
    The resulting data are written to files in the `data_files` directory.

### Performance Testing Results
On average, the time to search for a word with each method was:
1. Indexed: 0.0016 ms
2. Simple: 0.27 ms
3. Regexp: 1.316 ms

The indexed search was by far the fastest.
Even the 1.42 ms required for it to preprocess the documents is insignificant when amortized over enough searches.
I imagine that regular expression search is so slow because of the overhead they incur.
Matching whole words ins't really the typical use-case for regular expressions anyway.

### Thoughts on Scaling
- The more RAM the machine has, the more of the document can be searched at once.
- If you have multiple threads, you can give a chunk of the document to each thread and search more of the document at once.
- Assuming you're searching for whole words, pre-processing the documents is always going to win in the long run,
with the caveat that with large documents, preprocessing might take a long time.
In that case, it would be best to do the preprocessing at low-demand times.


### Notes
- I haven't done anything to make this runnable on windows, if that's necessary just let me know and I think I can make it work pretty quickly.
- I've only done search for words, not multi-word phrases, because I couldn't see how preprocessing the documents could possibly work for phrases of arbitrary length.
If what I've done is wrong though, I'm happy to adapt it.
The simple matching and regular expression searches would be trivial to adapt.
The indexed search would have to change completely.
