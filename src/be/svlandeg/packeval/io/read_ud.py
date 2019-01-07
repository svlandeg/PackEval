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
            # token.upos, token.xpos, token.feats, token.head, token.deps, token.deprel, token.misc
            print(token.id, token.form, '\t\t\t -->', token.lemma)
        print()


def read_raw_annotations():
    ud_eng = 'UD_English-ParTUT'
    ud_eng_path = os.path.join(ud_location, ud_eng)
    train_conllu = os.path.join(ud_eng_path, 'en_partut-ud-train.conllu')

    with open(train_conllu, 'r', encoding='utf-8') as fin:
        for line in fin:
            pure_text = line.rstrip('\n')
            is_comment = line.startswith("#")
            is_error_comment = line.startswith("# error_annotation =")
            is_doc = line.startswith("# newdoc")
            is_doc_id = line.startswith("# newdoc id = ")
            is_text = line.startswith("# text = ")
            is_sentence = line.startswith("# sent_id = ")
            if is_comment and not is_text and not is_sentence and not is_doc and not is_error_comment:
                print("Found weird comment line: ", pure_text)
            if is_doc:
                doc_id = pure_text.replace("# newdoc id = ", "")
            if is_text:
                text = pure_text.replace("# text = ", "")
            if is_sentence:
                sent_id = pure_text.replace("# sent_id = ", "")
            if not is_comment:
                word = pure_text.split('\t')
                # print(pure_text)
                # print(word)
                # print()
                if len(pure_text) > 0:
                    word_index = word[0]
                    if '-' in word_index:
                        print(word)


if __name__ == '__main__':
    print()

    # READING RAW TEXT
    # txt_train = read_english_training()
    # print(txt_train)

    # READING ANNOTATIONS
    # read_annotations()
    read_raw_annotations()


