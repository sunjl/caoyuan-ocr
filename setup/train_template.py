import json

x_offset = 98
y_offset = 157
x_padding = 3
y_padding = 80
region_width = 59
region_height = 34

user_id = '59f7e576b2c79a43548402e0'
storage_id = '5a000fb4b2c79a280e9c1944'

regions = []
filename = '../dict/en_dict.txt'
with open(filename) as file:
    for line_idx, line in enumerate(file, 1):
        line = line.strip()
        chars = list(line)
        for char_idx, char in enumerate(chars):
            region = {
                'name': char,
                'pt1': {
                    'x': x_offset + char_idx * region_width + char_idx * x_padding,
                    'y': y_offset + (line_idx - 1) * region_height + (line_idx - 1) * y_padding
                },
                'pt2': {
                    'x': x_offset + (char_idx + 1) * region_width + char_idx * x_padding,
                    'y': y_offset + line_idx * region_height + (line_idx - 1) * y_padding
                },
                'correction': char
            }
            regions.append(region)

data = {
    'user_id': user_id,
    'kind': 'train',
    'name': 'train_template',
    'regions': regions,
    'storage_id': storage_id,
    'filename': 'train_template.png'
}
json_data = json.dumps(data)
filename = 'train_template.json'
with open(filename, 'w') as file:
    file.write(json_data)
