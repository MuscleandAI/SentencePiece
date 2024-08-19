import json
import pandas as pd
json_file_path= 'tigerbot-alpaca-zh-0.5m.json'
text = []
with open(json_file_path, 'r') as json_file:
    # 逐行读取JSON数据
    for line in json_file:
        data = json.loads(line)

        # 合并input和output内容
        combined_content = f"{data['input']}{data['output']}"

        # 提取instruction内容
        # instruction = data['instruction']

        # 构建新的txt文件路径
        # txt_file_path = f'{json_file_path.split(".")[0]}_output.txt'

        # # 将合并的内容写入新的txt文件
        # with open(txt_file_path, 'a') as txt_file:
        #     # txt_file.write(f"Instruction: {instruction}\n\n{combined_content}\n\n")
        #     txt_file.write(f"{combined_content}\n")
        text.append(combined_content)

# print(f"合并的内容已写入到 {txt_file_path}")

# # 读取生成的txt文件
# generated_txt_file_path = txt_file_path  # 替换为上面生成的txt文件路径

# with open(generated_txt_file_path, 'r') as generated_txt_file:
#     # 读取前1000行内容
#     lines_to_save = [next(generated_txt_file) for _ in range(1000)]

# 构建新的txt文件路径
new_txt_file_path = 'train.txt'  # 替换为新的txt文件路径
text_col = text[:10000]
content_col = pd.DataFrame(text_col)
# 将数据追加写入txt文件
with open(new_txt_file_path, 'a') as file:
    content_col.to_csv(file, sep='\t', index=False, header=False)
print(f'前1万条content数据已写入到 {new_txt_file_path}')