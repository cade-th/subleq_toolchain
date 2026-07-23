class Parser:
    def __init__(self, tokens_in):
        self.tokens = tokens_in
        self.pos = 0
        self.macro_cnt = 0
        self.pc = 0
    
    def pass1(self):
        sym_table = {}
        mnt = {}
        mdt = []

        while self.pos < len(self.tokens):
            tok_t = self.tokens[self.pos][0]
            if tok_t == "label":
                sym_table[self.tokens[self.pos][1]]= self.pc
                self.pc += 1
                del self.tokens[self.pos]
            elif tok_t == "hash":
                mnt, mdt = self.record_macro(mnt, mdt)
            
            self.pos+=1

        
        self.pos = 0
        self.pc = 0

        return self.tokens, sym_table, mnt, mdt

    def record_macro(self, mnt, mdt):
        self.macro_cnt += 1

        # go to macro name
        del self.tokens[self.pos]
        del self.tokens[self.pos]
        # record macro name
        mnt[self.tokens[self.pos][1]] = {
            "mdt_index": self.macro_cnt,
            "parameters": []
        }

        # go to macro definition
        del self.tokens[self.pos]

        macro_tokens = []
        # record macro contents
        while self.tokens[self.pos][1] != "endM":
            tok_val = self.tokens[self.pos][0]
            tok_t = self.tokens[self.pos][1]


            macro_tok = [tok_t, tok_val]
            macro_tokens.append(macro_tok)
            del self.tokens[self.pos]


        mdt.append(macro_tokens)
        # delete endM
        del self.tokens[self.pos]

        return mnt, mdt



    def pass2(self, tokens, sym_table, mnt, mdt):
        
        while self.pos < len(tokens):
            tok_val = tokens[self.pos][1]
            tok_t = tokens[self.pos][0]
            if tok_t == "symbol":
                if tok_val in sym_table:
                    address = sym_table[tok_val]
                    tokens[self.pos] = ["number", tokens[address][1]]
                elif tok_val in mnt:
                    self.expand_macro(tok_val,mnt,mdt)
                else:
                    print("Unknown Symbol Found")
            self.pos+=1

        return tokens

    def expand_macro(self,mnt_key,mnt, mdt):

        del self.tokens[self.pos]
        
        mdt_tokens = mnt[mnt_key]["mdt_index"]
        for i in mdt[mdt_tokens]:
            self.tokens.insert(self.pos,i)



