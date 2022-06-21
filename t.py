

import os.path
import sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(),os.path.expanduser(__file__))))
# sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR,PACKAGE_PARENT)))


from sentenceninja import split as sentenceninja_split


from sentence_splitter import SentenceSplitter,split_text_into_sentences
# from .convert_review2script import *
text='So what I’m trying to say is I think that there should be a temporary trash pile section so that just in case somebody deleted the wrong thing or they want to edit it but didn’t expect to,they don’t have to worry about redoing everything they just did they can just go back to the original thing and recover it and just add in or take out whatever it is they were going to do.'
sces=split_text_into_sentences(text=text,language='en')
sces=sentenceninja_split(text)
# sces=long_cjk_text2paragraph_budouX(text,text_len=120,lang='en',count='')
for i in range(len(sces)):
    print('===',sces[i])