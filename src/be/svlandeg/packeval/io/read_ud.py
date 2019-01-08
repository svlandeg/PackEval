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


def read_raw_annotations(train_conllu, print_multi_word=False):
    docs = 0
    doc_ids = 0
    sentence_ids = 0
    words = 0
    multi_word_tokens = 0

    to_print_indices = []
    with open(train_conllu, 'r', encoding='utf-8') as fin:
        for line in fin:
            pure_text = line.rstrip('\n')
            is_comment = line.startswith("#")
            is_error_comment = line.startswith("# error_annotation =")
            is_doc = line.startswith("# newdoc")
            is_doc_id = line.startswith("# newdoc id = ")
            is_text = line.startswith("# text = ")
            is_sentence = line.startswith("# sent_id = ")
            is_speaker = line.startswith("# speaker=")
            is_s_type = line.startswith("# s_type=")

            if is_comment and not is_text and not is_sentence and not is_doc and not is_error_comment and not is_speaker and not is_s_type:
                print("Found weird comment line: ", pure_text)
            if is_doc_id:
                doc_id = pure_text.replace("# newdoc id = ", "")
                to_print_indices = []
                doc_ids = doc_ids+1
            if is_doc:
                docs = docs+1
            if is_text:
                text = pure_text.replace("# text = ", "")
            if is_sentence:
                sent_id = pure_text.replace("# sent_id = ", "")
                to_print_indices = []
                sentence_ids = sentence_ids+1
            if not is_comment:
                # printing multi-word tokens such as can't --> can not
                word = pure_text.split('\t')
                words = words+1
                if len(pure_text) > 0:
                    word_index = word[0]
                    if '-' in word_index:
                        indices = word_index.split('-')
                        to_print_indices = range(int(indices[0]), int(indices[1])+1)
                        multi_word_tokens = multi_word_tokens+1
                        if print_multi_word:
                            print()
                            print(word)
                    elif int(word_index.split('.')[0]) in to_print_indices:
                        if print_multi_word:
                            print(word)

    print()
    print(docs, "documents")
    print(doc_ids, "documents IDs")
    print(sentence_ids, "sentence IDs")
    print(words, "words")
    print(multi_word_tokens, "multi_word_tokens")


if __name__ == '__main__':
    print()

    # READING RAW TEXT
    # txt_train = read_english_training()
    # print(txt_train)

    # READING ANNOTATIONS WITH LIB
    # read_annotations()

    # READING RAW ANNOTATIONS
    list_files = list()
    list_files.append(os.path.join(ud_location, 'UD_English-ESL', 'en_esl-ud-train.conllu'))
    list_files.append(os.path.join(ud_location, 'UD_English-EWT', 'en_ewt-ud-train.conllu'))
    list_files.append(os.path.join(ud_location, 'UD_English-GUM', 'en_gum-ud-train.conllu'))
    list_files.append(os.path.join(ud_location, 'UD_English-LinES', 'en_lines-ud-train.conllu'))
    list_files.append(os.path.join(ud_location, 'UD_English-ParTUT', 'en_partut-ud-train.conllu'))

    for train_conllu in list_files:
        print(train_conllu)
        read_raw_annotations(train_conllu, print_multi_word=True)
        print()


