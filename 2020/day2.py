import re

PASSWORDS = [
    ('1-4 m', 'mrfmmbjxr'),
    ('5-16 b', 'bbbbhbbbbpbxbbbcb'),
    ('7-8 x', 'qxrxmxccxxx'),
    ('9-11 k', 'kkkkkkktmkhk'),
    ('8-12 g', 'sgwvdxzhkvndv'),
    ('6-9 v', 'zvmvvmvvvd'),
    ('8-19 f', 'ffffsplmfflffhtfrfj'),
    ('5-16 p', 'pppppppppspppjpcp'),
    ('2-3 w', 'wwmw'),
    ('7-19 j', 'jjjjjjjjjjjjjjjjjjvj'),
    ('5-9 q', 'wqzqqqqqq'),
    ('14-15 g', 'gggggggggglggfgg'),
    ('4-6 p', 'tppzkppdt'),
    ('11-14 p', 'vppgpktpppppptpppqp'),
    ('5-9 f', 'bfflffrfgf'),
    ('7-9 p', 'ppppptbzn'),
    ('1-3 l', 'lllvn'),
    ('2-4 g', 'qvcdg'),
    ('1-3 m', 'wsmdv'),
    ('1-5 v', 'vvvvvvvv'),
    ('10-14 l', 'lckqlgjllltlwbl'),
    ('3-4 t', 'bsttftltjhbqbgtm'),
    ('15-17 j', 'jjzjjjjjhjjjjjjpzjj'),
    ('2-3 t', 'thtt'),
    ('6-17 f', 'ffwkwzjtjktvsfmfhvsf'),
    ('3-5 b', 'rqxbb'),
    ('4-7 m', 'nbcmcwmmxrxqvtjfmm'),
    ('1-2 v', 'gzvvvv'),
    ('1-3 w', 'hkwhv'),
    ('7-8 p', 'pppppppp'),
    ('3-4 h', 'hhnwh'),
    ('2-4 t', 'ttrtjtththkr'),
    ('3-4 w', 'wwww'),
    ('4-6 s', 'xsntgrftmpx'),
    ('4-7 s', 'ssskssmsbs'),
    ('10-15 m', 'bmmrbmmmmlmmmmmm'),
    ('12-13 w', 'wqpwdmwllnjwx'),
    ('5-14 n', 'nnnnlnnnnnnnnmnn'),
    ('5-6 k', 'kktkfczk'),
    ('5-7 r', 'nrdrtrvr'),
    ('4-6 c', 'ccqchcc'),
    ('2-9 l', 'fnldtfnbxjlvnlsnjhml'),
    ('1-13 d', 'dlchvkccnwrcc'),
    ('5-7 j', 'jjjjjjj'),
    ('3-5 z', 'zzzzz'),
    ('6-12 f', 'ffffflvmfhfx'),
    ('8-10 w', 'wwwwwwwwww'),
    ('3-4 r', 'rrbtr'),
    ('3-11 b', 'bbbrbbvphbxbqk'),
    ('16-17 n', 'nqhknnnnsnnnnnnnnnb'),
    ('18-20 k', 'kkkkkkkkkkkkkkkkkhtj'),
    ('3-15 r', 'ktvzqbmbrvczprfcw'),
    ('9-11 q', 'qnqqdqqqgrrqsqq'),
    ('3-5 p', 'pvppp'),
    ('7-11 m', 'mfcdmmxmmmp'),
    ('7-8 t', 'ttttktnt'),
    ('5-6 b', 'bbpbbbv'),
    ('14-16 z', 'zzzzzzzzzrzzblzw'),
    ('11-12 j', 'jkjjjkjjjjjjgj'),
    ('7-9 q', 'qqqqqqqqqq'),
    ('10-11 f', 'cfffffffffff'),
    ('4-6 c', 'nccccc'),
    ('7-8 r', 'gmdlqfpwmrr'),
    ('6-8 v', 'nvvpdnjx'),
    ('8-12 x', 'xxlxxbbxxxxx'),
    ('8-10 s', 'ssxssssssss'),
    ('5-12 z', 'zhzdfzgdzzhzlz'),
    ('11-12 k', 'qbkhvqjpqzfq'),
    ('2-11 w', 'wwmlttwjflwdjcpclww'),
    ('2-16 w', 'twkkmcrxmvjtwxlwsksf'),
    ('6-8 s', 'sssfxbskvs'),
    ('5-6 s', 'ssnsxsbs'),
    ('10-19 l', 'ndzmdxqlnllxsbbwvsl'),
    ('2-4 g', 'gggg'),
    ('5-10 x', 'zxxxsxxxxxxxsxx'),
    ('7-15 f', 'ffbrbdtzvdffktxfm'),
    ('7-8 m', 'xmkmmmmmtmm'),
    ('9-13 s', 'hksrdhzlsdmps'),
    ('15-17 b', 'bbbbbbbrbbbbbbbrbb'),
    ('3-5 x', 'xxxxxxx'),
    ('2-6 t', 'wtltztnct'),
    ('3-15 v', 'vvwvvvvvhvvvbwwvmdvr'),
    ('12-14 p', 'ppphsppppppbphp'),
    ('8-9 t', 'ttttvttttttt'),
    ('2-3 c', 'cchvj'),
    ('8-9 z', 'vzzzzzzgl'),
    ('11-12 q', 'qqmqqqqqqqsnqqqqqqq'),
    ('12-13 d', 'dddddddddddmd'),
    ('8-9 t', 'wttttttqt'),
    ('7-8 p', 'ppppvvcw'),
    ('4-5 g', 'gncgj'),
    ('12-13 s', 'sssssssssssmw'),
    ('7-9 f', 'pswpnjftf'),
    ('11-16 p', 'ppppnpkpkzppcpzbppp'),
    ('1-12 q', 'ksqrqpqnqmqxqb'),
    ('2-10 l', 'lllllllllll'),
    ('17-18 z', 'zzzzzzzzzzzxzzzzzz'),
    ('11-12 g', 'qggbjgggggssgggrk'),
    ('3-4 s', 'bpss'),
    ('6-8 v', 'vwvvvrvvv'),
    ('3-4 t', 'tglktt'),
    ('4-12 l', 'kvrnzqslwrdkfll'),
    ('12-16 b', 'fbbbbbnbbvbbbbbcbbb'),
    ('5-6 t', 'ttttzz'),
    ('5-8 w', 'sqwhwwxw'),
    ('8-9 z', 'zzzvztzrzzzz'),
    ('3-6 l', 'llvdlt'),
    ('7-8 r', 'mrcvnrrr'),
    ('10-11 k', 'kkkkkkkkkmc'),
    ('1-3 n', 'nnnmn'),
    ('4-16 c', 'dqlcbclcrxkkszvcv'),
    ('9-10 g', 'fxssmlmgbh'),
    ('5-6 p', 'nwpfpp'),
    ('3-7 w', 'cwhgrfshdwhwwll'),
    ('14-16 l', 'llllllllllllllpll'),
    ('3-4 f', 'ffff'),
    ('4-9 d', 'dcdddxzvmrd'),
    ('4-11 w', 'jwwnwwwwwvx'),
    ('3-4 t', 'ttvc'),
    ('4-17 r', 'rrsrrrrrrrrrbtrrrr'),
    ('8-9 x', 'wqxxxcfdx'),
    ('6-8 d', 'qgddwddtdddlc'),
    ('12-13 v', 'vvjvvvvvzvvtvv'),
    ('3-4 g', 'sghxg'),
    ('3-4 b', 'ckbbmprfbbmzgqtkbw'),
    ('5-6 x', 'xxxxxv'),
    ('10-13 f', 'zpfffbfchxfffffjff'),
    ('5-6 f', 'ffffwf'),
    ('12-19 l', 'mlllllplllldllnsllql'),
    ('4-5 v', 'vvvvp'),
    ('5-8 w', 'vjwvghggwww'),
    ('1-3 n', 'lnnn'),
    ('16-18 p', 'ppppppvpppppwppppppp'),
    ('15-18 z', 'zzzzzzzzzzzzzzjzzg'),
    ('4-6 b', 'bbmbbb'),
    ('5-7 z', 'wzlwzmzzzzzzzzzzzwz'),
    ('8-12 p', 'gppmpppvppkzpcnpb'),
    ('16-19 h', 'hhbhhhhhhhhhhhlnhhw'),
    ('2-3 n', 'nnnn'),
    ('3-10 m', 'mmntfkdjftmtmmbm'),
    ('3-5 j', 'jjjjw'),
    ('4-6 z', 'zjnzzzdzz'),
    ('1-7 s', 'zsvsssf'),
    ('6-7 v', 'vtvvvcg'),
    ('3-12 f', 'qsrtmnxkvlcmt'),
    ('5-11 q', 'mqgqqqqqrpch'),
    ('5-9 g', 'msxkggnggg'),
    ('3-8 v', 'vvvvhvjvdvxtr'),
    ('4-6 k', 'jcklxdhkwhsqhq'),
    ('6-7 x', 'vppxbhcjzxdqx'),
    ('2-3 n', 'ntrg'),
    ('7-8 g', 'gggwgjdhg'),
    ('1-3 d', 'dddd'),
    ('14-18 l', 'llllllllwlllxllllllz'),
    ('8-19 g', 'ggggghggkhgrtzcgrrk'),
    ('7-14 q', 'phzxvmbxxfsfwr'),
    ('8-14 r', 'hbjmdrhnpxnwgz'),
    ('15-17 d', 'dddddpddddldddtdgddd'),
    ('6-7 k', 'kkkkkgkkq'),
    ('2-12 w', 'wwzwwwwwwwwww'),
    ('5-8 q', 'qqqqqqqzqqwqqzqcq'),
    ('5-6 z', 'czzzrz'),
    ('14-15 b', 'bbbrzhbbbbnxbgbb'),
    ('12-13 d', 'dgddddddddtvddddvbz'),
    ('3-5 v', 'vvvvv'),
    ('13-16 q', 'qqqqqvzwqqqqqqqq'),
    ('2-3 n', 'jpznnwfpchs'),
    ('7-10 w', 'jwwpwkwwwpw'),
    ('6-7 b', 'bbcnbcjxbbb'),
    ('14-17 w', 'wqtwwwwwnwcwwbsww'),
    ('3-14 w', 'gwwwwwwwhwwnxwwwww'),
    ('4-9 w', 'mwllcfjfwwwjp'),
    ('9-12 n', 'nnnnnnnhnwjnn'),
    ('2-4 j', 'jjjjj'),
    ('3-6 t', 'mrmttccttqt'),
    ('16-17 p', 'ppmjpgptzgbppphfbp'),
    ('12-17 v', 'vvvvvvvvvvvvvfvvvv'),
    ('13-15 x', 'xxxxxxxxxxxxxxgx'),
    ('2-4 d', 'dddddddd'),
    ('2-5 t', 'ttmvt'),
    ('13-14 j', 'jjjjjjjjjjjjtj'),
    ('3-5 r', 'ggmrdf'),
    ('7-8 f', 'ffdfflszfsfffqff'),
    ('10-11 t', 'ttpttttttrgtt'),
    ('8-12 j', 'jjjjqdhzjhjdj'),
    ('19-20 z', 'zbzzzzzzzzzzzzzzzzrq'),
    ('7-11 b', 'bbbbbhbbbxbbb'),
    ('4-9 p', 'gzmkkbtpkzpgthklpq'),
    ('2-5 b', 'bbbbxgb'),
    ('4-13 k', 'kkkkkkzktckkkwkjkk'),
    ('10-12 q', 'vrxznfqqnqgq'),
    ('15-16 m', 'mmmmkmmmmmmmmmmmm'),
    ('15-18 h', 'hlhhvhchthhhhtphhh'),
    ('2-3 m', 'mftzmc'),
    ('6-11 s', 'ksssssssssszs'),
    ('5-6 q', 'qqqpqkq'),
    ('7-8 n', 'nnfnnnnpn'),
    ('6-8 c', 'chfcllrvxcnnjhtc'),
    ('6-8 k', 'kkkkkxlk'),
    ('2-4 s', 'tsspb'),
    ('9-12 q', 'qqqqqqqqqqqqqq'),
    ('17-20 h', 'hhhhhhhhhhhhhhhhhhhh'),
    ('6-13 r', 'rrrrrgrrrrrrn'),
    ('4-8 f', 'fffrfffz'),
    ('13-14 n', 'nbnnnngnnnnnnpz'),
    ('8-11 f', 'fvffsfqftcffff'),
    ('3-5 w', 'vwhxz'),
    ('8-10 x', 'nmxxknlptx'),
    ('3-4 p', 'pppt'),
    ('17-18 v', 'vvvvvvhkvvvvvnvvjlvv'),
    ('10-15 z', 'twnsdkmgpvzfmzg'),
    ('3-5 n', 'njnjnkghp'),
    ('10-12 q', 'qvqqqqqqqqqq'),
    ('6-7 r', 'rrrrrrrr'),
    ('3-4 t', 'qltt'),
    ('2-16 f', 'gffflcvtpfkfcjfrjvfs'),
    ('3-5 s', 'swssp'),
    ('11-13 l', 'lrpllllllvtslwllllld'),
    ('1-3 n', 'nnnn'),
    ('3-5 g', 'jjggnvg'),
    ('4-5 b', 'bvbbb'),
    ('13-15 l', 'llvllllllllllnll'),
    ('5-6 j', 'hjjjjfsj'),
    ('3-4 b', 'bkfbnb'),
    ('5-8 z', 'zdzzzzzzzrzzz'),
    ('3-4 r', 'rrrx'),
    ('2-12 c', 'mczhvchkmjdrjh'),
    ('12-16 x', 'sjxbcgdqtpfxflsxx'),
    ('2-4 c', 'tcxf'),
    ('4-5 w', 'kwjww'),
    ('1-2 r', 'rrrwzc'),
    ('4-7 d', 'ddddddkdd'),
    ('5-6 q', 'qqqqqp'),
    ('13-16 l', 'flljlllvnzlllllclldl'),
    ('3-6 j', 'jjjpjj'),
    ('3-4 g', 'gxgg'),
    ('10-11 n', 'nnnnnnnnnnn'),
    ('2-5 j', 'ztchj'),
    ('4-6 j', 'pjzzrmjvhcxn'),
    ('4-11 c', 'jchcccgccckc'),
    ('11-12 d', 'dddddddddddd'),
    ('6-7 n', 'nznnnnnntnnnnzpjfjnn'),
    ('8-9 k', 'kbkkkkkkk'),
    ('13-18 x', 'xbxxmxqxxxmxkxsxxxx'),
    ('7-16 r', 'rrrrrrzrrrrrrrjmrrr'),
    ('3-5 h', 'hhqhd'),
    ('1-2 b', 'bbmb'),
    ('2-3 n', 'rlnntn'),
    ('2-8 q', 'qnfqnqhx'),
    ('2-5 b', 'bjbbh'),
    ('5-11 t', 'twtjnpttqtvtttptt'),
    ('16-17 w', 'wtmwwhxtgwrrswwfblll'),
    ('8-16 g', 'ggggghshggdggggcpwg'),
    ('1-3 l', 'lsllzl'),
    ('11-13 n', 'nnnvncnnmvnqnnnnn'),
    ('6-7 s', 'ssqssss'),
    ('10-18 t', 'tttnmjxttjttttttdzt'),
    ('4-10 n', 'nkvncgtdpz'),
    ('16-18 p', 'cphtrgffcpphfspxppgp'),
    ('2-6 k', 'kkhgkskkm'),
    ('6-20 r', 'fhrwtrzwrddfrndnrlgr'),
    ('2-8 w', 'lkwnccgw'),
    ('6-10 x', 'lxxxxxxgxwxxxrxqxx'),
    ('4-9 q', 'tqtpgqjzdmqfq'),
    ('9-12 k', 'kkkkkqbkkckkkjkql'),
    ('5-9 r', 'rrrrrrrhcr'),
    ('17-20 h', 'hhshshhhhhhhshhhbhhq'),
    ('7-9 s', 'dngddfsss'),
    ('12-13 q', 'qqqqqqqqqqqcq'),
    ('2-6 v', 'vqtvvvv'),
    ('8-10 c', 'cccfcncccccc'),
    ('14-15 m', 'mmmmmmmmmmmmmmdm'),
    ('7-14 s', 'ssslssfdssflvvsj'),
    ('2-5 z', 'wcllj'),
    ('2-11 n', 'cvnrlftcjct'),
    ('8-16 k', 'krzkfbkkqkhnsjkjgkk'),
    ('2-7 q', 'mvhvqnzdjw'),
    ('5-8 l', 'lgbnlnclkllll'),
    ('4-12 l', 'llllmllrlgllrklnlrbt'),
    ('7-10 j', 'jjjjjjnjjcjsj'),
    ('1-2 k', 'dgwmgsn'),
    ('2-5 z', 'zjmxc'),
    ('6-7 c', 'ccccccccc'),
    ('14-17 k', 'bkkkkkkkkkkkndkkkk'),
    ('2-4 x', 'xxjxtxbq'),
    ('7-9 w', 'drjcfwzwwwfwwfzxww'),
    ('4-5 p', 'pppwc'),
    ('4-5 r', 'rrrvm'),
    ('1-8 r', 'qrrrmrrrrr'),
    ('16-18 l', 'llllllllldllltlklk'),
    ('1-11 p', 'pwcpppbppppppp'),
    ('5-19 w', 'wwwwwwwwwwwwwwwcwww'),
    ('17-18 k', 'kkkkkwkkkkkkkkkkkxk'),
    ('12-15 f', 'fsffffffflfqgfx'),
    ('6-13 d', 'zddpdvddrvrdxq'),
    ('1-10 f', 'ffffffrfkb'),
    ('13-14 x', 'xxxxxxxxxxxxxxx'),
    ('16-20 j', 'jjjjjjjdwjjfjjjjjjdj'),
    ('8-11 r', 'rrrrrrrrrrrr'),
    ('15-16 x', 'dxjxxxdxxxxxxxxxwxx'),
    ('3-9 m', 'mjhqdgkmzmsmtdmhfn'),
    ('2-7 k', 'kkkhwgtxlkmkqkk'),
    ('11-15 m', 'mmgmmmmnsjmmlmmm'),
    ('1-2 v', 'wvvk'),
    ('8-14 s', 'zssssssssssssts'),
    ('3-4 z', 'ztbzzr'),
    ('4-10 x', 'xxkmqxxxxx'),
    ('3-5 p', 'pkppppppppzpp'),
    ('3-15 q', 'qpqmkqfqqlqqdfqtkqq'),
    ('16-17 d', 'ddddddzbxcdddcddq'),
    ('4-5 s', 'nqssf'),
    ('4-5 s', 'sssbks'),
    ('4-5 s', 'tsjlhsbsmt'),
    ('1-5 z', 'zzzbztzf'),
    ('1-4 l', 'pvsgtvt'),
    ('3-6 b', 'bbbjbb'),
    ('2-4 d', 'wkdvd'),
    ('16-18 w', 'wwwwwwwrwwwwwwwzwkw'),
    ('15-17 t', 'tqttjttttttttvtttt'),
    ('5-9 q', 'qcqqqqdtqq'),
    ('8-11 s', 'sssssssfssssssssssss'),
    ('5-6 x', 'xxxvcpbxr'),
    ('13-15 d', 'ddwdtctnjdcdpch'),
    ('5-6 z', 'zzzwzzzq'),
    ('3-7 v', 'bsphcnvwvtvphdp'),
    ('3-4 q', 'vhcprqqgdmlfpwqqw'),
    ('11-18 b', 'bfbbbfbbbbvhwbbbzlb'),
    ('12-15 c', 'cccccccccccccqfcc'),
    ('4-10 j', 'jjjjjjjjjjjw'),
    ('8-14 s', 'ssssssspmssssssssms'),
    ('6-15 b', 'jxnbdvxbbbcbrsbxrs'),
    ('10-12 s', 'ssssjsssssfs'),
    ('8-12 f', 'ffffdfkqflfpf'),
    ('8-9 w', 'wwwwwwwwz'),
    ('7-10 z', 'fzzlzzbtmthzzzz'),
    ('2-3 k', 'kqzzb'),
    ('11-12 s', 'ssssssssssls'),
    ('16-17 r', 'rrrrhrrrrrrrrrrnr'),
    ('3-11 b', 'czpbpbzswgcddm'),
    ('4-8 z', 'cnzztzgzqz'),
    ('18-19 m', 'mjmmmmmmmmmmmmmmmpk'),
    ('10-13 q', 'gqqqqqqsxqqqqdtqkq'),
    ('10-11 x', 'nxmbxxxrgpmxxxfnxxxz'),
    ('2-5 x', 'xbxzrxd'),
    ('9-14 l', 'llllpljlllfllwv'),
    ('1-2 m', 'mmmmmm'),
    ('1-3 b', 'fblbbfbbbbbtbbgbbb'),
    ('3-4 g', 'gnnccg'),
    ('8-9 f', 'fffffffkffff'),
    ('5-6 r', 'rrrrhf'),
    ('7-8 l', 'lwlwllllllctl'),
    ('5-7 j', 'jrjjwgjvkkncnjbqc'),
    ('3-4 b', 'bbsbb'),
    ('4-13 c', 'jmcczvkbxccdf'),
    ('4-5 g', 'wgrgg'),
    ('7-8 d', 'dgddddzh'),
    ('3-8 h', 'hhbhhhhhhhh'),
    ('15-16 l', 'llldllllllldlllllll'),
    ('11-15 r', 'rrgrrrrrrrnrrgxr'),
    ('10-11 l', 'lllllllllll'),
    ('4-5 x', 'xfdbjsmbbcxdphvlfkxr'),
    ('9-12 m', 'rqmnmrmhcmmms'),
    ('3-8 b', 'tzsnnndnbwgbskbb'),
    ('4-10 v', 'vvkvvdrvwvc'),
    ('9-11 j', 'jjjdjjjjjsj'),
    ('6-11 b', 'hbbmbbbbbbjbtrbbbz'),
    ('13-16 v', 'vvpvvvbvcvvvvvvvv'),
    ('11-14 j', 'jjjjjjljjjtjjmj'),
    ('7-11 v', 'cvdglnvjxkvvgptxvp'),
    ('1-6 t', 'ttjqtttzt'),
    ('7-10 f', 'ffwpzfxjfgffzf'),
    ('4-7 d', 'dddgddp'),
    ('4-19 n', 'mjbdzqxhtfbnbfxrpgnh'),
    ('6-13 d', 'ddddddddddddd'),
    ('2-4 t', 'rhkd'),
    ('5-9 c', 'ccrcxzjdzccx'),
    ('3-4 j', 'fwjj'),
    ('15-19 q', 'qqqtxqqqqqqqqqqqqqqq'),
    ('1-11 c', 'gcccccmccctcc'),
    ('3-5 d', 'dxhhdr'),
    ('8-12 k', 'pkvrkkkvkkmbkcxjwktk'),
    ('9-11 p', 'ppnpppppxppp'),
    ('11-12 p', 'dppcsppppppqppp'),
    ('7-8 b', 'bbbbbbmbqp'),
    ('7-8 c', 'cbccccccc'),
    ('8-9 b', 'bbbbbbbcrbb'),
    ('2-6 z', 'gzlnpzpkhjwwqtswcrz'),
    ('5-6 d', 'dddsdkd'),
    ('1-5 w', 'dxwkgwwwwwwmwwwww'),
    ('4-7 q', 'qqqnwqlqrqdcqpq'),
    ('6-9 m', 'lmmmdmmvmmmm'),
    ('7-8 h', 'hhhghhxh'),
    ('2-3 j', 'jjjj'),
    ('1-4 r', 'rrrw'),
    ('4-7 m', 'mmjmmrm'),
    ('4-5 j', 'vljjrj'),
    ('19-20 j', 'jjjjjtjjjjjjjjjjjjgx'),
    ('2-6 h', 'xhltfh'),
    ('5-11 s', 'ssssjsssssss'),
    ('3-4 b', 'bbbb'),
    ('1-5 g', 'chgmtgnn'),
    ('6-7 j', 'jjjjjjz'),
    ('3-8 c', 'cccccrccccc'),
    ('3-17 s', 'sslstssssssssspsgs'),
    ('17-18 x', 'bxxxxxxxqxxxxxxxkwxx'),
    ('9-10 q', 'qfqqzqqqsddqqqqqqq'),
    ('6-10 k', 'kmkkkxvqkrk'),
    ('5-9 f', 'kffffffffcdfffffplf'),
    ('5-6 r', 'rrrrrz'),
    ('2-5 d', 'hdgzt'),
    ('7-10 k', 'zkrllwkkkjrkqfkkk'),
    ('9-11 b', 'bbrkbbbbcbqqb'),
    ('8-12 g', 'gfgkgggggggggggggg'),
    ('12-14 s', 'sssjsspstlvlsrsssss'),
    ('4-8 g', 'pqgzcgvgflgntlp'),
    ('13-14 j', 'jjjjjjjjjjjjjx'),
    ('4-6 k', 'kkkmqpk'),
    ('3-5 j', 'sjjbjlvjjvjr'),
    ('2-9 c', 'ckccjxzcrcctbfn'),
    ('10-12 n', 'hvnnnnxnntnlnn'),
    ('11-15 m', 'mmrmmmdmmmlmmmjqm'),
    ('6-8 p', 'qpzrrpcpbxg'),
    ('5-8 w', 'xwdzcgclxwsvfwtwbxnw'),
    ('3-8 q', 'qzqzhlzc'),
    ('2-3 v', 'hvvvvltft'),
    ('5-12 s', 'tgvsswttkwfssnsqjsxk'),
    ('5-17 b', 'bbbbbbbbbbbrbcbbbhb'),
    ('3-6 p', 'ppjpzw'),
    ('3-5 k', 'kkxvkswk'),
    ('4-8 v', 'vbvrvxvgrvvwwvvm'),
    ('3-12 v', 'njvvgvdcjvvtvvcnvg'),
    ('4-5 n', 'bnnnrn'),
    ('8-9 l', 'jlvxdlpll'),
    ('12-14 w', 'fkwwwwwwcwwjwmwc'),
    ('1-4 q', 'wmqrzpqhj'),
    ('4-7 t', 'tctsttlt'),
    ('13-14 h', 'hhhhhhhhhhhhhf'),
    ('2-3 j', 'jmjjjjj'),
    ('5-6 v', 'vvvvlv'),
    ('5-13 v', 'fnxvvvvvnvqvvvvvws'),
    ('16-17 l', 'gllllllllllgwqlll'),
    ('1-2 s', 'pnpfsqw'),
    ('6-13 g', 'ntzqggvbnwxrgskg'),
    ('5-12 k', 'krxmbxqbkhxlnvdxdkkq'),
    ('14-18 d', 'ddddddddjdddbdddddd'),
    ('4-7 z', 'zzzzxzzs'),
    ('15-18 d', 'dddddddddbddddpddh'),
    ('8-11 x', 'slxxxxxjkxxxrsdx'),
    ('4-6 n', 'nnnfzzn'),
    ('1-4 h', 'gslcmnhhfhvz'),
    ('1-4 d', 'tddqds'),
    ('2-3 c', 'fccp'),
    ('2-5 k', 'mkqrknj'),
    ('9-16 g', 'gpggdggwgwgwglggg'),
    ('2-5 h', 'hhjds'),
    ('4-5 b', 'zbnvld'),
    ('6-14 m', 'mfqmnmqtdmmzmm'),
    ('7-8 j', 'thvcsgjn'),
    ('1-5 x', 'xwjdxdqjtc'),
    ('4-17 r', 'fqbrqrnpslndrmjdhpjp'),
    ('4-5 c', 'ccccw'),
    ('5-6 v', 'vvvvdm'),
    ('5-12 n', 'nnqzjntfnnnd'),
    ('3-4 c', 'nccqlccq'),
    ('1-10 p', 'nrvvzpppqpn'),
    ('9-16 v', 'jvvrpvvvvvzvhhvvgz'),
    ('12-13 s', 'sjsslsssfxxkrssstkss'),
    ('1-3 t', 'vtwbh'),
    ('5-16 q', 'sxxfrqhqtvzbzqwg'),
    ('5-9 z', 'dnzlhzzzsdzz'),
    ('15-16 d', 'pdddddjddpkdddtdddd'),
    ('3-4 p', 'pplqppp'),
    ('7-9 s', 'scsslshsqssw'),
    ('2-3 v', 'vxvxv'),
    ('8-9 w', 'wqwwwwwgshww'),
    ('8-9 k', 'kkkkkkkkc'),
    ('9-10 v', 'vhfvvnvvtvvb'),
    ('1-12 z', 'zzzbzzzzzzzdzzzz'),
    ('6-7 b', 'bbbbbwhb'),
    ('12-13 z', 'zzzsvtlzzzzzz'),
    ('1-3 s', 'pssssssxw'),
    ('8-9 w', 'xwwwwwwdzw'),
    ('1-4 x', 'xxkxxx'),
    ('10-12 f', 'fffffffpffvffff'),
    ('18-19 w', 'wwspwwzwwqcrwwhwwww'),
    ('6-8 s', 'ssssstsks'),
    ('5-6 j', 'jjcjgm'),
    ('2-5 p', 'wprwpxbdkrfpmppqpd'),
    ('8-18 n', 'nnnnnnnnnnnnnnnnnn'),
    ('4-11 c', 'txncpqclrlc'),
    ('2-10 f', 'ffcffftfffxrxf'),
    ('1-4 t', 'ttttttt'),
    ('4-9 f', 'zdpjffffbfbl'),
    ('6-7 f', 'kfsffffffm'),
    ('1-4 b', 'bbdn'),
    ('6-12 k', 'kkhkkkkdqkbkjkkkl'),
    ('3-4 n', 'kmnn'),
    ('4-11 l', 'kllcllldllclll'),
    ('7-19 w', 'pfwdwdnkblwzgkfnfmh'),
    ('3-9 z', 'zzphzdnhqwlzzwzz'),
    ('15-16 h', 'hhhhhhhnhhhhhhhd'),
    ('1-4 l', 'vllll'),
    ('2-13 l', 'hdhvgdrlltlmjptzq'),
    ('1-3 p', 'njvpltppbkxpfpppp'),
    ('1-2 j', 'kkjv'),
    ('10-11 c', 'ccccccmcccjcc'),
    ('5-8 v', 'tqvmvtwvzfczvvvvw'),
    ('6-9 x', 'xxmxxxfxxxxx'),
    ('1-10 z', 'zgzzztmdtkzzpxztbgpp'),
    ('10-12 g', 'ggwzjgdsgbnggl'),
    ('5-6 j', 'jvxjvjj'),
    ('4-7 x', 'xnxxmgxxtjxxkj'),
    ('13-14 d', 'ddddmddddddddd'),
    ('12-15 c', 'cccccccccccnccc'),
    ('16-17 n', 'nnnnnnnntnnnnngnmn'),
    ('1-12 m', 'bzckgvmmbdcxtgtmb'),
    ('4-7 l', 'ljllllljl'),
    ('5-11 w', 'wzvzwwrkmtwh'),
    ('11-13 l', 'lmtpwxlllhlgllwvqnp'),
    ('6-10 f', 'fvgkffqvcfffdbfff'),
    ('3-5 j', 'kbfjjj'),
    ('1-2 h', 'hhztdpbttnc'),
    ('8-10 b', 'bbbbjbbqkbbbd'),
    ('1-13 c', 'hccvcxtcclpckzd'),
    ('6-10 w', 'wwwwwtwwzrwwf'),
    ('2-3 j', 'fjnnj'),
    ('2-4 j', 'njtjjjxrjv'),
    ('4-5 w', 'fwwzw'),
    ('7-9 k', 'qbnkghdbqlz'),
    ('2-9 s', 'dsdftlzsszlf'),
    ('4-5 v', 'vvvvd'),
    ('1-2 w', 'fbfwwb'),
    ('4-7 t', 'tttttmt'),
    ('3-10 h', 'hhhhnhhhskhh'),
    ('3-8 w', 'qwswwswfl'),
    ('1-3 p', 'pmpgpp'),
    ('2-7 n', 'nmmgnssmtn'),
    ('2-3 j', 'djvjgjp'),
    ('6-13 x', 'jxxbxxgnxvbxx'),
    ('6-10 v', 'vrvvvvvvdz'),
    ('2-3 b', 'bbbbjrkwnc'),
    ('1-2 h', 'fshnf'),
    ('1-5 n', 'htsknrzqnntknfnjx'),
    ('5-9 d', 'kkgtwrdjmxkzc'),
    ('12-13 x', 'xxxxxxxxxxxxx'),
    ('2-10 m', 'wmmmmmdpmmmmh'),
    ('2-12 n', 'xttqcmfkvnlkzskjhmzn'),
    ('6-9 m', 'mmmmmxmkp'),
    ('10-16 m', 'gmmdqmjmflmmmmmcmmm'),
    ('13-14 p', 'pprprppppspxfgnptppp'),
    ('1-16 b', 'gcnbbnbbmsjxnbppcb'),
    ('10-11 d', 'dkdddddfjmpvdddd'),
    ('1-9 f', 'zlfwstnzp'),
    ('14-15 n', 'nnnnnndnnnnnrnnvcndn'),
    ('2-6 l', 'lvvldlzdzgdf'),
    ('6-10 z', 'zzzzztzzzhzz'),
    ('13-14 n', 'nnnnnnnnnnnngln'),
    ('8-9 z', 'zjqztzztqzzbxzz'),
    ('2-3 v', 'dwcv'),
    ('4-6 m', 'kmmmkmm'),
    ('5-9 g', 'wtgfgdmxkx'),
    ('3-5 b', 'vbzbf'),
    ('10-11 w', 'wwwwwwwvwwz'),
    ('2-8 s', 'sztstsnssq'),
    ('2-6 l', 'lldzcslxdwghmn'),
    ('1-2 n', 'vmznndnnnbrhknjwzkzx'),
    ('3-4 k', 'kknp'),
    ('1-5 h', 'hhhhhhh'),
    ('12-13 z', 'zzzzzlszzzzzxz'),
    ('1-12 m', 'mtbspfpdgpznrsmvgq'),
    ('11-13 q', 'qqqqkqnqhqrqrq'),
    ('14-18 d', 'dtdrdddddddddxfddddd'),
    ('1-6 q', 'bqqqqqgqqqq'),
    ('1-7 c', 'dlmvcsztzpx'),
    ('4-6 g', 'gmgggg'),
    ('5-6 s', 'ssswsssgdghv'),
    ('8-9 k', 'kkkkkkkgn'),
    ('1-17 s', 'ssssssssssksssssss'),
    ('4-5 b', 'qqtlsh'),
    ('5-6 g', 'gggggg'),
    ('2-11 r', 'drkpvrrlrtrvrjhpd'),
    ('3-7 k', 'fkkhmddh'),
    ('6-7 h', 'hhhwhnfph'),
    ('3-4 p', 'ptppmwpnps'),
    ('3-6 w', 'hwcshlrm'),
    ('7-8 d', 'dtddqddzn'),
    ('1-6 s', 'sslsbssbsg'),
    ('12-15 n', 'tbnnjknnkwnnnnsnnnz'),
    ('8-9 z', 'zzzzzzzzz'),
    ('2-5 w', 'kjnwn'),
    ('4-7 m', 'mmmtdjmmmmtl'),
    ('4-7 h', 'dqfhzrqhfhntzhkhhdvb'),
    ('3-5 g', 'zvflgg'),
    ('5-12 s', 'lvsvqnvssgcx'),
    ('11-19 p', 'pcppvppplpwppppjlps'),
    ('5-19 p', 'gkpmfxlmppczdnhbqcw'),
    ('5-17 b', 'mdzljsdvxdmbbbbddvrw'),
    ('1-5 s', 'shpdss'),
    ('2-5 t', 'btggtltvw'),
    ('1-6 b', 'sbbbbbb'),
    ('3-6 w', 'wwpsfkwnrrr'),
    ('13-18 f', 'ffffwfffsfffwffffn'),
    ('4-5 m', 'mpmmmxmmggvnb'),
    ('5-6 z', 'pwsqhcztlf'),
    ('8-11 d', 'ddddddddddlf'),
    ('1-2 t', 'xttt'),
    ('6-8 m', 'mmmpmvmmm'),
    ('16-17 h', 'hhhhhhhhhhhhhhhrw'),
    ('1-5 g', 'gpgpgg'),
    ('3-7 p', 'gplrpzp'),
    ('11-18 t', 'ftqnxttzttxtgttntrtt'),
    ('10-11 z', 'zzzzzzdzzlgzzz'),
    ('3-10 z', 'lzfzzzzszbzzztj'),
    ('2-10 l', 'khdbddnxltnk'),
    ('4-8 b', 'tbbcjsnbrbhfb'),
    ('3-6 x', 'xgsxmn'),
    ('9-13 t', 'ttttttttmtttt'),
    ('7-11 l', 'fllllllzllmdshrll'),
    ('18-19 g', 'hffqfwssgqpcnmddkcw'),
    ('3-4 m', 'mmhvmc'),
    ('1-3 w', 'vwnw'),
    ('5-6 r', 'rrrrrb'),
    ('2-4 j', 'rjqj'),
    ('5-7 b', 'kgblcbbdrb'),
    ('3-5 g', 'jgggggg'),
    ('1-11 v', 'vvrvvhxvrvvnrvvv'),
    ('3-14 w', 'ncwphcwvjwhdpwqkg'),
    ('6-7 x', 'xxxfqmkvxx'),
    ('13-14 v', 'vvvvvvvvvvvvkt'),
    ('2-12 x', 'xzcvvxhhwwxxc'),
    ('6-14 m', 'mdtnmjmhmnmmmmm'),
    ('15-16 z', 'zzzzzzzzzznzzzzzzz'),
    ('4-6 s', 'mcssdssjshscvcl'),
    ('11-12 b', 'bnbbbmbjsbxbbbbbj'),
    ('7-13 c', 'cccfhccczccwcccsc'),
    ('3-4 m', 'cgtmmm'),
    ('5-10 l', 'hxhbggrllmtgn'),
    ('6-8 d', 'sdfdddlv'),
    ('4-9 x', 'xxxxxvxxcx'),
    ('11-12 c', 'rcmqkzjccccrdccmc'),
    ('1-3 g', 'jgng'),
    ('4-5 l', 'lvlll'),
    ('9-16 n', 'rnnnqjnvqnnnlnnwdnnn'),
    ('4-10 x', 'crdxgxrfjhr'),
    ('1-5 f', 'tgdffffffqf'),
    ('15-16 q', 'qqqqqqqqvqbfqknqqqqq'),
    ('9-11 s', 'sssnffssksq'),
    ('3-4 v', 'vqvvv'),
    ('5-19 z', 'jthjzpgmwjbftzvmnpzk'),
    ('3-10 w', 'mpxhrrnqdvncwssqwlxz'),
    ('14-15 b', 'bzbbbbbsbbbbbbbbbbb'),
    ('3-5 j', 'jpjvjjrjtmjj'),
    ('3-6 w', 'wwmwwzw'),
    ('1-6 c', 'ccccvzcccm'),
    ('10-11 m', 'mmvwgmjmmmrqjmmmglm'),
    ('2-3 f', 'fffw'),
    ('6-12 m', 'bmbzmmrshmmz'),
    ('5-6 n', 'nnnnnn'),
    ('4-5 k', 'kmsgkwvkk'),
    ('6-8 t', 'tttttbttt'),
    ('4-5 j', 'vtmvsqjl'),
    ('5-6 q', 'qshzdqqk'),
    ('1-3 w', 'dwgw'),
    ('8-9 q', 'qbqqqqqwq'),
    ('5-10 m', 'lmmmkgmmwb'),
    ('6-9 n', 'nnnlnnnnn'),
    ('4-5 t', 'tntct'),
    ('6-8 g', 'hgngghgw'),
    ('6-9 t', 'gttwtgvpgtlt'),
    ('6-7 l', 'lllllll'),
    ('4-5 j', 'jhjkjjm'),
    ('13-15 h', 'hhhhhhhhhhhhxnh'),
    ('1-4 m', 'mmmmm'),
    ('4-6 q', 'cqrtqsdqqzrknf'),
    ('9-13 f', 'fffffffffzfvff'),
    ('2-16 p', 'prxdxjpkppgpxsjwpppp'),
    ('3-4 r', 'rrzh'),
    ('1-2 g', 'cglblsnkg'),
    ('1-3 f', 'xqnfwjmmwqffd'),
    ('13-14 q', 'qqqqqqqqqqqqvjqq'),
    ('18-19 g', 'dggggggggggggggggvgg'),
    ('5-6 s', 'dsssssss'),
    ('4-6 z', 'szdzzb'),
    ('9-12 t', 'xtltpgftttmtt'),
    ('10-16 m', 'mqmmmmmmmcmmmmqx'),
    ('3-7 c', 'cpccngcvccm'),
    ('2-16 s', 'jsdfsjsjtswhkvmsskj'),
    ('2-3 c', 'kccc'),
    ('4-16 k', 'qhndnqmrvjcczfkpds'),
    ('4-6 n', 'nnnrkxl'),
    ('9-10 s', 'ssssssssds'),
    ('2-3 z', 'hfzcz'),
    ('2-3 s', 'sssz'),
    ('8-10 b', 'qbbbjbbbbw'),
    ('7-16 k', 'gcvskkjkkkkwkzkz'),
    ('7-9 n', 'nnnnnnhnnnn'),
    ('1-10 q', 'qjxqmqxcgg'),
    ('9-11 l', 'jdhjbbcnlzll'),
    ('7-14 l', 'llrlxlllllltlnl'),
    ('3-6 f', 'wfdqfbrf'),
    ('3-8 t', 'ttzttmtvttzpl'),
    ('10-12 v', 'vfvvvvvvvsvv'),
    ('5-6 v', 'vvvvvm'),
    ('11-13 t', 'ttttxtttttptttctttt'),
    ('3-4 k', 'kkdm'),
    ('4-6 n', 'nnnlnt'),
    ('13-15 m', 'mmmmmbmmmbmmmmmm'),
    ('5-6 l', 'klllnl'),
    ('2-3 f', 'flzff'),
    ('3-4 r', 'frrs'),
    ('1-5 d', 'cqwkvsdqdvb'),
    ('9-15 l', 'jvtfqczlnlwdpclxwp'),
    ('12-14 t', 'ttttttlqtpttnt'),
    ('11-12 m', 'mmmmmmmmmmmm'),
    ('4-5 j', 'jjjkbjjjjj'),
    ('9-12 w', 'wwwwwwwwkwxkwcb'),
    ('6-12 q', 'tcqrqqqqxjqqqqmqhq'),
    ('5-6 m', 'mmmsmmmm'),
    ('2-5 t', 'mttbttprttddtv'),
    ('10-13 t', 'tttttttttttztt'),
    ('10-11 f', 'kmqfxttfkfd'),
    ('5-7 v', 'vrlzpvjtvv'),
    ('6-7 l', 'nlllllj'),
    ('1-5 q', 'szdbqqkqqtkmssq'),
    ('3-4 q', 'kcmlwqzczwms'),
    ('13-16 b', 'bsbbbbbbbbrbsbbpzbb'),
    ('9-11 d', 'dddsdbddkdkdd'),
    ('2-15 j', 'xkjnntffvvxfnntcv'),
    ('4-6 v', 'hvvvcvqvrwv'),
    ('9-12 j', 'qjjjjdjgqhrjjfjrdj'),
    ('8-10 v', 'vvvvvvvnvnvv'),
    ('4-9 t', 'ttttthttt'),
    ('8-16 g', 'ggggklggcggggxgg'),
    ('1-3 z', 'wpqz'),
    ('4-5 g', 'wgdnmxccgj'),
    ('8-11 r', 'rrrrrrrxrrmd'),
    ('1-9 f', 'ffffsfgdbsqfffzf'),
    ('7-8 q', 'qzqqqqrrq'),
    ('12-13 n', 'nnnnnnnnnnnnnn'),
    ('8-12 j', 'jpjjjmjjjjjzj'),
    ('1-4 j', 'nvjw'),
    ('7-13 z', 'zzzzsnzxzznzrzgzzzz'),
    ('14-16 z', 'zzzzzzzzzzzzzzzm'),
    ('1-4 x', 'xxxxnxh'),
    ('8-15 k', 'gnrkktkpcmklkksnkk'),
    ('2-4 h', 'klph'),
    ('11-16 c', 'ccckzdccgckpcccsc'),
    ('15-16 l', 'dlllllllllllllll'),
    ('2-3 s', 'dsxss'),
    ('1-4 v', 'jvvv'),
    ('2-8 t', 'ktkdtxkt'),
    ('1-3 t', 'ftftttttt'),
    ('4-5 k', 'kkkbkk'),
    ('4-6 g', 'llqcggg'),
    ('4-14 r', 'fmdvrrwlstlbjr'),
    ('2-16 p', 'rpdfhpbqfwxlxhhc'),
    ('6-8 j', 'jjjjjjjjj'),
    ('1-7 f', 'fnnffblbqffkrff'),
    ('1-3 k', 'rfqwlnnkzdq'),
    ('15-16 s', 'ssssswssssssskssss'),
    ('11-13 z', 'zzzzngfzzzzzz'),
    ('5-7 h', 'hhbhhcnhfghhhv'),
    ('2-7 j', 'zjrmjgmjdkp'),
    ('5-8 z', 'bzzzpzzrzzzz'),
    ('12-16 j', 'jtjnjjjjgjjjjjjsj'),
    ('5-9 s', 'ssssssssms'),
    ('2-3 s', 'ssss'),
    ('13-14 d', 'ddddddddddddkt'),
    ('12-13 r', 'wfdtrknrhvrrc'),
    ('6-8 p', 'vpxphxngzhnkppppfp'),
    ('2-3 j', 'jtjx'),
    ('3-6 k', 'tkkvjkb'),
    ('2-6 t', 'tvftftvbfx'),
    ('5-7 z', 'zzzqzzz'),
    ('14-15 h', 'whdhxhhhhhhhfxzhhh'),
    ('3-4 g', 'ngjgg'),
    ('9-10 z', 'zzzzztzztq'),
    ('2-7 f', 'fffffqfszchff'),
    ('4-6 f', 'lfqjnzccffjslsdf'),
    ('5-6 z', 'lpzzzzsz'),
    ('11-13 t', 'tttttwtttttttttttt'),
    ('2-6 z', 'zzzzzz'),
    ('9-10 m', 'mmmmmmmmjm'),
    ('5-6 w', 'xwggfcwvwlx'),
    ('1-4 j', 'jjjjjljjjjjjj'),
    ('8-10 t', 'ttttttwttt'),
    ('5-12 x', 'zxxxxxxpxxxn'),
    ('3-4 v', 'vvlrv'),
    ('3-6 h', 'hhhwhlxhlrhl'),
    ('2-5 p', 'cptsjktp'),
    ('4-11 j', 'bmjjjjjjnwwdk'),
    ('15-17 p', 'ppppppppppfpppvpp'),
    ('7-11 m', 'wnnmmwmtmmxmm'),
    ('9-19 k', 'kkkkkjkkhwkcvkkkmknw'),
    ('11-15 s', 'sspssbshssscssssss'),
    ('1-8 s', 'sssssmssssssssssss'),
    ('4-8 x', 'xxxxdxxx'),
    ('9-10 n', 'nnnrnlnnnnnnnnnnnnnn'),
    ('10-11 d', 'ddddddddddn'),
    ('5-9 z', 'tzzzqzbmzzzqzjkzlr'),
    ('9-20 f', 'fffffnfffffffsfnffff'),
    ('5-6 g', 'gvggggg'),
    ('13-14 x', 'xxxxxxxxxxxxxxx'),
    ('6-7 v', 'vvvzvvvv'),
    ('5-10 l', 'kbcvlfvlszndtlldjlh'),
    ('4-9 s', 'vkcsdvszthkwmmmxs'),
    ('3-4 b', 'jbmb'),
    ('2-4 w', 'nmwm'),
    ('5-10 z', 'tztzzfzgdzzszq'),
    ('2-8 k', 'kzkkkkzwf'),
    ('16-17 d', 'vxvzdgzwssqdcgbdb'),
    ('4-5 b', 'bbbbb'),
    ('7-9 w', 'wwfwwwjwln'),
    ('5-12 k', 'ljkkkqfvqtkkxsd'),
    ('5-7 q', 'qqqqhqqq'),
    ('8-9 n', 'vnnnnnnpstnn'),
    ('5-10 m', 'mmgzmmmmmm'),
    ('3-14 q', 'qgbvqjxqnqqqqqqq'),
    ('2-4 c', 'cccc'),
    ('3-7 b', 'szbbkbdbmbbzbqs'),
    ('1-5 m', 'mhmmc'),
    ('3-6 n', 'nnlvnnvnq'),
    ('2-3 c', 'mccc'),
    ('11-12 m', 'ddmmmmxmmmmwfmmm'),
    ('8-10 n', 'nnnnnrnnnn'),
    ('1-12 g', 'sgbggglnggddgggsngrx'),
    ('7-9 p', 'phppppppp'),
    ('4-5 q', 'qxqqqq'),
    ('3-7 v', 'vwsvvrvxvvvvvvwvvdlv'),
    ('8-18 j', 'jmjcjjltjmjwjzrllgcj'),
    ('2-14 r', 'rdrrrrrrrrrrrp'),
    ('2-4 r', 'cxcbkmr'),
    ('6-9 r', 'vtlnnvbcndqhrxkkjp'),
    ('2-3 s', 'hxssnsswzc'),
    ('10-16 r', 'csrsrxrrrrrrfrfdrr'),
    ('7-9 w', 'wwbwmvrwdxww'),
    ('12-14 p', 'pppbpppppppgpt'),
    ('2-7 n', 'nnnnnnnn'),
    ('3-12 f', 'mhjxfxgbbvffpclfffg'),
    ('10-14 l', 'lllskllljllllll'),
    ('11-16 l', 'lwlklllglzllllllll'),
    ('13-14 h', 'hhhhhhhhhhhhhdhhhh'),
    ('1-2 t', 'tttb'),
    ('1-6 z', 'zzzrrzzbf'),
    ('1-6 v', 'jrvzvvrs'),
    ('3-6 g', 'jggbnl'),
    ('17-18 x', 'xxxxxxxxxxxxxxxxrx'),
    ('8-17 f', 'xnmffffbwfdcfrdfw'),
    ('3-9 k', 'jmkdvkdnk'),
    ('7-9 m', 'mmmmmmdml'),
    ('9-11 c', 'cdmshccckqmcccccckp'),
    ('16-17 g', 'gggggngggggggggggdg'),
    ('7-8 n', 'nnknnnnnnn'),
    ('3-13 n', 'fjhgrspsnkmnf'),
    ('14-17 z', 'zzzzzzzzzzzzzqzzzzzt'),
    ('13-14 r', 'rrrtrrfsvrzngw'),
    ('7-8 k', 'kvkvkpvc'),
    ('1-2 b', 'bbpbb'),
    ('1-7 n', 'tchnrtbtldnmnnvvnn'),
    ('3-4 s', 'sssssjv'),
    ('1-9 l', 'cllllztmlllrzfl'),
    ('9-10 x', 'qjxxxxxxdhxxxxxh'),
    ('6-7 p', 'ppppfppv'),
    ('3-8 q', 'mkqzqqbqzjrqbq'),
    ('6-8 x', 'xxxxxxxx'),
    ('1-7 f', 'ffffffff'),
    ('5-16 b', 'jbbbbbqcbbbbbbfb'),
    ('9-11 c', 'ccccccccccq'),
    ('1-2 x', 'fqkx'),
    ('4-12 z', 'znzzzzzzzzzzzzz'),
    ('3-4 l', 'lglll'),
    ('9-11 m', 'mmmmmmmmmms'),
    ('14-17 x', 'xrxpxgkxxzdrxxxxckxv'),
    ('3-5 t', 'gxjbbfcpmkbkxbtwbt'),
    ('5-6 j', 'jmjjjj'),
    ('14-15 g', 'ggggggggggggggx'),
    ('6-7 l', 'lllllbl'),
    ('2-14 q', 'qqtsqkqvqqqpxzqqcqq'),
    ('2-4 w', 'fwhw'),
    ('4-5 m', 'mzmtkm'),
    ('2-4 g', 'ghghgp'),
    ('5-6 r', 'rrrrnl'),
    ('1-4 h', 'chghhw'),
    ('7-12 r', 'rrrzglvrrrrsrr'),
    ('1-7 x', 'xxcxdwxjmx'),
    ('5-12 r', 'rrgrrffwtrrnrrqrrjnr'),
    ('2-5 r', 'srdqrlxrkrrdkr'),
    ('3-4 t', 'ttdg'),
    ('11-12 s', 'bfjrkqqgdtlwrskmfrp'),
    ('3-5 n', 'nnrnfzsnm'),
    ('10-15 z', 'zzzzhzzqqczxwzqztv'),
    ('2-7 f', 'ffgdfgff'),
    ('7-10 d', 'ddtbdddddjtdqfdddfq'),
    ('2-9 k', 'gkrkkkkkkkkhkqkx'),
    ('13-14 n', 'nngnlnnnhnnnnnnnn'),
    ('6-9 r', 'qrxrxzrff'),
    ('7-9 m', 'mmmmmtmqqmml'),
    ('11-12 p', 'pppppppppppp'),
    ('10-13 j', 'jjjjjjjjjznvbjj'),
    ('1-2 c', 'ccvc'),
    ('7-8 m', 'mmmmtdmckkpmcbkjmm'),
    ('5-8 j', 'sjptjjbjjjjj'),
    ('6-8 d', 'jchdwrhd'),
    ('5-6 z', 'lqzzzzkrzzvzwbbzktp'),
    ('6-8 l', 'ztbltlll'),
    ('2-3 z', 'zkrxzp'),
    ('7-18 g', 'phgpgggqgzgnmwlpkwd'),
    ('8-9 f', 'hffffffqf'),
    ('17-19 p', 'pppppphpppppppppzpp'),
    ('2-3 z', 'zzzfg'),
    ('1-2 v', 'bfvj'),
    ('4-8 b', 'bcbbbbbb'),
    ('15-16 s', 'ppsnsssssssnssss'),
    ('2-3 m', 'mnsm'),
    ('2-4 h', 'hwfshh'),
    ('9-15 h', 'hhwhhhhxhhhhhhh'),
    ('17-18 n', 'nnnnnnnnnnnnnnnnnn'),
    ('7-11 n', 'nnnnnqpnlbgqnqnshn'),
    ('15-16 j', 'cdjmbcwdppvvjqvv'),
    ('6-11 p', 'ppplppppxpt'),
    ('4-5 r', 'rrrrrr'),
    ('10-11 w', 'wwwwwwwwwww'),
    ('3-7 p', 'pzppzspppmkxbldwpnwf'),
    ('2-12 w', 'zwdljlzwgxfwvtdm'),
    ('2-10 f', 'mzfjqfspgfrfhst'),
    ('14-15 m', 'mzmmmvhwmdmmdpz'),
    ('1-12 r', 'vrxrrtrxgvrd'),
    ('4-5 n', 'nnnnnnpn'),
    ('6-12 x', 'xkbwfsxxxxxkxxxxk'),
    ('4-6 n', 'mncnxn'),
    ('9-10 f', 'ffffpfqftbf'),
    ('3-5 b', 'bzwbk'),
    ('4-7 c', 'ncdcccc'),
    ('11-12 t', 'dgdkrjgsgtlf'),
    ('8-11 z', 'rqzdjqznrpkzmblbt'),
    ('1-3 z', 'zfzx'),
    ('2-4 z', 'kzgzkp'),
    ('6-10 v', 'jvvvvvvvvs'),
    ('2-9 v', 'vrvvvvvvvc'),
    ('5-6 q', 'qqqqqqc'),
    ('6-10 p', 'ppdknlgpqkp'),
    ('10-13 z', 'zzzzzzzzzzzzvz'),
    ('19-20 g', 'dtckblrmggknmxwnrjgg'),
    ('4-18 p', 'ppcjpqfpcxtphlppmhcx'),
    ('6-7 n', 'nnsnnknthn'),
    ('10-11 f', 'fffffffffff'),
    ('2-4 f', 'ffccltsfgk'),
    ('6-11 d', 'dsqddtddddjcnssrcd'),
    ('7-13 x', 'xxxxxqlxxxxfw'),
    ('12-13 r', 'rrrdrrrrrmrrrr'),
    ('15-17 p', 'pqppppppppppvppppppp'),
    ('7-8 j', 'jjjjjrdp'),
    ('4-6 v', 'vvvvvt'),
    ('1-4 t', 'tltftjtjhz'),
    ('9-15 j', 'jjjjjjhjjjjjjjkjj'),
    ('6-7 c', 'ccccccccz'),
    ('8-9 x', 'xxjxxxxxsx'),
    ('4-5 h', 'hhrhh'),
    ('2-3 g', 'cgnm'),
    ('8-10 l', 'llqlgllzlvrllg'),
    ('12-13 c', 'cvnbccpzzxcccfh'),
    ('3-8 z', 'zbzrwzzzwrzbqnr'),
    ('6-7 n', 'nnnnnnn'),
    ('8-11 j', 'tjqjrjggjxxjggjj'),
    ('7-12 l', 'bsvxdhljlcsj'),
    ('3-6 j', 'jjfjjjjb'),
    ('2-3 z', 'dzztwhmzqdx'),
    ('9-12 v', 'vvvvvvmvzvvcv'),
    ('13-14 v', 'vvvzvvvvvvvvvk'),
    ('6-7 g', 'fgggghgng'),
    ('13-14 h', 'wcghlwdbjhpdphkcv'),
    ('1-2 t', 'nncsg'),
    ('6-7 w', 'kwjwwxlwz'),
    ('4-5 z', 'zzztvz'),
    ('3-4 n', 'nvbvngnw'),
    ('15-17 z', 'zzzzzzzzzzzzzzzzzzp'),
    ('8-10 r', 'rrrstrgxrhrr'),
    ('8-10 g', 'cggggggvgcg'),
    ('1-4 m', 'mmvbz'),
    ('3-14 j', 'bdbhbjnjnrldhwlbrkrj'),
    ('1-4 r', 'rrkrnnd'),
    ('2-3 f', 'fvwc'),
    ('4-13 c', 'ccccvcgwbhwrcqf'),
    ('3-9 c', 'jcghltcfkjchxmccccbs'),
    ('3-5 h', 'hhhshm'),
    ('5-9 h', 'hhhsjhhhhgthfgldw'),
    ('4-12 h', 'mcwvwwphwwbc'),
    ('6-11 g', 'gqgggvggggh'),
    ('9-15 x', 'xxxxxxxxxxxxxxsx'),
    ('16-18 t', 'rmqqtbtvttsdtjvbttl'),
    ('9-20 f', 'cllnvlfkfrwzpqxwqgnn'),
    ('9-18 v', 'vvvvvvvvzvvvvvvzvxvv'),
    ('4-5 f', 'fzffbfvfff'),
    ('1-5 p', 'pppppp'),
    ('1-7 z', 'zjvchwzqjrtxzgz'),
    ('4-9 v', 'vvvvvvvvvv'),
    ('5-8 w', 'cwwwzwwb'),
    ('7-8 r', 'rrrrxrrr'),
    ('8-9 f', 'sgdcqfhfcfsflb'),
    ('3-7 g', 'gdgtnfggq'),
]


def is_valid_part1(rules, password):
    matches = re.match(r'^(\d{1,2})\-(\d{1,2}) ([a-z])$', rules)
    min_count = int(matches.group(1))
    max_count = int(matches.group(2))
    letter = matches.group(3)

    letter_count = 0
    for char in password:
        if char == letter:
            letter_count += 1
            if letter_count > max_count:
                return False

    if letter_count < min_count:
        return False

    return True


def is_valid_part2(rules, password):
    matches = re.match(r'^(\d{1,2})\-(\d{1,2}) ([a-z])$', rules)
    first_index = int(matches.group(1)) - 1
    second_index = int(matches.group(2)) - 1
    letter = matches.group(3)

    if password[first_index] == letter and password[second_index] != letter:
        return True
    if password[first_index] != letter and password[second_index] == letter:
        return True
    return False


valid_password_count_part1 = 0
valid_password_count_part2 = 0

for rules, password in PASSWORDS:
    if is_valid_part1(rules, password):
        valid_password_count_part1 += 1

    if is_valid_part2(rules, password):
        valid_password_count_part2 += 1

print(valid_password_count_part1)  # 607
print(valid_password_count_part2)  # 321
