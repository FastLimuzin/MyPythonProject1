from my_modules.module1 import report_origin as report_origin_module1
from my_modules.module2 import report_origin as report_origin_module2
from my_package.sub_package1.file1 import report_origin as report_origin_sub1_file1
from my_package.sub_package1.file2 import report_origin as report_origin_sub1_file2
from my_package.sub_package2.file1 import report_origin as report_origin_sub2_file1
from my_package.sub_package2.file2 import report_origin as report_origin_sub2_file2
from my_package.sub_package3.file1 import report_origin as report_origin_sub3_file1
from my_package.sub_package3.file2 import report_origin as report_origin_sub3_file2

def main():
    report_origin_module1()
    report_origin_module2()
    report_origin_sub1_file1()
    report_origin_sub1_file2()
    report_origin_sub2_file1()
    report_origin_sub2_file2()
    report_origin_sub3_file1()
    report_origin_sub3_file2()

if __name__ == '__main__':
    main()