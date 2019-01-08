import time
import os

try:
    from quickumls import QuickUMLS
except ImportError:
    from .quickumls import QuickUMLS

print('Creating QuickUMLS object...')
    
quickumls_path = r'C:\quickumls'
    
matcher = QuickUMLS(quickumls_path)

print('QuickUMLS object created...')

total_iterations = 1000
ignore_syntax = False

text_file_path = r'data/colonoscopy-1.txt'
file = open(text_file_path, 'r') 
text = file.read()
file.close()

print('Length of Text : {0} characters'.format(len(text)))

print('About to reprocess this text [{0}] times'.format(total_iterations))

results_list = []
result_count = 0

start_time = time.time()

for i in range(total_iterations):
    if i % 100 == 0:
        print('Progress : [{0}/{1}]'.format(i, total_iterations))

    res = matcher.match(text, best_match=True, ignore_syntax=ignore_syntax)
    results_list.append(res)
    result_count += len(res)
    
    #print('Matching results:')
    #print(res)
    
end_time = time.time()

elapsed_time_seconds = end_time - start_time

avg_doc_time_seconds = elapsed_time_seconds / float(len(results_list))

print('Total results received : [{0}]'.format(result_count))
print('Total time for [{0}] documents was [{1}] seconds'.format(len(results_list), elapsed_time_seconds))
print('Avg time per document : [{0}] seconds'.format(avg_doc_time_seconds))

print('DONE with performance test')