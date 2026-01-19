import sys, os

inputfile = ''

#####################################################################################
# fetch arguments
#####################################################################################
args = sys.argv
for arg in args:
    if arg.endswith('.py'):
        pass

    # inputfile
    elif arg.startswith('--file=') or arg.startswith('-f='):
        arg = arg.replace('--file=', '')
        arg = arg.replace('-f=', '')
        inputfile = arg

#####################################################################################
# set parameters
#####################################################################################

par_sep = '\n\n'
max_words = 320
min_words = 230
max_excerpts = 10

#####################################################################################
# read file and set separation points
#####################################################################################

file = open(inputfile, 'r')
text = file.read()

paragraphs = []
par = ""
for i in range(len(text)):
    if text[i:i+2] == par_sep:
        paragraphs.append(par[1:]+'\n')
        par = ""
    else:
        par += text[i].replace('\n\n', '')

separation = []
chunk = ""
curr_words = 0
for par in paragraphs:
    words = par.count(" ")+1
    if curr_words + words < max_words:
        chunk += par
        curr_words += words
        if curr_words > min_words:
            separation.append(chunk)
            chunk = ""
            curr_words = 0
    else:
        chunk += par
        curr_words += words
        separation.append(chunk)
        chunk = ""
        curr_words = 0

excerpts = []
size = len(separation)
num_excerpts = min(size, max_excerpts)
for i in range(num_excerpts):
        index = round(size * i / num_excerpts)
        excerpts.append(separation[index])

filename = inputfile[inputfile.index('/')+1:-4]
out_dir = "excerpts-"+filename
os.makedirs(out_dir, exist_ok=True)
for i in range(len(excerpts)):
    out_file = filename + "-excerpts-" + str(i+1)+ '.txt'
    full_path = os.path.join(out_dir, out_file)
    with open(full_path, 'w') as f:
        f.write(excerpts[i])


