# print("Hello World!")
#
# def feature_1():
#     print("A bug can be seen as a feature.")
#
# feature_1()

from SyntheticTestLauncher import TestRunner

def main():
    suite = TestRunner()
    suite.run_tests()

if __name__ == "__main__":
    main()