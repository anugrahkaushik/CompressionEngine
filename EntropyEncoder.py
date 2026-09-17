import os

class Heap:
    def __init__(self):
        self.arr=[]
        self.length=0

    def insert(self,value):
        self.arr.append(value)
        self.length+=1
        self.heapify_up(self.length-1)

    def heapify_up(self,i):
        while i>0:
            parent=(i+1)//2-1
            if self.arr[i][1]>=self.arr[parent][1]:
                break
            self.arr[parent],self.arr[i]=self.arr[i],self.arr[parent]
            i=parent

    def delete(self):
        value=self.arr[0]
        self.arr[0]=self.arr[-1]
        self.arr.pop()
        self.length-=1
        self.heapify_down()
        return value

    def heapify_down(self):
        i=0
        while i<self.length:
            minimum=i
            left=2*i+1
            right=2*i+2
            if left<self.length and self.arr[minimum][1]>self.arr[left][1]:
                minimum=left
            if right<self.length and self.arr[minimum][1]>self.arr[right][1]:
                minimum=right
            if minimum==i:
                break
            self.arr[i],self.arr[minimum]=self.arr[minimum],self.arr[i]
            i=minimum

    def build_heap(self,values):
        self.arr=values.copy()
        self.length=len(self.arr)
        for i in range(self.length-1,-1,-1):
            j=i
            while j<self.length:
                minimum=j       
                left=2*j+1
                right=2*j+2
                if left<self.length and self.arr[left][1]<self.arr[minimum][1]:
                    minimum=left
                if right<self.length and self.arr[right][1]<self.arr[minimum][1]:
                    minimum=right
                if minimum==j:
                    break
                self.arr[minimum],self.arr[j]=self.arr[j],self.arr[minimum]
                j=minimum

def encode(heap):
    if heap.length==1:
        return {heap.arr[0][0][0]:"0"}
    result={i[0]:"" for i,j in heap.arr}
    while heap.length>1:
        small=heap.delete()
        large=heap.delete()
        for i in small[0]:
            result[i]='0'+result[i]
        for i in large[0]:
            result[i]='1'+result[i]
        heap.insert((small[0]+large[0],small[1]+large[1]))
    return result

def main():
    original_bitlength=0
    heap=Heap()
    byte_dict=dict()
    input_file_path=input("Enter file path: ")
    input_file_path=input_file_path.strip().strip('"').strip("'")
    compressed_dir=os.path.join(os.path.dirname(input_file_path),os.path.splitext(os.path.basename(input_file_path))[0]+"-Compressed"+os.sep)
    with open(input_file_path,'rb') as file:
        for byte in file.read():
            original_bitlength+=8
            if byte not in byte_dict.keys():
                byte_dict[byte]=1
            else:
                byte_dict[byte]+=1
    heap.build_heap([([i],byte_dict[i]) for i in byte_dict.keys()])
    result=encode(heap)
    encoded_string=[]
    with open(input_file_path,'rb') as file:
        for byte in file.read():
            encoded_string.append(result[byte])
    encoded_string="".join(encoded_string)
    compressed_bitlength=len(encoded_string)
    os.makedirs(compressed_dir,exist_ok=True)
    with open(compressed_dir+os.path.splitext(os.path.basename(input_file_path))[0]+'k.txt','w') as file:
        if len(encoded_string)%8!=0:
            file.write(str(8-len(encoded_string)%8)+"\n")
        else:
            file.write("0\n")
        file.write("\n".join([str(i)+":"+str(result[i]) for i in result.keys()]))
    if len(encoded_string)%8!=0:
        encoded_string+='0'*(8-len(encoded_string)%8)
    b=bytearray()
    for i in range(0,len(encoded_string),8):
        b.append(int(encoded_string[i:i+8],2))
    with open(compressed_dir+os.path.splitext(os.path.basename(input_file_path))[0]+'.bin','wb') as file:
        file.write(b)
    print(f"{100*(original_bitlength-compressed_bitlength)/original_bitlength:.2f}% compressed")

main()