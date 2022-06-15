# Load Pkgs
import spacy 
# Text Preprocessing Pkg
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
# Import Heapq 
from heapq import nlargest , nsmallest



# Build a List of Stopwords
stopwords = list(STOP_WORDS)
#load the english model
nlp = spacy.load('en_core_web_sm')

#inital test value
test = """
        aaaaa
    """

# text preprocessing function
def text_summarizer(raw_docx = test):
    raw_text = raw_docx
    docx = nlp(raw_text)
    stopwords = list(STOP_WORDS)
    # Build Word Frequency
    # word.text is tokenization in spacy
    word_frequencies = {}  
    for word in docx:  
        if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1

    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    # Sentence Tokens
    sentence_list = [ sentence for sentence in docx.sents ]

    # Calculate Sentence Score and Ranking
    sentence_scores = {}  
    for sent in sentence_list:  
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]

    # Find N Largest
    summary_sentences = nlargest(4, sentence_scores, key=sentence_scores.get)
    final_sentences = [ w.text for w in summary_sentences ]
    summary = ' '.join(final_sentences)
    print("Original Document\n")
    print(raw_docx)
    print("Total Length:",len(raw_docx))
    print('\n\nSummarized Document\n')
    print(summary)
    print("Total Length:",len(summary))
    
    #clear summary to have one space between sentences and words and \n
    summary = summary.replace('\n', ' ')
    summary = summary.replace('\r', ' ')
    summary_list = summary.split(' ')
    summary_list = [x for x in summary_list if x != '' and x != ' ']
    summary = ' '.join(summary_list)
    
    obj = {
        "length": len(summary),
        "summary": summary
    }
    return obj


if __name__=="__main__":
    text_summarizer(test)