from txt_to_mif import convert, cmdline

try:
    convert("test")
    test_lines = open("test.mif", "r").readlines()
    real_lines = open("compare.mif", "r").readlines()
except:
    pass

if(test_lines == real_lines):
    print(f"{cmdline.BOLD}{cmdline.UNDERLINE}{cmdline.OK}TESTS PASSED{cmdline.ENDC}")
else:
    print(f"{cmdline.BOLD}{cmdline.UNDERLINE}{cmdline.FAIL}TESTS FAILED{cmdline.ENDC}")