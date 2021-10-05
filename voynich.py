class Line:
    def __init__(self, page_name, line_num, locator, locus, text):
        self.page_name = page_name
        self.line_num = line_num
        self.locator = locator
        self.locus = locus
        self.text = text

class Page:
    def __init__(self, page_name, page_num=None, quire_num=None,
                 folio_num=None, bifolio_num=None, illust_type=None,
                 currier_language=None, hand=None, extraneous_writing=None):
        self.page_name = page_name
        self.page_num = page_num
        self.quire_num = quire_num
        self.folio_num = folio_num
        self.bifolio_num = bifolio_num
        self.illust_type = illust_type
        self.currier_language = currier_language
        self.hand = hand
        self.extraneous_writing = extraneous_writing
        
        self.lines = []
        
    def __len__(self):
        return len(self.lines)
    
    def __getitem__(self, i):
        return self.lines[i]

    def __iter__(self):
        return iter(self.lines)
    
    def __repr__(self):
        return f"Page(page_name={self.page_name})"
        
    def iterlines(self):
        return self.__iter__()
    
class VoynichManuscript:
    def __init__(self, path_to_txt, inline_comments=False):
        self.remove_comments = remove_comments
        self._parse_txt(path_to_txt)
        
    def _parse_txt(self, path_to_txt):
        # read in txt file (without comments or blank lines)
        with open(path_to_txt, "r") as f:
            lines = [l.strip() for l in f.readlines() if l[0] != "#" and len(l) > 1]
        
        # iterate through each line and construct page and line objects
        page = None
        for line in lines:
            # split into metadata and data 
            a, b = line.split("> ")
            a = a[1:]
            
            # identify if this line is a page header or transliteration item
            if "," not in a: # page header
                page_name = a
                var_dict = _parse_variables(b)
            else: # transliteration item
                

        if not self.inline_comments:
            lines = [l.replace("<->", "") for l in lines]

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_to_idx = {l:i for i, l in enumerate(alphabet)}

def _parse_variables(var_str):
    var_dict = dict()
    
    # split the header str into tuples of variables and their values
    variables = var_str.replace(">", "").replace("<!", "").strip().split()
    variables = [s[1:].split("=") for s in variables]
    
    # iter through the var/val tuples and parse them accordingly
    for (var, val) in variables:
        if var == "Q": # quire number
            letter_to_idx