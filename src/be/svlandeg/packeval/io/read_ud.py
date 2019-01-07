import os

import pyconll
import pyconll.util

# C:\Users\Sofie\Documents\data\UD_2_3\ud-treebanks-v2.3\UD_English-EWT
ud_location = os.path.join('C:', os.sep, 'Users', 'Sofie', 'Documents', 'data', 'UD_2_3', 'ud-treebanks-v2.3')


def read_english_training():
    ud_eng = 'UD_English-EWT'
    ud_eng_path = os.path.join(ud_location, ud_eng)
    train_txt = os.path.join(ud_eng_path, 'en_ewt-ud-train.txt')

    with open(train_txt, 'r', encoding='utf-8') as fin:
        data = fin.read()

    return data


def read_annotations():
    ud_eng = 'UD_English-EWT'
    ud_eng_path = os.path.join(ud_location, ud_eng)
    train_conllu = os.path.join(ud_eng_path, 'en_ewt-ud-train.conllu')

    train = pyconll.load_from_file(train_conllu)
    for sentence in train:
        print(sentence.id)
        for token in sentence:
            # token.upos, token.xpos, token.feats, token.head, token.deps, token.misc
            print(token.id, token.form, '\t\t\t -->', token.lemma)
        print()


if __name__ == '__main__':
    print()

    # READING RAW TEXT
    # txt_train = read_english_training()
    # print(txt_train)

    # READING ANNOTATIONS
    read_annotations()


