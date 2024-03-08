import sys
import pprint as pp
import psicalc as pc

sys.path.insert(0, 'local')

#data1 = pc.durston_schema(pc.read_csv_file_format("hist-mini.csv"), 1)
#data1 = pc.durston_schema(pc.read_csv_file_format("../Histone H3 105 seq alignment.csv"), 1)
data1 = pc.durston_schema(pc.read_csv_file_format("../TOP2A_protein_105species REV trunc to HTIIa d.csv"), 1)
#data1 = pc.durston_schema(pc.read_csv_file_format("hist-test.csv"), 1)
#data2 = pc.durston_schema(pc.read_csv_file_format("test-hist-trunc.csv"), 1)
labels = []
msa = pc.merge_sequences([data1], labels)
result = pc.find_clusters(1, msa, "pairwise", 0.0)

pp.pprint(result)

#    mm = unique_values([d.index.unique() for d in data])
# def unique_values(lists):
#     elements = [item for sublist in lists for item in sublist]
#     unique = [i for i in set(elements) if elements.count(i) == 1]
