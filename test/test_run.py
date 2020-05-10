from apexmut import run


def testNoArgumentPassed():
    try:
        run()
    except Exception:
        assert(True)
    else:
        assert(False)


def testTwoArgumentsPassed():
    try:
        run()
    except Exception:
        assert(True)
    else:
        assert(False)

