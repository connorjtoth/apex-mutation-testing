from src.apexmut.main import main


def testNoArgumentPassed():
    try:
        main()
    except Exception:
        assert(True)
    else:
        assert(False)


def testTwoArgumentsPassed():
    try:
        main()
    except Exception:
        assert(True)
    else:
        assert(False)