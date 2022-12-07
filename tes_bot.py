import subprocess
import os
import time
#assign directory for pdf files
directory = 'D:\ocr_bot\pdf-files'

# list pdf files 
print("Selected Files:")
for file in os.listdir(directory):
	f = os.path.join(directory, file)
    # checking if it is a file
	if os.path.isfile(f):
		print(f)

print("---------------------------------")
# convert pdf files to high res images
# convert -density 300 .\test1.pdf -depth 8 -strip -background white -alpha off out.tiff
#     subprocess.run(['gmtselect', '-Fother.txt'], stdin=f)

for file in os.listdir(directory):
	# f stores path of pdf
	path = os.path.join(directory, file)
	with open(path,"r") as f:
		subprocess.run(['magick','convert','-density', '300',path,'-depth', '8', '-strip', '-background', 'white', '-alpha', 'off', 'out.tiff'], shell=True,stdin=True)
# convert high res photos to text
# run tesseract ocr on output.tiff obtained above
print("Finished converting .pdf -> .tiff")
print("saved in directory :"+os.getcwd()+" with name out.tiff")
tiff_img_path=os.getcwd()+"\out.tiff"
# cmd to pass output imagr to tesseract ocr and force language to kan
# output obtained in demo.txt
# tesseract .\out.tiff demo -l kan
output_file="demo"
print("Starting Convertion :")
#start timer
tic=time.perf_counter()
subprocess.run(['tesseract',tiff_img_path,output_file,'-l','kan'])
toc=time.perf_counter()
print(f"Finished in {toc-tic:0.4f} seconds")
print("Text Stored in " + output_file+".txt")


