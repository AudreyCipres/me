TODO: Reflect on what you learned this week and what is still unclear.
TO MERGE MULTIPLE CSV FILES INTO ONE FILEPATH/DEFINED VARIABLE USE:

path = "[file path]"
file_list = [path + f for f in os.listdir(path) if f.startswith("name that is repeated throughout the multiple files_n")]
csv_list = []
for file in sorted(file_list):
csv_list.append(pd.read_csv(file).assign(File_Name = os.path.basename(file)))
csv_merged = pd.concat(csv_list, ignore_index=True)
csv_merged.to_csv(path + "file_with_merged_csv_files.csv", index=False)
