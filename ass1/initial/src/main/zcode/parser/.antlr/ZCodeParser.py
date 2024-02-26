# Generated from /home/qmi/repos/initial/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,50,479,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,1,0,
        1,0,1,1,5,1,122,8,1,10,1,12,1,125,9,1,1,1,5,1,128,8,1,10,1,12,1,
        131,9,1,1,1,1,1,1,2,1,2,3,2,137,8,2,1,2,4,2,140,8,2,11,2,12,2,141,
        1,2,3,2,145,8,2,1,3,1,3,3,3,149,8,3,1,4,1,4,1,5,1,5,1,5,1,5,1,5,
        1,5,3,5,159,8,5,1,6,1,6,1,6,1,6,3,6,165,8,6,1,7,1,7,1,7,1,7,1,7,
        1,7,3,7,173,8,7,1,8,1,8,1,8,3,8,178,8,8,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,3,9,190,8,9,1,10,1,10,1,10,1,10,1,10,3,10,197,8,
        10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,3,12,206,8,12,1,13,1,13,1,
        13,1,13,1,13,3,13,213,8,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,3,
        15,222,8,15,1,16,1,16,1,16,1,16,1,16,3,16,229,8,16,1,17,1,17,1,18,
        1,18,3,18,235,8,18,1,19,1,19,1,19,1,19,1,20,1,20,3,20,243,8,20,1,
        20,1,20,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,255,8,21,1,
        21,4,21,258,8,21,11,21,12,21,259,1,21,3,21,263,8,21,1,22,1,22,1,
        22,1,22,3,22,269,8,22,1,23,1,23,1,23,3,23,274,8,23,1,24,1,24,1,25,
        1,25,1,25,1,25,1,26,1,26,1,26,3,26,285,8,26,1,27,1,27,1,27,1,28,
        1,28,3,28,292,8,28,1,29,1,29,1,29,1,29,1,29,3,29,299,8,29,1,30,1,
        30,1,30,1,30,1,30,1,30,3,30,307,8,30,1,31,1,31,1,31,1,31,5,31,313,
        8,31,10,31,12,31,316,9,31,1,31,1,31,1,32,1,32,1,32,1,32,1,33,1,33,
        1,33,1,33,1,34,1,34,3,34,330,8,34,1,35,1,35,1,35,1,35,1,35,3,35,
        337,8,35,1,36,1,36,3,36,341,8,36,1,37,1,37,5,37,345,8,37,10,37,12,
        37,348,9,37,1,37,1,37,1,37,3,37,353,8,37,1,38,1,38,1,38,1,38,1,39,
        1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,1,40,5,40,370,8,40,
        10,40,12,40,373,9,40,1,40,1,40,1,41,1,41,1,42,1,42,1,43,1,43,1,44,
        1,44,3,44,385,8,44,1,45,1,45,1,46,1,46,1,46,1,46,1,47,1,47,1,48,
        1,48,5,48,397,8,48,10,48,12,48,400,9,48,1,49,1,49,1,49,1,49,1,49,
        3,49,407,8,49,1,50,1,50,1,50,1,50,1,50,3,50,414,8,50,1,51,1,51,1,
        51,1,51,1,51,3,51,421,8,51,1,52,1,52,1,52,1,52,1,52,1,52,5,52,429,
        8,52,10,52,12,52,432,9,52,1,53,1,53,1,53,1,53,1,53,1,53,5,53,440,
        8,53,10,53,12,53,443,9,53,1,54,1,54,1,54,1,54,1,54,1,54,5,54,451,
        8,54,10,54,12,54,454,9,54,1,55,1,55,1,55,3,55,459,8,55,1,56,1,56,
        1,56,3,56,464,8,56,1,57,1,57,3,57,468,8,57,1,58,1,58,1,58,1,58,1,
        58,1,58,1,58,3,58,477,8,58,1,58,0,3,104,106,108,59,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,
        100,102,104,106,108,110,112,114,116,0,6,2,0,1,2,43,44,1,0,3,5,2,
        0,28,28,30,35,1,0,21,22,1,0,23,24,1,0,25,27,477,0,118,1,0,0,0,2,
        123,1,0,0,0,4,136,1,0,0,0,6,148,1,0,0,0,8,150,1,0,0,0,10,152,1,0,
        0,0,12,164,1,0,0,0,14,166,1,0,0,0,16,177,1,0,0,0,18,189,1,0,0,0,
        20,196,1,0,0,0,22,198,1,0,0,0,24,205,1,0,0,0,26,212,1,0,0,0,28,214,
        1,0,0,0,30,221,1,0,0,0,32,228,1,0,0,0,34,230,1,0,0,0,36,234,1,0,
        0,0,38,236,1,0,0,0,40,242,1,0,0,0,42,254,1,0,0,0,44,268,1,0,0,0,
        46,270,1,0,0,0,48,275,1,0,0,0,50,277,1,0,0,0,52,281,1,0,0,0,54,286,
        1,0,0,0,56,291,1,0,0,0,58,298,1,0,0,0,60,300,1,0,0,0,62,308,1,0,
        0,0,64,319,1,0,0,0,66,323,1,0,0,0,68,329,1,0,0,0,70,331,1,0,0,0,
        72,340,1,0,0,0,74,352,1,0,0,0,76,354,1,0,0,0,78,358,1,0,0,0,80,362,
        1,0,0,0,82,376,1,0,0,0,84,378,1,0,0,0,86,380,1,0,0,0,88,382,1,0,
        0,0,90,386,1,0,0,0,92,388,1,0,0,0,94,392,1,0,0,0,96,398,1,0,0,0,
        98,406,1,0,0,0,100,413,1,0,0,0,102,420,1,0,0,0,104,422,1,0,0,0,106,
        433,1,0,0,0,108,444,1,0,0,0,110,458,1,0,0,0,112,463,1,0,0,0,114,
        467,1,0,0,0,116,476,1,0,0,0,118,119,7,0,0,0,119,1,1,0,0,0,120,122,
        5,42,0,0,121,120,1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,123,124,
        1,0,0,0,124,129,1,0,0,0,125,123,1,0,0,0,126,128,3,4,2,0,127,126,
        1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,132,
        1,0,0,0,131,129,1,0,0,0,132,133,5,0,0,1,133,3,1,0,0,0,134,137,3,
        6,3,0,135,137,3,44,22,0,136,134,1,0,0,0,136,135,1,0,0,0,137,144,
        1,0,0,0,138,140,5,42,0,0,139,138,1,0,0,0,140,141,1,0,0,0,141,139,
        1,0,0,0,141,142,1,0,0,0,142,145,1,0,0,0,143,145,5,0,0,1,144,139,
        1,0,0,0,144,143,1,0,0,0,145,5,1,0,0,0,146,149,3,8,4,0,147,149,3,
        64,32,0,148,146,1,0,0,0,148,147,1,0,0,0,149,7,1,0,0,0,150,151,3,
        62,31,0,151,9,1,0,0,0,152,153,3,48,24,0,153,154,5,45,0,0,154,155,
        5,39,0,0,155,156,3,12,6,0,156,158,5,40,0,0,157,159,3,14,7,0,158,
        157,1,0,0,0,158,159,1,0,0,0,159,11,1,0,0,0,160,161,5,43,0,0,161,
        162,5,41,0,0,162,165,3,12,6,0,163,165,5,43,0,0,164,160,1,0,0,0,164,
        163,1,0,0,0,165,13,1,0,0,0,166,172,5,29,0,0,167,168,5,39,0,0,168,
        169,3,16,8,0,169,170,5,40,0,0,170,173,1,0,0,0,171,173,3,100,50,0,
        172,167,1,0,0,0,172,171,1,0,0,0,173,15,1,0,0,0,174,178,3,20,10,0,
        175,178,3,18,9,0,176,178,3,98,49,0,177,174,1,0,0,0,177,175,1,0,0,
        0,177,176,1,0,0,0,178,17,1,0,0,0,179,180,5,39,0,0,180,181,3,16,8,
        0,181,182,5,40,0,0,182,183,5,41,0,0,183,184,3,18,9,0,184,190,1,0,
        0,0,185,186,5,39,0,0,186,187,3,16,8,0,187,188,5,40,0,0,188,190,1,
        0,0,0,189,179,1,0,0,0,189,185,1,0,0,0,190,19,1,0,0,0,191,192,3,0,
        0,0,192,193,5,41,0,0,193,194,3,20,10,0,194,197,1,0,0,0,195,197,3,
        0,0,0,196,191,1,0,0,0,196,195,1,0,0,0,197,21,1,0,0,0,198,199,3,24,
        12,0,199,200,5,39,0,0,200,201,3,26,13,0,201,202,5,40,0,0,202,23,
        1,0,0,0,203,206,5,45,0,0,204,206,3,28,14,0,205,203,1,0,0,0,205,204,
        1,0,0,0,206,25,1,0,0,0,207,208,3,100,50,0,208,209,5,41,0,0,209,210,
        3,26,13,0,210,213,1,0,0,0,211,213,3,100,50,0,212,207,1,0,0,0,212,
        211,1,0,0,0,213,27,1,0,0,0,214,215,5,45,0,0,215,216,5,37,0,0,216,
        217,3,30,15,0,217,218,5,38,0,0,218,29,1,0,0,0,219,222,3,32,16,0,
        220,222,1,0,0,0,221,219,1,0,0,0,221,220,1,0,0,0,222,31,1,0,0,0,223,
        224,3,34,17,0,224,225,5,41,0,0,225,226,3,32,16,0,226,229,1,0,0,0,
        227,229,3,34,17,0,228,223,1,0,0,0,228,227,1,0,0,0,229,33,1,0,0,0,
        230,231,3,100,50,0,231,35,1,0,0,0,232,235,3,38,19,0,233,235,3,40,
        20,0,234,232,1,0,0,0,234,233,1,0,0,0,235,37,1,0,0,0,236,237,5,45,
        0,0,237,238,5,29,0,0,238,239,3,100,50,0,239,39,1,0,0,0,240,243,5,
        45,0,0,241,243,3,22,11,0,242,240,1,0,0,0,242,241,1,0,0,0,243,244,
        1,0,0,0,244,245,3,14,7,0,245,41,1,0,0,0,246,255,3,70,35,0,247,255,
        3,80,40,0,248,255,3,84,42,0,249,255,3,86,43,0,250,255,3,88,44,0,
        251,255,3,90,45,0,252,255,3,92,46,0,253,255,3,36,18,0,254,246,1,
        0,0,0,254,247,1,0,0,0,254,248,1,0,0,0,254,249,1,0,0,0,254,250,1,
        0,0,0,254,251,1,0,0,0,254,252,1,0,0,0,254,253,1,0,0,0,255,262,1,
        0,0,0,256,258,5,42,0,0,257,256,1,0,0,0,258,259,1,0,0,0,259,257,1,
        0,0,0,259,260,1,0,0,0,260,263,1,0,0,0,261,263,5,0,0,1,262,257,1,
        0,0,0,262,261,1,0,0,0,263,43,1,0,0,0,264,269,3,46,23,0,265,269,3,
        10,5,0,266,269,3,50,25,0,267,269,3,52,26,0,268,264,1,0,0,0,268,265,
        1,0,0,0,268,266,1,0,0,0,268,267,1,0,0,0,269,45,1,0,0,0,270,271,3,
        48,24,0,271,273,5,45,0,0,272,274,3,54,27,0,273,272,1,0,0,0,273,274,
        1,0,0,0,274,47,1,0,0,0,275,276,7,1,0,0,276,49,1,0,0,0,277,278,5,
        7,0,0,278,279,5,45,0,0,279,280,3,54,27,0,280,51,1,0,0,0,281,282,
        5,8,0,0,282,284,5,45,0,0,283,285,3,54,27,0,284,283,1,0,0,0,284,285,
        1,0,0,0,285,53,1,0,0,0,286,287,5,29,0,0,287,288,3,100,50,0,288,55,
        1,0,0,0,289,292,3,58,29,0,290,292,1,0,0,0,291,289,1,0,0,0,291,290,
        1,0,0,0,292,57,1,0,0,0,293,294,3,60,30,0,294,295,5,41,0,0,295,296,
        3,58,29,0,296,299,1,0,0,0,297,299,3,60,30,0,298,293,1,0,0,0,298,
        297,1,0,0,0,299,59,1,0,0,0,300,301,3,48,24,0,301,306,5,45,0,0,302,
        303,5,39,0,0,303,304,3,12,6,0,304,305,5,40,0,0,305,307,1,0,0,0,306,
        302,1,0,0,0,306,307,1,0,0,0,307,61,1,0,0,0,308,309,5,9,0,0,309,310,
        5,45,0,0,310,314,3,66,33,0,311,313,5,42,0,0,312,311,1,0,0,0,313,
        316,1,0,0,0,314,312,1,0,0,0,314,315,1,0,0,0,315,317,1,0,0,0,316,
        314,1,0,0,0,317,318,3,68,34,0,318,63,1,0,0,0,319,320,5,9,0,0,320,
        321,5,45,0,0,321,322,3,66,33,0,322,65,1,0,0,0,323,324,5,37,0,0,324,
        325,3,56,28,0,325,326,5,38,0,0,326,67,1,0,0,0,327,330,3,92,46,0,
        328,330,3,88,44,0,329,327,1,0,0,0,329,328,1,0,0,0,330,69,1,0,0,0,
        331,332,5,15,0,0,332,333,3,100,50,0,333,334,3,42,21,0,334,336,3,
        72,36,0,335,337,3,78,39,0,336,335,1,0,0,0,336,337,1,0,0,0,337,71,
        1,0,0,0,338,341,3,74,37,0,339,341,1,0,0,0,340,338,1,0,0,0,340,339,
        1,0,0,0,341,73,1,0,0,0,342,346,3,76,38,0,343,345,5,42,0,0,344,343,
        1,0,0,0,345,348,1,0,0,0,346,344,1,0,0,0,346,347,1,0,0,0,347,349,
        1,0,0,0,348,346,1,0,0,0,349,350,3,74,37,0,350,353,1,0,0,0,351,353,
        3,76,38,0,352,342,1,0,0,0,352,351,1,0,0,0,353,75,1,0,0,0,354,355,
        5,17,0,0,355,356,3,100,50,0,356,357,3,42,21,0,357,77,1,0,0,0,358,
        359,5,16,0,0,359,360,3,100,50,0,360,361,3,42,21,0,361,79,1,0,0,0,
        362,363,5,10,0,0,363,364,5,45,0,0,364,365,5,11,0,0,365,366,3,100,
        50,0,366,367,5,12,0,0,367,371,3,82,41,0,368,370,5,42,0,0,369,368,
        1,0,0,0,370,373,1,0,0,0,371,369,1,0,0,0,371,372,1,0,0,0,372,374,
        1,0,0,0,373,371,1,0,0,0,374,375,3,42,21,0,375,81,1,0,0,0,376,377,
        3,100,50,0,377,83,1,0,0,0,378,379,5,13,0,0,379,85,1,0,0,0,380,381,
        5,14,0,0,381,87,1,0,0,0,382,384,5,6,0,0,383,385,3,100,50,0,384,383,
        1,0,0,0,384,385,1,0,0,0,385,89,1,0,0,0,386,387,3,28,14,0,387,91,
        1,0,0,0,388,389,5,18,0,0,389,390,3,94,47,0,390,391,5,19,0,0,391,
        93,1,0,0,0,392,393,3,96,48,0,393,95,1,0,0,0,394,397,3,42,21,0,395,
        397,3,4,2,0,396,394,1,0,0,0,396,395,1,0,0,0,397,400,1,0,0,0,398,
        396,1,0,0,0,398,399,1,0,0,0,399,97,1,0,0,0,400,398,1,0,0,0,401,402,
        3,100,50,0,402,403,5,41,0,0,403,404,3,98,49,0,404,407,1,0,0,0,405,
        407,3,100,50,0,406,401,1,0,0,0,406,405,1,0,0,0,407,99,1,0,0,0,408,
        409,3,102,51,0,409,410,5,36,0,0,410,411,3,102,51,0,411,414,1,0,0,
        0,412,414,3,102,51,0,413,408,1,0,0,0,413,412,1,0,0,0,414,101,1,0,
        0,0,415,416,3,104,52,0,416,417,7,2,0,0,417,418,3,104,52,0,418,421,
        1,0,0,0,419,421,3,104,52,0,420,415,1,0,0,0,420,419,1,0,0,0,421,103,
        1,0,0,0,422,423,6,52,-1,0,423,424,3,106,53,0,424,430,1,0,0,0,425,
        426,10,2,0,0,426,427,7,3,0,0,427,429,3,106,53,0,428,425,1,0,0,0,
        429,432,1,0,0,0,430,428,1,0,0,0,430,431,1,0,0,0,431,105,1,0,0,0,
        432,430,1,0,0,0,433,434,6,53,-1,0,434,435,3,108,54,0,435,441,1,0,
        0,0,436,437,10,2,0,0,437,438,7,4,0,0,438,440,3,108,54,0,439,436,
        1,0,0,0,440,443,1,0,0,0,441,439,1,0,0,0,441,442,1,0,0,0,442,107,
        1,0,0,0,443,441,1,0,0,0,444,445,6,54,-1,0,445,446,3,110,55,0,446,
        452,1,0,0,0,447,448,10,2,0,0,448,449,7,5,0,0,449,451,3,110,55,0,
        450,447,1,0,0,0,451,454,1,0,0,0,452,450,1,0,0,0,452,453,1,0,0,0,
        453,109,1,0,0,0,454,452,1,0,0,0,455,456,5,20,0,0,456,459,3,110,55,
        0,457,459,3,112,56,0,458,455,1,0,0,0,458,457,1,0,0,0,459,111,1,0,
        0,0,460,461,5,24,0,0,461,464,3,112,56,0,462,464,3,114,57,0,463,460,
        1,0,0,0,463,462,1,0,0,0,464,113,1,0,0,0,465,468,3,22,11,0,466,468,
        3,116,58,0,467,465,1,0,0,0,467,466,1,0,0,0,468,115,1,0,0,0,469,477,
        3,0,0,0,470,477,5,45,0,0,471,472,5,37,0,0,472,473,3,100,50,0,473,
        474,5,38,0,0,474,477,1,0,0,0,475,477,3,28,14,0,476,469,1,0,0,0,476,
        470,1,0,0,0,476,471,1,0,0,0,476,475,1,0,0,0,477,117,1,0,0,0,47,123,
        129,136,141,144,148,158,164,172,177,189,196,205,212,221,228,234,
        242,254,259,262,268,273,284,291,298,306,314,329,336,340,346,352,
        371,384,396,398,406,413,420,430,441,452,458,463,467,476
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "<INVALID>", "'end'", "'not'", 
                     "'and'", "'or'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'='", "'<-'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'...'", "'('", "')'", "'['", "']'", "','", 
                     "'\\n'" ]

    symbolicNames = [ "<INVALID>", "TRUE", "FALSE", "NUMBER", "BOOL", "STRING", 
                      "RETURN", "VAR", "DYNAMIC", "FUNC", "FOR", "UNTIL", 
                      "BY", "BREAK", "CONTINUE", "IF", "ELSE", "ELIF", "BEGIN", 
                      "END", "NOT", "AND", "OR", "PLUS", "MINUS", "MULT", 
                      "DIV", "MOD", "EQUAL", "LEFTARR", "EQUALEQUAL", "NOTEQUAL", 
                      "LESS", "GREATER", "LESSOREQUAL", "GREATEROREQUAL", 
                      "ELLIPSIS", "LBracket", "RBracket", "LSBracket", "RSBracket", 
                      "COMMA", "NEWLINE", "NumberLit", "StringLit", "IDENTIFIER", 
                      "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_literal = 0
    RULE_program = 1
    RULE_declaration = 2
    RULE_function = 3
    RULE_function1 = 4
    RULE_arrayDeclaration = 5
    RULE_arrayDim = 6
    RULE_arrayAssign = 7
    RULE_arrayElementList = 8
    RULE_arrayList = 9
    RULE_literalList = 10
    RULE_elementAccessExpr = 11
    RULE_arrExpr = 12
    RULE_indexList = 13
    RULE_functionCall = 14
    RULE_functionArgsList = 15
    RULE_argsPrime = 16
    RULE_arg = 17
    RULE_assignStatement = 18
    RULE_scalarAssignStatement = 19
    RULE_arrayAssignStatement = 20
    RULE_statement = 21
    RULE_variableDeclaration = 22
    RULE_normalDeclaration = 23
    RULE_varType = 24
    RULE_varDecl = 25
    RULE_dynamicDecl = 26
    RULE_variableInitialization = 27
    RULE_paramDeclList = 28
    RULE_paramDeclPrime = 29
    RULE_paramDeclAtom = 30
    RULE_functionDecl = 31
    RULE_functionPreDecl = 32
    RULE_paramDecl = 33
    RULE_functionBody = 34
    RULE_ifStatement = 35
    RULE_elifStatementList = 36
    RULE_elifStatementPrime = 37
    RULE_elifStatement = 38
    RULE_elseStatement = 39
    RULE_forStatement = 40
    RULE_updateExpr = 41
    RULE_breakStatement = 42
    RULE_continueStatement = 43
    RULE_returnStatement = 44
    RULE_functionCallStatement = 45
    RULE_blockStatement = 46
    RULE_blockStatementBody = 47
    RULE_nullableListOfStatement = 48
    RULE_expressionList = 49
    RULE_expression = 50
    RULE_expression1 = 51
    RULE_expression2 = 52
    RULE_expression3 = 53
    RULE_expression4 = 54
    RULE_expression5 = 55
    RULE_expression6 = 56
    RULE_expression7 = 57
    RULE_operands = 58

    ruleNames =  [ "literal", "program", "declaration", "function", "function1", 
                   "arrayDeclaration", "arrayDim", "arrayAssign", "arrayElementList", 
                   "arrayList", "literalList", "elementAccessExpr", "arrExpr", 
                   "indexList", "functionCall", "functionArgsList", "argsPrime", 
                   "arg", "assignStatement", "scalarAssignStatement", "arrayAssignStatement", 
                   "statement", "variableDeclaration", "normalDeclaration", 
                   "varType", "varDecl", "dynamicDecl", "variableInitialization", 
                   "paramDeclList", "paramDeclPrime", "paramDeclAtom", "functionDecl", 
                   "functionPreDecl", "paramDecl", "functionBody", "ifStatement", 
                   "elifStatementList", "elifStatementPrime", "elifStatement", 
                   "elseStatement", "forStatement", "updateExpr", "breakStatement", 
                   "continueStatement", "returnStatement", "functionCallStatement", 
                   "blockStatement", "blockStatementBody", "nullableListOfStatement", 
                   "expressionList", "expression", "expression1", "expression2", 
                   "expression3", "expression4", "expression5", "expression6", 
                   "expression7", "operands" ]

    EOF = Token.EOF
    TRUE=1
    FALSE=2
    NUMBER=3
    BOOL=4
    STRING=5
    RETURN=6
    VAR=7
    DYNAMIC=8
    FUNC=9
    FOR=10
    UNTIL=11
    BY=12
    BREAK=13
    CONTINUE=14
    IF=15
    ELSE=16
    ELIF=17
    BEGIN=18
    END=19
    NOT=20
    AND=21
    OR=22
    PLUS=23
    MINUS=24
    MULT=25
    DIV=26
    MOD=27
    EQUAL=28
    LEFTARR=29
    EQUALEQUAL=30
    NOTEQUAL=31
    LESS=32
    GREATER=33
    LESSOREQUAL=34
    GREATEROREQUAL=35
    ELLIPSIS=36
    LBracket=37
    RBracket=38
    LSBracket=39
    RSBracket=40
    COMMA=41
    NEWLINE=42
    NumberLit=43
    StringLit=44
    IDENTIFIER=45
    COMMENT=46
    WS=47
    ERROR_CHAR=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NumberLit(self):
            return self.getToken(ZCodeParser.NumberLit, 0)

        def TRUE(self):
            return self.getToken(ZCodeParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(ZCodeParser.FALSE, 0)

        def StringLit(self):
            return self.getToken(ZCodeParser.StringLit, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_literal




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 26388279066630) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.DeclarationContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 120
                self.match(ZCodeParser.NEWLINE)
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 952) != 0):
                self.state = 126
                self.declaration()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(ZCodeParser.VariableDeclarationContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_declaration




    def declaration(self):

        localctx = ZCodeParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.state = 134
                self.function()
                pass
            elif token in [3, 4, 5, 7, 8]:
                self.state = 135
                self.variableDeclaration()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.state = 139 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 138
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 141 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==42):
                        break

                pass
            elif token in [-1]:
                self.state = 143
                self.match(ZCodeParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function1(self):
            return self.getTypedRuleContext(ZCodeParser.Function1Context,0)


        def functionPreDecl(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionPreDeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function




    def function(self):

        localctx = ZCodeParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function)
        try:
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.function1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.functionPreDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDecl(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionDeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function1




    def function1(self):

        localctx = ZCodeParser.Function1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_function1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.functionDecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varType(self):
            return self.getTypedRuleContext(ZCodeParser.VarTypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LSBracket(self):
            return self.getToken(ZCodeParser.LSBracket, 0)

        def arrayDim(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayDimContext,0)


        def RSBracket(self):
            return self.getToken(ZCodeParser.RSBracket, 0)

        def arrayAssign(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayAssignContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayDeclaration




    def arrayDeclaration(self):

        localctx = ZCodeParser.ArrayDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.varType()
            self.state = 153
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 154
            self.match(ZCodeParser.LSBracket)
            self.state = 155
            self.arrayDim()
            self.state = 156
            self.match(ZCodeParser.RSBracket)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 157
                self.arrayAssign()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayDimContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NumberLit(self):
            return self.getToken(ZCodeParser.NumberLit, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def arrayDim(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayDimContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayDim




    def arrayDim(self):

        localctx = ZCodeParser.ArrayDimContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arrayDim)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(ZCodeParser.NumberLit)
                self.state = 161
                self.match(ZCodeParser.COMMA)
                self.state = 162
                self.arrayDim()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(ZCodeParser.NumberLit)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFTARR(self):
            return self.getToken(ZCodeParser.LEFTARR, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def LSBracket(self):
            return self.getToken(ZCodeParser.LSBracket, 0)

        def arrayElementList(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayElementListContext,0)


        def RSBracket(self):
            return self.getToken(ZCodeParser.RSBracket, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayAssign




    def arrayAssign(self):

        localctx = ZCodeParser.ArrayAssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_arrayAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(ZCodeParser.LEFTARR)
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.state = 167
                self.match(ZCodeParser.LSBracket)
                self.state = 168
                self.arrayElementList()
                self.state = 169
                self.match(ZCodeParser.RSBracket)
                pass
            elif token in [1, 2, 20, 24, 37, 43, 44, 45]:
                self.state = 171
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayElementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literalList(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralListContext,0)


        def arrayList(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayListContext,0)


        def expressionList(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayElementList




    def arrayElementList(self):

        localctx = ZCodeParser.ArrayElementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_arrayElementList)
        try:
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 174
                self.literalList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.arrayList()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 176
                self.expressionList()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSBracket(self):
            return self.getToken(ZCodeParser.LSBracket, 0)

        def arrayElementList(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayElementListContext,0)


        def RSBracket(self):
            return self.getToken(ZCodeParser.RSBracket, 0)

        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def arrayList(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayList




    def arrayList(self):

        localctx = ZCodeParser.ArrayListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arrayList)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(ZCodeParser.LSBracket)
                self.state = 180
                self.arrayElementList()
                self.state = 181
                self.match(ZCodeParser.RSBracket)
                self.state = 182
                self.match(ZCodeParser.COMMA)
                self.state = 183
                self.arrayList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(ZCodeParser.LSBracket)
                self.state = 186
                self.arrayElementList()
                self.state = 187
                self.match(ZCodeParser.RSBracket)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def literalList(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_literalList




    def literalList(self):

        localctx = ZCodeParser.LiteralListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_literalList)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.literal()
                self.state = 192
                self.match(ZCodeParser.COMMA)
                self.state = 193
                self.literalList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementAccessExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrExpr(self):
            return self.getTypedRuleContext(ZCodeParser.ArrExprContext,0)


        def LSBracket(self):
            return self.getToken(ZCodeParser.LSBracket, 0)

        def indexList(self):
            return self.getTypedRuleContext(ZCodeParser.IndexListContext,0)


        def RSBracket(self):
            return self.getToken(ZCodeParser.RSBracket, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elementAccessExpr




    def elementAccessExpr(self):

        localctx = ZCodeParser.ElementAccessExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_elementAccessExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.arrExpr()
            self.state = 199
            self.match(ZCodeParser.LSBracket)
            self.state = 200
            self.indexList()
            self.state = 201
            self.match(ZCodeParser.RSBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def functionCall(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrExpr




    def arrExpr(self):

        localctx = ZCodeParser.ArrExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_arrExpr)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def indexList(self):
            return self.getTypedRuleContext(ZCodeParser.IndexListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_indexList




    def indexList(self):

        localctx = ZCodeParser.IndexListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_indexList)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.expression()
                self.state = 208
                self.match(ZCodeParser.COMMA)
                self.state = 209
                self.indexList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LBracket(self):
            return self.getToken(ZCodeParser.LBracket, 0)

        def functionArgsList(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionArgsListContext,0)


        def RBracket(self):
            return self.getToken(ZCodeParser.RBracket, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_functionCall




    def functionCall(self):

        localctx = ZCodeParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 215
            self.match(ZCodeParser.LBracket)
            self.state = 216
            self.functionArgsList()
            self.state = 217
            self.match(ZCodeParser.RBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionArgsListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argsPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ArgsPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_functionArgsList




    def functionArgsList(self):

        localctx = ZCodeParser.FunctionArgsListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_functionArgsList)
        try:
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 20, 24, 37, 43, 44, 45]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.argsPrime()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arg(self):
            return self.getTypedRuleContext(ZCodeParser.ArgContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def argsPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ArgsPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_argsPrime




    def argsPrime(self):

        localctx = ZCodeParser.ArgsPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_argsPrime)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self.arg()
                self.state = 224
                self.match(ZCodeParser.COMMA)
                self.state = 225
                self.argsPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.arg()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arg




    def arg(self):

        localctx = ZCodeParser.ArgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalarAssignStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ScalarAssignStatementContext,0)


        def arrayAssignStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayAssignStatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_assignStatement




    def assignStatement(self):

        localctx = ZCodeParser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assignStatement)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.scalarAssignStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.arrayAssignStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarAssignStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LEFTARR(self):
            return self.getToken(ZCodeParser.LEFTARR, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_scalarAssignStatement




    def scalarAssignStatement(self):

        localctx = ZCodeParser.ScalarAssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_scalarAssignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 237
            self.match(ZCodeParser.LEFTARR)
            self.state = 238
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAssignStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrayAssign(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayAssignContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def elementAccessExpr(self):
            return self.getTypedRuleContext(ZCodeParser.ElementAccessExprContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_arrayAssignStatement




    def arrayAssignStatement(self):

        localctx = ZCodeParser.ArrayAssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_arrayAssignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 240
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 241
                self.elementAccessExpr()
                pass


            self.state = 244
            self.arrayAssign()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(ZCodeParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ForStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(ZCodeParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ContinueStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnStatementContext,0)


        def functionCallStatement(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionCallStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(ZCodeParser.BlockStatementContext,0)


        def assignStatement(self):
            return self.getTypedRuleContext(ZCodeParser.AssignStatementContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_statement




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 246
                self.ifStatement()
                pass

            elif la_ == 2:
                self.state = 247
                self.forStatement()
                pass

            elif la_ == 3:
                self.state = 248
                self.breakStatement()
                pass

            elif la_ == 4:
                self.state = 249
                self.continueStatement()
                pass

            elif la_ == 5:
                self.state = 250
                self.returnStatement()
                pass

            elif la_ == 6:
                self.state = 251
                self.functionCallStatement()
                pass

            elif la_ == 7:
                self.state = 252
                self.blockStatement()
                pass

            elif la_ == 8:
                self.state = 253
                self.assignStatement()
                pass


            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.state = 257 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 256
                        self.match(ZCodeParser.NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 259 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                pass
            elif token in [-1]:
                self.state = 261
                self.match(ZCodeParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normalDeclaration(self):
            return self.getTypedRuleContext(ZCodeParser.NormalDeclarationContext,0)


        def arrayDeclaration(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayDeclarationContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(ZCodeParser.VarDeclContext,0)


        def dynamicDecl(self):
            return self.getTypedRuleContext(ZCodeParser.DynamicDeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variableDeclaration




    def variableDeclaration(self):

        localctx = ZCodeParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 264
                self.normalDeclaration()
                pass

            elif la_ == 2:
                self.state = 265
                self.arrayDeclaration()
                pass

            elif la_ == 3:
                self.state = 266
                self.varDecl()
                pass

            elif la_ == 4:
                self.state = 267
                self.dynamicDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NormalDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varType(self):
            return self.getTypedRuleContext(ZCodeParser.VarTypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def variableInitialization(self):
            return self.getTypedRuleContext(ZCodeParser.VariableInitializationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_normalDeclaration




    def normalDeclaration(self):

        localctx = ZCodeParser.NormalDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_normalDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.varType()
            self.state = 271
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 272
                self.variableInitialization()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_varType




    def varType(self):

        localctx = ZCodeParser.VarTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_varType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 56) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(ZCodeParser.VAR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def variableInitialization(self):
            return self.getTypedRuleContext(ZCodeParser.VariableInitializationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_varDecl




    def varDecl(self):

        localctx = ZCodeParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(ZCodeParser.VAR)
            self.state = 278
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 279
            self.variableInitialization()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DynamicDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DYNAMIC(self):
            return self.getToken(ZCodeParser.DYNAMIC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def variableInitialization(self):
            return self.getTypedRuleContext(ZCodeParser.VariableInitializationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_dynamicDecl




    def dynamicDecl(self):

        localctx = ZCodeParser.DynamicDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_dynamicDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(ZCodeParser.DYNAMIC)
            self.state = 282
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 283
                self.variableInitialization()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableInitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFTARR(self):
            return self.getToken(ZCodeParser.LEFTARR, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_variableInitialization




    def variableInitialization(self):

        localctx = ZCodeParser.VariableInitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_variableInitialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.match(ZCodeParser.LEFTARR)
            self.state = 287
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramDeclPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamDeclPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramDeclList




    def paramDeclList(self):

        localctx = ZCodeParser.ParamDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_paramDeclList)
        try:
            self.state = 291
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.paramDeclPrime()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramDeclAtom(self):
            return self.getTypedRuleContext(ZCodeParser.ParamDeclAtomContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def paramDeclPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ParamDeclPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_paramDeclPrime




    def paramDeclPrime(self):

        localctx = ZCodeParser.ParamDeclPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_paramDeclPrime)
        try:
            self.state = 298
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.paramDeclAtom()
                self.state = 294
                self.match(ZCodeParser.COMMA)
                self.state = 295
                self.paramDeclPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.paramDeclAtom()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclAtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varType(self):
            return self.getTypedRuleContext(ZCodeParser.VarTypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LSBracket(self):
            return self.getToken(ZCodeParser.LSBracket, 0)

        def arrayDim(self):
            return self.getTypedRuleContext(ZCodeParser.ArrayDimContext,0)


        def RSBracket(self):
            return self.getToken(ZCodeParser.RSBracket, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_paramDeclAtom




    def paramDeclAtom(self):

        localctx = ZCodeParser.ParamDeclAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_paramDeclAtom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.varType()
            self.state = 301
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 306
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 302
                self.match(ZCodeParser.LSBracket)
                self.state = 303
                self.arrayDim()
                self.state = 304
                self.match(ZCodeParser.RSBracket)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def paramDecl(self):
            return self.getTypedRuleContext(ZCodeParser.ParamDeclContext,0)


        def functionBody(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionBodyContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_functionDecl




    def functionDecl(self):

        localctx = ZCodeParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(ZCodeParser.FUNC)
            self.state = 309
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 310
            self.paramDecl()
            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 311
                self.match(ZCodeParser.NEWLINE)
                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 317
            self.functionBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionPreDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ZCodeParser.FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def paramDecl(self):
            return self.getTypedRuleContext(ZCodeParser.ParamDeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_functionPreDecl




    def functionPreDecl(self):

        localctx = ZCodeParser.FunctionPreDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_functionPreDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(ZCodeParser.FUNC)
            self.state = 320
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 321
            self.paramDecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBracket(self):
            return self.getToken(ZCodeParser.LBracket, 0)

        def paramDeclList(self):
            return self.getTypedRuleContext(ZCodeParser.ParamDeclListContext,0)


        def RBracket(self):
            return self.getToken(ZCodeParser.RBracket, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_paramDecl




    def paramDecl(self):

        localctx = ZCodeParser.ParamDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_paramDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.match(ZCodeParser.LBracket)
            self.state = 324
            self.paramDeclList()
            self.state = 325
            self.match(ZCodeParser.RBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStatement(self):
            return self.getTypedRuleContext(ZCodeParser.BlockStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ReturnStatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_functionBody




    def functionBody(self):

        localctx = ZCodeParser.FunctionBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_functionBody)
        try:
            self.state = 329
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.blockStatement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
                self.returnStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ZCodeParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def elifStatementList(self):
            return self.getTypedRuleContext(ZCodeParser.ElifStatementListContext,0)


        def elseStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ElseStatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_ifStatement




    def ifStatement(self):

        localctx = ZCodeParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(ZCodeParser.IF)
            self.state = 332
            self.expression()
            self.state = 333
            self.statement()
            self.state = 334
            self.elifStatementList()
            self.state = 336
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 335
                self.elseStatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifStatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifStatementPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ElifStatementPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifStatementList




    def elifStatementList(self):

        localctx = ZCodeParser.ElifStatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_elifStatementList)
        try:
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.elifStatementPrime()
                pass
            elif token in [-1, 16, 42]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifStatementPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elifStatement(self):
            return self.getTypedRuleContext(ZCodeParser.ElifStatementContext,0)


        def elifStatementPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ElifStatementPrimeContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_elifStatementPrime




    def elifStatementPrime(self):

        localctx = ZCodeParser.ElifStatementPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_elifStatementPrime)
        self._la = 0 # Token type
        try:
            self.state = 352
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.elifStatement()
                self.state = 346
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==42:
                    self.state = 343
                    self.match(ZCodeParser.NEWLINE)
                    self.state = 348
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 349
                self.elifStatementPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.elifStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIF(self):
            return self.getToken(ZCodeParser.ELIF, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifStatement




    def elifStatement(self):

        localctx = ZCodeParser.ElifStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_elifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(ZCodeParser.ELIF)
            self.state = 355
            self.expression()
            self.state = 356
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(ZCodeParser.ELSE, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elseStatement




    def elseStatement(self):

        localctx = ZCodeParser.ElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(ZCodeParser.ELSE)
            self.state = 359
            self.expression()
            self.state = 360
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(ZCodeParser.FOR, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def UNTIL(self):
            return self.getToken(ZCodeParser.UNTIL, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def BY(self):
            return self.getToken(ZCodeParser.BY, 0)

        def updateExpr(self):
            return self.getTypedRuleContext(ZCodeParser.UpdateExprContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(ZCodeParser.NEWLINE)
            else:
                return self.getToken(ZCodeParser.NEWLINE, i)

        def getRuleIndex(self):
            return ZCodeParser.RULE_forStatement




    def forStatement(self):

        localctx = ZCodeParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.match(ZCodeParser.FOR)
            self.state = 363
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 364
            self.match(ZCodeParser.UNTIL)
            self.state = 365
            self.expression()
            self.state = 366
            self.match(ZCodeParser.BY)
            self.state = 367
            self.updateExpr()
            self.state = 371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 368
                self.match(ZCodeParser.NEWLINE)
                self.state = 373
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 374
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_updateExpr




    def updateExpr(self):

        localctx = ZCodeParser.UpdateExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_updateExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(ZCodeParser.BREAK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_breakStatement




    def breakStatement(self):

        localctx = ZCodeParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(ZCodeParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(ZCodeParser.CONTINUE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_continueStatement




    def continueStatement(self):

        localctx = ZCodeParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(ZCodeParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(ZCodeParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_returnStatement




    def returnStatement(self):

        localctx = ZCodeParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(ZCodeParser.RETURN)
            self.state = 384
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 61710107934726) != 0):
                self.state = 383
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_functionCallStatement




    def functionCallStatement(self):

        localctx = ZCodeParser.FunctionCallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_functionCallStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.functionCall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(ZCodeParser.BEGIN, 0)

        def END(self):
            return self.getToken(ZCodeParser.END, 0)

        def blockStatementBody(self):
            return self.getTypedRuleContext(ZCodeParser.BlockStatementBodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_blockStatement




    def blockStatement(self):

        localctx = ZCodeParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_blockStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(ZCodeParser.BEGIN)

            self.state = 389
            self.blockStatementBody()
            self.state = 390
            self.match(ZCodeParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nullableListOfStatement(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfStatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_blockStatementBody




    def blockStatementBody(self):

        localctx = ZCodeParser.BlockStatementBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_blockStatementBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.nullableListOfStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NullableListOfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.StatementContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.StatementContext,i)


        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.DeclarationContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullableListOfStatement




    def nullableListOfStatement(self):

        localctx = ZCodeParser.NullableListOfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_nullableListOfStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 35184372410360) != 0):
                self.state = 396
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6, 10, 13, 14, 15, 18, 45]:
                    self.state = 394
                    self.statement()
                    pass
                elif token in [3, 4, 5, 7, 8, 9]:
                    self.state = 395
                    self.declaration()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 400
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def COMMA(self):
            return self.getToken(ZCodeParser.COMMA, 0)

        def expressionList(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expressionList




    def expressionList(self):

        localctx = ZCodeParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expressionList)
        try:
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.expression()
                self.state = 402
                self.match(ZCodeParser.COMMA)
                self.state = 403
                self.expressionList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression1Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression1Context,i)


        def ELLIPSIS(self):
            return self.getToken(ZCodeParser.ELLIPSIS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expression)
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.expression1()
                self.state = 409
                self.match(ZCodeParser.ELLIPSIS)
                self.state = 410
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Expression2Context)
            else:
                return self.getTypedRuleContext(ZCodeParser.Expression2Context,i)


        def EQUAL(self):
            return self.getToken(ZCodeParser.EQUAL, 0)

        def EQUALEQUAL(self):
            return self.getToken(ZCodeParser.EQUALEQUAL, 0)

        def NOTEQUAL(self):
            return self.getToken(ZCodeParser.NOTEQUAL, 0)

        def LESS(self):
            return self.getToken(ZCodeParser.LESS, 0)

        def LESSOREQUAL(self):
            return self.getToken(ZCodeParser.LESSOREQUAL, 0)

        def GREATER(self):
            return self.getToken(ZCodeParser.GREATER, 0)

        def GREATEROREQUAL(self):
            return self.getToken(ZCodeParser.GREATEROREQUAL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression1




    def expression1(self):

        localctx = ZCodeParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 415
                self.expression2(0)
                self.state = 416
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67914170368) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 417
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 419
                self.expression2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def expression2(self):
            return self.getTypedRuleContext(ZCodeParser.Expression2Context,0)


        def AND(self):
            return self.getToken(ZCodeParser.AND, 0)

        def OR(self):
            return self.getToken(ZCodeParser.OR, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression2



    def expression2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 430
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 425
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 426
                    _la = self._input.LA(1)
                    if not(_la==21 or _la==22):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 427
                    self.expression3(0) 
                self.state = 432
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def expression3(self):
            return self.getTypedRuleContext(ZCodeParser.Expression3Context,0)


        def PLUS(self):
            return self.getToken(ZCodeParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression3



    def expression3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 441
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 436
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 437
                    _la = self._input.LA(1)
                    if not(_la==23 or _la==24):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 438
                    self.expression4(0) 
                self.state = 443
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression4(self):
            return self.getTypedRuleContext(ZCodeParser.Expression4Context,0)


        def MULT(self):
            return self.getToken(ZCodeParser.MULT, 0)

        def DIV(self):
            return self.getToken(ZCodeParser.DIV, 0)

        def MOD(self):
            return self.getToken(ZCodeParser.MOD, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_expression4



    def expression4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ZCodeParser.Expression4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 452
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 447
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 448
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 449
                    self.expression5() 
                self.state = 454
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ZCodeParser.NOT, 0)

        def expression5(self):
            return self.getTypedRuleContext(ZCodeParser.Expression5Context,0)


        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression5




    def expression5(self):

        localctx = ZCodeParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_expression5)
        try:
            self.state = 458
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 455
                self.match(ZCodeParser.NOT)
                self.state = 456
                self.expression5()
                pass
            elif token in [1, 2, 24, 37, 43, 44, 45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
                self.expression6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(ZCodeParser.MINUS, 0)

        def expression6(self):
            return self.getTypedRuleContext(ZCodeParser.Expression6Context,0)


        def expression7(self):
            return self.getTypedRuleContext(ZCodeParser.Expression7Context,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression6




    def expression6(self):

        localctx = ZCodeParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_expression6)
        try:
            self.state = 463
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.match(ZCodeParser.MINUS)
                self.state = 461
                self.expression6()
                pass
            elif token in [1, 2, 37, 43, 44, 45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.expression7()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementAccessExpr(self):
            return self.getTypedRuleContext(ZCodeParser.ElementAccessExprContext,0)


        def operands(self):
            return self.getTypedRuleContext(ZCodeParser.OperandsContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression7




    def expression7(self):

        localctx = ZCodeParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_expression7)
        try:
            self.state = 467
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.elementAccessExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
                self.operands()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def LBracket(self):
            return self.getToken(ZCodeParser.LBracket, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def RBracket(self):
            return self.getToken(ZCodeParser.RBracket, 0)

        def functionCall(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_operands




    def operands(self):

        localctx = ZCodeParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_operands)
        try:
            self.state = 476
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 469
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 470
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 471
                self.match(ZCodeParser.LBracket)
                self.state = 472
                self.expression()
                self.state = 473
                self.match(ZCodeParser.RBracket)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 475
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[52] = self.expression2_sempred
        self._predicates[53] = self.expression3_sempred
        self._predicates[54] = self.expression4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression2_sempred(self, localctx:Expression2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expression3_sempred(self, localctx:Expression3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expression4_sempred(self, localctx:Expression4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




