class Parser:
    def __init__(self, tokens_in):
        self.tokens = tokens_in
        self.pos = 0
        self.macro_cnt = -1
        self.pc = 0

    def preproc(self):
        self.tokens, mnt, mdt = self.macro_p1()
        self.tokens = self.macro_p2(mnt, mdt)
        self.pos = 0
        return self.tokens
    
    def macro_p1(self):
        mnt = {}
        mdt = []

        while self.pos < len(self.tokens):
            tok_t = self.tokens[self.pos][0]
            tok_val = self.tokens[self.pos][1]
            if tok_t == "hash":
                mnt, mdt = self.record_macro(self.tokens,mnt, mdt)
                self.pos-=1
            
            self.pc+= 1
            self.pos+=1

        
        self.pos = 0
        self.pc = 0

        return self.tokens, mnt, mdt

    def record_params(self):
            params = []

            if self.tokens[self.pos][0] != "RPAREN":
                return params 

            # move past the rparen
            del self.tokens[self.pos]

            while self.tokens[self.pos][0] != "LPAREN":
                if self.tokens[self.pos][0] == "comma":
                    del self.tokens[self.pos]
                params.append(self.tokens[self.pos])
                del self.tokens[self.pos] 

            # move past lparen
            del self.tokens[self.pos]

            return params

    def record_macro(self,tokens,mnt, mdt):
        self.macro_cnt += 1

        # go to macro name
        del self.tokens[self.pos]
        del self.tokens[self.pos]
        macro_name = self.tokens[self.pos][1]
        # go to either definition or parameters
        del self.tokens[self.pos]
        
        # record macro name
        mnt[macro_name] = {
            "mdt_index": self.macro_cnt,
            "params": self.record_params()
        }

        tok_t = self.tokens[self.pos][0]
        tok_val = self.tokens[self.pos][1]

        # print(tok_t)  
        # print(tok_val)  

        macro_tokens = []
        # record macro contents
        while self.tokens[self.pos][1] != "endM":
            tok_val = self.tokens[self.pos][1]
            tok_t = self.tokens[self.pos][0]


            macro_tok = [tok_t, tok_val]
            macro_tokens.append(macro_tok)
            del self.tokens[self.pos]


        mdt.append(macro_tokens)
        # delete endM
        del self.tokens[self.pos]

        return mnt, mdt

    
    def macro_p2(self, mnt, mdt):
        
        while self.pos < len(self.tokens):
            tok_val = self.tokens[self.pos][1]
            tok_t = self.tokens[self.pos][0]
            if tok_t == "symbol":
                if tok_val in mnt:
                    self.expand_macro(tok_val,mnt,mdt)
            self.pos+=1

        return self.tokens

    def expand_macro(self,mnt_key,mnt, mdt):

        args = []
        del self.tokens[self.pos]

        if self.tokens[self.pos][0] == "RPAREN":
            args = self.collect_args()

        mdt_index = mnt[mnt_key]["mdt_index"]
        params = mnt[mnt_key]["params"]

        # replace parameters with arguments
        for i in range(0,len(mdt[mdt_index])):
            for j in range(0,len(params)):
                if mdt[mdt_index][i] == params[j]:
                    mdt[mdt_index][i] = args[j]

        self.tokens[self.pos:self.pos] = mdt[mdt_index]

    def collect_args(self):
        args = []
        del self.tokens[self.pos]
        while self.tokens[self.pos][0] != "LPAREN":
            if self.tokens[self.pos][0] == "comma":
                del self.tokens[self.pos]
            else:
                args.append(self.tokens[self.pos])
                del self.tokens[self.pos]
        del self.tokens[self.pos]
        
        return args


    def p1_label(self):
            sym_table = {}

            while self.pos < len(self.tokens):
                if self.tokens[self.pos][0] == "label":
                    sym_table[self.tokens[self.pos][1]] = self.pc
                    del self.tokens[self.pos]
                
                self.pos+=1
                self.pc+=1
            return self.tokens, sym_table

    def p2_label(self, sym_table):
            while self.pos < len(self.tokens):
                if self.tokens[self.pos][1] in sym_table:
                    address = sym_table[self.tokens[self.pos][1]]
                    self.tokens[self.pos] = ["number", self.tokens[address][1]]
                self.pos+=1
            return self.tokens


    def resolve_labels(self):
        self.tokens, sym_table = self.p1_label()
        self.pos = 0
        self.pc = 0
        self.tokens = self.p2_label(sym_table)
        return self.tokens
