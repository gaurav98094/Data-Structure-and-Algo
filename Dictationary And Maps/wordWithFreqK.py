'''

Print all those word which occur in string k times

'''


def word_with_Freq_K(st,k):
    data = st.split()
    freq = {}

    for x in data:
        x = x.lower()
        freq[x] = freq.get(x,0)+1
    
    for x,y in freq.items():
        if y==k:
            print(x,end=" --> ")

word_with_Freq_K("I am You in love with python programming Python is just awesome also learn and you will start loving it",2)











