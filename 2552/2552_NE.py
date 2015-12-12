import pygal
"""show graph of income of thai population in 2552"""
def neast_2552():
    """show graph that use data from dic in 2552"""
    dic = {
        'ภาคกลาง': {
            'ฉะเชิงเทรา': {
                2552: 7040,
                2545: 12204,
                2547: 17961,
                2549: 20599,
                2550: 23235
            },
            'ปทุมธานี': {
                2552: 9474,
                2545: 16592,
                2547: 20006,
                2549: 24569,
                2550: 25225
            },
            'ประจวบคีรีขันธ์': {
                2552: 6814,
                2545: 7311,
                2547: 8695,
                2549: 9729,
                2550: 10015
            },
            'นนทบุรี': {
                2552: 11925,
                2545: 7974,
                2547: 9259,
                2549: 11464,
                2550: 12301
            },
            'กาญจนบุรี': {
                2552: 4986,
                2545: 4706,
                2547: 5074,
                2549: 6131,
                2550: 6807
            },
            'จันทบุรี': {
                2552: 7787,
                2545: 6932,
                2547: 7713,
                2549: 9308,
                2550: 10690
            },
            'ตราด': {
                2552: 6667,
                2545: 6870,
                2547: 7886,
                2549: 9259,
                2550: 9969
            },
            'อ่างทอง': {
                2552: 7773,
                2545: 3828,
                2547: 4634,
                2549: 5269,
                2550: 5507
            },
            'เพชรบุรี': {
                2552: 8582,
                2545: 5622,
                2547: 6848,
                2549: 7679,
                2550: 8066
            },
            'สระแก้ว': {
                2552: 6122,
                2545: 2311,
                2547: 2730,
                2549: 3441,
                2550: 3782
            },
            'นครปฐม': {
                2552: 7916,
                2545: 9976,
                2547: 11603,
                2549: 13592,
                2550: 12761
            },
            'นครนายก': {
                2552: 6064,
                2545: 3877,
                2547: 4181,
                2549: 4349,
                2550: 4770
            },
            'ปราจีนบุรี': {
                2552: 8983,
                2545: 13669,
                2547: 19484,
                2549: 25662,
                2550: 31645
            },
            'สุพรรณบุรี': {
                2552: 4691,
                2545: 3274,
                2547: 4044,
                2549: 4718,
                2550: 4954
            },
            'กรุงเทพมหานคร': {
                2552: 11829,
                2545: 25448,
                2547: 29167,
                2549: 32986,
                2550: 34240
            },
            'พระนครศรีอยุธยา': {
                2552: 7489,
                2545: 19266,
                2547: 23289,
                2549: 26376,
                2550: 30024
            },
            'สมุทรปราการ': {
                2552: 8902,
                2545: 26409,
                2547: 27235,
                2549: 29890,
                2550: 37437
            },
            'ชัยนาท': {
                2552: 6920,
                2545: 3769,
                2547: 4076,
                2549: 4341,
                2550: 4892
            },
            'สมุทรสาคร': {
                2552: 7114,
                2545: 27617,
                2547: 33819,
                2549: 36274,
                2550: 37318
            },
            'สิงห์บุรี': {
                2552: 7629,
                2545: 4429,
                2547: 5592,
                2549: 6598,
                2550: 7075
            },
            'สระบุรี': {
                2552: 7179,
                2545: 12207,
                2547: 15502,
                2549: 18344,
                2550: 18792
            },
            'ชลบุรี': {
                2552: 8489,
                2545: 20456,
                2547: 24351,
                2549: 35347,
                2550: 40532
            },
            'ลพบุรี': {
                2552: 6552,
                2545: 5682,
                2547: 6049,
                2549: 6570,
                2550: 6521
            },
            'ระยอง': {
                2552: 8262,
                2545: 45448,
                2547: 56429,
                2549: 78547,
                2550: 88512
            },
            'ราชบุรี': {
                2552: 7469,
                2545: 7853,
                2547: 8875,
                2549: 10014,
                2550: 10181
            },
            'สมุทรสงคราม': {
                2552: 7495,
                2545: 3860,
                2547: 4629,
                2549: 6118,
                2550: 5974
            }
        },
        'ภาคตะวันออกเฉียงเหนือ': {
            'กาฬสินธุ์': {
                2552: 6834,
                2545: 1577,
                2547: 1940,
                2549: 2340,
                2550: 2506
            },
            'อำนาจเจริญ': {
                2552: 3221,
                2545: 1330,
                2547: 1592,
                2549: 1957,
                2550: 2180
            },
            'สกลนคร': {
                2552: 4783,
                2545: 1603,
                2547: 2033,
                2549: 2095,
                2550: 2228
            },
            'นครราชสีมา': {
                2552: 5586,
                2545: 3581,
                2547: 4087,
                2549: 4499,
                2550: 4704
            },
            'อุดรธานี': {
                2552: 8184,
                2545: 2037,
                2547: 2428,
                2549: 2779,
                2550: 3182
            },
            'มุกดาหาร': {
                2552: 5551,
                2545: 2025,
                2547: 2351,
                2549: 2776,
                2550: 2918
            },
            'ยโสธร': {
                2552: 3181,
                2545: 1445,
                2547: 1760,
                2549: 1915,
                2550: 2045
            },
            'ร้อยเอ็ด': {
                2552: 3862,
                2545: 1570,
                2547: 1912,
                2549: 2225,
                2550: 2514
            },
            'บึงกาฬ': {
                2552: 0,
                2545: 0,
                2547: 0,
                2549: 0,
                2550: 0
            },
            'ขอนแก่น': {
                2552: 5914,
                2545: 3241,
                2547: 3888,
                2549: 4836,
                2550: 5164
            },
            'เลย': {
                2552: 4513,
                2545: 1893,
                2547: 2124,
                2549: 2459,
                2550: 2982
            },
            'สุรินทร์': {
                2552: 3067,
                2545: 1512,
                2547: 1797,
                2549: 2106,
                2550: 2303
            },
            'หนองบัวลำภู': {
                2552: 5311,
                2545: 1267,
                2547: 1673,
                2549: 2048,
                2550: 2239
            },
            'ชัยภูมิ': {
                2552: 3563,
                2545: 1622,
                2547: 1815,
                2549: 2142,
                2550: 2285
            },
            'บุรีรัมย์': {
                2552: 4172,
                2545: 1664,
                2547: 1850,
                2549: 2183,
                2550: 2297
            },
            'หนองคาย': {
                2552: 4793,
                2545: 1855,
                2547: 2154,
                2549: 2558,
                2550: 2611
            },
            'ศรีสะเกษ': {
                2552: 3011,
                2545: 1265,
                2547: 1528,
                2549: 1854,
                2550: 2034
            },
            'มหาสารคาม': {
                2552: 5579,
                2545: 1513,
                2547: 2130,
                2549: 2134,
                2550: 2367
            },
            'อุบลราชธานี': {
                2552: 3695,
                2545: 1935,
                2547: 2207,
                2549: 2462,
                2550: 2610
            },
            'นครพนม': {
                2552: 3940,
                2545: 1639,
                2547: 1847,
                2549: 2134,
                2550: 2267
            }
        },
        'ภาคใต้': {
            'นครศรีธรรมราช': {
                2552: 9434,
                2545: 4285,
                2547: 5233,
                2549: 5811,
                2550: 5989
            },
            'ระนอง': {
                2552: 7495,
                2545: 5641,
                2547: 7325,
                2549: 8075,
                2550: 8405
            },
            'พังงา': {
                2552: 8211,
                2545: 5638,
                2547: 7777,
                2549: 9519,
                2550: 9821
            },
            'กระบี่': {
                2552: 6098,
                2545: 5640,
                2547: 8471,
                2549: 9808,
                2550: 11024
            },
            'สตูล': {
                2552: 5419,
                2545: 5523,
                2547: 6294,
                2549: 7240,
                2550: 7417
            },
            'ปัตตานี': {
                2552: 4183,
                2545: 4006,
                2547: 4014,
                2549: 4319,
                2550: 4034
            },
            'ตรัง': {
                2552: 5779,
                2545: 4491,
                2547: 6000,
                2549: 7650,
                2550: 7504
            },
            'พัทลุง': {
                2552: 6317,
                2545: 2274,
                2547: 3170,
                2549: 4164,
                2550: 4270
            },
            'นราธิวาส': {
                2552: 3251,
                2545: 2292,
                2547: 3251,
                2549: 4324,
                2550: 4444
            },
            'ชุมพร': {
                2552: 8318,
                2545: 5279,
                2547: 6652,
                2549: 7665,
                2550: 8617
            },
            'ภูเก็ต': {
                2552: 10873,
                2545: 16912,
                2547: 19294,
                2549: 21373,
                2550: 24727
            },
            'สุราษฎร์ธานี': {
                2552: 8333,
                2545: 5874,
                2547: 8256,
                2549: 10488,
                2550: 10167
            },
            'สงขลา': {
                2552: 8772,
                2545: 6896,
                2547: 8171,
                2549: 9504,
                2550: 9401
            },
            'ยะลา': {
                2552: 5700,
                2545: 3433,
                2547: 4851,
                2549: 6386,
                2550: 6718
            }
        },
        'ภาคเหนือ': {
            'ลำพูน': {
                2552: 4758,
                2545: 7171,
                2547: 7933,
                2549: 9699,
                2550: 9908
            },
            'กำแพงเพชร': {
                2552: 5346,
                2545: 4503,
                2547: 6149,
                2549: 7514,
                2550: 8006
            },
            'เชียงราย': {
                2552: 5051,
                2545: 2314,
                2547: 2778,
                2549: 3310,
                2550: 3654
            },
            'พิจิตร': {
                2552: 6291,
                2545: 2514,
                2547: 2956,
                2549: 3616,
                2550: 3653
            },
            'เพชรบูรณ์': {
                2552: 6773,
                2545: 2222,
                2547: 2645,
                2549: 3288,
                2550: 3546
            },
            'อุตรดิตถ์': {
                2552: 5934,
                2545: 2490,
                2547: 2897,
                2549: 3620,
                2550: 3591
            },
            'แม่ฮ่องสอน': {
                2552: 2861,
                2545: 1968,
                2547: 2220,
                2549: 2510,
                2550: 2648
            },
            'พะเยา': {
                2552: 4555,
                2545: 2091,
                2547: 2533,
                2549: 3176,
                2550: 3356
            },
            'น่าน': {
                2552: 4285,
                2545: 2136,
                2547: 2427,
                2549: 2760,
                2550: 3043
            },
            'นครสวรรค์': {
                2552: 5528,
                2545: 3121,
                2547: 3938,
                2549: 4776,
                2550: 4826
            },
            'ลำปาง': {
                2552: 5162,
                2545: 3476,
                2547: 3774,
                2549: 4046,
                2550: 4170
            },
            'สุโขทัย': {
                2552: 6686,
                2545: 2212,
                2547: 2641,
                2549: 3000,
                2550: 3178
            },
            'พิษณุโลก': {
                2552: 6491,
                2545: 3585,
                2547: 3930,
                2549: 4703,
                2550: 4952
            },
            'ตาก': {
                2552: 4574,
                2545: 2864,
                2547: 3603,
                2549: 4564,
                2550: 4659
            },
            'แพร่': {
                2552: 6399,
                2545: 2063,
                2547: 2459,
                2549: 2704,
                2550: 2857
            },
            'อุทัยธานี': {
                2552: 5878,
                2545: 2650,
                2547: 3236,
                2549: 3849,
                2550: 4475
            },
            'เชียงใหม่': {
                2552: 5793,
                2545: 4470,
                2547: 5202,
                2549: 6064,
                2550: 6241
            }
        }
    }
    line_chart = pygal.HorizontalBar()
    line_chart.title = 'สถิติรายได้ของประชากรภาคตะวันออกเฉียงเหนือในปี 2552'
    for i in dic['ภาคตะวันออกเฉียงเหนือ']:
        line_chart.add(i, dic['ภาคตะวันออกเฉียงเหนือ'][i][2552])

    output_file = open('2552_NE.html', 'w')
    output_file.write(line_chart.render_data_uri())
    output_file.close()
neast_2552()
