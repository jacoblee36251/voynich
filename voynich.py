import re

class Line:
    def __init__(self, page_name, line_num, locator, locus, text):
        self.page_name = page_name
        self.line_num = line_num
        self.locator = locator
        self.locus = locus
        self.text = text
    
    def __len__(self):
        return len(self.text)
    
    def __getitem__(self, i):
        return self.text[i]
    
    def __iter__(self):
        return iter(self.text)
    
    def __repr__(self):
        return f"Line({self.text})"
        

class Page:
    def __init__(self, page_name, page_num=None, quire_num=None,
                 folio_num=None, bifolio_num=None, illust_type=None,
                 currier_language=None, hand=None, currier_hand=None,
                 extraneous_writing=None):
        self.page_name = page_name
        self.page_num = page_num
        self.quire_num = quire_num
        self.folio_num = folio_num
        self.bifolio_num = bifolio_num
        self.illust_type = illust_type
        self.currier_language = currier_language
        self.hand = hand
        self.currier_hand = currier_hand
        self.extraneous_writing = extraneous_writing
        
        self.lines = []
        
        self.num_lines = self.__len__()

    def __len__(self):
        return len(self.lines)
    
    def __getitem__(self, i):
        return self.lines[i]

    def __iter__(self):
        return iter(self.lines)
    
    def __repr__(self):
        return f"Page(page_name={self.page_name}, quire_num={self.quire_num}, folio_num={self.folio_num}, num_lines={self.__len__()}, illust_type={self.illust_type})"
        
    def iterlines(self):
        return self.__iter__()
    
class VoynichManuscript:
    def __init__(self, path_to_txt, inline_comments=False):
        self.inline_comments = inline_comments
        self.pages = dict()
        self._parse_txt(path_to_txt)
        
    def __repr__(self):
        return f"VoynichManuscript(num_pages={len(self.pages)}, inline_comments={self.inline_comments})"
        
    def _parse_txt(self, path_to_txt):
        # read in txt file (without comments or blank lines)
        with open(path_to_txt, "r") as f:
            lines = [l.strip() for l in f.readlines() if l[0] != "#" and len(l) > 1]
        
        # Trim excess spaces
        lines = [re.sub("\s\s+" , " ", line) for line in lines]
        
        # iterate through each line and construct page and line objects
        page = None
        for line in lines:
            # split into metadata and data 
            a, b = line.split("> ")
            a = a[1:]
            
            # if this line is start of new page
            if "," not in a:
                # Create a new page object, store it
                page_name = a
                page = Page(page_name, _parse_variables(b))
                self.pages[page_name] = page
            
            # or if this line is a transliteration item 
            else:
                # parse metadata of line
                page_info, locus_info = a.split(",")
                page_name, line_num = page_info.split(".")
                locator, locus = locus_info[0], locus_info[1:]
                
                # parse corpus of line
                text = b
                
                # remove inline comments (if specified)
                if not self.inline_comments:
                    text = text.replace("<->", "")
                    text = re.sub("\<!.*?\>", "", text) # anything between <! and >
                
                # make new line object and store it
                page.lines.append(Line(page_name, line_num, locator, locus, text))
                


# For converting letters to numbers (both upper and lower case map to same number)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_to_num = {l:i+1 for i,l in enumerate(alphabet)}
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_to_num.update({l:i+1 for i,l in enumerate(alphabet)})

# Mapping illustration type abbreviation to full str
char_to_illust_type = {
    "A":"Astronomical",
    "B":"Biological",
    "C":"Cosmological",
    "H":"Herbal",
    "P":"Pharmaceutical",
    "S":"Marginal Stars Only",
    "T":"Text-Only",
    "Z":"Zodiac",
}

def _parse_variables(var_str):
    var_dict = dict()
    
    # split the header str into tuples of variables and their values
    variables = var_str.replace(">", "").replace("<!", "").strip().split()
    variables = [s[1:].split("=") for s in variables]
    
    # iter through the var/val tuples and parse them accordingly
    for (var, val) in variables:
        if var == "Q":
            var_dict["quire_num"] = letter_to_num[val]
        elif var == "P":
            var_dict["page_num"] = letter_to_num[val]
        elif var == "F":
            var_dict["folio_num"] = letter_to_num[val]
        elif var == "B":
            var_dict["bifolio_num"] = int(val)
        elif var == "I":
            var_dict["illust_type"] = char_to_illust_type[val]
        elif var == "L":
            var_dict["currier_language"] = val
        elif var == "H":
            var_dict["hand"] = int(val) if val.isnumeric() else val
        elif var == "C":
            var_dict["currier_hand"] = int(val) if val.isnumeric() else val
        elif var == "X":
            var_dict["extraneous_writing"] = val # will leave this as abbreviation for now
    
    return var_dict