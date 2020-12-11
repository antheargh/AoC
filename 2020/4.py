#!/usr/bin/env python3

import sys
from copy import deepcopy
import re


# Run with input file name/path as single argument

# --- Day 4: Passport Processing ---
#
# You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport.
# While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't
# actually valid documentation for travel in most of the world.
#
# It seems like you're not the only one having problems, though; a very long line has formed for the automatic
# passport scanners, and the delay could upset your travel itinerary.
#
# Due to some questionable network security, you realize you might be able to solve both of these problems at the
# same time.
#
# The automatic passport scanners are slow because they're having trouble detecting which passports have all required
# fields. The expected fields are as follows:
#
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
# Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of
# key:value pairs separated by spaces or newlines. Passports are separated by blank lines.

VALID_SET = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])


def main(inputf):
    passports = []
    with open(inputf) as f:
        pp = []
        for line in f:
            if line == "\n":
                passports.append(pp)
                pp = []
            else:
                pp.extend(re.split(' ', line.strip()))
        passports.append(pp)





    ans_1 = pt_1(deepcopy(passports))
    print(ans_1)

    ans_2 = pt_2(deepcopy(passports))
    print(ans_2)


def pt_1(passports):
    # Here is an example batch file containing four passports:
    #
    # ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    # byr:1937 iyr:2017 cid:147 hgt:183cm
    #
    # iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
    # hcl:#cfa07d byr:1929
    #
    # hcl:#ae17e1 iyr:2013
    # eyr:2024
    # ecl:brn pid:760753108 byr:1931
    # hgt:179cm
    #
    # hcl:#cfa07d eyr:2025 pid:166559648
    # iyr:2011 ecl:brn hgt:59in
    #
    # The first passport is valid - all eight fields are present. The second passport is invalid - it is missing hgt
    # (the Height field).
    #
    # The third passport is interesting; the only missing field is cid, so it looks like data from North Pole
    # Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing
    # cid fields. Treat this "passport" as valid.
    #
    # The fourth passport is missing two fields, cid and byr. Missing cid is fine, but missing any other field is
    # not, so this passport is invalid.
    #
    # According to the above rules, your improved system would report 2 valid passports.
    #
    # Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch
    # file, how many passports are valid?

    valid = get_valids(passports)
    return len(valid)



def pt_2(passports):

    # The line is moving more quickly now, but you overhear airport security talking about how passports with invalid
    # data are getting through. Better add some data validation, quick!
    #
    # You can continue to ignore the cid field, but each other field has strict rules about what values are valid for
    # automatic validation:
    #
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.

    valid1 = get_valids(passports)
    year_dict = {"b": (1920, 2002), "i": (2010, 2020), "e": (2020, 2030)}
    hgt_dict = {"cm": (150, 193), "in": (59, 76)}
    ecl_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    valid2 = []


    for pp in valid1:
        for pair in pp:
            field, value = pair.split(':', 1)
            print(field, value)
            if field[1:] == "yr":
                value = int(value)
                yr_type = field[0]
                if value < year_dict[yr_type][0] or value > year_dict[yr_type][1]:
                    print("invalid")
                    break
            elif field == "hgt":
                unit = value[-2:]
                if unit not in ("cm", "in"):
                    print("invalid unit")
                    print(unit)
                    break
                height = int(value[:-2])
                if height < hgt_dict[unit][0] or height > hgt_dict[unit][1]:
                    print("invalid")
                    print(height)
                    break
            elif field == "hcl":
                if not re.match("#[0-9a-f]{6}", value):
                    print("invalid")
                    break
            elif field == "ecl":
                if value not in ecl_list:
                    print("invalid")
                    break
            elif field == "pid":
                if len(value) > 9:
                    break
                if not re.match("[0-9]{9}", value):
                    print("invalid")
                    break
        else:
            valid2.append(pp)

    print(len(valid1))
    return len(valid2)

def get_valids(passports):
    valid = []
    for pp in passports:
        if len(pp) == 8:
            valid.append(pp)
        elif len(pp) == 7:
            fields = set([i[:3] for i in pp])
            if fields == VALID_SET:
                valid.append(pp)
    return valid





if __name__ == '__main__':
    inputf = sys.argv[-1]
    main(inputf)

