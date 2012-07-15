#!/usr/bin/env pypy

from pprint import pprint

with open('poker.txt') as f:
    lines = f.readlines()


single_values = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
}

hands_a = []
hands_b = []
for i in lines:
    i = i.strip().split(' ')
    l = []
    for j in i:
        l.append({'value': single_values[j[0]], 'suit': j[1]})
    hands_a.append(l[:5])
    hands_b.append(l[5:])
    hands_a[-1].sort(key=lambda x: x['value'], reverse=True)
    hands_b[-1].sort(key=lambda x: x['value'], reverse=True)


def compute_hand_value(hand):
    val = {}

    # High Card
    val['High Card'] = hand[0]['value'] * 100000000 \
                     + hand[1]['value'] * 1000000 \
                     + hand[2]['value'] * 10000 \
                     + hand[3]['value'] * 100 \
                     + hand[4]['value']

    # One Pair
    val['One Pair'] = 0
    for i in range(4):
        if hand[i]['value'] == hand[i + 1]['value']:
            val['One Pair'] = hand[i]['value']
            break

    # Two Pairs
    val['Two Pairs'] = 0
    if val['One Pair']:
        for i in range(4):
            if hand[i]['value'] == hand[i + 1]['value'] \
                    and hand[i]['value'] != val['One Pair']:
                val['Two Pairs'] = hand[i]['value']
                break
    if val['Two Pairs']:
        val['Two Pairs'] += val['One Pair'] * 100

    # Three of a Kind
    val['Three of a Kind'] = 0
    if val['One Pair']:
        for i in range(3):
            if hand[i]['value'] == hand[i + 1]['value'] \
                    and hand[i]['value'] == hand[i + 2]['value']:
                val['Three of a Kind'] = hand[i]['value']
                break

    # Straight
    val['Straight'] = 0
    if hand[1]['value'] == hand[0]['value'] - 1 and \
            hand[2]['value'] == hand[0]['value'] - 2 and \
            hand[3]['value'] == hand[0]['value'] - 3 and \
            hand[4]['value'] == hand[0]['value'] - 4:
        val['Straight'] = hand[0]['value']

    # Flush
    val['Flush'] = 0
    if hand[1]['suit'] == hand[0]['suit'] and \
            hand[2]['suit'] == hand[0]['suit'] and \
            hand[3]['suit'] == hand[0]['suit'] and \
            hand[4]['suit'] == hand[0]['suit']:
        val['Flush'] = hand[0]['value']

    # Full House
    val['Full House'] = 0
    if val['Three of a Kind'] and val['Two Pairs']:
        val['Full House'] = val['Three of a Kind']

    # Four of a Kind
    val['Four of a Kind'] = 0
    if val['Three of a Kind']:
        for i in range(2):
            if hand[i]['value'] == hand[i + 1]['value'] and \
                    hand[i]['value'] == hand[i + 2]['value'] and \
                    hand[i]['value'] == hand[i + 3]['value']:
                val['Four of a Kind'] = hand[i]['value']
                break

    # Straight Flush
    val['Straight Flush'] = 0
    if val['Straight'] and val['Flush']:
        val['Straight Flush'] = val['Straight']

    # Royal Flush
    val['Royal Flush'] = 0
    if val['Straight Flush']:
        val['Royal Flush'] = 10000000000

    return val


def compare_two_hands(h1, h2):
    v1 = compute_hand_value(h1)
    v2 = compute_hand_value(h2)

    tiers_to_compare = (
            'Royal Flush',
            'Straight Flush',
            'Four of a Kind',
            'Full House',
            'Flush',
            'Straight',
            'Three of a Kind',
            'Two Pairs',
            'One Pair'
    )

    for to_compare in tiers_to_compare:
        if v1[to_compare] or v2[to_compare]:
            if v1[to_compare] != v2[to_compare]:
                return v1[to_compare] - v2[to_compare]
            else:
                return v1['High Card'] - v2['High Card']
    return v1['High Card'] - v2['High Card']


if True:
    count = 0
    for i in range(len(hands_a)):
        ha = hands_a[i]
        hb = hands_b[i]
        if compare_two_hands(ha, hb) > 0:
            count += 1
    print count


if False:  # for testing
    def process_str(s):
        i = s.split(' ')
        hand = []
        for j in i:
            hand.append({'value': single_values[j[0]], 'suit': j[1]})
        hand.sort(key=lambda x: x['value'], reverse=True)
        return hand

    test_1 = '5H 5C 6S 7S KD'
    test_2 = '2C 3S 8S 8D TD'
    hand_1 = process_str(test_1)
    hand_2 = process_str(test_2)

    pprint(hand_1)
    pprint(hand_2)
    pprint(compute_hand_value(hand_1))
    pprint(compute_hand_value(hand_2))
    pprint(compare_two_hands(hand_1, hand_2))
