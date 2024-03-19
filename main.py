import json
import yaml
import os

class FormComponent:
    def __init__(self):
        self.forms = {}

    def import_form(self, file_path):
        try:
            _, file_extension = os.path.splitext(file_path)
            if file_extension.lower() == ".json":
                with open(file_path, 'r') as file:
                    self.forms = json.load(file)
            elif file_extension.lower() == ".yaml":
                with open(file_path, 'r') as file:
                    self.forms = yaml.safe_load(file)
            else:
                raise ValueError("Unsupported file format. Only JSON and YAML are supported.")
            print("Form imported successfully.")
        except FileNotFoundError:
            print("Error: File not found.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format.")
        except yaml.YAMLError:
            print("Error: Invalid YAML format.")
        except ValueError as e:
            print(e)


    def fill_form(self):
        try:
            if not self.forms:
                print("Error: No form imported. Please import a form first.")
                return

            print("Choose a form:")
            for i, form_name in enumerate(self.forms.keys(), start=1):
                print(f"{i}. {form_name}")

            form_choice = int(input()) - 1
            form_name = list(self.forms.keys())[form_choice]
            form = self.forms[form_name]

            filled_form = {}
            print(f"Fill in the '{form_name}' form:")
            for question, options in form.items():
                if isinstance(options, list):
                    print(f"Choose {question} (options: {', '.join(options)}):")
                    answer = input().strip()
                    if answer not in options:
                        print("Invalid input. Please choose from the provided options.")
                        return
                    filled_form[question] = answer
                else:
                    print(f"Enter {question}:")
                    answer = input().strip()
                    filled_form[question] = answer

            print("Thank you for filling the form! Here is the filled form:")
            print(json.dumps(filled_form, indent=4))
        except IndexError:
            print("Error: Invalid form choice.")
        except ValueError:
            print("Error: Invalid input.")

def main():
    form_component = FormComponent()
    while True:
        print("Welcome, choose an action:")
        print("1. Import a form")
        print("2. Fill in a form")
        print("3. Exit")

        choice = input()
        if choice == "1":
            print("Enter the path to the form:")
            file_path = input()
            form_component.import_form(file_path)
        elif choice == "2":
            form_component.fill_form()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
