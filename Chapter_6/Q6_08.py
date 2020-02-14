import os
import json
from datetime import date


def serialize_to_json(file):
    file_info = os.stat(file)
    info = {
        'name': os.path.basename(file),
        'size': file_info."""①""",
        'last_modification': file_info."""②"""
    }
    return json."""③"""(info)


file_list = []
extensions = ('.wp1', '.wp2', '.sc1', '.sc2')
for dirpath, dirnames, filenames in os.walk('upload'):
    for filename in filenames:
        if filename.endswith(extensions):
            file_list.append(serialize_to_json(os.path.join("""④""", """⑤""")))

target_file = 'weekly_export_' + date.today().strftime('%Y%m%d') + '.json'
with open(target_file, 'w') as f:
    json.dump(file_list, f)
