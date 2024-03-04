# Generated from /home/qmi/repos/PPL_232/ass1/initial/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
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
        4,1,51,511,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,65,
        2,66,7,66,1,0,1,0,1,1,1,1,1,1,3,1,140,8,1,1,2,1,2,1,2,3,2,145,8,
        2,1,3,1,3,1,3,1,3,1,4,1,4,3,4,153,8,4,1,5,1,5,3,5,157,8,5,1,6,1,
        6,1,6,1,6,1,6,3,6,164,8,6,1,7,1,7,3,7,168,8,7,1,8,1,8,3,8,172,8,
        8,1,9,1,9,1,9,1,9,1,9,3,9,179,8,9,1,10,1,10,3,10,183,8,10,1,11,1,
        11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,193,8,12,1,13,1,13,1,13,1,
        13,3,13,199,8,13,1,14,1,14,1,14,1,14,1,14,1,14,3,14,207,8,14,1,15,
        1,15,1,15,3,15,212,8,15,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,3,16,224,8,16,1,17,1,17,1,17,1,17,1,17,3,17,231,8,17,1,
        18,1,18,1,18,1,18,1,18,1,19,1,19,3,19,240,8,19,1,20,1,20,1,20,1,
        20,1,20,3,20,247,8,20,1,21,1,21,1,21,1,21,1,21,1,22,1,22,3,22,256,
        8,22,1,23,1,23,1,23,1,23,1,23,3,23,263,8,23,1,24,1,24,1,25,1,25,
        3,25,269,8,25,1,26,1,26,1,26,1,26,1,27,1,27,3,27,277,8,27,1,27,1,
        27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,289,8,28,1,28,4,
        28,292,8,28,11,28,12,28,293,1,28,3,28,297,8,28,1,29,1,29,1,29,1,
        29,3,29,303,8,29,1,30,1,30,1,30,3,30,308,8,30,1,31,1,31,1,32,1,32,
        1,32,1,32,1,33,1,33,1,33,3,33,319,8,33,1,34,1,34,1,34,1,35,1,35,
        3,35,326,8,35,1,36,1,36,1,36,1,36,1,36,3,36,333,8,36,1,37,1,37,1,
        37,1,37,1,37,1,37,3,37,341,8,37,1,38,1,38,1,38,1,38,1,39,1,39,1,
        39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,41,1,41,3,41,359,8,41,1,
        42,1,42,1,42,1,42,1,42,1,42,3,42,367,8,42,1,43,1,43,3,43,371,8,43,
        1,44,1,44,1,44,1,44,1,44,3,44,378,8,44,1,45,1,45,1,45,1,45,1,45,
        1,46,1,46,1,46,1,46,1,46,1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,47,
        1,47,1,48,1,48,1,49,1,49,1,50,1,50,1,51,1,51,3,51,407,8,51,1,52,
        1,52,1,53,1,53,1,53,1,53,1,54,1,54,1,55,1,55,3,55,419,8,55,1,56,
        1,56,3,56,423,8,56,1,56,1,56,1,56,1,56,1,56,3,56,430,8,56,3,56,432,
        8,56,1,57,1,57,1,57,1,57,1,57,3,57,439,8,57,1,58,1,58,1,58,1,58,
        1,58,3,58,446,8,58,1,59,1,59,1,59,1,59,1,59,3,59,453,8,59,1,60,1,
        60,1,60,1,60,1,60,1,60,5,60,461,8,60,10,60,12,60,464,9,60,1,61,1,
        61,1,61,1,61,1,61,1,61,5,61,472,8,61,10,61,12,61,475,9,61,1,62,1,
        62,1,62,1,62,1,62,1,62,5,62,483,8,62,10,62,12,62,486,9,62,1,63,1,
        63,1,63,3,63,491,8,63,1,64,1,64,1,64,3,64,496,8,64,1,65,1,65,3,65,
        500,8,65,1,66,1,66,1,66,1,66,1,66,1,66,1,66,3,66,509,8,66,1,66,0,
        3,120,122,124,67,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,
        80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,114,116,
        118,120,122,124,126,128,130,132,0,6,1,0,43,45,1,0,3,5,2,0,28,28,
        30,35,1,0,21,22,1,0,23,24,1,0,25,27,503,0,134,1,0,0,0,2,139,1,0,
        0,0,4,144,1,0,0,0,6,146,1,0,0,0,8,152,1,0,0,0,10,156,1,0,0,0,12,
        163,1,0,0,0,14,167,1,0,0,0,16,171,1,0,0,0,18,178,1,0,0,0,20,182,
        1,0,0,0,22,184,1,0,0,0,24,186,1,0,0,0,26,198,1,0,0,0,28,200,1,0,
        0,0,30,211,1,0,0,0,32,223,1,0,0,0,34,230,1,0,0,0,36,232,1,0,0,0,
        38,239,1,0,0,0,40,246,1,0,0,0,42,248,1,0,0,0,44,255,1,0,0,0,46,262,
        1,0,0,0,48,264,1,0,0,0,50,268,1,0,0,0,52,270,1,0,0,0,54,276,1,0,
        0,0,56,288,1,0,0,0,58,302,1,0,0,0,60,304,1,0,0,0,62,309,1,0,0,0,
        64,311,1,0,0,0,66,315,1,0,0,0,68,320,1,0,0,0,70,325,1,0,0,0,72,332,
        1,0,0,0,74,334,1,0,0,0,76,342,1,0,0,0,78,346,1,0,0,0,80,352,1,0,
        0,0,82,358,1,0,0,0,84,360,1,0,0,0,86,370,1,0,0,0,88,377,1,0,0,0,
        90,379,1,0,0,0,92,384,1,0,0,0,94,389,1,0,0,0,96,398,1,0,0,0,98,400,
        1,0,0,0,100,402,1,0,0,0,102,404,1,0,0,0,104,408,1,0,0,0,106,410,
        1,0,0,0,108,414,1,0,0,0,110,418,1,0,0,0,112,431,1,0,0,0,114,438,
        1,0,0,0,116,445,1,0,0,0,118,452,1,0,0,0,120,454,1,0,0,0,122,465,
        1,0,0,0,124,476,1,0,0,0,126,490,1,0,0,0,128,495,1,0,0,0,130,499,
        1,0,0,0,132,508,1,0,0,0,134,135,7,0,0,0,135,1,1,0,0,0,136,137,5,
        42,0,0,137,140,3,2,1,0,138,140,1,0,0,0,139,136,1,0,0,0,139,138,1,
        0,0,0,140,3,1,0,0,0,141,142,5,42,0,0,142,145,3,4,2,0,143,145,5,42,
        0,0,144,141,1,0,0,0,144,143,1,0,0,0,145,5,1,0,0,0,146,147,3,2,1,
        0,147,148,3,10,5,0,148,149,5,0,0,1,149,7,1,0,0,0,150,153,3,20,10,
        0,151,153,3,58,29,0,152,150,1,0,0,0,152,151,1,0,0,0,153,9,1,0,0,
        0,154,157,3,12,6,0,155,157,1,0,0,0,156,154,1,0,0,0,156,155,1,0,0,
        0,157,11,1,0,0,0,158,159,3,8,4,0,159,160,3,4,2,0,160,161,3,12,6,
        0,161,164,1,0,0,0,162,164,3,8,4,0,163,158,1,0,0,0,163,162,1,0,0,
        0,164,13,1,0,0,0,165,168,3,20,10,0,166,168,3,58,29,0,167,165,1,0,
        0,0,167,166,1,0,0,0,168,15,1,0,0,0,169,172,3,18,9,0,170,172,1,0,
        0,0,171,169,1,0,0,0,171,170,1,0,0,0,172,17,1,0,0,0,173,174,3,14,
        7,0,174,175,3,4,2,0,175,176,3,18,9,0,176,179,1,0,0,0,177,179,3,14,
        7,0,178,173,1,0,0,0,178,177,1,0,0,0,179,19,1,0,0,0,180,183,3,22,
        11,0,181,183,3,76,38,0,182,180,1,0,0,0,182,181,1,0,0,0,183,21,1,
        0,0,0,184,185,3,78,39,0,185,23,1,0,0,0,186,187,3,62,31,0,187,188,
        5,46,0,0,188,189,5,39,0,0,189,190,3,26,13,0,190,192,5,40,0,0,191,
        193,3,28,14,0,192,191,1,0,0,0,192,193,1,0,0,0,193,25,1,0,0,0,194,
        195,5,43,0,0,195,196,5,41,0,0,196,199,3,26,13,0,197,199,5,43,0,0,
        198,194,1,0,0,0,198,197,1,0,0,0,199,27,1,0,0,0,200,206,5,29,0,0,
        201,202,5,39,0,0,202,203,3,30,15,0,203,204,5,40,0,0,204,207,1,0,
        0,0,205,207,3,116,58,0,206,201,1,0,0,0,206,205,1,0,0,0,207,29,1,
        0,0,0,208,212,3,34,17,0,209,212,3,32,16,0,210,212,3,114,57,0,211,
        208,1,0,0,0,211,209,1,0,0,0,211,210,1,0,0,0,212,31,1,0,0,0,213,214,
        5,39,0,0,214,215,3,30,15,0,215,216,5,40,0,0,216,217,5,41,0,0,217,
        218,3,32,16,0,218,224,1,0,0,0,219,220,5,39,0,0,220,221,3,30,15,0,
        221,222,5,40,0,0,222,224,1,0,0,0,223,213,1,0,0,0,223,219,1,0,0,0,
        224,33,1,0,0,0,225,226,3,0,0,0,226,227,5,41,0,0,227,228,3,34,17,
        0,228,231,1,0,0,0,229,231,3,0,0,0,230,225,1,0,0,0,230,229,1,0,0,
        0,231,35,1,0,0,0,232,233,3,38,19,0,233,234,5,39,0,0,234,235,3,40,
        20,0,235,236,5,40,0,0,236,37,1,0,0,0,237,240,5,46,0,0,238,240,3,
        42,21,0,239,237,1,0,0,0,239,238,1,0,0,0,240,39,1,0,0,0,241,242,3,
        116,58,0,242,243,5,41,0,0,243,244,3,40,20,0,244,247,1,0,0,0,245,
        247,3,116,58,0,246,241,1,0,0,0,246,245,1,0,0,0,247,41,1,0,0,0,248,
        249,5,46,0,0,249,250,5,37,0,0,250,251,3,44,22,0,251,252,5,38,0,0,
        252,43,1,0,0,0,253,256,3,46,23,0,254,256,1,0,0,0,255,253,1,0,0,0,
        255,254,1,0,0,0,256,45,1,0,0,0,257,258,3,48,24,0,258,259,5,41,0,
        0,259,260,3,46,23,0,260,263,1,0,0,0,261,263,3,48,24,0,262,257,1,
        0,0,0,262,261,1,0,0,0,263,47,1,0,0,0,264,265,3,116,58,0,265,49,1,
        0,0,0,266,269,3,52,26,0,267,269,3,54,27,0,268,266,1,0,0,0,268,267,
        1,0,0,0,269,51,1,0,0,0,270,271,5,46,0,0,271,272,5,29,0,0,272,273,
        3,116,58,0,273,53,1,0,0,0,274,277,5,46,0,0,275,277,3,36,18,0,276,
        274,1,0,0,0,276,275,1,0,0,0,277,278,1,0,0,0,278,279,3,28,14,0,279,
        55,1,0,0,0,280,289,3,84,42,0,281,289,3,94,47,0,282,289,3,98,49,0,
        283,289,3,100,50,0,284,289,3,102,51,0,285,289,3,104,52,0,286,289,
        3,106,53,0,287,289,3,50,25,0,288,280,1,0,0,0,288,281,1,0,0,0,288,
        282,1,0,0,0,288,283,1,0,0,0,288,284,1,0,0,0,288,285,1,0,0,0,288,
        286,1,0,0,0,288,287,1,0,0,0,289,296,1,0,0,0,290,292,5,42,0,0,291,
        290,1,0,0,0,292,293,1,0,0,0,293,291,1,0,0,0,293,294,1,0,0,0,294,
        297,1,0,0,0,295,297,5,0,0,1,296,291,1,0,0,0,296,295,1,0,0,0,297,
        57,1,0,0,0,298,303,3,60,30,0,299,303,3,24,12,0,300,303,3,64,32,0,
        301,303,3,66,33,0,302,298,1,0,0,0,302,299,1,0,0,0,302,300,1,0,0,
        0,302,301,1,0,0,0,303,59,1,0,0,0,304,305,3,62,31,0,305,307,5,46,
        0,0,306,308,3,68,34,0,307,306,1,0,0,0,307,308,1,0,0,0,308,61,1,0,
        0,0,309,310,7,1,0,0,310,63,1,0,0,0,311,312,5,7,0,0,312,313,5,46,
        0,0,313,314,3,68,34,0,314,65,1,0,0,0,315,316,5,8,0,0,316,318,5,46,
        0,0,317,319,3,68,34,0,318,317,1,0,0,0,318,319,1,0,0,0,319,67,1,0,
        0,0,320,321,5,29,0,0,321,322,3,116,58,0,322,69,1,0,0,0,323,326,3,
        72,36,0,324,326,1,0,0,0,325,323,1,0,0,0,325,324,1,0,0,0,326,71,1,
        0,0,0,327,328,3,74,37,0,328,329,5,41,0,0,329,330,3,72,36,0,330,333,
        1,0,0,0,331,333,3,74,37,0,332,327,1,0,0,0,332,331,1,0,0,0,333,73,
        1,0,0,0,334,335,3,62,31,0,335,340,5,46,0,0,336,337,5,39,0,0,337,
        338,3,26,13,0,338,339,5,40,0,0,339,341,1,0,0,0,340,336,1,0,0,0,340,
        341,1,0,0,0,341,75,1,0,0,0,342,343,5,9,0,0,343,344,5,46,0,0,344,
        345,3,80,40,0,345,77,1,0,0,0,346,347,5,9,0,0,347,348,5,46,0,0,348,
        349,3,80,40,0,349,350,3,2,1,0,350,351,3,82,41,0,351,79,1,0,0,0,352,
        353,5,37,0,0,353,354,3,70,35,0,354,355,5,38,0,0,355,81,1,0,0,0,356,
        359,3,106,53,0,357,359,3,102,51,0,358,356,1,0,0,0,358,357,1,0,0,
        0,359,83,1,0,0,0,360,361,5,15,0,0,361,362,3,116,58,0,362,363,3,2,
        1,0,363,364,3,56,28,0,364,366,3,86,43,0,365,367,3,92,46,0,366,365,
        1,0,0,0,366,367,1,0,0,0,367,85,1,0,0,0,368,371,3,88,44,0,369,371,
        1,0,0,0,370,368,1,0,0,0,370,369,1,0,0,0,371,87,1,0,0,0,372,373,3,
        90,45,0,373,374,3,2,1,0,374,375,3,88,44,0,375,378,1,0,0,0,376,378,
        3,90,45,0,377,372,1,0,0,0,377,376,1,0,0,0,378,89,1,0,0,0,379,380,
        5,17,0,0,380,381,3,116,58,0,381,382,3,2,1,0,382,383,3,56,28,0,383,
        91,1,0,0,0,384,385,5,16,0,0,385,386,3,116,58,0,386,387,3,2,1,0,387,
        388,3,56,28,0,388,93,1,0,0,0,389,390,5,10,0,0,390,391,5,46,0,0,391,
        392,5,11,0,0,392,393,3,116,58,0,393,394,5,12,0,0,394,395,3,96,48,
        0,395,396,3,2,1,0,396,397,3,56,28,0,397,95,1,0,0,0,398,399,3,116,
        58,0,399,97,1,0,0,0,400,401,5,13,0,0,401,99,1,0,0,0,402,403,5,14,
        0,0,403,101,1,0,0,0,404,406,5,6,0,0,405,407,3,116,58,0,406,405,1,
        0,0,0,406,407,1,0,0,0,407,103,1,0,0,0,408,409,3,42,21,0,409,105,
        1,0,0,0,410,411,5,18,0,0,411,412,3,108,54,0,412,413,5,19,0,0,413,
        107,1,0,0,0,414,415,3,110,55,0,415,109,1,0,0,0,416,419,3,112,56,
        0,417,419,1,0,0,0,418,416,1,0,0,0,418,417,1,0,0,0,419,111,1,0,0,
        0,420,423,3,56,28,0,421,423,3,14,7,0,422,420,1,0,0,0,422,421,1,0,
        0,0,423,424,1,0,0,0,424,425,3,4,2,0,425,426,3,112,56,0,426,432,1,
        0,0,0,427,430,3,56,28,0,428,430,3,14,7,0,429,427,1,0,0,0,429,428,
        1,0,0,0,430,432,1,0,0,0,431,422,1,0,0,0,431,429,1,0,0,0,432,113,
        1,0,0,0,433,434,3,116,58,0,434,435,5,41,0,0,435,436,3,114,57,0,436,
        439,1,0,0,0,437,439,3,116,58,0,438,433,1,0,0,0,438,437,1,0,0,0,439,
        115,1,0,0,0,440,441,3,118,59,0,441,442,5,36,0,0,442,443,3,118,59,
        0,443,446,1,0,0,0,444,446,3,118,59,0,445,440,1,0,0,0,445,444,1,0,
        0,0,446,117,1,0,0,0,447,448,3,120,60,0,448,449,7,2,0,0,449,450,3,
        120,60,0,450,453,1,0,0,0,451,453,3,120,60,0,452,447,1,0,0,0,452,
        451,1,0,0,0,453,119,1,0,0,0,454,455,6,60,-1,0,455,456,3,122,61,0,
        456,462,1,0,0,0,457,458,10,2,0,0,458,459,7,3,0,0,459,461,3,122,61,
        0,460,457,1,0,0,0,461,464,1,0,0,0,462,460,1,0,0,0,462,463,1,0,0,
        0,463,121,1,0,0,0,464,462,1,0,0,0,465,466,6,61,-1,0,466,467,3,124,
        62,0,467,473,1,0,0,0,468,469,10,2,0,0,469,470,7,4,0,0,470,472,3,
        124,62,0,471,468,1,0,0,0,472,475,1,0,0,0,473,471,1,0,0,0,473,474,
        1,0,0,0,474,123,1,0,0,0,475,473,1,0,0,0,476,477,6,62,-1,0,477,478,
        3,126,63,0,478,484,1,0,0,0,479,480,10,2,0,0,480,481,7,5,0,0,481,
        483,3,126,63,0,482,479,1,0,0,0,483,486,1,0,0,0,484,482,1,0,0,0,484,
        485,1,0,0,0,485,125,1,0,0,0,486,484,1,0,0,0,487,488,5,20,0,0,488,
        491,3,126,63,0,489,491,3,128,64,0,490,487,1,0,0,0,490,489,1,0,0,
        0,491,127,1,0,0,0,492,493,5,24,0,0,493,496,3,128,64,0,494,496,3,
        130,65,0,495,492,1,0,0,0,495,494,1,0,0,0,496,129,1,0,0,0,497,500,
        3,36,18,0,498,500,3,132,66,0,499,497,1,0,0,0,499,498,1,0,0,0,500,
        131,1,0,0,0,501,509,3,0,0,0,502,509,5,46,0,0,503,504,5,37,0,0,504,
        505,3,116,58,0,505,506,5,38,0,0,506,509,1,0,0,0,507,509,3,42,21,
        0,508,501,1,0,0,0,508,502,1,0,0,0,508,503,1,0,0,0,508,507,1,0,0,
        0,509,133,1,0,0,0,49,139,144,152,156,163,167,171,178,182,192,198,
        206,211,223,230,239,246,255,262,268,276,288,293,296,302,307,318,
        325,332,340,358,366,370,377,406,418,422,429,431,438,445,452,462,
        473,484,490,495,499,508
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'not'", 
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
                      "COMMA", "NEWLINE", "NumberLit", "StringLit", "BoolLit", 
                      "IDENTIFIER", "COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_literal = 0
    RULE_nullableListOfNEWLINE = 1
    RULE_listOfNEWLINE = 2
    RULE_program = 3
    RULE_globalLevelDecl = 4
    RULE_globalLevelDeclList = 5
    RULE_globalLevelDeclListPrime = 6
    RULE_blockLevelDecl = 7
    RULE_blockLevelDeclList = 8
    RULE_blockLevelDeclListPrime = 9
    RULE_functionDecl = 10
    RULE_functionDecl1 = 11
    RULE_arrayDeclaration = 12
    RULE_arrayDim = 13
    RULE_arrayAssign = 14
    RULE_arrayElementList = 15
    RULE_arrayList = 16
    RULE_literalList = 17
    RULE_elementAccessExpr = 18
    RULE_arrExpr = 19
    RULE_indexList = 20
    RULE_functionCall = 21
    RULE_functionArgsList = 22
    RULE_argsPrime = 23
    RULE_arg = 24
    RULE_assignStatement = 25
    RULE_scalarAssignStatement = 26
    RULE_arrayAssignStatement = 27
    RULE_statement = 28
    RULE_variableDeclaration = 29
    RULE_normalDeclaration = 30
    RULE_varType = 31
    RULE_varDecl = 32
    RULE_dynamicDecl = 33
    RULE_variableInitialization = 34
    RULE_paramDeclList = 35
    RULE_paramDeclPrime = 36
    RULE_paramDeclAtom = 37
    RULE_functionPreDecl = 38
    RULE_functionFullDecl = 39
    RULE_paramDecl = 40
    RULE_functionBody = 41
    RULE_ifStatement = 42
    RULE_elifStatementList = 43
    RULE_elifStatementPrime = 44
    RULE_elifStatement = 45
    RULE_elseStatement = 46
    RULE_forStatement = 47
    RULE_updateExpr = 48
    RULE_breakStatement = 49
    RULE_continueStatement = 50
    RULE_returnStatement = 51
    RULE_functionCallStatement = 52
    RULE_blockStatement = 53
    RULE_blockStatementBody = 54
    RULE_nullableListOfStatement = 55
    RULE_nullableListOfStatementPrime = 56
    RULE_expressionList = 57
    RULE_expression = 58
    RULE_expression1 = 59
    RULE_expression2 = 60
    RULE_expression3 = 61
    RULE_expression4 = 62
    RULE_expression5 = 63
    RULE_expression6 = 64
    RULE_expression7 = 65
    RULE_operands = 66

    ruleNames =  [ "literal", "nullableListOfNEWLINE", "listOfNEWLINE", 
                   "program", "globalLevelDecl", "globalLevelDeclList", 
                   "globalLevelDeclListPrime", "blockLevelDecl", "blockLevelDeclList", 
                   "blockLevelDeclListPrime", "functionDecl", "functionDecl1", 
                   "arrayDeclaration", "arrayDim", "arrayAssign", "arrayElementList", 
                   "arrayList", "literalList", "elementAccessExpr", "arrExpr", 
                   "indexList", "functionCall", "functionArgsList", "argsPrime", 
                   "arg", "assignStatement", "scalarAssignStatement", "arrayAssignStatement", 
                   "statement", "variableDeclaration", "normalDeclaration", 
                   "varType", "varDecl", "dynamicDecl", "variableInitialization", 
                   "paramDeclList", "paramDeclPrime", "paramDeclAtom", "functionPreDecl", 
                   "functionFullDecl", "paramDecl", "functionBody", "ifStatement", 
                   "elifStatementList", "elifStatementPrime", "elifStatement", 
                   "elseStatement", "forStatement", "updateExpr", "breakStatement", 
                   "continueStatement", "returnStatement", "functionCallStatement", 
                   "blockStatement", "blockStatementBody", "nullableListOfStatement", 
                   "nullableListOfStatementPrime", "expressionList", "expression", 
                   "expression1", "expression2", "expression3", "expression4", 
                   "expression5", "expression6", "expression7", "operands" ]

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
    BoolLit=45
    IDENTIFIER=46
    COMMENT=47
    WS=48
    ERROR_CHAR=49
    UNCLOSE_STRING=50
    ILLEGAL_ESCAPE=51

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

        def BoolLit(self):
            return self.getToken(ZCodeParser.BoolLit, 0)

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
            self.state = 134
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61572651155456) != 0)):
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


    class NullableListOfNEWLINEContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def nullableListOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfNEWLINEContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullableListOfNEWLINE




    def nullableListOfNEWLINE(self):

        localctx = ZCodeParser.NullableListOfNEWLINEContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_nullableListOfNEWLINE)
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(ZCodeParser.NEWLINE)
                self.state = 137
                self.nullableListOfNEWLINE()
                pass
            elif token in [-1, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 17, 18, 46]:
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


    class ListOfNEWLINEContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(ZCodeParser.NEWLINE, 0)

        def listOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.ListOfNEWLINEContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_listOfNEWLINE




    def listOfNEWLINE(self):

        localctx = ZCodeParser.ListOfNEWLINEContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_listOfNEWLINE)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(ZCodeParser.NEWLINE)
                self.state = 142
                self.listOfNEWLINE()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.match(ZCodeParser.NEWLINE)
                pass


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

        def nullableListOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfNEWLINEContext,0)


        def globalLevelDeclList(self):
            return self.getTypedRuleContext(ZCodeParser.GlobalLevelDeclListContext,0)


        def EOF(self):
            return self.getToken(ZCodeParser.EOF, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.nullableListOfNEWLINE()
            self.state = 147
            self.globalLevelDeclList()
            self.state = 148
            self.match(ZCodeParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GlobalLevelDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDecl(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionDeclContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(ZCodeParser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_globalLevelDecl




    def globalLevelDecl(self):

        localctx = ZCodeParser.GlobalLevelDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_globalLevelDecl)
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.functionDecl()
                pass
            elif token in [3, 4, 5, 7, 8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 151
                self.variableDeclaration()
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


    class GlobalLevelDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def globalLevelDeclListPrime(self):
            return self.getTypedRuleContext(ZCodeParser.GlobalLevelDeclListPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_globalLevelDeclList




    def globalLevelDeclList(self):

        localctx = ZCodeParser.GlobalLevelDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_globalLevelDeclList)
        try:
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 7, 8, 9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 154
                self.globalLevelDeclListPrime()
                pass
            elif token in [-1]:
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


    class GlobalLevelDeclListPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def globalLevelDecl(self):
            return self.getTypedRuleContext(ZCodeParser.GlobalLevelDeclContext,0)


        def listOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.ListOfNEWLINEContext,0)


        def globalLevelDeclListPrime(self):
            return self.getTypedRuleContext(ZCodeParser.GlobalLevelDeclListPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_globalLevelDeclListPrime




    def globalLevelDeclListPrime(self):

        localctx = ZCodeParser.GlobalLevelDeclListPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_globalLevelDeclListPrime)
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.globalLevelDecl()
                self.state = 159
                self.listOfNEWLINE()
                self.state = 160
                self.globalLevelDeclListPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.globalLevelDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockLevelDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDecl(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionDeclContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(ZCodeParser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_blockLevelDecl




    def blockLevelDecl(self):

        localctx = ZCodeParser.BlockLevelDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_blockLevelDecl)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.functionDecl()
                pass
            elif token in [3, 4, 5, 7, 8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.variableDeclaration()
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


    class BlockLevelDeclListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockLevelDeclListPrime(self):
            return self.getTypedRuleContext(ZCodeParser.BlockLevelDeclListPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_blockLevelDeclList




    def blockLevelDeclList(self):

        localctx = ZCodeParser.BlockLevelDeclListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_blockLevelDeclList)
        try:
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 7, 8, 9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 169
                self.blockLevelDeclListPrime()
                pass
            elif token in [-1]:
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


    class BlockLevelDeclListPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockLevelDecl(self):
            return self.getTypedRuleContext(ZCodeParser.BlockLevelDeclContext,0)


        def listOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.ListOfNEWLINEContext,0)


        def blockLevelDeclListPrime(self):
            return self.getTypedRuleContext(ZCodeParser.BlockLevelDeclListPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_blockLevelDeclListPrime




    def blockLevelDeclListPrime(self):

        localctx = ZCodeParser.BlockLevelDeclListPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_blockLevelDeclListPrime)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.blockLevelDecl()
                self.state = 174
                self.listOfNEWLINE()
                self.state = 175
                self.blockLevelDeclListPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.blockLevelDecl()
                pass


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

        def functionDecl1(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionDecl1Context,0)


        def functionPreDecl(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionPreDeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_functionDecl




    def functionDecl(self):

        localctx = ZCodeParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_functionDecl)
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.functionDecl1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.functionPreDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDecl1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionFullDecl(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionFullDeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_functionDecl1




    def functionDecl1(self):

        localctx = ZCodeParser.FunctionDecl1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_functionDecl1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.functionFullDecl()
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
        self.enterRule(localctx, 24, self.RULE_arrayDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.varType()
            self.state = 187
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 188
            self.match(ZCodeParser.LSBracket)
            self.state = 189
            self.arrayDim()
            self.state = 190
            self.match(ZCodeParser.RSBracket)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 191
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
        self.enterRule(localctx, 26, self.RULE_arrayDim)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(ZCodeParser.NumberLit)
                self.state = 195
                self.match(ZCodeParser.COMMA)
                self.state = 196
                self.arrayDim()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
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
        self.enterRule(localctx, 28, self.RULE_arrayAssign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(ZCodeParser.LEFTARR)
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.state = 201
                self.match(ZCodeParser.LSBracket)
                self.state = 202
                self.arrayElementList()
                self.state = 203
                self.match(ZCodeParser.RSBracket)
                pass
            elif token in [20, 24, 37, 43, 44, 45, 46]:
                self.state = 205
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
        self.enterRule(localctx, 30, self.RULE_arrayElementList)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.literalList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 209
                self.arrayList()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 210
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
        self.enterRule(localctx, 32, self.RULE_arrayList)
        try:
            self.state = 223
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(ZCodeParser.LSBracket)
                self.state = 214
                self.arrayElementList()
                self.state = 215
                self.match(ZCodeParser.RSBracket)
                self.state = 216
                self.match(ZCodeParser.COMMA)
                self.state = 217
                self.arrayList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.match(ZCodeParser.LSBracket)
                self.state = 220
                self.arrayElementList()
                self.state = 221
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
        self.enterRule(localctx, 34, self.RULE_literalList)
        try:
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.literal()
                self.state = 226
                self.match(ZCodeParser.COMMA)
                self.state = 227
                self.literalList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
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
        self.enterRule(localctx, 36, self.RULE_elementAccessExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.arrExpr()
            self.state = 233
            self.match(ZCodeParser.LSBracket)
            self.state = 234
            self.indexList()
            self.state = 235
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
        self.enterRule(localctx, 38, self.RULE_arrExpr)
        try:
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
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
        self.enterRule(localctx, 40, self.RULE_indexList)
        try:
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.expression()
                self.state = 242
                self.match(ZCodeParser.COMMA)
                self.state = 243
                self.indexList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
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
        self.enterRule(localctx, 42, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 249
            self.match(ZCodeParser.LBracket)
            self.state = 250
            self.functionArgsList()
            self.state = 251
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
        self.enterRule(localctx, 44, self.RULE_functionArgsList)
        try:
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 24, 37, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
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
        self.enterRule(localctx, 46, self.RULE_argsPrime)
        try:
            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self.arg()
                self.state = 258
                self.match(ZCodeParser.COMMA)
                self.state = 259
                self.argsPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 261
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
        self.enterRule(localctx, 48, self.RULE_arg)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
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
        self.enterRule(localctx, 50, self.RULE_assignStatement)
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 266
                self.scalarAssignStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
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
        self.enterRule(localctx, 52, self.RULE_scalarAssignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 271
            self.match(ZCodeParser.LEFTARR)
            self.state = 272
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
        self.enterRule(localctx, 54, self.RULE_arrayAssignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 274
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.state = 275
                self.elementAccessExpr()
                pass


            self.state = 278
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
        self.enterRule(localctx, 56, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 280
                self.ifStatement()
                pass

            elif la_ == 2:
                self.state = 281
                self.forStatement()
                pass

            elif la_ == 3:
                self.state = 282
                self.breakStatement()
                pass

            elif la_ == 4:
                self.state = 283
                self.continueStatement()
                pass

            elif la_ == 5:
                self.state = 284
                self.returnStatement()
                pass

            elif la_ == 6:
                self.state = 285
                self.functionCallStatement()
                pass

            elif la_ == 7:
                self.state = 286
                self.blockStatement()
                pass

            elif la_ == 8:
                self.state = 287
                self.assignStatement()
                pass


            self.state = 296
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.state = 291 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 290
                        self.match(ZCodeParser.NEWLINE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 293 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                pass
            elif token in [-1]:
                self.state = 295
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
        self.enterRule(localctx, 58, self.RULE_variableDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 298
                self.normalDeclaration()
                pass

            elif la_ == 2:
                self.state = 299
                self.arrayDeclaration()
                pass

            elif la_ == 3:
                self.state = 300
                self.varDecl()
                pass

            elif la_ == 4:
                self.state = 301
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
        self.enterRule(localctx, 60, self.RULE_normalDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.varType()
            self.state = 305
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 306
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
        self.enterRule(localctx, 62, self.RULE_varType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
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
        self.enterRule(localctx, 64, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(ZCodeParser.VAR)
            self.state = 312
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 313
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
        self.enterRule(localctx, 66, self.RULE_dynamicDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.match(ZCodeParser.DYNAMIC)
            self.state = 316
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 317
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
        self.enterRule(localctx, 68, self.RULE_variableInitialization)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(ZCodeParser.LEFTARR)
            self.state = 321
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
        self.enterRule(localctx, 70, self.RULE_paramDeclList)
        try:
            self.state = 325
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
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
        self.enterRule(localctx, 72, self.RULE_paramDeclPrime)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.paramDeclAtom()
                self.state = 328
                self.match(ZCodeParser.COMMA)
                self.state = 329
                self.paramDeclPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 331
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
        self.enterRule(localctx, 74, self.RULE_paramDeclAtom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.varType()
            self.state = 335
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 336
                self.match(ZCodeParser.LSBracket)
                self.state = 337
                self.arrayDim()
                self.state = 338
                self.match(ZCodeParser.RSBracket)


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
        self.enterRule(localctx, 76, self.RULE_functionPreDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(ZCodeParser.FUNC)
            self.state = 343
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 344
            self.paramDecl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionFullDeclContext(ParserRuleContext):
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


        def nullableListOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfNEWLINEContext,0)


        def functionBody(self):
            return self.getTypedRuleContext(ZCodeParser.FunctionBodyContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_functionFullDecl




    def functionFullDecl(self):

        localctx = ZCodeParser.FunctionFullDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_functionFullDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(ZCodeParser.FUNC)
            self.state = 347
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 348
            self.paramDecl()
            self.state = 349
            self.nullableListOfNEWLINE()
            self.state = 350
            self.functionBody()
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
        self.enterRule(localctx, 80, self.RULE_paramDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.match(ZCodeParser.LBracket)
            self.state = 353
            self.paramDeclList()
            self.state = 354
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
        self.enterRule(localctx, 82, self.RULE_functionBody)
        try:
            self.state = 358
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.blockStatement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 357
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


        def nullableListOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfNEWLINEContext,0)


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
        self.enterRule(localctx, 84, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(ZCodeParser.IF)
            self.state = 361
            self.expression()
            self.state = 362
            self.nullableListOfNEWLINE()
            self.state = 363
            self.statement()
            self.state = 364
            self.elifStatementList()
            self.state = 366
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 365
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
        self.enterRule(localctx, 86, self.RULE_elifStatementList)
        try:
            self.state = 370
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
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


        def nullableListOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfNEWLINEContext,0)


        def elifStatementPrime(self):
            return self.getTypedRuleContext(ZCodeParser.ElifStatementPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifStatementPrime




    def elifStatementPrime(self):

        localctx = ZCodeParser.ElifStatementPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_elifStatementPrime)
        try:
            self.state = 377
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.elifStatement()
                self.state = 373
                self.nullableListOfNEWLINE()
                self.state = 374
                self.elifStatementPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
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


        def nullableListOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfNEWLINEContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elifStatement




    def elifStatement(self):

        localctx = ZCodeParser.ElifStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_elifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(ZCodeParser.ELIF)
            self.state = 380
            self.expression()
            self.state = 381
            self.nullableListOfNEWLINE()
            self.state = 382
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


        def nullableListOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfNEWLINEContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_elseStatement




    def elseStatement(self):

        localctx = ZCodeParser.ElseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_elseStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 384
            self.match(ZCodeParser.ELSE)
            self.state = 385
            self.expression()
            self.state = 386
            self.nullableListOfNEWLINE()
            self.state = 387
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


        def nullableListOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfNEWLINEContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_forStatement




    def forStatement(self):

        localctx = ZCodeParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.match(ZCodeParser.FOR)
            self.state = 390
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 391
            self.match(ZCodeParser.UNTIL)
            self.state = 392
            self.expression()
            self.state = 393
            self.match(ZCodeParser.BY)
            self.state = 394
            self.updateExpr()
            self.state = 395
            self.nullableListOfNEWLINE()
            self.state = 396
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
        self.enterRule(localctx, 96, self.RULE_updateExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
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
        self.enterRule(localctx, 98, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
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
        self.enterRule(localctx, 100, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
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
        self.enterRule(localctx, 102, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(ZCodeParser.RETURN)
            self.state = 406
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 132078852112384) != 0):
                self.state = 405
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
        self.enterRule(localctx, 104, self.RULE_functionCallStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
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
        self.enterRule(localctx, 106, self.RULE_blockStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(ZCodeParser.BEGIN)

            self.state = 411
            self.blockStatementBody()
            self.state = 412
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
        self.enterRule(localctx, 108, self.RULE_blockStatementBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
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

        def nullableListOfStatementPrime(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfStatementPrimeContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullableListOfStatement




    def nullableListOfStatement(self):

        localctx = ZCodeParser.NullableListOfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_nullableListOfStatement)
        try:
            self.state = 418
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 18, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.nullableListOfStatementPrime()
                pass
            elif token in [19]:
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


    class NullableListOfStatementPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listOfNEWLINE(self):
            return self.getTypedRuleContext(ZCodeParser.ListOfNEWLINEContext,0)


        def nullableListOfStatementPrime(self):
            return self.getTypedRuleContext(ZCodeParser.NullableListOfStatementPrimeContext,0)


        def statement(self):
            return self.getTypedRuleContext(ZCodeParser.StatementContext,0)


        def blockLevelDecl(self):
            return self.getTypedRuleContext(ZCodeParser.BlockLevelDeclContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_nullableListOfStatementPrime




    def nullableListOfStatementPrime(self):

        localctx = ZCodeParser.NullableListOfStatementPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_nullableListOfStatementPrime)
        try:
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6, 10, 13, 14, 15, 18, 46]:
                    self.state = 420
                    self.statement()
                    pass
                elif token in [3, 4, 5, 7, 8, 9]:
                    self.state = 421
                    self.blockLevelDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 424
                self.listOfNEWLINE()
                self.state = 425
                self.nullableListOfStatementPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [6, 10, 13, 14, 15, 18, 46]:
                    self.state = 427
                    self.statement()
                    pass
                elif token in [3, 4, 5, 7, 8, 9]:
                    self.state = 428
                    self.blockLevelDecl()
                    pass
                else:
                    raise NoViableAltException(self)

                pass


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
        self.enterRule(localctx, 114, self.RULE_expressionList)
        try:
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.expression()
                self.state = 434
                self.match(ZCodeParser.COMMA)
                self.state = 435
                self.expressionList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
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
        self.enterRule(localctx, 116, self.RULE_expression)
        try:
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.expression1()
                self.state = 441
                self.match(ZCodeParser.ELLIPSIS)
                self.state = 442
                self.expression1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
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
        self.enterRule(localctx, 118, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.expression2(0)
                self.state = 448
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 67914170368) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 449
                self.expression2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
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
        _startState = 120
        self.enterRecursionRule(localctx, 120, self.RULE_expression2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455
            self.expression3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 462
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression2)
                    self.state = 457
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 458
                    _la = self._input.LA(1)
                    if not(_la==21 or _la==22):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 459
                    self.expression3(0) 
                self.state = 464
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
        _startState = 122
        self.enterRecursionRule(localctx, 122, self.RULE_expression3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.expression4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 473
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression3)
                    self.state = 468
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 469
                    _la = self._input.LA(1)
                    if not(_la==23 or _la==24):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 470
                    self.expression4(0) 
                self.state = 475
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

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
        _startState = 124
        self.enterRecursionRule(localctx, 124, self.RULE_expression4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.expression5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 484
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ZCodeParser.Expression4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression4)
                    self.state = 479
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 480
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 234881024) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 481
                    self.expression5() 
                self.state = 486
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

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
        self.enterRule(localctx, 126, self.RULE_expression5)
        try:
            self.state = 490
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 487
                self.match(ZCodeParser.NOT)
                self.state = 488
                self.expression5()
                pass
            elif token in [24, 37, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
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
        self.enterRule(localctx, 128, self.RULE_expression6)
        try:
            self.state = 495
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.match(ZCodeParser.MINUS)
                self.state = 493
                self.expression6()
                pass
            elif token in [37, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 494
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
        self.enterRule(localctx, 130, self.RULE_expression7)
        try:
            self.state = 499
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 497
                self.elementAccessExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 498
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
        self.enterRule(localctx, 132, self.RULE_operands)
        try:
            self.state = 508
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 501
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 502
                self.match(ZCodeParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 503
                self.match(ZCodeParser.LBracket)
                self.state = 504
                self.expression()
                self.state = 505
                self.match(ZCodeParser.RBracket)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 507
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
        self._predicates[60] = self.expression2_sempred
        self._predicates[61] = self.expression3_sempred
        self._predicates[62] = self.expression4_sempred
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
         




