import os

# C:\Users\Sofie\Documents\data\UD_2_3\ud-treebanks-v2.3\UD_English-EWT
ud_location = os.path.join('C:', os.sep, 'Users', 'Sofie', 'Documents', 'data', 'UD_2_3', 'ud-treebanks-v2.3')


def read_english_training():
    ud_eng = 'UD_English-EWT'
    ud_eng_path = os.path.join(ud_location, ud_eng)
    train_txt = os.path.join(ud_eng_path, 'en_ewt-ud-train.txt')

    with open(train_txt, 'r', encoding='utf-8') as fin:
        data = fin.read()

    return data


if __name__ == '__main__':
    print()
    txt_train = read_english_training()
    print(txt_train)


