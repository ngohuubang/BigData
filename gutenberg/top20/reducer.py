#!/usr/bin/python3
"""reducer.py"""

from operator import itemgetter

import sys


current_word = None
current_count = 0
word = None
word_counts = {}
# lấy dữ liệu từ thiết bị nhập chuẩn
for line in sys.stdin:
    # loại bỏ ký tự trắng ở đầu và cuối chuỗi
    line = line.strip()

    # tách ra thành cặp <word, 1> (Chú ý: Ở file reducer.py cặp <word, 1> xuất ra với ký tự phân cách tab)
    word, count = line.split('\t', 1)

    # chuyển giá trị count thành kiểu số
    try:
        count = int(count)
    except ValueError:
        # nếu không phải giá trị số thì bỏ qua
        continue

    # Ở cuối pha Map, các cặp (key, value) đã được sắp xếp theo key (ở đây là các từ).
    # Vì vậy ở pha Reduce, chương trình sẽ cộng giá trị value của dãy liên tiếp các từ trùng nhau
    # cho đến khi gặp từ mới.
    if word == current_word: # nếu từ mới trùng với từ đang xét thì tăng giá trị đếm của từ đang xét
        current_count += count
    else:
        if current_word: # nếu gặp từ mới thì in ra số lần xuất hiện của từ đang xét
            # print('%s\t%s' % (current_word, current_count))
            #dua vao mang
            word_counts[current_word]=current_count;
       


        # sau đó chuyển sang xử lý từ mới
        current_count = count
        current_word = word

    
# in ra từ cuối cùng
if current_word == word:
    # print('%s\t%s' % (current_word, current_count))
    word_counts[current_word]=current_count;

#copy tuple
# lst=deepcopy(word_counts)
#sap xep

word_counts_sorted = dict(sorted(word_counts.items(),key=lambda x:x[1],reverse=True))

#in list


for w in list(word_counts_sorted)[0:19]:
    print('%s\t%s' % (w, word_counts_sorted[w]))
    #print('%s' % (list[-1]))