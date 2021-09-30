import os, json
import pandas as pd

all_papers = []
for fname in sorted(os.listdir('json_data')):
    if fname[-4:] == 'json':
        with open('json_data/' + fname) as fp:
            json_data = json.load(fp)
        print(fname, len(json_data['result']['hits']['hit']))
        
        all_papers.extend(json_data['result']['hits']['hit'])

df = pd.DataFrame([d['info'] for d in all_papers])
df[['title', 'venue', 'year', 'ee']].to_json('summary_papers.json', orient='records')
print("SUCCESS")
