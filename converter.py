
import json
docs = json.load(open('/data/document_passages.json'))

finput = open('/data/input_file.txt', 'w+')

for i in range(len(docs)):
    for doc_id in docs[str(i)].keys():
        finput.write('<DOC>\n')
    
        finput.write('<DOCNO>'+ str(i)+'-'+str(doc_id) +'</DOCNO>\n')
        finput.write('<TEXT>\n')
        finput.write(docs[str(i)][str(doc_id)]+'\n')
        finput.write('</TEXT>\n')
        finput.write('</DOC>\n')
    
finput.close()
