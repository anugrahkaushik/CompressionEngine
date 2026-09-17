import os

byte_dict=dict()
compressed_file_path=input("Enter the compressed file path: ").strip().strip('"').strip("'")
compressed_dir=os.path.dirname(compressed_file_path)+os.sep
with open(compressed_dir+os.path.splitext(os.path.basename(compressed_file_path))[0]+'k.txt','r') as file:
    padding=int(file.readline())
    for row in file:
        (key,value)=row.split(':')
        byte_dict[value.strip()]=format(int(key),'08b')
encoded_string=[]
with open(compressed_file_path,'rb') as file:
    for byte in file.read():
        encoded_string.append(format(byte,'08b'))
encoded_string="".join(encoded_string)
encoded_string=encoded_string[:len(encoded_string)-padding]
original_string=[]
left=0
right=1
while left<len(encoded_string):
    while encoded_string[left:right] not in byte_dict.keys():
        right+=1
    original_string.append(byte_dict[encoded_string[left:right]])
    left=right
    right+=1
original_string="".join(original_string)
b=bytearray()
for i in range(0,len(original_string),8):
    b.append(int(original_string[i:i+8],2))
extension=input("Enter the extension in which to extract: ").strip().strip('.')
with open(compressed_dir+os.path.splitext(os.path.basename(compressed_file_path))[0]+'.'+extension,'wb') as file:
    file.write(b)