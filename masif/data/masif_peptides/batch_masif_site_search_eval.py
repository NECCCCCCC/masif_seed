import os


finished_list = os.listdir("data_preparation/01-benchmark_surfaces")
peptide_ids = [p.split('.')[0] for p in finished_list]

list_path = "/job/stash/peptides_list.txt"
with open(list_path, "w") as list_txt:
    list_txt.writelines("\n".join(peptide_ids))

os.system(f"./predict_site.sh -l {list_path}")
os.system(f"./compute_descriptors.sh -l {list_path}")
