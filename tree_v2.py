data = [
    {"name": "Ads","id": "1", "parent_id": "0"},        ####
    {"name": "ASR","id": "2","parent_id": "1"},
    {"name": "Customer Engagment","id": "3","parent_id": "1"},
    {"name": "Sales Platform","id": "4","parent_id": "3"},
    {"name": "Web Signals","id": "5","parent_id": "4"},
    {"name": "Ads Publisher","id": "6","parent_id": "5"},
    {"name": "Cloud","id": "7","parent_id": "0"},        ####
    {"name": "Concord","id": "8","parent_id": "7"},
    {"name": "Finance","id": "9","parent_id": "8"},
    {"name": "Dev","id": "10","parent_id": "9"},
    {"name": "Prod","id": "11","parent_id": "9"},
    {"name": "Concierge","id": "12","parent_id": "0"},        ####
    {"name": "Finance","id": "13","parent_id": "12"},
    {"name": "POps","id": "14","parent_id": "12"},
    {"name": "Release","id": "15","parent_id": "12"},
    {"name": "Dev","id": "16","parent_id": "15"},
    {"name": "Staging","id": "17","parent_id": "15"},
    {"name": "UAT","id": "18","parent_id": "15"},
    {"name": "GBO","id": "19","parent_id": "0"},        ####
    {"name": "F360","id": "20","parent_id": "19"},
    {"name": "Marketing","id": "21","parent_id": "0"},        ####
    {"name": "Cross_Product","id": "22","parent_id": "21"},
    {"name": "Santorio","id": "23","parent_id": "22"}
]

levels = {}
for n in data:
	levels.setdefault(n['parent_id'], []).append(n)

def build_tree(parent_id=0):
    nodes = [dict(n) for n in levels.get(str(parent_id), [])]
    for n in nodes:
        children = build_tree(n['id'])
        if children: n['children'] = children
    return nodes

tree = build_tree()
print(tree)
