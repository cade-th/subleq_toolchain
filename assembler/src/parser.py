class Parser:
    def __init__(self, tokens_in):
        self.tokens = tokens_in
        self.pos = 0
        self.macro_cnt = -1
        self.pc = 0
    
    def macro_p1(self):
        mnt = {}
        mdt = []

        while self.pos < len(self.tokens):
            tok_t = self.tokens[self.pos][0]
            tok_val = self.tokens[self.pos][1]
            if tok_t == "hash":
                mnt, mdt = self.record_macro(self.tokens,mnt, mdt)
                # has to be a number here
            
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
            "parameters": self.record_params()
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
        if self.tokens[self.pos] == "RPAREN":
            args = self.collect_args()

        print(args)

        
        mdt_index = mnt[mnt_key]["mdt_index"]
        print("got here")
        print(mnt[mnt_key]["params"])
        params = mnt[mnt_key]

        print(mdt[mdt_index])
        print(params)

        for i in range(0,mdt[mdt_index]):
            for j in range(0, params):
                if params and params[j] == mdt[mdt_index][i]: 
                    self.tokens.insert(self.pos, args[0])
                else:
                    self.tokens.insert(self.pos, mdt[mdt_index][i])

    def collect_args(self):
        args = []
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
            print("TODO")
            return self.tokens, sym_table

    def p2_label(self, sym_table):
            print("TODO")
            return self.tokens

