import re
import csv

from pattern import PATTERN, SUB_PATTERN, ADD_PATTERN, ADD_SUB_PATTERN

def get_names():
    for i in contacts_list[1:]:
        lastname_firstname_surname = ' '.join(i[:3]).split()
        if len(lastname_firstname_surname) < 3:
            lastname_firstname_surname = lastname_firstname_surname + [''] * (3 - len(lastname_firstname_surname))
        i[:3] = lastname_firstname_surname[:3]


def telephone_number_correction():
    for phone_number in contacts_list:
        result_phone = re.sub(PATTERN, SUB_PATTERN, phone_number[5])
        result = re.sub(ADD_PATTERN, ADD_SUB_PATTERN, result_phone)
        phone_number[5] = result


def merge_duplicate_records():
    contacts_dict = {}
    for name in contacts_list:
        if name[0] not in contacts_dict:
            contacts_dict[name[0]] = name
        else:
            for ind, item in enumerate(contacts_dict[name[0]]):
                if item == '':
                    contacts_dict[name[0]][ind] = name[ind]

    for last_name, all_info in contacts_dict.items():
        if all_info not in final_edited_list:
            final_edited_list.append(all_info)


if __name__ == "__main__":
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
        final_edited_list = []
        get_names()
        telephone_number_correction()
        merge_duplicate_records()

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(final_edited_list)
