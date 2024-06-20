import re

# 读取OUTCAR文件
with open('OUTCAR', 'r') as file:
    outcar_content = file.readlines()

# 查找所有cm-1出现的行号
cm1_lines = [i for i, line in enumerate(outcar_content) if 'f/i' in line]

# 提取每个cm-1对应的频率数据并写入新文件
for line_number in cm1_lines:
    line = outcar_content[line_number]
    frequency = re.findall(r'\d+\.\d+', line)[0]

    # 寻找频率数据所在块的结束行号
    end_line = line_number + 2
    while outcar_content[end_line].strip():  # 寻找空行
        end_line += 1

    # 提取频率数据并写入新文件
    data = []
    for i in range(line_number + 2, end_line):
        values = outcar_content[i].split()[-3:]
        data.append(' '.join(values))

    with open(f'freq_{frequency}', 'w') as new_file:
        new_file.write('\n'.join(data))
