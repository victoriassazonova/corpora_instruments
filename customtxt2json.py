tags_dict = {'n' :'g.pos',
             'np' : 'g.pos',
             'adj' :'g.pos',
             'num' : 'g.pos',
             'prn' : 'g.pos',
             'det' : 'g.pos',
             'v' : 'g.pos',
             'vaux' : 'g.pos',
             'adv' : 'g.pos',
             'post' : 'g.pos',
             'conj' : 'g.pos',
             'ij' : 'g.pos',
             'sg' : 'g.num',
             'pl' : 'g.num',
             'pe' : 'g.num',
             'pi' : 'g.num',
             'p1' : 'g.pers',
             'p2' : 'g.pers',
             'p3' : 'g.pers',
             'pers' : 'g.pron',
             'dem' : 'g.pron',
             'recip' : 'g.pron',
             'itg' : 'g.pron',
             'ref' : 'g.pron',
             'ind' : 'g.def',
             'def' : 'g.def',
             'px1sg' : 'g.poss',
             'px2sg' : 'g.poss',
             'px3sg' : 'g.poss',
             'px1pe' : 'g.poss',
             'px1pi' : 'g.poss',
             'px2pl' : 'g.poss',
             'px3pl' : 'g.poss',
             'indposs' : 'g.poss',
             'ref-sg' : 'g.poss',
             'ref-pl' : 'g.poss',
             'com-nun' : 'g.comitative',
             'com-nan' : 'g.comitative',
             'com-gali' : 'g.comitative',
             'com-taj' : 'g.comitative',
             'eqt-gačin' : 'g.equation',
             'eqt-dyn' : 'g.equation',
             'n-neg' : 'g.negation',
             'vaux-neg' : 'g.negation',
             'part-neg' : 'g.negation',
             'comp' : 'g.compdegree',
             'sup' : 'g.compdegree',
             'imp' : 'g.mood',
             'cond' : 'g.mood',
             'opt' : 'g.mood',
             'oblg' : 'g.mood',
             'prob1' : 'g.mood',
             'prob2' : 'g.mood',
             'prob3' : 'g.mood',
             'mon-imp' : 'g.mood',
             'pres' : 'g.tense',
             'nfut' : 'g.tense',
             'nfut-irreg' : 'g.tense',
             'past' : 'g.tense',
             'past-iter' : 'g.tense',
             'fut' : 'g.tense',
             'futcnt' : 'g.tense',
             'futnear' : 'g.tense',
             'impf' : 'g.aspect',
             'hab' : 'g.aspect',
             'dur' : 'g.aspect',
             'inch' : 'g.aspect',
             'iter' : 'g.aspect',
             'smlf' : 'g.aspect',
             'dsprs' : 'g.aspect',
             'dstr' : 'g.aspect',
             'quickly' : 'g.aspect',
             'res' : 'g.aspect',
             'p-sim' : 'g.participle',
             'p-ant' : 'g.participle',
             'p-pf' : 'g.participle',
             'p-hab' : 'g.participle',
             'p-post' : 'g.participle',
             'p-neg' : 'g.participle',
             'p-deb' : 'g.participle',
             'p-purp' : 'g.participle',
             'p-imdeb' : 'g.participle',
             'p-fict' : 'g.participle',
             'p-immfut' : 'g.participle',
             'conv-sim' : 'g.converb',
             'conv-cond' : 'g.converb',
             'conv-cond-ds' : 'g.converb',
             'conv-post-ds' : 'g.converb',
             'conv-antcnt' : 'g.converb',
             'conv-conc-ss' : 'g.converb',
             'conv-post-ss' : 'g.converb',
             'conv-sim-ds' : 'g.converb',
             'conv-conc-ds' : 'g.converb',
             'conv-ant-ss' : 'g.converb',
             'conv-nsim' : 'g.converb',
             'conv-ant-ds' : 'g.converb',
             'conv-purp' : 'g.converb',
             'conv-int' : 'g.converb',
             'conv-lim' : 'g.converb',
             'conv-bd' : 'g.converb',
             'inf' : 'g.infinitive',
             'prox' : 'g.prox',
             'rem' : 'g.rem',
             'nom' : 'g.case',
             'acc' : 'g.case',
             'ins' : 'g.case',
             'datloc' : 'g.case',
             'locall' : 'g.case',
             'all' : 'g.case',
             'prl' : 'g.case',
             'locdir' : 'g.case',
             'allprl' : 'g.case',
             'abl' : 'g.case',
             'ela' : 'g.case'}

import re
import json
import os
import csv
from pymorphy2 import MorphAnalyzer
morph = MorphAnalyzer()

def make_json(folder):
    num = 0
    csv_r = []
    with open("corpus/evenki_master_corpus/meta.csv") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            csv_r.append(row)
    for file_path in os.listdir(folder):
        if file_path.endswith('.txt'):
            dict_main = {}
            dict_evenk = []
            dict_rus = []
            met = csv_r[num]
            dict_main["meta"] = {}
            dict_main["meta"]["author"] = met[1]
            dict_main["meta"]["title"] = met[2]
            dict_main["meta"]["year"] = met[3]
            num += 1
            dict_main["sentences"] = []
            with open(folder+'/'+file_path,  encoding='utf-8') as f:
                f = f.read()
                c = 0
                d = f.split("\n\n")
                for i, sent in enumerate(d):
                    if c == 1:
                        c = 0
                        continue
                    off_start = 0
                    off_end = 0
                    r_off_start = 0
                    r_off_end = 0
                    next_word = 1
                    r_next_word = 1
                    sentence_index = 0
                    r_sentence_index = 0
                    sent = sent.split("\n")
                    cur_dict = {}
                    cur_dict["text"] = sent[0]
                    if '—' in cur_dict["text"]:
                        my_replace = str.replace
                        cur_dict["text"] = my_replace(cur_dict["text"], '—', ' — ')
                        cur_dict["text"] = my_replace(cur_dict["text"], ',', ', ')
                        cur_dict["text"] = my_replace(cur_dict["text"], ':', ': ')
                        cur_dict["text"] = my_replace(cur_dict["text"], '   ', ' ')
                        cur_dict["text"] = my_replace(cur_dict["text"], '  ', ' ')
                    if len(sent) == 1:
                        sent.append('\n')
                        sent.append(d[i + 1])
                        c = 1
                    else:
                        rus_dict = {}
                        rus_dict["text"] = sent[1]
                        if '—' in rus_dict["text"]:
                            my_replace = str.replace
                            rus_dict["text"] = my_replace(rus_dict["text"], '—', ' — ')
                            rus_dict["text"] = my_replace(rus_dict["text"], ',', ', ')
                            rus_dict["text"] = my_replace(rus_dict["text"], ':', ': ')
                            rus_dict["text"] = my_replace(rus_dict["text"], '   ', ' ')
                            rus_dict["text"] = my_replace(rus_dict["text"], '  ', ' ')
                        words = re.findall(r"[&\^\'\w-]+|[\[\]\"()«»{}*\„.,!?;:~—/]", sent[1])
                        rus_dict["words"] = []
                        for q, w in enumerate(words):
                            rus_word = {}
                            rus_word['wf'] = w
                            if w.split()[0].isalpha() == True or '-' in w  or '^' in w  or '&' in w:  # из-за этого слова в скобках не аннотируются
                                rus_word['wtype'] = 'word'
                                rus_word['sentence_index'] = r_sentence_index
                                ana = []
                                c_ana = {}
                                if w[0].isdigit() != True:
                                    c_ana['lex'] = morph.parse(w.lower())[0].normal_form
                                    ana.append(c_ana)
                                    rus_word['ana'] = ana
                                    rus_word['off_start'] = r_off_start
                                    rus_word['off_end'] = r_off_start + len(w)
                                    r_off_end = r_off_start + len(w)
                                    r_off_start = r_off_start + len(w) + 1
                                    r_sentence_index += 1
                            else:
                                if w[0].isdigit() == True:
                                    rus_word['wtype'] = 'punct'
                                    rus_word['off_start'] = r_off_start
                                    rus_word['off_end'] = r_off_start + len(w)
                                    r_off_start = r_off_start + len(w) + 1
                                elif w[0] == '—':
                                    try:
                                        if words[q - 1] == ',':
                                            rus_word['wtype'] = 'punct'
                                            rus_word['off_start'] = r_off_start
                                            rus_word['off_end'] = r_off_start + len(w)
                                            r_off_start = r_off_start + len(w) +1
                                        else:
                                            rus_word['wtype'] = 'punct'
                                            rus_word['off_start'] = r_off_start
                                            rus_word['off_end'] = r_off_start - 1 + len(w)
                                            r_off_start = r_off_start + len(w)+1
                                    except:
                                        rus_word['wtype'] = 'punct'
                                        rus_word['off_start'] = r_off_start
                                        rus_word['off_end'] = r_off_start - 1 + len(w)
                                        r_off_start = r_off_start + len(w)
                                elif w[0] == ',' and words[q + 1] == '—':
                                    rus_word['wtype'] = 'punct'
                                    rus_word['off_start'] = r_off_start - 1
                                    rus_word['off_end'] = r_off_start - 1 + len(w)
                                    r_off_start = r_off_start + len(w)
                                elif w[0] == '~':
                                    if words[q + 1] == '~':
                                        rus_word['wtype'] = 'punct'
                                        rus_word['off_start'] = r_off_start - 1
                                        rus_word['off_end'] = r_off_start - 1 + len(w)
                                        r_off_start = r_off_start + len(w)
                                    else:
                                        rus_word['wtype'] = 'punct'
                                        rus_word['off_start'] = r_off_start - 1
                                        rus_word['off_end'] = r_off_start - 1 + len(w)
                                        r_off_start = r_off_start + len(w) + 1

                                else:
                                    rus_word['wtype'] = 'punct'
                                    rus_word['off_start'] = r_off_start - 1
                                    rus_word['off_end'] = r_off_start - 1 + len(w)
                                    r_off_start = r_off_start + len(w)
                            rus_word['next_word'] = r_next_word
                            r_next_word += 1
                            # ana
                            rus_dict["words"].append(rus_word)
                        rus_dict["lang"] = 1
                        rus_dict["meta"] = {}
                        rus_dict["src_alignment"] = []
                        rus_dict["style_spans"] = []
                        # words
                    words = re.findall(r"[&\^\'\w-]+|[\[\]\"(){}.,!?«»\„~;:—/]", sent[0])
                    s = ' '.join(sent[2:])
                    s = s.split('  ')
                    s = s[1:]
                    cur_dict["words"] = []
                    for q, word in enumerate(words):
                        cur_word = {}
                        cur_word['wf'] = word
                        if word.split()[0].isalpha() == True or '-' in word or '^' in word or '&' in word  or '\'' in word:  # из-за этого слова в скобках не аннотируются
                            cur_word['wtype'] = 'word'
                            cur_word['sentence_index'] = sentence_index
                            ana = []
                            try:
                                a = s[sentence_index].split(' ')
                            except:
                                print(s)
                                print(sent)
                            a = a[1:]
                            for i in a:
                                i = i.split(' ')
                                # делим на лексему и теги

                                for j in i:
                                    c_ana = {}
                                    if j[0].isdigit() != True:
                                        j = j.split('<')
                                        c_ana['lex'] = j[0]
                                        j = j[1:]
                                        for tag in j:
                                            for key, value in tags_dict.items():
                                                if tag.startswith(key + '>'):
                                                    c_ana[value] = key
                                        # print(j[0])
                                        # for t in z:
                                        # for keys() in
                                        # все это добавляем в c_ana
                                        ana.append(c_ana)
                            sentence_index += 1
                            cur_word['ana'] = ana
                            cur_word['off_start'] = off_start
                            cur_word['off_end'] = off_start + len(word)
                            off_end = off_start + len(word)
                            off_start = off_start + len(word) + 1
                        else:
                            if word[0].isdigit() == True:
                                cur_word['wtype'] = 'punct'
                                cur_word['off_start'] = off_start
                                cur_word['off_end'] = off_start + len(word)
                                off_start = off_start + len(word) + 1
                            elif word[0] == '—':
                                try:
                                    if words[q - 1] == ',':
                                        cur_word['wtype'] = 'punct'
                                        cur_word['off_start'] = off_start
                                        cur_word['off_end'] = off_start + len(word)
                                        off_start = off_start + len(word) +1
                                    else:
                                        cur_word['wtype'] = 'punct'
                                        cur_word['off_start'] = off_start
                                        cur_word['off_end'] = off_start - 1 + len(word)
                                        off_start = off_start + len(word) + 1
                                except:
                                    cur_word['wtype'] = 'punct'
                                    cur_word['off_start'] = off_start
                                    cur_word['off_end'] = off_start - 1 + len(word)
                                    off_start = off_start + len(word)
                            elif word[0] == ',' and words[q + 1] == '—':
                                cur_word['wtype'] = 'punct'
                                cur_word['off_start'] = off_start - 1
                                cur_word['off_end'] = off_start - 1 + len(word)
                                off_start = off_start + len(word)

                            elif word[0] == '~':
                                if words[q+1] == '~':
                                    cur_word['wtype'] = 'punct'
                                    cur_word['off_start'] = off_start - 1
                                    cur_word['off_end'] = off_start - 1 + len(word)
                                    off_start = off_start + len(word)
                                else:
                                    cur_word['wtype'] = 'punct'
                                    cur_word['off_start'] = off_start - 1
                                    cur_word['off_end'] = off_start - 1 + len(word)
                                    off_start = off_start + len(word)+1
                            else:
                                cur_word['wtype'] = 'punct'
                                cur_word['off_start'] = off_start - 1
                                cur_word['off_end'] = off_start - 1 + len(word)
                                off_start = off_start + len(word)
                        cur_word['next_word'] = next_word
                        next_word += 1
                        # ana
                        cur_dict["words"].append(cur_word)
                    # language
                    cur_dict["lang"] = 0
                    # meta
                    cur_dict["meta"] = {}
                    # para_alignment
                    if c == 0:
                        cur_dict["para_alignment"] = []
                        rus_dict["para_alignment"] = []
                        par = {}
                        par['off_start'] = 0
                        par['off_end'] = off_end
                        par['para_id'] = len(dict_evenk)
                        cur_dict["para_alignment"].append(par)
                        par['off_end'] = len(rus_dict['text'])
                        rus_dict["para_alignment"].append(par)
                        dict_rus.append(rus_dict)
                    # src_alignment
                    cur_dict["src_alignment"] = []
                    # style_spans
                    cur_dict["style_spans"] = []
                    dict_evenk.append(cur_dict)

            for i in dict_evenk:
                dict_main['sentences'].append(i)
            for i in dict_rus:
                dict_main['sentences'].append(i)
            file = file_path.split('/')[-1]
            print(file)
            file = file.split('.')[0]
            file = 'corpus/evenki_master_corpus/JSON/'+file+'.JSON'
            f = open(file, "w", encoding='utf-8')
            json.dump(dict_main, f, ensure_ascii=False)

def main():
    make_json('corpus/evenki_master_corpus/txt')

if __name__ == "__main__":
    main()