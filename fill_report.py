import sys
import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def fill_values(tests, values_dict):
    for test in tests:
        if 'id' in test and test['id'] in values_dict:
            test['value'] = values_dict[test['id']]
        
        if 'values' in test:
            fill_values(test['values'], values_dict)
    
    return tests

if __name__ == "__main__":
    if len(sys.argv) != 4:
       
        sys.exit(1)
    
    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]
    

    values_data = load_json(values_file)
    tests_data = load_json(tests_file)
    
   
    values_dict = {item['id']: item['value'] for item in values_data['values']}
    
    
    filled_tests = fill_values(tests_data['tests'], values_dict)
    

    save_json({"tests": filled_tests}, report_file)

    print(f"Отчет сохранен в {report_file}")
