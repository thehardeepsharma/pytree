data_list = [
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
    {"name": "DSF Concierge","id": "12","parent_id": "0"},        ####
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

parent_child, nodes_dict, children_dict = {}, {}, {}

for node in data_list:
    parent_id = node.get('parent_id')
    parent_child.setdefault(parent_id, [])
    parent_child[parent_id].append(node)
    nodes_dict[node.get('id')] = node
    if parent_id != '0':
        children_dict.setdefault(parent_id, [])
        children_dict[parent_id].append(node)

# print(parent_child)
# print("=================")
# print(children_dict)


def get_children(children_dict, ch_list):
    child_list, child_dict = [], {}
    if ch_list is not None:
        for ch_dict in ch_list:
            ch_id = ch_dict.get('id')
            if ch_id in children_dict:
                c_list = children_dict.get(ch_id)
                get_children(children_dict, c_list)
                ch_dict.update({'children': c_list})
            else:
                ch_dict.update({'children': []})
            child_list.append(ch_dict)
    return child_list

def get_categories(categories, children_dict):
    category_list, category_dict = [], {}
    for category_id, category in categories.items():
        parent_id = category.get('parent_id')
        if parent_id == '0' or parent_id == '' or parent_id is None:
            category_dict = {}
            category_dict.setdefault(category_id, {})
            children_categories = children_dict.get(category_id)
            new_child_categories = []
            if children_categories is not None:
                for ch in children_categories:
                    ch_id = ch.get('id')
                    if ch_id in children_dict:
                        ch_list = children_dict.get(ch_id)
                        ch1_list = get_children(children_dict, ch_list)
                        ch.update({'children': ch1_list})
                    else:
                        ch.update({'children': []})
                    new_child_categories.append(ch)
            category_dict[category_id] = {
                'id': category_id,
                'parent_id': parent_id,
                'name': category.get('name'),
                'children': new_child_categories
            }
            category_list.append(category_dict)
    return category_list


categories = get_categories(nodes_dict, children_dict)
# print('categories: ', categories)

product_list, family_list, cat_list, cat_select_dict, parent_id = [], [], [], {}, 0
cat_tree_dict = {}

def get_nameed_tree(child_list, current_cat, main_cat_id):
    if child_list:
        for ch_dict in child_list:
            current_cat_2 = current_cat + " / " + ch_dict.get('name')
            cat_id = ch_dict.get('id')
            cat_tree_dict.setdefault(cat_id, '')
            if main_cat_id != cat_id:
                cat_tree_dict[cat_id] = current_cat_2 + " - " + str(cat_id)
            ch_list = ch_dict.get('children')
            if ch_list:
                get_nameed_tree(ch_list, current_cat_2, main_cat_id)

def get_category_select(categories, main_cat_id):
    for category_dict in categories:
        for category_id, cat_dict in category_dict.items():
            cat_tree_dict.setdefault(category_id, '')
            current_cat = cat_dict.get('name')
            if category_id is not None:
                cat_tree_dict[category_id] = current_cat + ' - ' + str(category_id)
            cat_child_list = cat_dict.get('children')
            if cat_child_list:
                get_nameed_tree(cat_child_list, current_cat, main_cat_id)

main_cat_id = None
get_category_select(categories, main_cat_id)

print('cat_tree_dict: ', cat_tree_dict)


