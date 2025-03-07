import json


def count_objects_with_same_labels(json_file, label):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    count = 0
    for obj in data.values():
        if 'labels_task3_1' in obj and all(l.upper() == label for l in obj['labels_task3_1']):
            count += 1
    
    return count


def count_objects_in_language(json_file, lang):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    count = 0
    for obj in data.values():
        if 'lang' in obj and obj['lang'] == lang:
            count += 1
    
    return count


def get_annotator_lst(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    annotators = []
    for obj in data.values():
        if 'annotators' in obj:
            for a in obj['annotators']:
                if not a in annotators:
                    annotators.append(a)
    return annotators


def get_classifications_lst(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    classifications = []
    for obj in data.values():
        if 'labels_task3_3' in obj:
            for c in obj['labels_task3_3']:
                if not c in classifications:
                    classifications.append(c)
    return classifications


def get_types_lst(json_file):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    types = []
    for obj in data.values():
        if 'labels_task3_2' in obj:
            for t in obj['labels_task3_2']:
                if not t in types:
                    types.append(t)
    return types

def get_type_count(json_file, type_val):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    counter = 0
    for obj in data.values():
        if 'labels_task3_2' in obj:
            for t in obj['labels_task3_2']:
                if t == type_val:
                    counter +=1
                    break
    return counter

def get_annotator_sample_count(json_file, annotator):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    counter = 0
    for obj in data.values():
        if 'annotators' in obj:
            for a in obj['annotators']:
                if a == annotator:
                    counter +=1
    return counter

def get_annotator_sample_count_positive(json_file, annotator):
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    counter = 0
    for obj in data.values():
        if 'annotators' in obj:
            for i in range(len(obj['annotators'])):
                if obj['annotators'][i] == annotator:
                    if obj['labels_task3_1'][i] == 'YES':
                        counter +=1
    return counter
    
def main():
    #Update the file location below before running
    json_file = "C:\\Users\\bisho\\Downloads\\EXIST 2025 Dataset V0.1_Extract\\EXIST 2025 Dataset V0.1 (3)\\EXIST 2025 Videos Dataset\\training\\EXIST2025_training.json"
    label_val = "YES"
    result = count_objects_with_same_labels(json_file, label_val)
    print(f"Number of objects with all {label_val} labels in 'labels_task3_1':  {result}")
    label_val_no = "NO"
    result_no = count_objects_with_same_labels(json_file, label_val_no)
    print(f"Number of objects with all {label_val_no} labels in 'labels_task3_1':  {result_no}")
    lang= "en"
    result_lang = count_objects_in_language(json_file, lang)
    print(f"Number of objects in {lang}: {result_lang}")
    annotators = get_annotator_lst(json_file)
    print(f"Annotators: {annotators}")
    classifications = get_classifications_lst(json_file)
    print(f"Classifications: {classifications}")
    print(f"Classifications count: {len(classifications)}")
    print(f"types: {get_types_lst(json_file)}")
    print(f"DIRECT count: {get_type_count(json_file, 'DIRECT')}")
    print(f"JUDGEMENTAL count: {get_type_count(json_file, 'JUDGEMENTAL')}")
    for a in annotators:
        print(f"{a} sample count: {get_annotator_sample_count(json_file, a)} {a} positive sample count: {get_annotator_sample_count_positive(json_file, a)}")

if __name__ == "__main__":
    main()
