'''Input:
N = 4
arr[] = {geeksforgeeks, geeks, geek,
         geezer}
Output: gee
         {apple ape april}
Explanation: "gee" is the longest common
prefix in all the given strings.'''

#User function Template for python3


def longestCommonPrefix(arr, n):
        # code here
        ans=""
        for i in range(0,len(arr[0])):
            all=True
            for s in arr:
                if i>=len(s) or s[i]!=arr[0][i]:
                    all=False
                    break
            if all:
                ans+=arr[0][i]
            else:
                break
        return ans
                


       
            


            
    
               
         

print(longestCommonPrefix(["neykgrybpitzfunlefmtmbikgpxkqingmmsudqysarrilgtrnhka","tmrklbbtojfadcftaxwtqegyxymeioodcfonirhxaozdsfyseulxysvxsjdazsgbzupilyfnmgqflqzsllplfmjzwobvghzibos","mzbaftfrkhjxuaibmtakibiqjhamvsbjrcjxwrqgybfsbntpjtatwilfrmsmgtvyxextxpbvqgntwiihbkcyunflbzxku","ksbjnyypuqxjjtstcvgevaubmxclhxgtpjcchatdsrpdmhzpefvafpdtpffyenstwuydxrjrkyvxhuonzjpgbsaqa","oesgaodytcretccoblkrzjaosdjstjxkprsphvpazj","tljjovufwfhkxltpeeoowfhnoedpemwzzhipeeuakdljogzvnpljxuwlzzcfnygogodkvxnhdyqrgpmtfycesb","tcsaqsgeaxknsjazmapeghsaoseslfjgibhaupgu","qhgajhojzsq","lswdyoqexzobiovxwrknbspkaduzymhledqctjisiwtqmqpjkbylunxws","vqdcdjhuoadwsntofheuqqwobsdzoysjoynujuoxwtuogpenwjhpbdfdxjelhyuxyjridhfzabqiquvp","dehilmgw","tdqodpxwzdegegiupapmpwpvdajpifhblarorrmquqw","xgvohmayiswouffekphvpzlgsywoquonbjdkxgiiygwuldyysfthghpyfnmvibllmqvmw","uwmsszvqxoytxgcnfhctekwrxlisxgarfolxngqnwqiwwkld","nzzyvrvgbqfjqyoejmtqegouqkqaxwvlvvlsoibrygaqfrwofsgjaxdrhvrfrnsoidhylipmopevidknvswvpb","zzggsvyhfdqdqyseojjksowflqeigfvfgdlzylidoyiewajml","ydkwlvnpdvwaaffne","amiokquisfwebvjntuiglobkodpusvzshkitafbvmzzowibqfmysaacqftmyoosxydqaitvutukpfmfmaeeagj","nefntvgqtljttcppxlansoueoaloguiwypjtkrmdcvxxxonvzpksdeyrfjhndplefvxpojvrg","qgidbjundxtcqanxqrpbxwwwnliieoeuuoaxyukduehkgvkwobylxwhkjpvngbkaqmyoiktcqbp","wztkcrvzqelzwinc","zcalcqvnjydkpcgqwqspnrfuefqnuuxvwzibpdoadtl","wtksmcjzvrtaylpufopenxfecte","orakllexnoyjfulffaznoordnwhprnvffysqjwnyklhrfuwnuvakltnyr","oiklpplhfue","tqhckpzgc","eegpxtqqseacrptfzyzfuuvbzfsyowtsazjzvzpnfrrzhkeikfneakhbsczgyuazujarlseqjxpshvarbpxdaggsifahba","xlkoycuporggaejtfyqkyzqshxsqyuawilkgphvdyemzivsptlzumpmvo","mmbokjzxqrenuctgdbdy","xlrtxihswoglqxvbwstnwjkbcsggw","yvrqoqyvlxmtieqdfpwbcskovmhcsfitaajqsjndgzxodnulcqmhkwxgkgkflsy","ujdnstsbuppyfjljbxsovqwhwgokaoxxxdkswetqwiqbub","xaflxvhftptdqkbnhgzzcdsubdnezqryrwkottvmjrqbbtoizpkduezwjoakfrjypvoiomxzdpcekqolhyocd","aogaznukljfbuvntxqizwuslfzjvdokdfqeedaoqjvufqhypaipwchhjgtekjppohtunvi","hfzmyjnnjxchcjrl","kqevhtkopebkphruigurviasmkwybiqnywifruvgzztqimm","uhiprkkdugbxqtmqrxx","rvrsukiczvuteclvpvaldejwxxmrumamhrebepfd","zwqehlteleippgpnughgivnzcqfrvidxftboeutradhqjyfdgokokzpmqvfndikkdnzhj","akvjcghjjpxvdhxvvpqacvipglchuozvywecconndkljsienxwqbtyqzmvgijhdjfknjaaxfkkoes","urqkukknlwkuhtdkejwtsytrefb","mvpiohsjrewfdgbkbeuhntait","zxcbsoyjwnqqwkvupycqiduemkzmsthtsjukattygmpewkylkcbufxyrjafbtovlzryz","tyufpybbymlap","hpfayfhcyvzmvskwfdwzjlakoazzdqgmfmpgrwissjepbqngtkiexkrmmqnriueqgtwz","gtlpzaspozlajpxtgjhyxzjtdzbyvcrdwduvfm","tlyvwntrwezwdyfwde","dbaugyzavfniaygwxwrouvnqbnyxqexvizqozppuwcdxcltzjmodhdwitwilahhiizxhqobnqgksufudrkjanflgbv","dcbokantqbudrdplxwhanrjqhqbptyjxaknmmafdbbi"],3))
