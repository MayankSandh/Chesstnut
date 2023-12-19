from datetime import datetime

filename = ""
def write_to_file(text):
    global filename
    if not filename:
        filename =  "match_data/"+datetime.now().strftime("%d_%m_%Y")+datetime.now().strftime("%H_%M_%S")+".txt"
    try:
        with open(filename, 'a') as file:
            file.write(text)
        # print(f"Text has been written to {filename} successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage: